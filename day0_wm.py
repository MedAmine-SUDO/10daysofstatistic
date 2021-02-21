if __name__ == '__main__':
    n = int(input())
    x_array = list(map(int, input().rstrip().split(' ')))
    w_array = list(map(int, input().rstrip().split(' ')))

    weighted_mean = 0
    for i, value in enumerate(x_array):
        weighted_mean += x_array[i] * w_array[i]

    print('{0:.1f}'.format(weighted_mean / sum(w_array)))