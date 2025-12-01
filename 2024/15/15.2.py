grid, movements = open(0).read().split('\n\n')

def enlarge(c):
    if c == '#': return '##'
    elif c == 'O': return '[]'
    elif c == '.': return '..'
    elif c == '@': return '@.'

grid = [[cc for c in l for cc in enlarge(c)] for l in str(grid).splitlines()]

movements = [m for m in movements if m != '\n']

y = [i for i, line in enumerate(grid) if '@' in line][0]
x = grid[y].index('@')

boxes = [(y, x) for y, line in enumerate(grid) if '[' in line for x, char in enumerate(line) if char == '[']

def can_move_box(y, x, dy, dx):
    if dy != 0:
        if grid[y+dy][x] == '#' or grid[y+dy][x+1] == '#': return False

        neighbors = [[y,x] for y,x in [[y+dy, x-1], [y+dy, x], [y+dy, x+1]] if grid[y][x] == '[']

        if grid[y+dy][x] == '.' and grid[y+dy][x+1] == '.' or all(can_move_box(ny, nx, dy, dx) for ny, nx in neighbors):
            return True
        return False
    else:
        next_x = x + (2 if dx == 1 else -1)
        if grid[y][next_x] == '.':
            return True
        if grid[y][x+2*dx] == '[':
            return can_move_box(y, x+2*dx, dy, dx)
        return False

def move_box(y, x, dy, dx):
    # print(f", moving box {y},{x}", end='')
    if dy != 0:
        neighbors = []
        if grid[y+dy][x-1] == '[': neighbors.append([y+dy, x-1])
        if grid[y+dy][x] == '[': neighbors.append([y+dy, x])
        if grid[y+dy][x+1] == '[': neighbors.append([y+dy, x+1])

        for ny, nx in neighbors:
            move_box(ny, nx, dy, dx)

        if grid[y+dy][x:x+2] != ['#', '#']:
            grid[y+dy][x:x+2] = ['[', ']']
            grid[y][x:x+2] = ['.', '.']
    else:
        if grid[y][x+2*dx] == '[':
            move_box(y, x+2*dx, dy, dx)
            
        next_x = x + (2 if dx == 1 else -1)
        if grid[y][next_x] != '#':
            if dx == 1:
                grid[y][x:x+3] = ['.', grid[y][x], grid[y][x+1]]
            else:
                grid[y][x-1:x+2] = [grid[y][x], grid[y][x+1], '.']

# for line in grid: print(''.join(line))

for m in movements:

    dy, dx = (-1,0) if m == '^' else (0,1) if m == '>' else (1,0) if m == 'v' else (0,-1)

    # if m == '^': print("up", end='')
    # if m == '>': print("right", end='')
    # if m == 'v': print("down", end='')
    # if m == '<': print("left", end='')

    box = None
    if grid[y+dy][x+dx] == '#':
        can_move = False
    elif grid[y+dy][x+dx] == '.':
        can_move = True
    else:
        box = (y+dy, x+dx) if grid[y+dy][x+dx] == '[' else (y+dy, x+dx-1)
        can_move = can_move_box(*box, dy, dx)

    if can_move:
        if box: move_box(*box, dy, dx)
        grid[y+dy][x+dx] = grid[y][x]
        grid[y][x] = '.'
        y += dy
        x += dx

    # print()
    # for line in grid: print(''.join(line))
    # robot_y = [i for i, line in enumerate(grid) if '@' in line]
    # if not robot_y:
    #     print("ERROR")
    #     __import__("sys").exit(1)

print(sum(100*i + j for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '['))
