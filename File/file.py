with open("data.txt","r+") as new:
    data = new.read()
    print(data)

# with open("hello.docx","w+") as old:
#     f = old.writelines("hello guys")
#     print(f)

with open("hello.docx","r+") as old:
    f = old.read()
    print(f)
    old.write("\nmodule:EC2 \nCloud:AWS")
    old.seek(0)
    print("after adding")
    f = old.read()
    print(f)

with open ("og.jpg","br") as img:
    data = img.read()
with open ("copyOG.jpg","bw") as img2:
    dat = img2.write(data)
    




    



