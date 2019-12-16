
def legoBlocks(wall_height, wall_width):

    f = []
    f.append(0)
    f.append(1)
    if wall_width > 1:
        f.append(2)
    if wall_width > 2:
        f.append(4)
    if wall_width > 3:
        f.append(8)

    if wall_width > 4:
        for i in range(5, wall_width + 1):  # stop at index wall_width - 1
            f.append(f[i - 1] + f[i - 2] + f[i - 3] + f[i - 4])

    total_combos = f[-1] ** wall_height

    g = []
    for i in range(len(f)):
        g.append(f[i] ** wall_height)

    print('f')
    for _ in range(wall_height): print(f)
    print('---')
    print('g')
    print(g)
    print('---')

    # h = 0
    # for i in range(1, wall_width):  # 1 to 6 inclusive
    #     temp2 = i
    #     j = wall_width - i
    #     tmp = g[i - 1] * g[j - 1]
    #     h +=
    # return (total_combos - h)


    h = [0] * (wall_width + 1)
    h[1] = 1

    for i in range(2, wall_width + 1):
        h[i] = g[i]
        for j in range(1, i):
            h[i] = h[i] - h[j] * g[i-j]
            a=1

    print('h')
    print(h)
    print('---')

    return (h[-1])


print('result:', legoBlocks(12, 12))