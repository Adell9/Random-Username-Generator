import random
import string
import tkinter as tk
from tkinter import messagebox, filedialog
import datetime

# قوائم جاهزة من الصفات والأسماء
adjectives = ["Cool", "Happy", "Brave", "Funky", "Witty", "Epic", "Swift", "Sneaky", "Chill", "Mighty"]
nouns = ["Tiger", "Dragon", "Ninja", "Panda", "Phoenix", "Gamer", "Wizard", "Samurai", "Shadow", "Knight"]

# دالة توليد اسم مستخدم
def generate_username(add_numbers=True, add_special_chars=False, length=None):
    adj = random.choice(adjectives)
    noun = random.choice(nouns)
    username = adj + noun

    if add_numbers:
        username += str(random.randint(10, 99))  # رقمين عشـوائيين

    if add_special_chars:
        username += random.choice("!@#$%^&*")

    # إذا تم تحديد طول معين، نقص الجزء الإضافي فقط
    if length and len(username) > length:
        username = username[:length]

    return username

# دالة الحفظ
def save_to_file(usernames):
    today = datetime.date.today().strftime("%Y-%m-%d")
    filename = f"usernames_{today}.txt"
    with open(filename, "w") as file:
        for username in usernames:
            file.write(username + "\n")
    messagebox.showinfo("✅ Saved", f"Usernames saved to {filename}")

# الوظيفة عند الضغط على زر التوليد
def on_generate():
    try:
        add_numbers = numbers_var.get()
        add_special_chars = special_chars_var.get()
        length = length_entry.get()
        length = int(length) if length.isdigit() else None
        count = int(count_entry.get())

        usernames = set()  # نستخدم set لتجنب التكرارات
        while len(usernames) < count:
            usernames.add(generate_username(add_numbers, add_special_chars, length))

        output_box.delete("1.0", tk.END)
        for name in usernames:
            output_box.insert(tk.END, name + "\n")

        global generated_usernames
        generated_usernames = list(usernames)

    except Exception as e:
        messagebox.showerror("❌ Error", str(e))

# الوظيفة عند الضغط على زر الحفظ
def on_save():
    if generated_usernames:
        save_to_file(generated_usernames)
    else:
        messagebox.showwarning("⚠️ Warning", "No usernames generated yet.")

# الواجهة الرسومية
app = tk.Tk()
app.title("✨ Random Username Generator")
app.geometry("500x500")

# خيارات المستخدم
tk.Label(app, text="How many usernames?").pack()
count_entry = tk.Entry(app)
count_entry.insert(0, "5")
count_entry.pack()

tk.Label(app, text="Max username length (optional):").pack()
length_entry = tk.Entry(app)
length_entry.pack()

numbers_var = tk.BooleanVar(value=True)
tk.Checkbutton(app, text="Include numbers", variable=numbers_var).pack()

special_chars_var = tk.BooleanVar()
tk.Checkbutton(app, text="Include special characters", variable=special_chars_var).pack()

# زر التوليد
tk.Button(app, text="Generate Usernames", command=on_generate, bg="green", fg="white").pack(pady=10)

# المخرجات
output_box = tk.Text(app, height=10)
output_box.pack()

# زر الحفظ
tk.Button(app, text="Save to File", command=on_save, bg="blue", fg="white").pack(pady=10)

generated_usernames = []

app.mainloop()
