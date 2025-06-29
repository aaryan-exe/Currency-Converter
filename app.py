import tkinter as tk
import customtkinter as ctk
import requests
def onClick():
    api_key="your api key"
    currency1=dropdown1.get()
    currency2=dropdown2.get()
    number=textbox.get("0.0", "end").strip()
    amount=int(number)
    url=f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{currency1}"
    response=requests.get(url)
    data=response.json()
    if response.status_code == 200:
        currency3=data["conversion_rates"][currency2]
        exchange_rate=data["conversion_rates"][currency1]
        output=exchange_rate*currency3
        final=amount*output
        textbox2.insert("0.0",final)
    
app = ctk.CTk()
app.title("Currency Conversion")
app.geometry("600x300")
app.resizable("false","false")
# app._set_appearance_mode("Light")

frame=ctk.CTkFrame(master=app)
frame.pack(pady=2, fill="x")

label = ctk.CTkLabel(
    master=frame,
    text="Currency Converter",
    font=("Arial", 28, "bold")
)
label.pack(padx=20, pady=10, fill="x")

innerFrame=ctk.CTkFrame(master=frame)
innerFrame.pack(side="left",padx=20,pady=20,)


options = ["USD", "EUR", "JPY", "GBP"]

dropdown1=ctk.CTkOptionMenu(master=innerFrame,
 values=options
 )
dropdown1.pack(padx=10,pady=10)

textbox = ctk.CTkTextbox(master=innerFrame,
                          width=150,
                            height=50,
                              font=("Arial", 32)
                              )
textbox.pack(pady=10, padx=20)

innerFrame3=ctk.CTkFrame(master=frame,
                         )
innerFrame3.pack(side="left",padx=20,pady=20,)

label = ctk.CTkLabel(
    master=innerFrame3,
    text="to",
    anchor="w",
    font=("Arial", 24, "bold")
)
label.pack(padx=20, pady=10, fill="x")


innerFrame2=ctk.CTkFrame(master=frame)
innerFrame2.pack(side="left",
                 padx=20,
                 pady=20
                 )

options2 = ["INR","USD", "EUR", "JPY", "GBP"]

dropdown2=ctk.CTkOptionMenu(master=innerFrame2,
                           values=options2,
                           )
dropdown2.pack(padx=10,
              pady=10
              )

textbox2 = ctk.CTkTextbox(master=innerFrame2,
                         width=150,
                         height=50,
                         font=("Arial", 32)
                         )
# textbox2.configure(state="disabled")
textbox2.pack(pady=10, padx=20)

btn=ctk.CTkButton(app, text="Convert",command=onClick )
btn.pack(padx=10, pady=10)
app.mainloop()