import sys
sys.stdin = open("ex_002_input.txt","r")

T=int(input())      #input, print에 어떤 것을 입력해도 문자형 
# print("%0.2fkg => %0.2flb" %(T, 2.2046*T) )

print(f"{T:.2f} kg =>  {T*2.2046:.2f} lb")
