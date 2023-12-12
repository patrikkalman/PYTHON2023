program=[]
f=open("program.txt", "r")
for sor in f:
    program.append(sor.strip())
f.close()
print(program) 