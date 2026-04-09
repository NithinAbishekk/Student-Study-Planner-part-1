title = "---------Student Study Planner---------"
print(title)

subject = input("Enter Subject : ").title()
hour = input("Enter hours studied : ").title()

if subject == "Maths":
    if hour < "1":
        print("Maths needs more focus")
        print("Performance : Below required")
        print("Comment : start now, you can improve")
    elif "1" < hour < "2":
        print("Performance : Average")
        print("Comment : Keep pushing, you're improving")
    else:
        print("Performance : Extraordinary")
        print("Comment : outstanding work, aim even higher")

if subject == "Physics":
    if hour < "1":
        print("Performance : Below required")
        print("Comment : Its all about logical thinking try to develop it.")
    elif "1" < hour < "2":
        print("Performance : Average")
        print("Comment : It won't take so much time to reach above average, or below it even, so work more")
    else:
        print("Performance : Extraordinary")
        print("Comment : Good")

if subject == "Chemistry":
    if hour < "1":
        print("Performance : Below required")
        print("Comment : try to master direct questions")
    elif "1" < hour < "2":
        print("Performance : Average")
        print("Comment : focus on numericals")
    else:
        print("Performance : Extraordinary")
        print("Comment : memorise each and every exception cases")

endpage = "----------------------------------------"
print(endpage)