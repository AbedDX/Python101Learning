import os,shutil,customtkinter
from tkinter import filedialog

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

categories = {
    "Pictures": ["jpg", "jpeg", "png", "gif", "bmp"],
    "Archives": ["zip", "rar", "7z", "tar", "gz"],
    "Software": ["exe", "msi"],
    "Videos": ["mp4", "avi", "mkv", "mov"],
    "Documents": ["pdf", "docx", "xlsx", "pptx","txt"],
    "Music": ["mp3", "wav", "flac", "ogg"],
}

# Function to browse for a directory
def browse_path():
    selected_path = filedialog.askdirectory()
    if selected_path:
        entry1.delete(0, 'end')  # Clear the current text
        entry1.insert(0, selected_path)  # Insert the selected directory path

# Function to sort files based on their extensions
def sort_files():
    source_path = entry1.get()

    for category, extensions in categories.items():
        category_path = os.path.join(source_path, category)
        os.makedirs(category_path, exist_ok=True)
        # Check if the category folder already exists
        if not os.path.exists(category_path):
            os.makedirs(category_path)

        for extension in extensions:
            files = [file for file in os.listdir(source_path) if file.lower().endswith(f".{extension}")]
            for file in files:
                source_file = os.path.join(source_path, file)
                destination_file = os.path.join(category_path, file)
                shutil.move(source_file, destination_file)

    # Corrected line to update the label text
    result_label.config(text="Sorting complete")


tk = customtkinter.CTk()
tk.geometry("600x350")
tk.title("File Sorting System")

frame = customtkinter.CTkFrame(master=tk)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="File Sorting System")
label.pack(pady=12, padx=10)

# Entry to display and input the source directory path
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Enter File Path")
entry1.pack(pady=12, padx=10)

# Browse button to select a directory
browse_button = customtkinter.CTkButton(master=frame, text="Browse", command=browse_path)
browse_button.pack(pady=12, padx=10)

# Sort button to initiate the sorting process
sort_button = customtkinter.CTkButton(master=frame, text="Sort", command=sort_files)
sort_button.pack(pady=12, padx=10)

# Label to display the result
result_label = customtkinter.CTkLabel(master=frame, text="")
result_label.pack(pady=12, padx=10)

tk.mainloop()