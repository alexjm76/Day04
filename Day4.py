#list comprehension

# odd_lists=[]
# for i in range(1,11):
#     if i % 2==1:
#         odd_lists.append(1)
# print(odd_lists)''

odd_lists=[i for i in range(1,11) if i % 2 ==1]
for i in range(1,11):
    if i % 2==1:
        odd_lists.append(1)
print(odd_lists)