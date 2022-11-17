import requests
import pandas as pd
from datetime import datetime
from cwbplot import opdata
#2022-11-09 11:00:00
def apiget(api=False):
    if api == False:
        print("Plz give the path for api readable")
    else:
        with open(api,"r") as myapi:
            apiapi = myapi.read().rstrip("\n")
    dataid="O-B0045-001"
    dformat="json"
    url = f"https://opendata.cwb.gov.tw/fileapi/v1/opendataapi/{dataid}?Authorization={apiapi}&downloadType=WEB&format={dformat}"
    r = requests.get(url)
    fn = r.json()
    pp = opdata.radarcomp(fn,"json")
    return pp

#["records"]["location"][0]
