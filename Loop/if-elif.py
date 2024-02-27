
number=int(input("Num: "))

if (number>0):
    print("Pos")
elif (number<0):
    print("Neg")
else:
    print("zero")

cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
     print(cars[-2])
else :
    print(cars[2])
cars = ['toyota', 'honda', 'bmw', 'ford', 'chevrolet']

for car in cars:
    if car == 'bmw':
        print(cars[-2])

else:
    print(cars[2])

algo=['KNN', 'BFS' ,'DFS']
another = 'knapsack'

if another not in algo:
    print("false")
    print(f"{another.title()}, is one of the best Algorithm")