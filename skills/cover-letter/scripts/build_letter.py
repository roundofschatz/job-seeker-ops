#!/usr/bin/env python3
"""Write a cover letter's Word file from its checked text, the way resume-ops
writes a resume: by hand, with every part Word itself writes, and with the
writer's name in the author field.

    python build_letter.py letter.txt --company "Silver Larch School District" \\
        --resume Nadia-Haddad-Resume.docx --out .

The letter's text is the upload form: the contact block, the date, the
salutation, the body, the sign-off and the name, with a blank line between
paragraphs. The Word file takes the resume's font, size and margins when the
resume is a Word file; from a text resume it uses Calibri 11 with one-inch
margins and says so. The file is named FirstName_LastName_CoverLetter_Company.docx,
and a plain-text copy with straight quotes goes beside it for pasting.

It never makes a PDF. When a posting asks for one, the person exports it from
the Word file.

The build refuses, and writes nothing, when the letter has no salutation or
sign-off, holds a placeholder, has no contact block, or runs past one page by
estimate. After writing, it checks the file with check_letter.py.

Exit code 0 means the file was written and passed, 1 means a refusal or a
FAIL in the check, and 2 means the input needs fixing. Python 3.8 or newer,
standard library only.
"""
import argparse
import datetime
import importlib.util
import io
import re
import sys
import zipfile
from pathlib import Path
from xml.etree import ElementTree as ET
from xml.sax.saxutils import escape

__version__ = "0.3.0"

HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("check_letter", HERE / "check_letter.py")
cl = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(cl)

W = cl.W
NS = 'xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main"'
NS_R = 'xmlns:r="http://schemas.openxmlformats.org/officeDocument/2006/relationships"'
XML_HEAD = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
DEFAULT = {"font": "Calibri", "size": 11.0, "margins": (1440, 1440, 1440, 1440), "name_size": 14.0}
SERIF = {"georgia", "garamond", "times new roman"}
STRAIGHT = str.maketrans({chr(0x201C): '"', chr(0x201D): '"', chr(0x2018): "'", chr(0x2019): "'"})


# The resume's look

def resume_layout(path):
    """Font, body size, margins and the name's size, from a Word resume. A text
    resume has none of these, so the defaults stand."""
    layout = dict(DEFAULT, source="defaults")
    if not path or Path(path).suffix.lower() != ".docx":
        return layout
    try:
        with zipfile.ZipFile(path) as archive:
            doc = ET.fromstring(archive.read("word/document.xml"))
            styles = ET.fromstring(archive.read("word/styles.xml"))
    except (zipfile.BadZipFile, KeyError, ET.ParseError):
        return layout
    fonts = styles.find(f"{W}docDefaults/{W}rPrDefault/{W}rPr/{W}rFonts")
    if fonts is not None and fonts.get(W + "ascii"):
        layout["font"] = fonts.get(W + "ascii")
    sizes = []
    for p in doc.iter(W + "p"):
        text = "".join(t.text or "" for t in p.iter(W + "t"))
        szs = [int(s.get(W + "val")) / 2 for s in p.iter(W + "sz")]
        if text.strip() and szs:
            sizes.append((text, max(szs)))
    sz = styles.find(f"{W}docDefaults/{W}rPrDefault/{W}rPr/{W}sz")
    if sz is not None:
        layout["size"] = int(sz.get(W + "val")) / 2
    if sizes:
        body = [s for t, s in sizes[1:] if len(t.split()) > 8]
        if body:
            layout["size"] = max(set(body), key=body.count)
        layout["name_size"] = sizes[0][1]
    mar = doc.find(f".//{W}sectPr/{W}pgMar")
    if mar is not None:
        layout["margins"] = tuple(int(mar.get(W + k, 1440)) for k in ("top", "right", "bottom", "left"))
    layout["source"] = Path(path).name
    return layout


# The paragraphs

def paragraphs(letter, layout):
    """(text, size, bold, space before, space after) for each paragraph, in points."""
    size = layout["size"]
    out = []
    header = letter.header
    for k, line in enumerate(header):
        first = k == 0
        after = size if k == len(header)-1 else 0
        out.append((line, layout["name_size"] if first else size, first, 0, after))
    if letter.date:
        out.append((letter.date, size, False, 0, size))
    out.append((letter.salutation, size, False, 0, size))
    for para in letter.paragraphs:
        out.append((para, size, False, 0, size))
    out.append((letter.sign_off + ",", size, False, 0, 0))
    out.append((letter.name, size, False, 0, 0))
    for line in letter.after_name:
        out.append((line, size, False, 0, 0))
    return out


