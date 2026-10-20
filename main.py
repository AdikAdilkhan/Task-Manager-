try:
    while True:
        print("""--- ТАПСЫРМАЛАР ЖУРНАЛЫ ---"
            "1. Барлық тапсырмаларды көру"
            "2. Жаңа тапсырма қосу"
            "3. Тапсырманы іздеу"
            "4. Тапсырманы жою"
            "5. Шығу"
            "Таңдауыңызды енгізіңіз (1-5):""")
        user_choice = int(input("Қажетті бөлімді таңдаңыз: : "))

        if user_choice == 1:
            try:
                with open("numbers.txt","r") as file:
                    count = 1
                    for line in file:
                        print(count,line.strip())
                        count+=1
            except FileNotFoundError:
                print("Файл табылмады!")

        elif user_choice == 2:
            try:
                with open("numbers.txt", "a") as file:
                    new_tasks = input("Жаңа тапсырманы енгізіңіз: ")
                    file.write(f"\n{new_tasks}")
            except FileNotFoundError:
                print("Файл табылмады!")

        elif user_choice == 3:
            try:
                with open("numbers.txt", "r") as file:
                    search_term = input("Іздеу үшін бір сөз енгізіңіз. \n").strip().lower()
                    c = 1
                    for line in file:
                        if search_term in line.strip():
                            print(line.strip())
            except FileNotFoundError:
                print("Файл табылмады!")

        elif user_choice == 4:
            try:
                with open("numbers.txt","r+") as file:
                    word = []
                    for line in file:
                        print(line.strip())
                        word.append(line.strip())
                    delite_task = int(input("Қай тапсырманы жоясыз = "))
                    word.pop(delite_task-1)
                    tasks = "\n".join(word)
                with open("numbers.txt","w") as file:
                    file.write(tasks)

            except FileNotFoundError:
                print("Файл табылмады!")

        elif user_choice == 5:
            break
        else: print("Қате!!! 1-5 аралығында сандарды таңдаңыз")

except ValueError:
    print("Сіз қате мән енгіздіңіз!")
