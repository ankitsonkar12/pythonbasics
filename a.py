def foo(*args):
    return sum(args) / len(args)
print(foo(12,13,14,15))    
def foo1(*args):
    args = [i.upper() for i in args]
    return sorted(args)
print(foo1("a","fg","ter","bg"))  

def foo(*args):
    return sum(args) / len(args)
print(foo(12,13,14,15))    

def transform(phrase):
    interro = ("how","who","why")
    capitalised = phrase.capitalize()
    if phrase.startswith(interro):
        return "{}?".format(capitalised)
    else:
        return "{}.".format(capitalised)
fin_phrase = []
while True:
    datain = input("please enter you text here: ")
    if datain =="\end":
        break
    else:
        fin_phrase.append(transform(datain))
print(" ".join(fin_phrase))            


