#컴퓨터(c)와 플레이어(p)의 순서를 랜덤으로 정한다
#컴퓨터가 먼저일경우, 플레이어가 먼저일경우를 나눈다
#while문이 start와 end이 31이하일때만
#list에서 시작하는 수를 start, 끝나는 수를 end
#이때 end=start+랜덤수

import random

print('베스킨라빈스 31! 귀엽고 깜찍하게~')

gamer=['c','p']
turn=random.choice(gamer)

list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]  #31까지의 리스트

def choose(start,end):              #시작점과 끝점
    print(list[start:end])          #list의 시작점~끝점-1까지 출력
    print('\n')

start=1
end=1

while start<=31:        #start,end 31초과될경우 이미 31을 출력한 후이므로 나간다
    if turn=='c':                   #computer의 순서일경우
        print('컴퓨터차례')
        end=start+random.randint(1,3)  #end의 위치를 시작한수+랜덤수
        turn='p'                    #순서를 player에게 넘김

    else:                           #player의 순서일경우
        print('플레이어차례')
        player=int(input())         #player의 입력
        if player>3:                #입력이 3보다 클경우 1~3만 입력해야 하므로 conrinue로 다시반복
            print('1~3중에 다시입력하세요\n')
            continue;
        end=start+player            #end의 위치를 시작한수+입력한수
        turn = 'c'                  #순서를 computer에 넘김

    choose(start, end)              #시작점과 끝점을 choose함수에 보냄
    start=end                       #출력후 시작점을 끝점으로 보냄(끝점-1까지 출력됐으므로)

if turn=='c':
    print('컴퓨터 승')

else:
    print('플레이어 승')







