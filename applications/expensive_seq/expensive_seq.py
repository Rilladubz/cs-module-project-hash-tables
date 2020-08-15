# Your code here

cache = {}
count = 0


def expensive_seq(x, y, z):
    # Your code here

    if x <= 0:
        cache[(x, y, z)] = y + z
        return y+z

    if (x, y, z) in cache:
        return cache[(x, y, z)]

    result_x = expensive_seq(x-1, y+1, z)
    result_y = expensive_seq(x-2, y+2, z*2)
    result_z = expensive_seq(x-3, y+3, z*3)
    result_xyz = result_x + result_y + result_z

    cache[(x, y, z)] = result_xyz

    return result_xyz


if __name__ == "__main__":
    for i in range(10):
        x = expensive_seq(i*2, i*3, i*4)
        print(f"{i*2} {i*3} {i*4} = {x}")

    # print(expensive_seq(150, 400, 800))
    print(expensive_seq(3, 333, 453))
