#8. Password Strength Checker
#Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).


password= input("\nEnter The Password to check it is Strong Medium or Weak:  ")
pass_length = len(password)

if pass_length >= 10:
    print("Your Password is Strong!\n")
elif pass_length > 5:
    print("Your Password is Medium Strong!\n")
elif pass_length > 0:
    print("Your Password is too Weak!\n")
else:
    print("Please Enter your Pasword!\n")
    exit()
