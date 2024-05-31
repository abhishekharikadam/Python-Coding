letter = '''Dear <|NAME|>,
Grettings from Kadam's house. We are happy to tell you about your selection.
You are selected
Have a great day ahead!
Thanks and regards,
Kadam...
Date:- <|DATE|>
'''

letter = letter.replace('<|NAME|>', 'Abhishek')
letter = letter.replace('<|DATE|>', '22/05/2024')

print(letter)