a = open("event1.txt", "r")
c = a.read()
b = c.split(" ")
count = 0
for i in range(len(b)): 
    if b[i] == "free":
        count = count + 1
print count
