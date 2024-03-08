#make empty dic
modes=[]

#make 30 green modes

for mode_number in range(30):
    new_mode={'Name':'c++', 'Speed':100}
    modes.append(new_mode)
    
#show the 5 modes

for mode in modes[:5]:
    print(mode)

print(". . .")

#how many modes i have
print(f"Total modes: {len(modes)}")   


for mode in modes[:2]:
    if mode['Speed']==100:
        mode['Best IDE']='Xcode'
        mode['Compiler']='gcc'

        
for mode in modes[:4]:
    print(mode)

print(". . .")


for mode in modes[0:1]:
    if mode['Best IDE']=='Xcode':
        mode['Operating System']='MAC'
       

        
for mode in modes[:4]:
    print(mode)

print(". . .")