def para_xml(text, size, bold, before, after):
    half = int(round(size*2))
    rpr = f'<w:rPr>{"<w:b/>" if bold else ""}<w:sz w:val="{half}"/><w:szCs w:val="{half}"/></w:rPr>'
    return (f'<w:p><w:pPr><w:spacing w:before="{int(before*20)}" w:after="{int(after*20)}" '
            f'w:line="240" w:lineRule="auto"/>{rpr}</w:pPr>'
            f'<w:r>{rpr}<w:t xml:space="preserve">{escape(text)}</w:t></w:r></w:p>')


# The package: the parts Word itself writes

def document(paras, margins):
    top, right, bottom, left = margins
    body = "".join(para_xml(*p) for p in paras)
    sect = (f'<w:sectPr><w:pgSz w:w="12240" w:h="15840"/><w:pgMar w:top="{top}" w:right="{right}" '
            f'w:bottom="{bottom}" w:left="{left}" w:header="720" w:footer="720" w:gutter="0"/>'
            '<w:cols w:space="720"/></w:sectPr>')
    return f'{XML_HEAD}<w:document {NS}><w:body>{body}{sect}</w:body></w:document>'


def styles(font, size):
    half = int(round(size*2))
    return (
        f'{XML_HEAD}<w:styles {NS}><w:docDefaults><w:rPrDefault><w:rPr>'
        f'<w:rFonts w:ascii="{escape(font)}" w:eastAsia="{escape(font)}" w:hAnsi="{escape(font)}" w:cs="{escape(font)}"/>'
        f'<w:sz w:val="{half}"/><w:szCs w:val="{half}"/>'
        '<w:lang w:val="en-US" w:eastAsia="en-US" w:bidi="ar-SA"/></w:rPr></w:rPrDefault>'
        '<w:pPrDefault><w:pPr><w:spacing w:after="0" w:line="240" w:lineRule="auto"/></w:pPr>'
        '</w:pPrDefault></w:docDefaults>'
        '<w:style w:type="paragraph" w:default="1" w:styleId="Normal"><w:name w:val="Normal"/><w:qFormat/></w:style>'
        '<w:style w:type="character" w:default="1" w:styleId="DefaultParagraphFont">'
        '<w:name w:val="Default Paragraph Font"/><w:uiPriority w:val="1"/><w:semiHidden/><w:unhideWhenUsed/></w:style>'
        '<w:style w:type="table" w:default="1" w:styleId="TableNormal"><w:name w:val="Normal Table"/>'
        '<w:uiPriority w:val="99"/><w:semiHidden/><w:unhideWhenUsed/><w:tblPr><w:tblInd w:w="0" w:type="dxa"/>'
        '<w:tblCellMar><w:top w:w="0" w:type="dxa"/><w:left w:w="108" w:type="dxa"/>'
        '<w:bottom w:w="0" w:type="dxa"/><w:right w:w="108" w:type="dxa"/></w:tblCellMar></w:tblPr></w:style>'
        '<w:style w:type="numbering" w:default="1" w:styleId="NoList"><w:name w:val="No List"/>'
        '<w:uiPriority w:val="99"/><w:semiHidden/><w:unhideWhenUsed/></w:style></w:styles>')


def settings():
    return (f'{XML_HEAD}<w:settings {NS}><w:zoom w:percent="100"/><w:defaultTabStop w:val="720"/>'
            '<w:characterSpacingControl w:val="doNotCompress"/><w:compat><w:compatSetting '
            'w:name="compatibilityMode" w:uri="http://schemas.microsoft.com/office/word" w:val="15"/>'
            '</w:compat></w:settings>')


def web_settings():
    return f'{XML_HEAD}<w:webSettings {NS}><w:optimizeForBrowser/><w:allowPNG/></w:webSettings>'


def numbering():
    return f'{XML_HEAD}<w:numbering {NS}/>'


def font_table(font):
    family = "roman" if font.lower() in SERIF else "swiss"
    return (f'{XML_HEAD}<w:fonts {NS} {NS_R}><w:font w:name="{escape(font)}"><w:charset w:val="00"/>'
            f'<w:family w:val="{family}"/><w:pitch w:val="variable"/></w:font></w:fonts>')


