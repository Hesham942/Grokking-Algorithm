def hi(x):
    if (x == 0):
        return
    else:
        print(f"hi it's {x} item")
        hi(x-1)

hi(5)

print("==================================================================================================== ")

def fact(x):
  if x == 1:
    return 1
  else:
    return x * fact(x-1)

print(fact(5))