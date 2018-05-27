import re


phone_message = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')

# the mo is the generic name to use for Match Objects
# search method with return Match object
mo = phone_message.search('My number is 415-555-4242.')

print('Phone number found: ' + mo.group())

"""
review of regular expression matching

While there are several steps to using regular expressions in Python, each step is fairly simple

1. Import the regex module with import re
2. Create a regex object with the re.compile() function. (remember to use a raw string.)
3. pass the string you want to search into the regex object's search() method. This returns a Match object.
4. Call the match object's group() method to return a string of the actual matched text.
"""

phone_num_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_num_regex.search('My number is 415-555-4242.')
print(mo.group(1))
print(mo.group(2))
print(mo.group(0))
print(mo.group())
print(mo.groups())


phone_num_regex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo = phone_num_regex.search('My phone number is (415) 555-4242')
print(mo.group(1))
print(mo.group(2))


hero_regex = re.compile(r'Batman|Tina Fey')
mo1 = hero_regex.search('Batman and Tina Fey')
print(mo1.group())

mo2 = hero_regex.search('Tina Fey and Batman')
print(mo2.group())

bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = bat_regex.search('Batmobile lost a wheel')
print(mo.group())
print(mo.group(1))

bat_regex = re.compile(r'Bat(wo)?man')
mo1 = bat_regex.search('The adventures of Batman')
print(mo1.group())

mo2 = bat_regex.search('The adventures of Batwoman')
print(mo2.group())

phone_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo1 = phone_regex.search('My number is 415-555-4242')
print(mo1.group())

mo2 = phone_regex.search('My number is 555-4242')
print(mo2.group())

bat_regex = re.compile(r'Bat(wo)*man')
mo1 = bat_regex.search('The adventures of Batman')
print(mo1.group())

mo2 = bat_regex.search('The adventures of Batwoman')
print(mo2.group())

mo3 = bat_regex.search('The adventures of Batwowowowowoman')
print(mo3.group())

bat_regex = re.compile(r'Bat(wo)+man')
mo1 = bat_regex.search('The adventures of Batwoman')
print(mo1.group())

mo2 = bat_regex.search('The adventures of Batwowowoman')
print(mo2.group())

mo3 = bat_regex.search('The adventures of Batman')
print(mo3 is None)


ha_regex = re.compile(r'(Ha){3}')
mo1 = ha_regex.search("HaHaHa")
print(mo1.group())

mo2 = ha_regex.search("Ha")
print(mo2 is None)

# Python's regular expression are greedy by default, which means that in ambiguous situations they wil match the longest
# string possible. The non-greedy version of teh curly brackets, which matches the shortest string possilbe, has the
# closing curly bracket followed by a question mark.

greed_regex = re.compile(r'(Ha){3,5}')
mo1 = greed_regex.search('HaHaHaHaHa')
print(mo1.group())

non_greedy_regex = re.compile(r'(Ha){3,5}?')
mo2 = non_greedy_regex.search('HaHaHaHaHa')
print(mo2.group())

phone_regex = re.compile(r'\d\d\d\-\d\d\d-\d\d\d\d')
mo = phone_regex.search('Cell: 415-555-9999 Work: 212-555-0000')
print(mo.group())

mo1 = phone_regex.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(mo1)