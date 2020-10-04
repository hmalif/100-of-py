#ইউজার একটি ক্যারেক্টার (আলফাবেট) ইনপুট দেবে। ক্যারেক্টারটা ছোট হাতের অক্ষর হলে
#  আউটপুট হবে Lower Case আর বড় হাতের অক্ষর হলে হবে Upper Case।
#  যদি ক্যারেক্টারটা আলফাবেটের মধ্যে না পড়ে, তবে আউটপুট Nothing হবে।
x=input("please, input your charecter..")
if x >= 'a' and x <= 'z':
    print("Lower Case")
elif x >= 'A' and x <= 'Z':
    print("Upper case")
else:
    print("Nothing")