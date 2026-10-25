// Pure reader state shared by the browser and deterministic Node checks.
export function publicationNotice(data, now = new Date()) {
  if (data.wireChecked) {
    const checked = new Date(data.wireChecked);
    if (!Number.isFinite(checked.getTime()) || now - checked > 3 * 60 * 60 * 1000) {
      return { message: 'The live feed has not been checked recently. These are the last saved links.' };
    }
  }
  if (data.editionDate) {
    const parts = Object.fromEntries(new Intl.DateTimeFormat('en-CA', {
      timeZone: 'America/Los_Angeles', year: 'numeric', month: '2-digit', day: '2-digit',
      hour: '2-digit', hourCycle: 'h23'
    }).formatToParts(now).map(part => [part.type, part.value]));
    const day = [parts.year, parts.month, parts.day].join('-');
    if (Number(parts.hour) >= 7 && data.editionDate < day) {
      const date = new Date(data.editionDate + 'T12:00:00Z').toLocaleDateString('en-US', {
        month: 'long', day: 'numeric', timeZone: 'UTC'
      });
      return { message: 'The latest edition is from ' + date + '. ',
        href: '/live/', link: 'Browse the live news for more recent links.' };
    }
  }
  return null;
}
