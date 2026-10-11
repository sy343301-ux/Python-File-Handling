file=open("demo3.txt","x+")
data=file.write("\n Adding New Line Here")
file.seek(0)
print(data)