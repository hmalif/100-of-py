#ইউজার একটি ক্যারেক্টার (আলফাবেট) ইনপুট দেবে। ক্যারেক্টারটা ভাওয়েল (Vowel) হলে আউটপুট হবে Vowel
#  আর কনসোনেন্ট (Consonant) হলে হবে Consonant; যদি ক্যারেক্টারটা আলফাবেটের মধ্যে না পড়ে, 
# তবে আউটপুট হবে Nothing
x=input("please, enter your charecter..." )
if x >= "a" and x <= "z" or x >= "A" and x <= "Z":
    if x in "aeiouAEIOU":
        print("Vowel")
    else:
        print("Consonent")
else:
    print("Nothing")