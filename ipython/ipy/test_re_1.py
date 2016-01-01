# coding: utf-8
# test_re_1.py

import re

regex = re.compile('\s+')

text = """Dave dave@google.com
Steve steve@gmail.com
Rob rob@gmail.com
Ryan ryan@yahoo.com
"""

pattern = r'[A-Z0-9._%+-]+@[A-Z0-9._]+\.[A-Z]{2,4]'

l = regex.findall(text)

m = regex.search(text)

print(m)

print(text[m.start():m.end()]

#print(regex.match(text))
#print(regex.sub('REDACTED', text))

regex = re.compile(pattern, flags=re.IGNORECASE)

m = regex.match('wesm@bright.net')
print(m.groups())

print(regex.findall(text))

