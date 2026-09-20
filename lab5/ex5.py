#25341a05l1 vinay
a=input('enter the string:')
vowels=0
consonants=0
digit=0
space=0
for ch in a:
    if ch.lower() in 'aeiou':
        vowels+=1
    elif ch.isalpha():
        consonants+=1
    elif ch.isdigit():
        digit+=1
    elif ch.isspace():
        space+=1
print('vowels:',vowels)
print('consonants:',consonants) 
print('digits:',digit)
print('spaces:',space)

''' output
enter the string:gmail is v6309
vowels: 3
consonants: 5
digits: 4
spaces: 2
'''