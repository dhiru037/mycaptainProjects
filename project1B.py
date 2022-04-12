filename=input("Input the Filename")
if filename.endswith(".py"):
    print("Extension of the file is: 'python'")
elif filename.endswith(".c"):
    print("Extension of the file is: 'c'")
elif filename.endswith(".java"):
    print("Extension of the file is: 'java'")
else:
    print("Other extension")
