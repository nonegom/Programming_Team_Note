# 격자 공간에서 캐릭터를 움직이는 게임 생성

n, m = 4, 4 # map(int, input().split())
x, y, position = 1, 1, 0 # map(int, input().split())

tmp = [[0]*n for _ in  range(m)]
game_map = []
for i in range(m):
    game_map.append(list(map(int,input().split())))
    
# 방향 전환
# 북 동 남 서 
direction = [0, 1, 2, 3]
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 움직임 설정_초기 설정
tmp[x][y]=1

# x, y가 좌표

def turn_left():
    global position
    position -= 1
    if position == -1:
        position = 3  
    
turn_time = 0
count = 1

while True:
    turn_left()
    next_x = x + dx[position]
    next_y = y + dy[position]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
    if game_map[next_x][next_y]==0 and tmp[next_x][next_y]==0:    
        tmp[next_x][next_y] = 1
        x, y = next_x, next_y
        count += 1
        turn_time = 0
        continue
        
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
        
    # 네 방향 모두 갈 수 없는 경우 
    if turn_time == 4:
        next_x = x - dx[position]
        next_y = y - dy[position]
        if game_map[next_x][next_y]==0:
                x = next_x
                y = next_y
        else:
            break
        turn_time = 0
print(count)