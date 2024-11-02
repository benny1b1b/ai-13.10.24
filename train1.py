# תנאים:

# .1 קל ווט מספר עשרוני, אם הוא גדול מ 10- הדפס את ההפרש בינו לבין ,10 אחרת הדפס את מכפלתו
# ב- .10
num: float = float(input("enter a float number: "))
if num > 10:
    print(num - 10)
else:
    print(num * 10)

num: float = float(input("enter a float number: "))
print(num - 10 if num > 10 else num * 10)



# .2 קל וט שלושה מספרים עשרוניים והדפס את הסכום שלהם רק אם הסכום גדול מ.100- אחרת הדפס
# "הסכום קטן מ.100-"
num1: float = float(input("number 1: "))
num2: float = float(input("number 2: "))
num3: float = float(input("number 3: "))
sum_: float = num1 + num2 + num3
if sum_ >= 100:
    print(num1 + num2 + num3)
else:
    print("The amount is less than 100")
    
    
more_100: list[float] = [float(input(f"enter number{i+1}: "))for i in range(3)]
if sum(more_100) >= 100:
    print(sum(more_100))
else:
    print("The amount is less than 100")

more_100: list[float] = [float(input(f"enter number{i+1}: "))for i in range(3)]
print(sum(more_100) if sum(more_100) >= 100 else "The amount is less than 100")


# .3 *בונוס/רשות : קלט שני עשרוניים והדפס את השבר הגדול יותר. אם השברים שווים הדפס "שווים."
num_f1: float = float(input("enter a number: "))
num_f2: float = float(input("enter a number: "))
shever_1: float = num_f1 %1
shever_2: float = num_f2 %1
if shever_1 > shever_2:
    print(f"{shever_1}, bigger")
elif shever_2 > shever_1:
    print(f"{shever_2}, bigger")
else:
    print("equal")



# .4 קל וט גיל וודא שהוא תקין )מעל 0 ומתחת 120(. אם הוא לא תקין הדפס "גיל לא תקין."
age: int = int(input("enter an age: "))
if age < 0 or age > 120:
    print("invalid age")
else:
    print(age)

# .5 קלוט מספר תלת ספרתי והדפס את הספרה האמצעית שלו.
dig3_num: int = int(input("enter a three-digit number: "))
print(dig3_num % 100//10)


# לולאות:

# .6 קל וט מספר טבעי n והדפס את כל המספרים השלמים מ n-עד 1 בסדר יורד.
n: int = int(input("enter a number: "))
print([i for i in range(n,0,-1)])


# .7 קל וט שני מספרים והדפס את כל המספרים הזוגיים בין הראשון לשני.
number1: int = int(input("enter number: "))
number2: int = int(input("enter number: "))
print([i for i in range(number1, number2 + 2) if i % 2 == 0])

# .8 קל וט מספר חיובי n והדפס את כל המספרים עד n שהם מתחלקים ב3- או ב ,5- או בשניהם.
n1: int = int(input("enter number: "))
print([i for i in range(0, n1 + 1) if i % 3 == 0 or i %5 == 0])

# .9 קל וט מספר n והדפס את כל המספרים שהינם כפולות של 7 עד n
n2: int = int(input("enter number: "))
print([i for i in range(0, n2 + 1) if i %7 == 0])

# עיבוד נתונים :


# .11 קלוט מספרים עד שנקלט המספר ,0 הדפס את סכום המספרים השליליים שנקלטו.
SENTINEL: int = 0
sum_neg: int = 0
while True:
    num = int(input("enter negative number: "))

    if num == SENTINEL:
        break
    if num < 0:
        sum_neg += num
print(sum_neg)

# .12 קלוט רשימה של 10 מספרים והדפס את המספרים בסדר הפוך.
list_1_10: list[int] = [i for i in range(1, 10+1)]
print(list_1_10[::-1])



# .13 קלוט סדרה של מספרים עד שנקלט המספר ,0 והדפס כמה מהמספרים שהוזנו הם ראשוניים.
list_prime: list[int] = []
SENTINEL: int = 0
counter: int = 0
while True:
    try:
        num: int = int(input("enter prime number: "))
        if num == SENTINEL:
            break
        if num < 2:
            continue
        is_prime: bool = True
        for divider in range(2, num + 1):
            if num % divider == 0:
                is_prime = False
                break
            if is_prime:
                counter +=1
        list_prime.append(num)
    except:
        print("bad number")

print(f"{counter} prime number ")
print(list_prime)



# .14 קלוט 5 מספרים והדפס את הממוצע שלהם, והדפס גם את כמות המספרים הגדולים מהממוצע.

numbers: list[int] = [int(input(f"enter number {i+1}: "))for i in range(5)]
print(numbers)
average: int = sum(numbers)/ len(numbers)
print("average:", average)
list_more_avg: list[int] = [i for i in numbers if i > average]
print(f"numbers large average: {list_more_avg}")

# .15 קלוט שני מספרים והדפס את תוצאת החילוק שלהם תוך שימוש בהפחתות בלבד.

mehulak: int = int(input("enter mehulak: "))
mehalek: int = int(input("enter mehulek: "))
counter_hiluk: int = 0
while mehulak > 0:
    mehulak -= mehalek
    counter_hiluk += 1
print(counter_hiluk)

# אתגרים :

# .16 קלוט מספר תלת ספרתי והדפס אם סכום הספרות שלו מתחלק ב .3-
num_3_digit: int = int(input("enter 3 digit number: "))
ahadot: int = num_3_digit % 10
asarot: int = num_3_digit // 10 % 10
meot: int = num_3_digit // 100
sum_3_digit = ahadot + asarot + meot
if sum_3_digit %3 == 0:
    print(f" numbers {num_3_digit} is divided 3: {sum_3_digit}")
else:
    print(f"sum numbers {num_3_digit} not divided 3")

# .17 קל וט מחרוזת ובדוק אם היא מהופכת )למשל: "אבבא" הפוך לאבבא(.