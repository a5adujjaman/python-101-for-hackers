if True:
    print("True")

if False:
    print("False") # this won't print

if not False:
    print("not false")

if 1<1:
    print("1<1")
elif 1<=1: #elif 1<=0: this won't also print
    print("1 <= 1")
    print("here")
else:
    print("else 1")

if 1 < 1:
    print("1<1")
elif 1<1:
    print("1<=1")
elif 2<2:
    print("2<=2")
else:
    print("else reached")
if 1>0 and 0<1:
    print("1 > 0 and 0 < 1")

if 1 < 0 and 0 > 1:
    print("1 < 0 and  0 < 1")

if 1 < 0 or 0 < 1:
    print("1 < 0 or 0 < 1")

if (1 < 0 or 0 < 1) or 1 == 0: # right side doesn't matter if inside parenthesis are True

    print("1 < 0 or 0 < 1")

if 0 < 1: print("0 < 1")
print("1 >= 1") if 1 >= 1 else print("1 < 1")

if 1 >= 1:
    print("1 >= 1")
else:
    print("1 < 1")

if 0 < 0:
    print("1")
elif 0 > 1:
    print("2")
else:
    print("3")

print("1") if 0 < 0 else print("2") if 0 > 1 else print("3")
