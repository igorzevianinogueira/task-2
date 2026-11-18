from fpdf import FPDF
import re, zlib

def gen(text, fname):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 18)
    try:
        pdf.multi_cell(0, 10, text)
        err = None
    except Exception as e:
        err = repr(e)
    pdf.output(fname)
    data = open(fname, "rb").read()
    streams = re.findall(rb"stream\r?\n(.*?)\r?\nendstream", data, re.DOTALL)
    found = []
    for s in streams:
        try:
            d = zlib.decompress(s)
            found += [m[1:-1].decode("latin-1","replace") for m in re.findall(rb"\((?:[^()\\]|\\.)*\)", d)]
        except Exception:
            pass
    print(f"[{fname}] err={err} bytes={len(data)} text={found}")

gen("Global Solution puro ASCII", "/tmp/a.pdf")
gen("Global Solution \u2014 TerraOps", "/tmp/b.pdf")
gen("acentos cao coracao ph", "/tmp/c.pdf")
