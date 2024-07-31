import json
with open("workouts.json" ,"r",encoding="utf-8") as f:
    data=json.load(f)
print(data)
for ember in data["members"]:
    print(f"nev:{ember['name']},kor:{ember['age']}")
osszsuly=0
for ember in data["members"]:
    osszsuly+=ember["weight"]
print(osszsuly)
atlagsuly=osszsuly/len(data["members"])
print(atlagsuly)
def szures(Data,tipus):
    visszertek={}
    for ember in data["members"]:
        szamlalo=0
        for w in ember["workouts"]:
            if w["type"]==tipus:
                szamlalo+=1
        visszertek[ember["name"]]=szamlalo
    return(visszertek)

    
szurtadatok=szures(data,"futás")
print(szurtadatok)
