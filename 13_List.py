marks = [99 ,98 , 95 , "Maths"]
# it is a list which is a data type and it is collection of primitive data types (can be of any kind)

print(marks)
print(marks[1])

print(marks[-1]) # counting from last no.
print(marks[-2])
print(marks[1:3])# only 2nd and 3rd will print

print("------------------------------")
for score in marks:
    print(score)



marks.append(95) # 95 is added to list

marks.insert(0,88) # index(index position , value)

print(marks)

print(88 in marks) # checks exists or not

print(len(marks)) # length of list