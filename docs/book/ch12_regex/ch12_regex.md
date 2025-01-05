---
title: RegEx
---
# RegEx
Regular Expression (RegEx) is a useful i extracting and searching a pattern. In Python, `re` module  is the standard library that work with RegEx. To specify a pattern one can use metacharacters `[].^$*+?{}()\|`, Square brackets (`[]`) specify  a set of chracters you wish to match, i.e., `[abcd]` will match if the string you are trying to match contains any of the `a`, `b`, `c`, or `d`. To specify a range, you can use `-`,, i,e '[a-d]' is the same as `[abcd]`. `[1-4]` is the same as `[1234]`. If you use the caret in a  square-bracket, it means the complements: `[^abcd]` means any character except `a` or `b`, `c`, or `d`.  `[^0-9]` means any non-digit character. A period matches any single character: `..` means any string of length two. The caret means start: `^ab` means any string that start with `ab`. The dollar symbol is used to check if a string ends with a certain character. `x$` any patter end to x. `*` 
The following table includes the characters that can be used in  RegEx. 

|--|--|
| `\d` | matches any decimal digit, `[0-9]` |
| `\t` | matches any non-digit character `[^0-9]`| 
| `\n` | matches any newline | 
| `\t` | matches any any tab | 
| `\0` | matches null character | 
| `\s` | matches any whitespace character `[ \t\n\r\f\v]` | 
| `\S` | matches any non-whitespace character `[^ \t\n\r\f\v]` |
| `\w` | matches any alphanumeric character `[a-zA-Z0-9_]` |
| `\W` | matches any non-alphanumeric character `[^a-zA-Z0-9_]` |
| `[ABC]` | one of characters A,B,C |
| `.` | any character except new line. |
| `^A` | not A |
| `+` | one or more of the preceding pattern |
| `*` | zero or more of preceding pattern |
| `?` | matches zero or one occurrence  |
| `a|b` | either a or b matches |
| `(a|c)yz`| Parentheses () is used to group sub-patterns|
| `{n,m}`| least n, and at most m repetitions of the pattern left to it|
|`\A`| Matches if the specified characters are at the start of a string \Athe |
| `\b` |  Matches if the specified characters are at the beginning or end of a word \bmon and mon\b.
|`\B`` | Opposite of \b. Matches if the specified characters are not at the beginning or end of a word . \Bmon and mon\B|

To specify a regular expression in Python, we precede it with r to create raw strings. The following show what trying with and without `r`. 

``` python
pattern = '\t'
print(pattern)
pattern = r'\t'
print(pattern)
```

## match
The `re.match` search for the given pattern, if it occurr, it the span of match object, otherwise it returns None.

``` python
import re

pattern = 'beer'
text= 'beer is cool'
result = re.match(pattern, text)

if result:
  print("Search successful.")
else:
  print("Search unsuccessful.")	
```



## search
`search()` scan through a string, looking for any location where this RE matches

``` python
pattern = r'beer'
text= 'the beer is cold, beer'
result = re.search(pattern, text)
result
```

## findall
`findall()` find all substrings where the RE matches, and returns them as a list


``` python
re.findall('1', '123411')
```

## finditer
`finditer()` find all substrings where the RE matches, and return them as an iterator

``` python
pattern = r'beer'
text= 'beer is cheap, bear'
result = re.finditer(pattern, text)
result
```

since it is a iterator, you can put it in a loop 

``` python 
for m in re.finditer(pattern, text):
    print('%02d-%02d: %s' % (m.start(), m.end(), m.group(0)))
```

## sub
The general syntax of `sub` is `re.sub(pattern, replace, string, count)`. The default `count` is zero and replace the first one, `count=1` will replace all occurrences.

``` python
text= 'beer is cheap, 10$'
re.sub('e','E',text)
url = 'company.com'
re.sub('\.com$', '.ai', url)
```
To count the number of replace, you can use `subn`

## split
The function `splits` drop the string where there is a match and returns a list of strings where the splits have occurred.

``` python
text= 'beer is cheap, 10$'
re.split('is',text)
```

Flag  `maxsplit=1` will replace all occurrences.

## Repetition
In the case you need a repetition, write a bracket infront it and specify the number of times a pattern should repetited, for example `\d{3}` is equvalent to `\d\d\d`. You can specify a range for repitition for example `\d{2,4}` means mathc to ditigal of length, 2, 3, and 4, e.g., 10, 101 and 1010. Using this notation you can state `*` and `+` are  equivalent to {0,} and `{1,}`

## compile
You can compile a regular expression pattern provided as a string into a regex pattern object and you can use the pattern object to search for a match inside different target strings using regex methods such as a re.match() or re.search(). It is useful that you want to use the same pattern over and over again. 


``` python
pattern = r"\d{3}"
regex = re.compile(pattern)
print(type(regex))
str = "the numbers are 1 23 456 7890"
result = regex.findall(str1)
print(result)
```


Useful reference: 
https://regex101.com/
https://docs.python.org/3.12/howto/regex.html