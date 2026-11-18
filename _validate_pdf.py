import re, zlib
from pathlib import Path
p = Path(__file__).resolve().parent / "entrega" / "GlobalSolution_Grupo49.pdf"
data = p.read_bytes()
print("bytes:", len(data))
streams = re.findall(rb"stream\r?\n(.*?)\r?\nendstream", data, re.DOTALL)
print("streams:", len(streams))
txt = []
for s in streams:
    try:
        d = zlib.decompress(s)
        for m in re.findall(rb"\((?:[^()\\]|\\.)*\)", d):
            txt.append(m[1:-1].decode("latin-1", "replace"))
    except Exception as e:
        pass
joined = " ".join(txt)
print("texto extraido (", len(joined), "chars):")
print(joined[:1500])
