import tkinter as tk
from tkinter import scrolledtext, filedialog, ttk
from openai import OpenAI
from PIL import Image

client = OpenAI()

tto_assistant_history = [{"role": "system", "content": "You are a tech transfer assistant, skilled in explaining complex adminitstrative tasks with clear and concise delivery."}]
technical_assistant_history = [{"role": "system", "content": "You are a technical assistant, skilled in providing detailed and accurate data driven marketing advice."}]
image_path = None  


def send_message(event=None):
    user_input = user_entry.get("1.0", tk.END).strip()
    if user_input or image_path:
        messages = tto_assistant_history + [{"role": "user", "content": user_input}]
        if image_path:
            with open(image_path, "rb") as img:
                image_data = img.read()
            response = client.images.create_completion(
                prompt=user_input,
                image=image_data,
                model="image-alpha-001"
            )
            response_text = response['choices'][0]['text']
            messages.append({"role": "assistant", "content": response_text})
        else:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            response_text = completion.choices[0].message.content
            messages.append({"role": "assistant", "content": response_text})

        tto_assistant_history.extend(messages[1:]) 
        response_display.config(state=tk.NORMAL)  
        if user_input:
            response_display.insert(tk.END, "User: " + user_input + "\n")
        if response_text:
            response_display.insert(tk.END, "TTO Assistant: " + response_text + "\n\n")
        response_display.config(state=tk.DISABLED)  
        user_entry.delete("1.0", tk.END) 
        clear_image()  

def send_message_alt(event=None):
    user_input = user_entry.get("1.0", tk.END).strip()
    if user_input or image_path:
        messages = technical_assistant_history + [{"role": "user", "content": user_input}]
        if image_path:
            with open(image_path, "rb") as img:
                image_data = img.read()
            response = client.images.create_completion(
                prompt=user_input,
                image=image_data,
                model="image-alpha-001"
            )
            response_text = response['choices'][0]['text']
            messages.append({"role": "assistant", "content": response_text})
        else:
            completion = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )
            response_text = completion.choices[0].message.content
            messages.append({"role": "assistant", "content": response_text})

        technical_assistant_history.extend(messages[1:]) 
        response_display.config(state=tk.NORMAL)  
        if user_input:
            response_display.insert(tk.END, "User: " + user_input + "\n")
        if response_text:
            response_display.insert(tk.END, "Technical Assistant: " + response_text + "\n\n")
        response_display.config(state=tk.DISABLED)
        user_entry.delete("1.0", tk.END) 
        clear_image() 

def set_assistant(assistant):
    global send_message_selected, current_history
    if assistant == "tto":
        send_message_selected = send_message
        current_history = tto_assistant_history
    else:
        send_message_selected = send_message_alt
        current_history = technical_assistant_history
    response_display.config(state=tk.NORMAL)  
    response_display.delete("1.0", tk.END)   
    for msg in current_history[1:]:  
        if msg["role"] == "user":
            response_display.insert(tk.END, "User: " + msg["content"] + "\n")
        else:
            response_display.insert(tk.END, "Assistant: " + msg["content"] + "\n\n")
    response_display.config(state=tk.DISABLED) 

def clear_chat():
    global tto_assistant_history, technical_assistant_history
    tto_assistant_history = [{"role": "system", "content": "You are a tech transfer assistant, skilled in explaining complex adminitstrative tasks with clear and concise delivery."}]
    technical_assistant_history = [{"role": "system", "content": "You are a technical assistant, skilled in providing detailed and accurate data driven marketing advice."}]
    response_display.config(state=tk.NORMAL)
    response_display.delete("1.0", tk.END) 
    response_display.config(state=tk.DISABLED)  
    clear_image() 

def call_send_message(event=None):
    send_message_selected(event)

def upload_image():
    global image_path
    image_path = filedialog.askopenfilename(title="Select an Image", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if image_path:
        response_display.config(state=tk.NORMAL)  
        response_display.insert(tk.END, "Image selected: " + image_path + "\n")
        response_display.config(state=tk.DISABLED) 

def clear_image():
    global image_path
    image_path = None


root = tk.Tk()
root.title("ChatGPT GUI")

chat_frame = tk.Frame(root)
chat_frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

response_display = scrolledtext.ScrolledText(chat_frame, height=20, width=70, state=tk.DISABLED)
response_display.pack(side=tk.RIGHT, pady=10, padx=10, fill=tk.BOTH, expand=True)

selection_frame = tk.Frame(chat_frame)
selection_frame.pack(side=tk.LEFT, padx=5, fill=tk.Y)

tto_button = ttk.Button(selection_frame, text="Tech Transfer Assistant", command=lambda: set_assistant("tto"))
tto_button.pack(pady=2)
technical_button = ttk.Button(selection_frame, text="Marketing Assistant", command=lambda: set_assistant("technical"))
technical_button.pack(pady=2)
clear_button = ttk.Button(selection_frame, text="Clear Chat", command=clear_chat)
clear_button.pack(pady=2)
upload_button = ttk.Button(selection_frame, text="Upload Image", command=upload_image)
upload_button.pack(pady=2)


input_frame = tk.Frame(root)
input_frame.pack(pady=10, padx=10, fill=tk.X)

user_entry = tk.Text(input_frame, height=5, width=50)
user_entry.pack(side=tk.LEFT, fill=tk.X, expand=True)
user_entry.bind("<Return>", call_send_message)

send_button = ttk.Button(input_frame, text="Send", command=call_send_message)
send_button.pack(side=tk.RIGHT, padx=5)

set_assistant("tto")

root.mainloop()
