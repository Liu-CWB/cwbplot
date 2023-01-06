import cwbplot
from pathlib import Path
import matplotlib
import os
from matplotlib.font_manager import FontProperties

__version__="0.0.8"

GISDATA="/nwpr/ait/p088/package/GISDATA"

verlist = matplotlib.__version__.split(".")
_cntjude4matplt = 0
if int(verlist[0]) < 3:
    _cntjude4matplt = 1
if _cntjude4matplt == 0 and int(verlist[1]) < 2:
    _cntjude4matplt = 1

cwbpakpath = cwbplot.__path__[0]

def font(lang = "en", weight="normal", size = 12):
    if lang.lower() == "en":
        if _cntjude4matplt == 0 and weight == "normal":
            getfont = Path(os.path.join(cwbpakpath, "fonts/times.ttf"))
        elif _cntjude4matplt == 0 and weight == "bold":
            getfont = Path(os.path.join(cwbpakpath, "fonts/timesbd.ttf"))
        elif _cntjude4matplt == 1 and weight == "normal":
            getfont = os.path.join(cwbpakpath, "fonts/times.ttf")
        elif _cntjude4matplt == 1 and weight == "bold":
            getfont = os.path.join(cwbpakpath, "fonts/timesbd.ttf")
    elif lang.lower() == "cht":
        if _cntjude4matplt == 0 and weight == "normal":
            getfont = Path(os.path.join(cwbpakpath, "fonts/TaipeiSansTCBeta-Regular.ttf"))
        elif _cntjude4matplt == 0 and weight == "bold":
            getfont = Path(os.path.join(cwbpakpath, "fonts/TaipeiSansTCBeta-Bold.ttf"))
        elif _cntjude4matplt == 1 and weight == "normal":
            getfont = os.path.join(cwbpakpath, "fonts/TaipeiSansTCBeta-Regular.ttf")
        elif _cntjude4matplt == 1 and weight == "bold":
            getfont = os.path.join(cwbpakpath, "fonts/TaipeiSansTCBeta-Bold.ttf")
    if _cntjude4matplt == 0:
        fontdict = {"fname":getfont,"size":size}
    else:
        fontdict = FontProperties(fname=getfont,size=size)
    return fontdict
