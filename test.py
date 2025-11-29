
indx = 0
ip = "la\nlbl\nalab\n\nbbbb\nballb\nalab\n"
for i in range(int(input("enter number of listed ip"))):
    indx = ("x"*(indx+1)+ip[indx+1:]).find("\n")
    print(ip)
print(indx)
print(ip[indx])
print(len(ip))