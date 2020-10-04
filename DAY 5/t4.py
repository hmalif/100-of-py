#ইউজার একটা সংখ্যা ইনপুট দেবে। সেটাকে আপনার স্কুল/কলেজ/বিশ্ববিদ্যালয়ের গ্রেডিং সিস্টেম অনুসারে 
# হিসেব-নিকেশ করে A+ বা B- বা F ইত্যাদি আউটপুট দেখাতে হবে।
a=int(input("Enter your marks.."))
if a <= 100 and a >= 80:
    print("A+")
elif a <= 79 and a >= 60:
    print("A")
elif a <= 59 and a >= 50:
    print("A-")
elif a <= 49 and a >= 40:
    print("B")
elif a <= 39 and a >= 33:
    print("B-")
elif a <= 32 and a >= 0:
    print("FAIL")
else:
    print("Wrong")