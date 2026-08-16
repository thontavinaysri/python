#25341a05l1 vinay
s=input('enter the string:')
vowels=0
consonants=0
digits=0
space=0
for ch in s:
    if ch.lower() in 'aeiou':
        vowels+=1
    elif ch.isalpha():
        consonants+=1
    elif ch.isdigit():
        digits+=1
    elif ch.isspace():
        space+=1

print('vowels:',vowels)
print('consonants:',consonants)
print('digits:',digits)
print('spaces:',space)

''' output
enter the string:maybe he is not player 121
vowels: 7
consonants: 11
digits: 3
spaces: 5
'''