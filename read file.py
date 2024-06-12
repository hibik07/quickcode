
AddressAll=[]
with open("C:\\Users\\lenovo\\Desktop\\address-some.txt", encoding='utf-8') as f: 
    for line in f.readlines():
        print(line)
        AddressAll.append(line)
print(AddressAll)

