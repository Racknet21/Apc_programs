#1.
text = input("Enter a string: ")

count = 0

for ch in text:
    count = count + 1

print("Length of string:", count)

#2.
text = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for ch in text:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    else:
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)

#3.
text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

print("Reversed string:", reverse)

#4.
text = input("Enter a string: ")

reverse = ""

for ch in text:
    reverse = ch + reverse

if text == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")

#5.
text = input("Enter a string: ")

upper = 0
lower = 0

for ch in text:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)

#6.
text = input("Enter a string: ")
old = input("Enter character to replace: ")
new = input("Enter new character: ")

result = ""

for ch in text:
    if ch == old:
        result = result + new
    else:
        result = result + ch

print("Updated string:", result)


#7.
text = input("Enter a string: ")

result = ""

for ch in text:
    if ch != " ":
        result = result + ch

print("String without spaces:", result)

#8.
text = input("Enter a string: ")
character = input("Enter character to count: ")

count = 0

for ch in text:
    if ch == character:
        count += 1

print("Frequency:", count)

#9.
text = input("Enter a string: ")

if text != "":
    print("First character:", text[0])
    print("Last character:", text[-1])
else:
    print("String is empty")

#10.
text = input("Enter a string: ")

for ch in text:
    print(ch, "=", ord(ch))

#11.
text = input("Enter a sentence: ")

words = text.split()

print("Total words:", len(words))

#12.
text = input("Enter a sentence: ")

words = text.split()
longest = words[0]

for word in words:
    if len(word) > len(longest):
        longest = word

print("Longest word:", longest)

#13.
text = input("Enter a sentence: ")

words = text.split()
shortest = words[0]

for word in words:
    if len(word) < len(shortest):
        shortest = word

print("Shortest word:", shortest)

#14.
text = input("Enter a sentence: ")

result = text.title()

print("Title case:", result)

#15.
text = input("Enter a string: ")

checked = ""

for ch in text:
    if text.count(ch) > 1 and ch not in checked:
        print(ch)
        checked = checked + ch

#16.
text = input("Enter a string: ")

checked = ""

for ch in text:
    if ch not in checked:
        count = text.count(ch)
        print(ch, ":", count)
        checked = checked + ch

#17.
text1 = input("Enter first string: ")
text2 = input("Enter second string: ")

text1 = text1.replace(" ", "").lower()
text2 = text2.replace(" ", "").lower()

if sorted(text1) == sorted(text2):
    print("Strings are anagrams")
else:
    print("Strings are not anagrams")

#18.
text = input("Enter a string: ")

result = ""

for ch in text:
    if ch not in result:
        result = result + ch

print("String without duplicates:", result)

#19.
text = input("Enter the main string: ")
sub = input("Enter substring to search: ")

if sub in text:
    print("Substring found")
else:
    print("Substring not found")

#20.
text = input("Enter a sentence: ")
word = input("Enter word to count: ")

words = text.split()
count = 0

for w in words:
    if w == word:
        count += 1

print("Word frequency:", count)

#21.
password = input("Enter password: ")

upper = False
lower = False
digit = False
special = False

for ch in password:
    if ch.isupper():
        upper = True
    elif ch.islower():
        lower = True
    elif ch.isdigit():
        digit = True
    else:
        special = True

if len(password) >= 8 and upper and lower and digit and special:
    print("Valid password")
else:
    print("Invalid password")

#22.
text = input("Enter a string: ")

result = ""
count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count += 1
    else:
        result = result + text[i - 1] + str(count)
        count = 1

if text != "":
    result = result + text[-1] + str(count)

print("Compressed string:", result)

#23.
text = input("Enter a string: ")

result = ""
count = 1

for i in range(1, len(text)):
    if text[i] == text[i - 1]:
        count += 1
    else:
        result = result + text[i - 1] + str(count)
        count = 1

if text != "":
    result = result + text[-1] + str(count)

if len(result) < len(text):
    print("Compressed string:", result)
else:
    print("Original string:", text)

#24.
text = input("Enter a string: ")

most = text[0]
maximum = 0

for ch in text:
    count = text.count(ch)

    if count > maximum:
        maximum = count
        most = ch

print("Most frequent character:", most)
print("Frequency:", maximum)

#25.
text = input("Enter a string: ")

characters = ""

for ch in text:
    if ch not in characters:
        characters = characters + ch

first = ""
second = ""
max1 = 0
max2 = 0

for ch in characters:
    count = text.count(ch)

    if count > max1:
        max2 = max1
        second = first

        max1 = count
        first = ch

    elif count > max2:
        max2 = count
        second = ch

if second != "":
    print("Second most frequent character:", second)
    print("Frequency:", max2)
else:
    print("No second most frequent character")

#26.
text = input("Enter a message: ")
shift = int(input("Enter shift value: "))

encrypted = ""

for ch in text:
    if ch.isupper():
        new = (ord(ch) - 65 + shift) % 26 + 65
        encrypted = encrypted + chr(new)

    elif ch.islower():
        new = (ord(ch) - 97 + shift) % 26 + 97
        encrypted = encrypted + chr(new)

    else:
        encrypted = encrypted + ch

print("Encrypted message:", encrypted)

decrypted = ""

for ch in encrypted:
    if ch.isupper():
        new = (ord(ch) - 65 - shift) % 26 + 65
        decrypted = decrypted + chr(new)

    elif ch.islower():
        new = (ord(ch) - 97 - shift) % 26 + 97
        decrypted = decrypted + chr(new)

    else:
        decrypted = decrypted + ch

print("Decrypted message:", decrypted)

#27.
email = input("Enter email address: ")

if "@" in email and "." in email and email.index("@") < email.rfind("."):
    print("Valid email format")
else:
    print("Invalid email format")
    

#28.
text = input("Enter a paragraph: ")

words = text.lower().split()
checked = []

for word in words:
    if word not in checked:
        count = words.count(word)
        print(word, ":", count)
        checked.append(word)

#29.
text = input("Enter a sentence: ")

words = text.split()
words.reverse()

result = " ".join(words)

print("Reversed sentence:", result)

#30.
text1 = input("Enter first string: ")
text2 = input("Enter second string: ")

if len(text1) == len(text2) and text2 in text1 + text1:
    print("Yes, it is a rotation")
else:
    print("No, it is not a rotation")
