#list
import copy

# primes = [2,19,3,5,7,11]
# primes_sorted = sorted(primes) #원본이 안바뀌고 새로운 변수 지정
# print(primes)
# print(primes_sorted)
#
# primes.sort() #원본이바뀐다.
# print(primes)

# mixed = [6, 4, 5, "A", 7 , "트와이스", "B", "b", "마마무"]
# mixed.sort()
# print(mixed) #int와 str가 같이 있어서 5,9안된다.

a = [1,2,[8,9,5]]
b = a.copy()
c = list(a)
d = a[:]
a[2][1] = 7 #mutable, b/c/d affects
print(a, b,c,d)




a = [1,2,[8,9,5]]
b = a.copy()
c = list(a)
d = a[:]
a[2][1] = 7 #mutable, b/c/d affects
print(a, b,c,d)
