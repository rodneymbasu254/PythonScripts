import customtkinter as ctk

r = ctk.CTk()
r.title=('Simple shit')
button = ctk.CTkButton(r, title='Stop', width=25, command=r.destroy())
button.pack()
r.mainloop()
