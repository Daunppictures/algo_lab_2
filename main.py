import math


def main():
    # Input number of angry cows
    angry_cows_number = int(input("Enter number of angry cows: "))

    # Input List
    list = []
    number_of_list_elements = int(input("Enter number of elements: "))

    for i in range(0, number_of_list_elements):
        list_element = int(input())

        list.append(list_element)

    list.sort()

    # Init variables
    low = 0
    high = list[-1]
    best = 0

    while (low <= high):
        mid = math.floor((low + high + 1) / 2)
        cnt = 1
        left = 0
        i = 1
        while (i < len(list)):
            if (list[i] - list[left] >= mid):
                left = i
                cnt += 1
            i += 1
        if (cnt >= angry_cows_number):
            best = mid
            low = mid + 1
        else:
            high = mid - 1

    return best

if __name__ == '__main__':
    b = main()
    # Output
    print("Largest minimum distance: " + str(b))