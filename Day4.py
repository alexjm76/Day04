#list

scores =("B+","A+","C+")
# print(scores[1])
# scores[1]="C+"
# scores["A+"] #tupel is immutable 변하지 않는다

temp = list(scores)
temp[1]="C+"
temp[2]="A+"
cores = tuple(temp)
print(scores[1],scores[2])