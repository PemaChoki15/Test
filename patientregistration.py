from queue import Queue

patient_queue = Queue()

while True:
    print("1. Register Patient")
    print("2. Remove Patient after metting doctor")
    print("3. Display Patient Queue")
    print("4. Exit")

    choice = (input("Enter your choice (Just enter the option number): "))

    if choice == "1":
        name = input("Enter patient name: ")
        patient_queue.put(name)
        print("Patient", name, "registered.")
    elif choice == "2":
        if patient_queue.empty():
            print("No patient in the queue.")
        else: 
            removed_patient = patient_queue.get()
            print("Patient", removed_patient, "removed after meeting doctor.")
    elif choice == "3":
        if patient_queue.empty():
            print("No patient in the queue.")
        else:
            print("Current patient queue:")
            for index, patient in enumerate(patient_queue.queue, start=1):
                print(index, ".", patient)
    elif choice == "4":
        print("Exiting program.........")
        break
    else:
        print("Invalid choice. Please enter a valid option.")


     
