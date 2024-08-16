#5. Weather Activity Suggestion
#Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).
weather = input("\nChoose the Weather condition:- \nSunny, Rainy or Snowy: ").lower()

if weather == "sunny":
    print("Go For a Walk!\n")
elif weather == "rainy":
    print("Read a Book!\n")
elif weather == "snowy":
    print("Build a Snowman\n!")
else:
    print("Input is Invalid. Try Again!\n")
    exit()

