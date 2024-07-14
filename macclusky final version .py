from collections import Counter
from nltk import flatten



def Finder(bin1,bin2,bites):
    
    list1 = []
    list2 = []
    finall_list = []
    dict = {}
    for i,v in enumerate(bin1):
        list1.append(list(v))
    for i,v in enumerate(bin2):
        list2.append(list(v))
    for i in range(len(bin1)):
        for j in range(len(bin2)):
            flagg = 0
            flag = 0
            for b_counter in range(bites):
                if(list1[i][b_counter]==list2[j][b_counter]):
                    finall_list.append(list(list1[i][b_counter]))
                else:
                    flagg+=1
                    if(flagg==2):
                        del finall_list[-b_counter:]
                        flag = 1
                        break
                    decoy = "-"
                    finall_list.append(list(decoy))
            if (flag!=1):
                flat_list = [item for sublist in finall_list for item in sublist]
                key = (int(bin1[i], 2), int(bin2[j], 2))
                value = ''.join(flat_list)
                dict[key] = value
                finall_list.clear()
    filtered_dict = {key: value for key, value in dict.items() if value}
    return(filtered_dict)



def Second_thought(number,y):
    dictionary =number
    fake_dictionary = dictionary.copy()
    list_tuple = []
    list_i = []
    list_j = []
    finall_list = []
    flag1 = []
    flag2 = []
    dictt = {}
    flag_origin = []
    for i in dictionary.keys():
        list_tuple.append(i)
    flattened_list = [element for tup in list_tuple for element in tup]
    for i in range(len(dictionary)-1):
        for q,v in enumerate(dictionary[list_tuple[i]]):
            list_i.append(list(v))
            key1 = list_tuple[i]
        for j in range(i+1,len(dictionary)):
            for q,v in enumerate(dictionary[list_tuple[j]]):
                list_j.append(list(v))
            key2 = list_tuple[j]
            flagg = 0
            flag = 0
            for b_counter in range(y):
                if(list_i[b_counter]==list_j[b_counter]):
                    finall_list.append(list(list_i[b_counter]))
                else:
                    flagg+=1
                    if(flagg==2):
                        del finall_list[-b_counter:]
                        flag2.pop()
                        flag1.pop()
                        flag = 1
                        break
                    flag2.append(j)
                    flag1.append(i)
                    decoy = "-"
                    finall_list.append(list(decoy))
            if (flag!=1):
                flag1 = list(set(flag1))
                flag2 = list(set(flag2))
                flat_list = [item for sublist in finall_list for item in sublist]
                merge_tuple = list_tuple[i] + list_tuple[j]
                flag_origin.append(list_tuple[i])
                flag_origin.append(list_tuple[j])
                key = merge_tuple
                for h in range(len(flag_origin)):
                    if flag_origin[h] in fake_dictionary:
                        del fake_dictionary[flag_origin[h]]
                flag_origin.clear()
                value = ''.join(flat_list)
                dictt[key] = value         
                finall_list.clear()
            list_j.clear()
        list_i.clear()
    filtered_dict = {key: value for key, value in dictt.items() if value}
    filtered_dict.update(fake_dictionary)
    return(filtered_dict)



index = int(input("How many terms do you have?"))
y = int(input("How many bites does it takes?"))
print("Enter your terms")
dictt = {}
dictt_index = {}
a = []
k=[]
t=0
decoy=[]
required1 = []
required = {}

for i in range(index):
    z = int(input())
    a.append(z)

a.sort()

for i in range(index):
    x = a[i]
    x = bin(x)[2:].zfill(y)
    for i,v in enumerate(x):
        if(v=="1"):
            t+=1
    if t in dictt.keys():
        dictt[t].append(x)
    else:
        dictt[t] = [x]
    t=0


last_key = next(reversed(dictt))
for i in range(last_key+1):
    if i in dictt.keys():
        if(i in dictt.keys() and i+1 in dictt.keys()):
            decoy = (Finder(dictt[i],dictt[i+1],y))
            
            required1.append(decoy)
combined_dict = {}

for d in required1:
    combined_dict.update(d)


for i in range(y):
    combined_dict= Second_thought(combined_dict,y)
combined_dict
unique_dict = {}


for key, value in combined_dict.items():
    unique_key = tuple(sorted(set(key)))
    if (unique_key, value) not in unique_dict.items():
        unique_dict[unique_key] = value
combined_dict = {}

required3 = []
unique_elements = []
for key_tuple in unique_dict.keys():
    unique_elements.append(key_tuple)
    unique_elements = list(set(unique_elements))
qwe = [element for tup in unique_elements for element in tup]

qwe = list(set(qwe))
for element in a:
    if element not in qwe:
        x = element
        x = bin(x)[2:].zfill(y)
        required3.append(x)


all_elements = []
required = []
all_keys= []
all_elements = []  
for key in unique_dict:
    all_elements.extend(key)
    all_keys.extend(key)
all_keys = list(set(all_keys))
element_count = Counter(all_elements)
elements_occuring_once = {element for element, count in element_count.items() if count == 1}


found_values = {}
for element_to_find in elements_occuring_once:
    found_value = None
    for key in unique_dict:
        if element_to_find in key:
            found_value = unique_dict[key]
            break
    if found_value is not None:
        found_values[element_to_find] = found_value
        required.append(found_value)
    else:
        found_values[element_to_find] = None


related_elements = set()
for key in unique_dict:
    if any(element in key for element in elements_occuring_once):
        related_elements.update(key)


keys_to_delete = [key for key, value in unique_dict.items() if value in required]
for key in keys_to_delete:
    del unique_dict[key]
    

elements_not_in_related_dict = {}
for key in unique_dict:
    for element in key:
        if element not in related_elements:
            if element not in elements_not_in_related_dict:
                elements_not_in_related_dict[element] = [key]
            else:
                elements_not_in_related_dict[element].append(key)

w =[]
t=0
rt=[]


for q in elements_not_in_related_dict.keys():
    w.append(q)  
    z = elements_not_in_related_dict[q][0]
    if(t==0):
        required.append(unique_dict[z])
        t=1
    rt.append(z)
if elements_not_in_related_dict:
    for tuple_value in elements_not_in_related_dict[q]:
        for i in range(len(w)):
            if(tuple_value[0]!=w[i] and tuple_value[1]!=w[i]):                
                required.append(unique_dict[tuple_value])
                break


required3 = list(set(required3))
required3 = required3
required = list(set(required))
required.append(required3)
flattened_list = flatten(required)

print(f"For the {a} elements you need {flattened_list} terms.")