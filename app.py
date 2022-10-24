"""
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

def main():
    number = int(input("Enter a whole number greater than 1: "))

    sum = 0
    for i in range(1, number + 1):
        sum += i ** i
    
    print(f"Sum of self powers up to {number}: {sum}")

if __name__ == "__main__":
    main()