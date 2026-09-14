def quickSort(arr, mi, ma):
    if (mi < ma):
        piv = part(arr, mi, ma)

        quickSort(arr, mi, piv - 1)
        quickSort(arr, piv + 1, ma)        


def part(arr, mi, ma):
    piv = arr[ma]
    i = mi - 1

    for j in range(mi, ma):
        if (arr[j] <= piv):
            i += 1
            tmp = arr[i]
            arr[i] = arr[j]
            arr[j] = tmp

    tmp = arr[i + 1]
    arr[i + 1] = arr[ma]
    arr[ma] = tmp

    return (i + 1)

arr = [2,8,4,2,3,6,9,4,0,2,5,4,1]
print(arr)
quickSort(arr, 0, len(arr) - 1)
print(arr)