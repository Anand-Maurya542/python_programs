from collections import defaultdict
class_list=['class V','class VI','class VII','class VIII']
id_list=[1,2,2,3]
temp=defaultdict(set)
for c,i
in zip (class_list,id_list):
       temp[c].add(i)
print(temp)
