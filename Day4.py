#list
big_bang = ["GD","태양","탑","대성","승리"]
exo=["백현","첸"]
exo[1]="시우민"
big_bang.append("윤정무")
big_bang.insert(1, "정도윤")
# print(big_bang)
# exo.extend(big_bang) #exo = exo + big_bang 이랑 같은 것이다.
print(exo)
exo.append(big_bang)
print(exo)
print(exo[-1][2])
#print(exo.pop())
print(exo[2].pop()) #pop에 지정안하면 제일 뒤에꺼 날라감
print(exo)   #빅뱅이 날라감
print(exo[2].pop(-2))
print(exo)
del exo[2][-1]
print(exo)
#exo.remove("탑")#탑은 리스트에 없다 리스트에는 백현 시우민 리스트 이렇게 3개인것
exo[2].remove("탑")
print(exo)
exo.clear()  #다 지운다.
print(exo)