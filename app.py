import tkinter as tk
import customtkinter as ctk
def onClick():
    api_key="Your_api_key"
    
    print("hello")
app = ctk.CTk(fg_color="#F7F1F0")
app.title("Currency Conversion")
app.geometry("600x300")
app.resizable("false","false")
app._set_appearance_mode("Light")

frame=ctk.CTkFrame(master=app, fg_color="#F7F1F0")
frame.pack(pady=2, fill="x")

label = ctk.CTkLabel(
    master=frame,
    text="Currency Converter",
    anchor="w",
    text_color="black",
    font=("Arial", 28, "bold")
)
label.pack(padx=20, pady=10, fill="x")

innerFrame=ctk.CTkFrame(master=frame,fg_color="#CFCFCF")
innerFrame.pack(side="left",padx=20,pady=20,)


options = ["USD", "EUR", "JPY", "GBP"]
dropdown=ctk.CTkOptionMenu(master=innerFrame, values=options)
dropdown.pack(padx=10,pady=10)

textbox = ctk.CTkTextbox(master=innerFrame, width=150, height=50,fg_color="#F7F1F0", text_color="black",font=("Arial", 32))
textbox.pack(pady=10, padx=20)

innerFrame3=ctk.CTkFrame(master=frame,fg_color="#F7F1F0")
innerFrame3.pack(side="left",padx=20,pady=20,)
label = ctk.CTkLabel(
    master=innerFrame3,
    text="to",
    anchor="w",
    text_color="black",
    font=("Arial", 24, "bold")
)
label.pack(padx=20, pady=10, fill="x")


innerFrame2=ctk.CTkFrame(master=frame,fg_color="#CFCFCF")
innerFrame2.pack(side="left",padx=20,pady=20,)

dropdown=ctk.CTkOptionMenu(master=innerFrame2, values=options)
dropdown.pack(padx=10,pady=10)
textbox = ctk.CTkTextbox(master=innerFrame2, width=150, height=50,fg_color="#F7F1F0", text_color="black",font=("Arial", 32))
textbox.pack(pady=10, padx=20)

btn=ctk.CTkButton(app, text="Convert",command=onClick )
btn.pack(padx=10, pady=10)
app.mainloop()