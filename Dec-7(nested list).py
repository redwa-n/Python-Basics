favorite_languages={
    'Redwan':['C++','Python'],
    'Simanto':['Python','JavaScript'],
    'Turzo':['HTML','CSS'],
    'Rudro':['C++','Java']
}

for name,languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language are: ")
    for language in languages:
        print(f"\t{language.title()}")