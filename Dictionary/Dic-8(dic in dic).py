Bedroom={
    'Turzo':{
        'First':'Iffti Hasan',
        'Last': 'Turzo',
        'District':'Gopalganj',
        'Phone': '01997905152'
    },
    'Redwan':{
        'First':'Kazi',
        'Last': 'Redwan',
        'District':'Gopalganj',
        'Phone': '01746244900' 
    }
}

for name,info in Bedroom.items():
    print(name,info)
    print(Bedroom.keys())
    print(f"\nUsername:{name}")
    fullName=f"{info['First']} {info['Last']}"
    location=info['District']
    contact=info['Phone']
    
    print(f"\tFull Name: {fullName.title()}")
    print(f"\tLocation: {location.title()}")
    print(f"\tContact: {contact}")