favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python'
}

people_to_interview = ['jen', 'james', 'kirk', 'john', 'phil', 'cliff']

for person in people_to_interview:
    if person in favorite_languages:
        print(f'{person.title()}, thanks for taking part in the interview!')
    else:
        print(f'{person.title()}, please take part in the interview.')
