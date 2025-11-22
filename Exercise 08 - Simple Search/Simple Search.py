names=["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
target="Sam"
found=False
for name in names:
    if name==target:
        found=True
        break
if found:
    print("Sam was found in the list!")
else:
    print("Sam was NOT found in the list.")
    
