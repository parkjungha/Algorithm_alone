import sys
from copy import deepcopy
input = sys.stdin.readline

n,k = map(int,input().split())
power = list(map(int,input().split()))
#print("input",power)
robot = [0]*n*2

def rotate(power): # 벨트가 한 칸 회전한다
    power2 = deepcopy(power)
    last = power[-1]
    for i in range(len(power)-1):
        power2[i+1] = power[i]
    power2[0] = last
 #   print("power", power2)
    return power2

def move(robot):
    robot2 = deepcopy(robot)
    for i in range(n): 
        if i == n-1: # 내려가는 위치에 도달하면 땅으로 내려감
            robot2[i] = 0
        elif robot[i]==1 and robot[i+1]==0 and power[i+1]>=1 : # 로봇이 있는 칸에, 옆칸은 로봇이 없으며, 옆칸의 내구도가 1이상 남아있어야
            robot2[i] = 0 # 현재 칸 로봇 비움
            robot2[i+1] = 1 # 로봇 이동
            power[i+1] -= 1 # 내구도 1 감소
#    print("robot: ",robot2)
    return robot2

cnt = 0

while True:
    cnt+=1
    # 벨트가 한 칸 회전한다
    power = rotate(power)
    robot = rotate(robot)
    # 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
    robot = move(robot)

    # 올라가는 위치에 로봇이 없다면 로봇을 하나 올린다.
    if robot[0] == 0 and power[0]>0:
        robot[0] = 1
        power[0] -= 1
    
    # 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
    if power.count(0)>=k:
        print(cnt)
        break 