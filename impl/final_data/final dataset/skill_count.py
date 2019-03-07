import json
from pprint import pprint

profiles = []
profiles.append(json.load(open("SE_37.json")))
profiles.append(json.load(open("ASA_6.json")))
profiles.append(json.load(open("ATL10.json")))
profiles.append(json.load(open("PM_12.json")))
profiles.append(json.load(open("SA_7.json")))
profiles.append(json.load(open("SE Intern_11.json")))
profiles.append(json.load(open("SE_37.json")))
profiles.append(json.load(open("SSE_26.json")))

skillset = set()
for profile in profiles:
    for p in profile:
        skillset.update(map(str.strip, p['allSkills'].split(',')))

lang_frameworks = json.load(open("lang_frameworks.json"))

listedset = set()
for lang in lang_frameworks.values():
    listedset.update(lang)

pprint(list(skillset-listedset))
# pprint(listedset)
# pprint(skillset)