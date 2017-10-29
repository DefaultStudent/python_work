favorite_language = {
    'jen': 'python',
    'sarach': 'c',
    'edward': 'ruby',
    'phil': 'python'
     }

print ("The following languages have been mentioned:")
for language in favorite_language.values():
    print (language.title())

print ('\n')

# use the 'set'
for language1 in set(favorite_language.values()):
    print (language1.title())