#!/usr/bin/env python3
"""Puts every post in _posts/YYYY/MM/ and pads the date in its file name
(2026-9-30-Dylan-Fan.md -> _posts/2026/09/2026-09-30-Dylan-Fan.md).
Only the file location and the date part of the name change. The address of a post
comes from its title part, so no post address changes."""
import os, re, subprocess, sys

PATTERN = re.compile(r'^(\d{4})-(\d{1,2})-(\d{1,2})-(.+\.(?:md|markdown))$')
moved = 0

for root, _, files in os.walk('_posts'):
    for name in sorted(files):
        m = PATTERN.match(name)
        if not m:
            continue
        year, month, day, rest = m.group(1), int(m.group(2)), int(m.group(3)), m.group(4)
        new_name = '%s-%02d-%02d-%s' % (year, month, day, rest)
        new_dir = os.path.join('_posts', year, '%02d' % month)
        old = os.path.join(root, name)
        new = os.path.join(new_dir, new_name)
        if os.path.normpath(old) == os.path.normpath(new):
            continue
        if os.path.exists(new):
            print('SKIPPED (target exists):', old, '->', new)
            continue
        os.makedirs(new_dir, exist_ok=True)
        subprocess.run(['git', 'mv', old, new], check=True)
        print('moved:', old, '->', new)
        moved += 1

print(moved, 'file(s) moved')
