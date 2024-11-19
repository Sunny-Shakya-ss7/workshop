below_20 = [
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
        "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"
    ]

tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

def num_to_word(n):
    if n == 0:
        return 'zero'
    elif n < 20:
        return below_20[n - 1]
    elif n < 100:
        return tens[n // 10] + ("" if n % 10 == 0 else " " + below_20[n % 10 - 1])
    else:
        return below_20[n // 100 - 1] + " hundred" + ("" if n % 100 == 0 else " " + num_to_word(n % 100))


n = int(input("Enter the number:"))
print(f'Input: {n}')
print(f'Words: {num_to_word(n)}')