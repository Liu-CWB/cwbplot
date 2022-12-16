import json, requests, sys
import pandas as pd
import numpy as np
from datetime import datetime

def apiapi(api,subdivs = False):
    with open(api,"r") as myapi:
        apiapi = myapi.read().rstrip("\n")
    dataid="F-D0047-011"
    dformat="json"
    url = f"https://opendata.cwb.gov.tw/api/v1/rest/datastore/{dataid}?Authorization={apiapi}&format={dformat}"
    r = requests.get(url)
    fn = r.json()
    collout = []
    df = pd.DataFrame([])
    countyname = fn["records"]["locations"][0]["locationsName"]
    for stn in range(len(fn["records"]["locations"][0]["location"])):
        dicts =  fn["records"]["locations"][0]["location"][0].keys()
        metidx = []
        coll = []
        header = []
        subdivision = []
        cnt = 1
        for dic in dicts:
            fndict = fn["records"]["locations"][0]["location"][stn][dic]
            if dic == "locationName":
                subdivision.append(fndict)
                header.append("subdivsion")
            elif dic == "weatherElement":
                for element in range(len(fndict)):
                    coll.append(countyname + fn["records"]["locations"][0]["location"][stn]["locationName"])
                    metidx.append(fndict[element]["elementName"])
                    if fndict[element]["elementName"] == "UVI":
                        count = float(len(fndict[element]["time"]))
                        hdlen = float((len(header) - 1)/2)
                        if count != hdlen:
                            coll.append(" ")
                        for metvar in range(len(fndict[element]["time"])):
                            coll.append(fndict[element]["time"][metvar]["elementValue"][0]["value"])
                            coll.append(fndict[element]["time"][metvar]["elementValue"][0]["value"])
                    elif fndict[element]["elementName"] != "UVI":
                        for metvar in range(len(fndict[element]["time"])):
                            if cnt == 1:
                                timestamp_st = fndict[element]["time"][metvar]["startTime"]
                                timestamp_st = datetime.strptime(timestamp_st,"%Y-%m-%d %H:%M:%S")
                                timestamp_ed = fndict[element]["time"][metvar]["endTime"]
                                timestamp_ed = datetime.strptime(timestamp_ed,"%Y-%m-%d %H:%M:%S")
                                header.append(timestamp_st.strftime("%y%m%d%H")+ "-" + timestamp_ed.strftime("%y%m%d%H"))
                            coll.append(fndict[element]["time"][metvar]["elementValue"][0]["value"])
                        cnt = 2
        dftemp = pd.DataFrame(np.array(coll).reshape(-1,len(fndict[element]["time"])+1),index=metidx,columns=header)
        df = pd.concat([df,dftemp])
    if subdivs:
        df = df.query("subdivsion == '{}'".format(subdivs))
    return df
