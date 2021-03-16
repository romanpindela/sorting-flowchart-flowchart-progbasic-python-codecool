
def bubble_sort(numbers) -> None:

    i = 0 
    N = len(numbers)
    while i < N :
        j = 0
        while j < N - i - 1:
            if numbers[j] > numbers[j+1]:
                temp = numbers[j+1]
                numbers[j+1] = numbers[j]
                numbers[j] = temp
            j += 1
        i += 1

def main() -> None:

    numbers = [1,2,56,32,51,2,8,92,15]
    print(numbers)
    bubble_sort(numbers)
    print(numbers)


if __name__ == '__main__':
    main()