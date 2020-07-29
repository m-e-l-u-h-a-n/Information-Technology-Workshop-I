setx = set(["apple", "mango"])
sety = set(["mango", "orange"])
setz = setx & sety

setb = setx - setz
print('union',setx|sety)
print('intersection: ',setb)
print('diffrence: ',setb)
