magicians=['A','B','C','D']

Letters=magicians[ : ] #doesnt exist same value

print(Letters)

magicians.append('E')
Letters.append('F')
print(magicians)
print(Letters)


Letters=magicians #for existing same value
magicians.append('E')
Letters.append('F')
print(magicians)
print(Letters)

print (Letters [1:2])
print (Letters [:2])
print (Letters [1:])
print (Letters [1:1])
print (Letters [0:2])

simnto=('simla','nusrat')
for x in simnto:
    print(x)
    
    simnto=('keunai','asoleikeunai')
    for s in simnto:{
    print(s)
    }