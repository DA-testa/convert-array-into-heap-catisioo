# python3


def build_heap(data):
    n = len(data)
    swaps = []

    for i in range((n//2), -1, -1):
        j = i
        while True:
            
            left = 2*j + 1
            right = 2*j + 2
            
            if left < n and data[left] < data [j]:
                j = left
            if right < n and data[right] < data [j]:
                j = right
            if i != j:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
                i = j
            else:
                break
 
    return swaps


def main():

    first_line = input()

    if "I" in first_line:
        n = int(input())
        data = list(map(int, input().split()))
    
    elif "F" in first_line:
        name = input()
        path = './tests/'
        file = path+name
        with open(file, 'r') as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
    
    else:
        print("error")
        return
    
    assert len(data) == n

    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    assert len(swaps) <= 4*n


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
