#안주
import random

alcohol_foods = {
    "맥주":"치킨",
    "소주":"골뱅이소면",
    "와인":"치즈",
    "고량주":"짬뽕"
}
alcohol_list = list(alcohol_foods) #키값만 추출
food_list = [food for food in alcohol_foods.values()] #value 추출
while True:
    alcohol = input(f"술을 선택하세요 1) {alcohol_list[0]} 2){alcohol_list[1]} 3){alcohol_list[2]} 4){alcohol_list[3]} 5) 랜덤")
    if alcohol == "6":
        print("다음에 또 오세요")
        break
    elif alcohol == "1":
        print(f"{alcohol_list[0]}에 어울리는 안주는 {alcohol_foods[alcohol_list[0]]}입니다")
        break
    elif alcohol == "2":
        print(f"{alcohol_list[1]}에 어울리는 안주는 {alcohol_foods[alcohol_list[1]]}입니다")
        break
    elif alcohol == "3":
        print(f"{alcohol_list[2]}에 어울리는 안주는 {alcohol_foods[alcohol_list[2]]}입니다")
        break
    elif alcohol == "4":
        print(f"{alcohol_list[3]}에 어울리는 안주는 {alcohol_foods[alcohol_list[3]]}입니다")
        break
    elif alcohol == "5" :
        print(f"{alcohol_list[random.randint(0,4)]}에 어울리는 안주는 {alcohol_foods[alcohol_list[random.randint(0,4)]]}입니다")
        break
    # elif alcohol == "5":
    #     print(f"{random.choice(alcohol_list)}에 어울리는 안주는 {random.choice(alcohol_foods)}입니다")  이것도 가능
    #     break
    else:
        print("메뉴에서 올라주세요")