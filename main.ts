// Entry program for the 21 November 2026 world-news image.
//
// The finished poster lives in this repository as entry.png (drawn by
// draw_poster.py, a Pillow script, from the day's reported news). This
// program only places that file where the grader expects it:
// /output/entry.png, or the directory named by MAKEFUN_OUTPUT_DIR when
// the program is run outside the grader's container:
//
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
//
// No network, no randomness, no writes besides the single copy, so two
// runs always produce byte-identical output.

import { copyFileSync, mkdirSync } from 'node:fs';
import { dirname, join } from 'node:path';
import { fileURLToPath } from 'node:url';

const here = dirname(fileURLToPath(import.meta.url));
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });
copyFileSync(join(here, 'entry.png'), join(outDir, 'entry.png'));
