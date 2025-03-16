#string formatting

#single line string
#multi line string

string1 = "i am a string"
string2 = 'I am a string'


print(string1)
print(string2)


string3 = """I am a long
long
string """


print(string3)




string6 = "I\"m a string \nI\"m on a newline!"
string6 = "\\ \x41\x42\x43"
print(string6)

string7="aaaaaaaaaa"
print(string7)

string7 = "a" * 10
print(string7)

string3 = "Hello My Name is Ashu"

print(len(string7))

print("neut" in string3)

print(string3.startswith("I"))
print(string3.startswith("n"))

print(string1.index("string"))


print(string3.upper())
print(string3.lower())


messy_string = "Messy, String"

print(messy_string)
print(messy_string.strip())

print(messy_string.replace("!", "?").strip())


print(messy_string.split(","))
print(messy_string.split())

string4 = "I am a string!"
print(string4)
print(string4.encode())

#in python3 all strings are represented as unicode

print(string4.encode("utf-8"))

#right justification

print(string4.rjust(25))
print(string4.rjust(25,"X"))

#left justification
print(string4.ljust(25))
print(string4.ljust(25,"X"))