def theme(font):
    solid = '<a:solidFill><a:schemeClr val="phClr"/></a:solidFill>'
    colors = "".join(f'<a:{n}><a:srgbClr val="{v}"/></a:{n}>' for n, v in (
        ("dk2", "44546A"), ("lt2", "E7E6E6"), ("accent1", "4472C4"), ("accent2", "ED7D31"),
        ("accent3", "A5A5A5"), ("accent4", "FFC000"), ("accent5", "5B9BD5"), ("accent6", "70AD47"),
        ("hlink", "0563C1"), ("folHlink", "954F72")))
    face = f'<a:latin typeface="{escape(font)}"/><a:ea typeface=""/><a:cs typeface=""/>'
    return (f'{XML_HEAD}<a:theme xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main" '
            'name="Office Theme"><a:themeElements><a:clrScheme name="Office">'
            '<a:dk1><a:sysClr val="windowText" lastClr="000000"/></a:dk1>'
            '<a:lt1><a:sysClr val="window" lastClr="FFFFFF"/></a:lt1>'
            f'{colors}</a:clrScheme><a:fontScheme name="Office"><a:majorFont>{face}</a:majorFont>'
            f'<a:minorFont>{face}</a:minorFont></a:fontScheme><a:fmtScheme name="Office">'
            f'<a:fillStyleLst>{solid*3}</a:fillStyleLst>'
            '<a:lnStyleLst>' + f'<a:ln w="6350">{solid}</a:ln>'*3 + '</a:lnStyleLst>'
            '<a:effectStyleLst>' + '<a:effectStyle><a:effectLst/></a:effectStyle>'*3 + '</a:effectStyleLst>'
            f'<a:bgFillStyleLst>{solid*3}</a:bgFillStyleLst></a:fmtScheme></a:themeElements>'
            '<a:objectDefaults/><a:extraClrSchemeLst/></a:theme>')


def core_props(name, when):
    stamp = when.strftime("%Y-%m-%dT%H:%M:%SZ")
    who = escape(name)
    return (f'{XML_HEAD}<cp:coreProperties '
            'xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" '
            'xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" '
            'xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">'
            f'<dc:title>{who} Cover Letter</dc:title><dc:creator>{who}</dc:creator>'
            f'<cp:lastModifiedBy>{who}</cp:lastModifiedBy><cp:revision>1</cp:revision>'
            f'<dcterms:created xsi:type="dcterms:W3CDTF">{stamp}</dcterms:created>'
            f'<dcterms:modified xsi:type="dcterms:W3CDTF">{stamp}</dcterms:modified></cp:coreProperties>')


def app_props():
    """No Application element, so the file names no program it wasn't made in."""
    return (f'{XML_HEAD}<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" '
            'xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">'
            '<Template>Normal.dotm</Template><TotalTime>0</TotalTime><DocSecurity>0</DocSecurity>'
            '<ScaleCrop>false</ScaleCrop><LinksUpToDate>false</LinksUpToDate><SharedDoc>false</SharedDoc>'
            '<HyperlinksChanged>false</HyperlinksChanged></Properties>')


_WML = "application/vnd.openxmlformats-officedocument.wordprocessingml"
_REL = "http://schemas.openxmlformats.org/officeDocument/2006/relationships"
CONTENT_TYPES = (
    f'{XML_HEAD}<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
    '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
    '<Default Extension="xml" ContentType="application/xml"/>'
    f'<Override PartName="/word/document.xml" ContentType="{_WML}.document.main+xml"/>'
    f'<Override PartName="/word/styles.xml" ContentType="{_WML}.styles+xml"/>'
    f'<Override PartName="/word/numbering.xml" ContentType="{_WML}.numbering+xml"/>'
    f'<Override PartName="/word/settings.xml" ContentType="{_WML}.settings+xml"/>'
    f'<Override PartName="/word/webSettings.xml" ContentType="{_WML}.webSettings+xml"/>'
    f'<Override PartName="/word/fontTable.xml" ContentType="{_WML}.fontTable+xml"/>'
    '<Override PartName="/word/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>'
    '<Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>'
    '<Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>'
    '</Types>')
ROOT_RELS = (
    f'{XML_HEAD}<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    f'<Relationship Id="rId3" Type="{_REL}/extended-properties" Target="docProps/app.xml"/>'
    '<Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/'
    'core-properties" Target="docProps/core.xml"/>'
    f'<Relationship Id="rId1" Type="{_REL}/officeDocument" Target="word/document.xml"/></Relationships>')
DOC_RELS = (
    f'{XML_HEAD}<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
    f'<Relationship Id="rId1" Type="{_REL}/styles" Target="styles.xml"/>'
    f'<Relationship Id="rId2" Type="{_REL}/numbering" Target="numbering.xml"/>'
    f'<Relationship Id="rId3" Type="{_REL}/settings" Target="settings.xml"/>'
    f'<Relationship Id="rId4" Type="{_REL}/webSettings" Target="webSettings.xml"/>'
    f'<Relationship Id="rId5" Type="{_REL}/fontTable" Target="fontTable.xml"/>'
    f'<Relationship Id="rId6" Type="{_REL}/theme" Target="theme/theme1.xml"/></Relationships>')
