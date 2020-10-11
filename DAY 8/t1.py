#ইউজার যেকোনো একটা পূর্ণসংখ্যা ইনপুট দেবে।
#  আর ওই পূর্ণসংখ্যার নামতা আউটপুট হিসেবে দেখাতে হবে।
a=int(input("input your number.."))
count=1
while count <=20:
    print(a,'x',count,'=',count*a)
    count +=1