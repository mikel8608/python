class calc:
    def add(x, y):
        ans = x + y
        print(ans)

    def sub(x, y):
        ans = x - y
        print(ans)


x = float(input("Value 1? "))
y = int(input("Value 2? "))

"""
https://stackoverflow.com/questions/21122540/input-error-nameerror-name-is-not-defined/21122817#21122817

For multiple integer in a single line, map might be better.
    arr = map(int, raw_input().split())

If the number is already known, (like 2 integers), you can use
    num1, num2 = map(int, raw_input().split())
"""

print("Calculating for", x, " & ", y)

calc.add(x, y)
calc.sub(x, y)
