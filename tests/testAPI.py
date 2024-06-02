from os import getenv
import json
from reqdb import ReqDB, models

with open("tests/asvs.json") as f:
    asvs = json.load(f)

client = ReqDB("127.0.0.1:3000", getenv("REQDB_ACCESS_TOKEN"), True)

l1 = client.Tags.add(models.Tag(name="Level 1"))
l2 = client.Tags.add(models.Tag(name="Level 2"))
l3 = client.Tags.add(models.Tag(name="Level 3"))

nist = client.ExtraTypes.add(models.ExtraType(title="NIST Ref", extraType=1, description="NIST Reference"))
cve = client.ExtraTypes.add(models.ExtraType(title="CVE Ref", extraType=1, description="CVE Reference"))

rootTopics = []

for itemL1 in asvs["Requirements"]:
    parentL1 = client.Topics.add(models.Topic(
        key=itemL1["Shortcode"],
        title=itemL1["ShortName"],
        description=itemL1["Name"],
    ))
    rootTopics.append(parentL1)
    for itemL2 in itemL1["Items"]:
        parentL2 = client.Topics.add(models.Topic(
            key=itemL2["Shortcode"],
            title=itemL2["Name"],
            description=itemL2["Name"],
            parent=parentL1
        ))
        for itemL3 in itemL2["Items"]:
            t = []
            if itemL3["L1"]["Required"] is True:
                t.append(l1)
            if itemL3["L2"]["Required"] is True:
                t.append(l2)
            if itemL3["L3"]["Required"] is True:
                t.append(l3)
            requirement = client.Requirements.add(models.Requirement(
                key=itemL3["Shortcode"],
                title=itemL3["Shortcode"] + " " + itemL2["Name"],
                description=itemL3["Description"],
                parent=parentL2,
                tags=t
            ))
            if itemL3["CWE"] != []:
                client.ExtraEntries.add(models.ExtraEntry(
                        content="\n".join(str(n) for n in itemL3["CWE"]),
                        extraTypeId=cve["id"], requirementId=requirement["id"]
                    )
                )
            if itemL3["NIST"] != []:
                client.ExtraEntries.add(models.ExtraEntry(
                        content="\n".join(str(n) for n in itemL3["NIST"]),
                        extraTypeId=nist["id"], requirementId=requirement["id"]
                    )
                )

catalogue = client.Catalogues.add(models.Catalogue(
    title=asvs["Name"],
    description=asvs["Description"],
    topics=rootTopics))
