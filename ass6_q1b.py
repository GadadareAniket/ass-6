import json

capitals={
    "Karnataka":"Bengaluru",
    "TamilNadu":"Chennai",
    "Kerala":"Trivandram",
    "AndhraPradesh":"Hyderabad",
    "Maharashtra":"Mumbai",
    "Bihar":"Patna",
    "Jharkand":"Ranchi"
}

p = json.dumps(capitals)
print(p)