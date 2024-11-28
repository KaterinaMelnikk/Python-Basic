def is_palindrome(text):
    cleaned_text= ''
    for char in text:
        if char.isalnum():
            cleaned_text = cleaned_text + char.lower()
    reversed_text = cleaned_text[::-1]
    #print(reversed_text == cleaned_text) #Перевірка
    return reversed_text == cleaned_text

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")