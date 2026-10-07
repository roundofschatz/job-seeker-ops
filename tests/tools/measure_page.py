#!/usr/bin/env python3
"""Measure how much of a page a cover letter's Word file fills, line by line,
with the real font's character widths. It checks build_letter.py's estimate on
a computer with no Word or LibreOffice to render the page.

    python tests/tools/measure_page.py Letter.docx

It needs Pillow and the font's own file (calibri.ttf, arial.ttf, georgia.ttf or
times.ttf), from C:/Windows/Fonts unless --fonts names another folder, and it
isn't part of the plugin. It wraps each paragraph the way
Word does for plain left-aligned text, at the page's text width, and adds each
paragraph's spacing and the font's single line height. It prints the measured
fraction of the page next to check_letter.py's estimate.
"""
import argparse
import importlib.util
import sys
from pathlib import Path

from PIL import ImageFont

REPO = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location(
    "check_letter", REPO / "skills" / "cover-letter" / "scripts" / "check_letter.py")
cl = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cl)

FILES = {"calibri": "calibri.ttf", "arial": "arial.ttf", "georgia": "georgia.ttf",
         "times new roman": "times.ttf"}


def measure(path, fonts):
    font, _size, margins, page, paras = cl.docx_layout(path)
    face_file = Path(fonts) / FILES[font.lower()]
    top, right, bottom, left = margins
    width = (page[0]-left-right)/20
    avail = (page[1]-top-bottom)/20
    height_em = cl.LINE_HEIGHT[font.lower()]
    used, lines = 0.0, 0
    for text, size, before, after in paras:
        face = ImageFont.truetype(str(face_file), 1000)
        scale = size/1000
        count, cur = 1, ""
        for word in text.split():
            trial = word if not cur else cur + " " + word
            if face.getlength(trial)*scale > width and cur:
                count += 1
                cur = word
            else:
                cur = trial
        lines += count
        used += before+after+count*size*height_em
    return used/avail, lines


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("docx")
    ap.add_argument("--fonts", default="C:/Windows/Fonts")
    args = ap.parse_args()
    measured, lines = measure(args.docx, args.fonts)
    font, _size, margins, page, paras = cl.docx_layout(args.docx)
    estimate, est_lines = cl.estimate_pages(paras, font, margins, page)
    print(f"{Path(args.docx).name}: measured {measured:.3f} of a page ({lines} lines); "
          f"check_letter.py estimates {estimate:.3f} ({est_lines} lines)")
    return 0 if measured <= 1 else 1


if __name__ == "__main__":
    sys.exit(main())
