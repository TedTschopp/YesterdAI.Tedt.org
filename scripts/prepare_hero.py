#!/usr/bin/env python3
"""Optimize a completed built-in generation and retain its actual dimensions."""
import argparse
import json
from pathlib import Path
import re
import shutil
import subprocess
from publish import ROOT, atomic_json, image_dimensions


def prepare(metadata_path):
    metadata = json.loads(Path(metadata_path).read_text())
    slug = metadata['slug']
    if not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', slug):
        raise ValueError('Invalid asset slug')
    output = ROOT / 'assets/images' / (slug + '.webp')
    if not output.exists():
        encoder = shutil.which('cwebp')
        if not encoder:
            raise ValueError('cwebp is required to optimize a generated hero')
        subprocess.run([encoder, '-quiet', '-q', '82', '-resize', '1536', '0', metadata['path'], '-o', str(output)], check=True)
    width, height = image_dimensions(output)
    result = {**metadata, 'path': '/assets/images/' + output.name, 'width': width, 'height': height, 'bytes': output.stat().st_size}
    atomic_json(Path(metadata_path), result)
    print(json.dumps(result, ensure_ascii=False))
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('metadata')
    prepare(parser.parse_args().metadata)
