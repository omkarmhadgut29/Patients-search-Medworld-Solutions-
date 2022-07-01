from tkinter import *

from automation import search_patients

def search(search_query):
    print(f"search_query: {search_query}")
    search_query = search_query.lower()
    search_parameters = search_query.split()
    name_list = search_patients(search_parameters)

    credits_dict = {}

    if len(name_list) == 1 and name_list[0] == "":
        print("\nNo record found..")
        print("--------------")

    else:
        for name in name_list:
            credits = 0
            if name != "":
                for search_parameter in search_parameters:
                    if search_parameter in name:
                        credits += 1
                credits_dict[name] = credits

        for name in credits_dict:
            print("\n------------\n")
            print(f"Name: {name}")
            print(f"Credits: {credits_dict[name]}")
            print("--------------")

def user_interface():
    root = Tk()

    root.geometry("500x300")

    def submit_value():
        name = name_box.get()
        if name != "":
            search(name)
        else:
            print("Please enter the name..")

    def close():
        root.quit()

    Label(root, text="Patients Search.....", font=("Calibri",14,"bold")).grid(row=0, column=3)

    patient_name = Label(root, text="Enter patient name: ", font="times 15")
    patient_name.grid(row=1, column=2)

    patient_name = StringVar
    name_box = Entry(root, textvariable=patient_name)
    name_box.grid(row=1, column=3)

    Button(root, text="Submit", font="times 12", command=submit_value).grid(row=2, column=2)

    Button(root, text= "Close the Window", font="times 12", command=close).grid(row=2, column=4)

    root.mainloop()

user_interface()
