#컴퓨터(c)와 플레이어(p)의 순서를 랜덤으로 정한다
#컴퓨터가 먼저일경우, 플레이어가 먼저일경우를 나눈다
#while문이 start<=31동안 반복
#list를 만들고 시작하는 수를 start, 끝나는 수를 end
#이떄 end=start+랜덤한수
#컴퓨터의 필승법은 4단위로 나타나기 떄문에 상대방의 위치%4의 값만큼 컴퓨터가 움직이면 된다.
#2,6,10,14,18,22,26,30를 컴퓨터가 끝점으로 출력하면 반드시 승리!
import random

print('베스킨라빈스 31! 귀엽고 깜찍하게~')

gamer=['c','p']
turn=random.choice(gamer)

list=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]

def choose(start,end):
    print(list[start:end])
    print('\n')

def computer_victory(num):  #시작점을 기준으로 컴퓨터가 이길수있는 필승법의 원리를 적용한다
    if num%4==0:   #시작점을 4로 나눈 나머지가 0일경우 3번을 가야 필승법에 만족
        return 3
    elif num%4==1:  #시작점을 4로 나눈 나머지가 1일경우 2번을 가야 필승법에 만족
        return 2
    elif num%4==2:  #시작점을 4로 나눈 나머지가 2일경우 1번을 가야 필승법에 만족
        return 1
    else:  #시작점을 4로 나눈 나머지가 3일경우 필승법에 모두 만족하지 않으므로 랜덤수 리턴
        return random.randint(1,3)
start=1
end=1

while start<=31:
    if turn=='c':
        print('컴퓨터차례')
        end=start+computer_victory(start)  #끝점을 시작점을 기준으로 컴퓨터가 이길수있는 필승법의 원리를 적용한다
        turn='p'

    else:
        print('플레이어차례')
        player=int(input())
        if player>3:
            print('1~3중에 다시입력하세요\n')
            continue;

        if start==31 and player!=1:  #시작점이 31이면 어차피 플레이어는 31밖에 낼것이 없기 빼문에
            print('어차피 졌습니다. 1을 입력하세요\n')
            continue;

        end=start+player
        turn = 'c'

    choose(start, end)
    start=end

if turn=='c':
    print('컴퓨터 승')

else:
    print('플레이어 승')







