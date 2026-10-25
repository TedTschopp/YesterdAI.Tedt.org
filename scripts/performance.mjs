// Reproducible CI lab checks. INP remains a field metric.
import fs from 'node:fs/promises';
import os from 'node:os';
import path from 'node:path';
import { spawn } from 'node:child_process';
import { once } from 'node:events';
import lighthouse from 'lighthouse';
import { chromium } from '@playwright/test';

if (!process.env.CI) throw new Error('Run the lab browser in GitHub Actions. Local interactive review uses CUA.');
const local = process.argv.includes('--local');
const origin = local ? 'http://127.0.0.1:4175' : 'https://yesterdai.tedt.org';
const temporary = await fs.mkdtemp(path.join(os.tmpdir(),'yesterdai-performance-'));
const chrome = spawn(chromium.executablePath(),[
  '--headless','--no-sandbox','--disable-dev-shm-usage','--remote-debugging-port=9222',
  '--user-data-dir='+temporary
],{stdio:'ignore'});
const server = local ? spawn('python3',['-m','http.server','4175','--bind','127.0.0.1','--directory','_site'],{stdio:'ignore'}) : null;
async function ready(url) {
  for (let i=0;i<80;i++) {
    try { if ((await fetch(url)).ok) return; } catch {}
    await new Promise(resolve=>setTimeout(resolve,250));
  }
  throw new Error('Lab service did not become ready: '+url);
}
const median = values => [...values].sort((a,b)=>a-b)[Math.floor(values.length/2)];
const report = { measured_at:new Date().toISOString(),origin,method:'Lighthouse simulated mobile, three cold navigations per page',field_INP:'unavailable',pages:[] };
try {
  await ready('http://127.0.0.1:9222/json/version');
  if (local) await ready(origin);
  for (const route of ['/','/articles/kapitsa-local-inference-operations/','/search/']) {
    const runs=[];
    for (let attempt=0;attempt<3;attempt++) {
      const {lhr}=await lighthouse(origin+route,{
        port:9222,output:'json',onlyCategories:['performance'],logLevel:'error',
        formFactor:'mobile',throttlingMethod:'simulate',
        screenEmulation:{mobile:true,width:390,height:844,deviceScaleFactor:1,disabled:false}
      });
      runs.push({
        lcp_ms:lhr.audits['largest-contentful-paint'].numericValue,
        cls:lhr.audits['cumulative-layout-shift'].numericValue,
        tbt_ms:lhr.audits['total-blocking-time'].numericValue,
        score:lhr.categories.performance.score,
        warnings:lhr.runWarnings
      });
    }
    const result={route,runs,lcp_ms:median(runs.map(r=>r.lcp_ms)),cls:median(runs.map(r=>r.cls)),tbt_ms:median(runs.map(r=>r.tbt_ms))};
    result.passed=result.lcp_ms<=2500 && result.cls<=0.1 && result.tbt_ms<=200;
    report.pages.push(result);
  }
  report.passed=report.pages.every(page=>page.passed);
  await fs.mkdir('test-results',{recursive:true});
  await fs.writeFile('test-results/performance.json',JSON.stringify(report,null,2)+'\n');
  console.log(JSON.stringify(report,null,2));
  if (!report.passed) process.exitCode=1;
} finally {
  const exits = [chrome,server].filter(child=>child && child.exitCode===null).map(child=>{
    const exited=once(child,'exit');child.kill();return exited;
  });
  await Promise.allSettled(exits);
  await fs.rm(temporary,{recursive:true,force:true,maxRetries:5,retryDelay:100});
}
