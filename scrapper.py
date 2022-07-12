#! python3

import re, pyperclip

#create a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0199, 555-0199, (801) 555-0199, 555-0199 ext 12345, ext. 12345, x12345

(
((\d\d\d) | (\(\d\d\d\)))?     #area code (optional)
(\s|-)       #first seperator
\d\d\d       #first 3 digits
-       #seperator
\d\d\d\d       #last 4 digits
(((ext(\.)?\s)|x)        #extension word part (optional)
(\d{2,5}))?         #extension num part (optional)
)
''', re.VERBOSE)

#create a regex for emails
emailRegex = re.compile(r'''
#some.+_thing@(\d{2,5}))?.com

[a-zA-Z0-9_.+]+    #name
@    #@symbol
[a-zA-Z0-9_.+]+    #domain name

''', re.VERBOSE)

#get the text off the keyboard
text = pyperclip.paste()

#extract email/phoner from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

#copy the extracted email/phone to the clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
