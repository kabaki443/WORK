import customtkinter
import names

app = customtkinter.CTk()
app.geometry('600x600')

label = customtkinter.CTkLabel(app, text ='Name1.0',font =('Aria',40))
label.pack(pady=(20,0))

#Output
namer_text = customtkinter.StringVar()
namer_label = customtkinter.CTkLabel(app, textvariable = namer_text, font=('Aria',40))
namer_label.pack(pady=(20,0))



def button_event():
    namer_text.set(names.get_full_name())

button = customtkinter.CTkButton(app, text ='Random',command = button_event)
button.pack(pady=(20,0))

app.mainloop()