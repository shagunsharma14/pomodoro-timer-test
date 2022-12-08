import re
phoneNumRegex=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo=phoneNumRegex.search('cell:415-555-9999 work:415-555-9999')
print(mo.group())

