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

#right justification of the string

print(string4.rjust(25))
print(string4.rjust(25,"X"))

#left justification of  string

#we have to know python string are immutable(that mean cannot be change after it create)

print(string4.ljust(25))
print(string4.ljust(25,"X"))


print("I am " + "a srting")
print("string4 is " + str(len(string4)) + " characters long")
print(1+1)
print("1" + "1")
print(type("1" + "1"))


print("string4 is {} characters long" .format(len(string4)))
print("{} {} {}".format(len(string4), 5.0, 0x12))

print("{0} {2} {1}".format(len(string4), 5.0, 0x12))
print("{length}".format(length=len(string4)))


length = len(string4)
print(f"string4 is {length} characters long")

#for different floating numbers
print("string4 is {length:.2f} characters long".format(length=len(string4)))
print("string4 is {length:.5f} characters long".format(length=len(string4)))
print("string4 is {length:.7f} characters long".format(length=len(string4)))

#for hex binary octal
print("string4 is {length:x} characters long".format(length=len(string4)))
print("string4 is {length:b} characters long".format(length=len(string4)))
print("string4 is {length:o} characters long".format(length=len(string4)))

also by this
print("string4 is %d characters long!" % len(string4))
print("string4 is %f characters long!" % len(string4))
print("string4 is %x characters long!" % len(string4))
