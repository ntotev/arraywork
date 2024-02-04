#python comprehensions
#list comprehensions is a precise way to create lists or to create a subsequence of those elements that satisfy a certain condition
names=["Nicholas","Tom","Malcolm","Ella","AJ","Bryson","Kaya","Mia","Stephen","Julian","Nick"]
Da_Peeps=[]
for name in names:
  Da_Peeps.append(name)
  print(Da_Peeps)

new_list=[n for n in names]
print(new_list)

n=[(a,b)for a in range(1,11) for b in range (1,11)]
print(n)

Da_Peeps=[]
for name in names:
  if name.startswith("N"):
    Da_Peeps.append(name)
print(Da_Peeps)

numbers=[1,2,3,4,5,6,7,8,9,10]
new_numbers=[n*2 if n%2==1 else n for n in numbers]
print(new_numbers)