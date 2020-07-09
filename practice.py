def func1(phrase):
    interro = ("how","whom","why","where")
    capitalised = phrase.capitalize()
    if phrase.startswith(interro):
        return "{}?".format(capitalised)
    else:
        return "{}.".format(capitalised)
final1 = []

while True:
    user_data = input("enter data: ") 

    if user_data == "\end":
        break
    else:
        final1.append(func1(user_data))
print(" ".join(final1))        
       




         
