#ইউজার তার জন্মসাল ইনপুট দেবে। চেক করে দেখতে হবে সেটা লিপ-ইয়ার কিনা।
a=int(input("Enter your birth year.."))
if a%4==0 and a%100 !=0:
    print("leapyear")
else:
    print("not leapyear")