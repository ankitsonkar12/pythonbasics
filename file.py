with open("file1.txt" ,"a+") as myfile:
    myfile.write("\nbeans")
    myfile.seek(0)

    context = myfile.read()
    
    print(context)  