PARTS = ("[Content_Types].xml", "_rels/.rels", "docProps/core.xml", "docProps/app.xml",
         "word/_rels/document.xml.rels", "word/document.xml", "word/styles.xml", "word/numbering.xml",
         "word/settings.xml", "word/webSettings.xml", "word/fontTable.xml", "word/theme/theme1.xml")


def docx_bytes(paras, layout, name, when=None):
    when = when or datetime.datetime.now(datetime.timezone.utc)
    parts = {
        "[Content_Types].xml": CONTENT_TYPES, "_rels/.rels": ROOT_RELS,
        "docProps/core.xml": core_props(name, when), "docProps/app.xml": app_props(),
        "word/_rels/document.xml.rels": DOC_RELS, "word/document.xml": document(paras, layout["margins"]),
        "word/styles.xml": styles(layout["font"], layout["size"]), "word/numbering.xml": numbering(),
        "word/settings.xml": settings(), "word/webSettings.xml": web_settings(),
        "word/fontTable.xml": font_table(layout["font"]), "word/theme/theme1.xml": theme(layout["font"]),
    }
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED) as archive:
        for part in PARTS:
            archive.writestr(part, parts[part])
    return buf.getvalue()


def file_stem(name, company):
    people = [w for w in re.sub(r"[^\w\s'-]", " ", cl.strip_credentials(name)).split() if w]
    firm = [w for w in re.sub(r"[^\w\s]", " ", company).split() if w.lower() not in
            {x.rstrip(".") for x in cl.LEGAL}]
    return "_".join(people) + "_CoverLetter_" + "".join(w[:1].upper() + w[1:] for w in firm)


def refuse(reasons):
    print("BUILD REFUSED\n")
    for line in reasons:
        print("  " + line)
    print("\nNothing was written.")
    return 1


def main(argv=None):
    ap = argparse.ArgumentParser(prog="build_letter.py", allow_abbrev=False,
                                 description="Write a cover letter's Word file from its checked text.")
    ap.add_argument("letter", help="the letter's text, in the upload form")
    ap.add_argument("--company", required=True, help="the firm, for the file name")
    ap.add_argument("--resume", help="the resume that goes with the letter, for its font, size and margins")
    ap.add_argument("--out", default=".", help="the folder to write into (default: here)")
    ap.add_argument("--name", help="the writer's name, when the sign-off doesn't give it")
    ap.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    args = ap.parse_args(argv)
    try:
        letter = cl.Letter(args.letter)
    except cl.InputError as exc:
        print(f"The letter can't be built, because {exc}", file=sys.stderr)
        return 2
    reasons = []
    if not letter.salutation:
        reasons.append("No salutation, like 'Dear Ironwood Trail hiring team,'.")
    if not letter.sign_off or not letter.name:
        reasons.append("No sign-off and name at the end.")
    if not letter.header:
        reasons.append("No contact block above the salutation. An uploaded letter opens with the "
                       "resume's contact block.")
    for pat, label in cl.PLACEHOLDERS:
        for m in pat.finditer(letter.raw):
            reasons.append(f"{label} is still in the letter: \"{m.group(0)[:60]}\".")
    if reasons:
        return refuse(reasons)
    name = args.name or letter.name
    layout = resume_layout(args.resume)
    paras = paragraphs(letter, layout)
    pages, lines = cl.estimate_pages([(t, s, b, a) for t, s, _bold, b, a in paras],
                                     layout["font"], layout["margins"], (12240, 15840))
    if pages > 1:
        return refuse([f"The letter fills about {pages:.2f} pages by estimate ({lines} lines). Cut words, "
                       "not spacing, until it fits on one page."])
    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    stem = file_stem(name, args.company)
    docx = out / f"{stem}.docx"
    text = out / f"{stem}.txt"
    docx.write_bytes(docx_bytes(paras, layout, cl.strip_credentials(name)))
    text.write_bytes((letter.raw.strip("\n").translate(STRAIGHT) + "\n").encode("utf-8"))
    if layout["source"] != "defaults":
        where = f"the font, size and margins of {layout['source']} ({layout['font']} {layout['size']:g} point)"
    else:
        where = "Calibri 11 and one-inch margins, since the resume isn't a Word file"
    print(f"{docx.name} and {text.name} written, with {where}.")
    rep = cl.Report()
    cl.check_docx(docx, rep, cl.strip_credentials(name))
    cl.print_report(docx.name, rep)
    return 1 if rep.fails else 0


if __name__ == "__main__":
    sys.exit(main())
