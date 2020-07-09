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
