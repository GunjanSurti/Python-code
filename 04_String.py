name = "Tony Stark"

print(name.upper)
print(name.find("s"))  #-1 bcz case sensitive
print(name.find("S"))
print(name.find("tark"))

print(name.replace("Tony Stark" , "Iron Man"))#does not change original string

print(name.replace("Stark" , "Iron Man"))
print(name)
print("S" in name)