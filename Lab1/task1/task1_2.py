def main():
    n = int(input("Enter a positive integer value for n: "))
    if n <= 0:
        print("n must be a positive integer.")
        return

    result = 0
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        result += factorial 
    print(f"S({n}) = {result}")

if __name__ == "__main__":
    main()
