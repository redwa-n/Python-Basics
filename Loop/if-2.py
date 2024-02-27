alien_color=[]
alien_color.append('green')
alien_color.append('yellow')
alien_color.append('red')
print(alien_color)

for color in alien_color:
    if (color == 'green') :
        print(f"Player earned {color} T-shirt")

number=int(input("Num: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Its Zero")

if number%2==0:
    print("Even Number")
else:
    print("Odd number")