---
title: RegEx Challange
---
# RegEx Challange

Consider "the quick brown fox jumps over the lazy dog" as text, 
a) Search for `o` and show adjacent characters:
b) Search for three-letter words enclosed by whitespace:
c) Substitute any of `dflj` by a `w`:


```python 
import re
text = "the quick brown fox jumps over the lazy dog"
print(re.findall(".o.", text))
print(re.findall("\s(\wo\w)\s*", text))
print(re.sub("[dflj]", "w", text))
print(re.search('jumps|swims', text))
```

Recognize phone numbers in Germany
```python 
import re
pattern = re.compile("(00|0 0|\+)\s*4\s*9[0-9 ]+")
text = [
"0049 190 34 57 90",
"+49 190 34 57 90",
"00 00 00 49 190 34 57 90 33",
"00 49 190 34 57 90",
"0049190345790",
"+48 60 60 606 9",
"+41 55 55 55 55"
]
for e in text:
    if pattern.match(e):
        print(e, "is a German phone number")
    else:
        print(e, "is some other number")
```

checking if a string starts with '>'
```python 
import re;
p = re.compile( '^>' )
m = p.match( '>hello' )
if m:
    print 'Match found: ', m.group()
else:
    print 'No match'
```

matchin more than one pattern on the same string
```python
m=re.search("^>|^#",line)
if m:
    print 'Match found: ', m.group()
```


Consider a text "All digits are 0 12 245 6789"
a) pattern to find three consecutive digits
b) compile string pattern to re.Pattern object
c) print the type of compiled pattern


import re
str = "All digits are 0 12 245 6789"
string_pattern = r"\d{3}"
regex_pattern = re.compile(string_pattern)
print(type(regex_pattern))
result = regex_pattern.findall(str)
print(result)
