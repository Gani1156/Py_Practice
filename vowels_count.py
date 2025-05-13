def vowel(phrase): #GanEsH
    count = ''
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
             count = count + 'G'
            else:
                count = count + 'g'
        else:
            count = count + letter
    return count
'''
ganesh koritala
rajesh koritala 
rocky koritala             #comments
lakshmi koritala 
lakshmi narayana koritala
'''
print(vowel(input('Enter a phrase: ')))