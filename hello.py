word = "marii"
with open("lopper.txt","r") as f:
    content = f.read()
    newcontent = content.replace(word,"yako sisya")
    with open("lopper.txt","w") as f:
        f.write(newcontent)
   