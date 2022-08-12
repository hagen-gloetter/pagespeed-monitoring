import urllib.request
import json
from pathlib import Path

secretAPIKey = Path('secretAPIKey.txt').read_text()
secretAPIKey = secretAPIKey.replace('\n', '')

hostname = "www.hagenfragen.de"
print(secretAPIKey)
url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url=https://" + \
    hostname + "/&strategy=desktop&locale=de&key="+secretAPIKey
print(secretAPIKey)
print(url)

response = urllib.request.urlopen(url)
data = json.loads(response.read())

# debug store the json
with open('debug.json', 'w') as f:
    json.dump(data, f, ensure_ascii=False)

# into seconds (/1000)
fcp = data["loadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]["percentile"]
fid = data["loadingExperience"]["metrics"]["FIRST_INPUT_DELAY_MS"]["percentile"]
lcp = data["loadingExperience"]["metrics"]["LARGEST_CONTENTFUL_PAINT_MS"]["percentile"]
cls = data["loadingExperience"]["metrics"]["CUMULATIVE_LAYOUT_SHIFT_SCORE"]["percentile"]/100

fcp_score = data["loadingExperience"]["metrics"]["FIRST_CONTENTFUL_PAINT_MS"]["category"]
fid_score = data["loadingExperience"]["metrics"]["FIRST_INPUT_DELAY_MS"]["category"]
lcp_score = data["loadingExperience"]["metrics"]["LARGEST_CONTENTFUL_PAINT_MS"]["category"]
cls_score = data["loadingExperience"]["metrics"]["CUMULATIVE_LAYOUT_SHIFT_SCORE"]["category"]

#perf scrore
performance_score = data["lighthouseResult"]["categories"]["performance"]["score"] * 100
print("FCP: "+ str(fcp) )
print("FID: "+ str(fid) )
print("LCP: "+ str(lcp) )
print("CLS: "+ str(cls) )

print ("PerformanceScore: " + str(performance_score))
