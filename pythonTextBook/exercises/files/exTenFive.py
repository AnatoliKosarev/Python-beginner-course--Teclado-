def why_like_programming():
    answer = input("Enter why you like programming or 'q' to exit: ")
    while answer != "q":
        if answer:
            with open("answers.txt", "a") as f:
                f.write(answer + "\n")
        answer = input("Enter why you like programming or 'q' to exit: ")


why_like_programming()
