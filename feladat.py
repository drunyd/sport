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