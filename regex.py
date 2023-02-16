#regex function exists as a module
import re
#Regular Expressions : sequence of characters that form a
# used to check if strings contain a pattern
text = "it is quite rainy today"
#search regex method : returns a match object if tehre is any match in the string
x= re.search("^it.*$", text)
print(x)
#findall
#returns a list containing all possible matches
x= re.findall("rainy", text)
print(x)

#split: returns a list where the string has been split at each
x= re.split("\t", text)
print(x)
x= re.split("\s", text, 1)
print(x)

#sub: replaces the searched term with a word of choice
x= re.sub("\s", "4", text)
print(x)