def build_person(first_name, last_name, age = ''):
    """return a dictory include a person info"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musuician = build_person('jimi', 'hendrix', age=27)
print (musuician)