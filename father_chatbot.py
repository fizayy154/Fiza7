import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime

# Chatbot Responses
def get_response(message):
    msg = message.lower()

    if "name" in msg:
        return "My father's name is Baqir Ali."

    elif "occupation" in msg or "job" in msg:
        return "My father works as an Operations Manager at National Bank."

    elif "operations manager" in msg:
        return "An Operations Manager supervises daily banking operations and ensures smooth workflow."

    elif "bank" in msg:
        return "My father works at National Bank."

    elif "duties" in msg or "responsibilities" in msg:
        return ("An Operations Manager manages banking operations, "
                "coordinates staff, handles customer service issues, "
                "and ensures bank policies are followed.")

    elif "skills" in msg:
        return ("Important skills include leadership, communication, "
                "problem-solving, teamwork, and management.")

    elif "hello" in msg or "hi" in msg:
        return "Hello! Ask me about my father's profession."

    elif "thank" in msg:
        return "You're welcome!"

    elif "bye" in msg:
        return "Goodbye! Have a great day."

    else:
        return "Sorry, I can answer questions about my father and his profession."


def send_message():
    user_text = entry.get()

    if user_text.strip() == "":
        return

    current_time = datetime.now().strftime("%H:%M")

    chat_area.insert(tk.END, f"You ({current_time}): {user_text}\n")

    bot_reply = get_response(user_text)

    chat_area.insert(tk.END, f"Bot ({current_time}): {bot_reply}\n\n")

    entry.delete(0, tk.END)

    chat_area.see(tk.END)


# Main Window
root = tk.Tk()
root.title("Father Occupation Chatbot")
root.geometry("700x550")
root.configure(bg="#EAF4FF")

# Heading
title = tk.Label(
    root,
    text="Father Occupation Chatbot",
    font=("Arial", 20, "bold"),
    bg="#EAF4FF",
    fg="#003366"
)
title.pack(pady=10)

# Information Label
info = tk.Label(
    root,
    text="Father: Baqir Ali | Occupation: Operations Manager (National Bank)",
    font=("Arial", 11),
    bg="#EAF4FF",
    fg="#333333"
)
info.pack()

# Chat Area
chat_area = scrolledtext.ScrolledText(
    root,
    wrap=tk.WORD,
    width=80,
    height=22,
    font=("Arial", 10)
)
chat_area.pack(padx=10, pady=15)

chat_area.insert(
    tk.END,
    "Bot: Hello! I am a chatbot about my father's profession.\n"
    "Ask me about Baqir Ali and his job at National Bank.\n\n"
)

# Bottom Frame
bottom_frame = tk.Frame(root, bg="#EAF4FF")
bottom_frame.pack(pady=10)

entry = tk.Entry(
    bottom_frame,
    width=50,
    font=("Arial", 12)
)
entry.grid(row=0, column=0, padx=5)

send_btn = tk.Button(
    bottom_frame,
    text="Send",
    command=send_message,
    font=("Arial", 11, "bold"),
    bg="#003366",
    fg="white",
    width=12
)
send_btn.grid(row=0, column=1, padx=5)

root.mainloop()