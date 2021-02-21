if __name__ == '__main__':

    n = int(input())
    array_element = list(map(int, input().rstrip().split()))

    mean = sum(array_element) / len(array_element)

    array_element = sorted(array_element)
    if (len(array_element) % 2) != 0:
        median = array_element[(len(array_element)-1)//2]
    else:
        median = (array_element[len(array_element)//2] + array_element[(len(array_element)//2)-1]) / 2

    cnt = {}
    for i in array_element:
        if i in cnt:
            cnt[i] += 1
        else:
            cnt[i] = 1
    
    l = []
    for key, value in cnt.items():
        if value == max(cnt.values()):
            l.append(key)

    print(mean)
    print(median)
    print(cnt)
    print(min(l))