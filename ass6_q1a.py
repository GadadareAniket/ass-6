import json
s = json.dumps(Employees)
print(s)

with open("D:\\employees.json.txt","w") as f:
  f.write(s)