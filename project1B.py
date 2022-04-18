filename=input("Input the Filename")
name, extension=filename.split('.')
if extension=='py':
    print("The extension of the file is: python")
elif extension=='c':
    print("The extension of the file is: c")
elif extension=='java':
    print("The extension of the file is: java")
elif extension=='js':
    print("The extension of the file is: java script")
elif extension=='html':
    print("The extension of the file is: HTML")
else:
    print("Some other extension")

