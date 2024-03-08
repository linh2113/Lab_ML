def main():
    n = int(input("Enter the number of elements: "))
    L = []
    for i in range(n):
        num = int(input(f"Enter number {i+1}: "))
        L.append(num)
    max_num = max(L)
    min_num = min(L)
    sum_of_elements = sum(L)
    L.sort()
    positive_count = sum(1 for num in L if num > 0)
    negative_count = sum(1 for num in L if num < 0)
    print(f"Max element in the list: {max_num}")
    print(f"Min element in the list: {min_num}")
    print(f"Sum of elements in the list: {sum_of_elements}")
    print(f"Sorted list: {L}")
    print(f"Number of positive elements: {positive_count}")
    print(f"Number of negative elements: {negative_count}")

if __name__ == "__main__":
    main()
