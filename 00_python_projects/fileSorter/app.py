import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

tk = customtkinter.CTk()
tk.geometry("500x350")

frame = customtkinter.CTkFrame(master=tk)
frame.pack(pady=20,padx=60,fill="both", expand=True)

#label = customtkinter.CTkLabel(master=frame, text =" FileSorting System")# add text font
#label.pack(pady=12, padx=10)

#entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Enter File Path")
#entry1.pack(pady=12, padx=10)

#button = customtkinter.CTkButton(master=frame, text="Sort")#command= "call the function"
#button.pack(pady=12, padx=10)

tk.mainloop()
"""
def inputPath():
    path = input("Enter Path: ")
    files = os.listdir(path)
    for file in files:
        filename,extension = os.path.splitext(file)
        extension = extension[1:]

        if os.path.exists(path+"/"+extension):
            shutil.move(path+"/"+file,path+"/"+extension+"/"+file)
        else:
            os.makedirs(path+"/"+extension)
            shutil.move(path+"/"+file,path+"/"+extension+"/"+file)
"""