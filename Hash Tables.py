d={}
x=int(input())
for i in range(x):
    d[i]=input()
for l,v in d.items():
    print(f"{l} : {v}")

print("===========================================================")
def twosums (nums , target):
    dict={}
    for i in range (len(nums)):
        c=target-nums[i]
        if c in dict:
            return [dict[c],i]
        dict[nums[i]]=i
    return []
t=twosums([2,7,11,15],9)
print(t)
