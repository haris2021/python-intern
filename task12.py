import  json
x={
    "Name":"John",
    "Age":30,
    "city":"New York",
    "grade": None,
    "result": True,
    "marks1":{"maths":98,"CS":99},
    "marks2":[90,98,89],
    "avg":97.99
}
y=json.dumps(x)
print(y)
print(json.dumps((1,2,3)))
print(json.dumps(list(range(9))))
