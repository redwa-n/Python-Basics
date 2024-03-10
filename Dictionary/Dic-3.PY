languages = {
    1: 'java',
    2: 'c++',
    3: 'python',
    4: 'R'
}

value_5=languages.get(5,'No value') #set default value by get()
print(value_5)

for name in languages.values():
    print(name.title())
    
for key in languages.keys():
    print(key)
    
for k,v in languages.items():
    print(k,v)  

for k in languages.items():
    print(k) 