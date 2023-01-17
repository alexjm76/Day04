#dictionary

students = {"name" : "윤정무", "age": 27, "eyes": [0.9, 1.1]}

#for k in students:  #students.keys를 생략해서 students라고 표현
#    print(k)
#
# for k in students.values():  #value 값만 출력
#     print(k)

for k , v in students.items():
    print(f"{k} : {v}")
print(f"이름은 {students['name']},나이는 {students['age']}세", end=' ')
print(f"시련은 좌 : {students['eyes'][0]}, 우 : {students['eyes'][1]}")