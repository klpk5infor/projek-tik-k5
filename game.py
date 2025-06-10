import tkinter as tk

def hitung_berat():
    try:
        berat = float(entry.get())
        planet = pilihan.get()

        if planet == "Mars":
            hasil = berat * 0.38
        elif planet == "Jupiter":
            hasil = berat * 2.34
        elif planet == "Venus":
            hasil = berat * 0.91
        elif planet == "Saturnus":
            hasil = berat * 1.06
        else:
            hasil = 0

        label_hasil.config(text=f"✨ Beratmu di {planet}: {hasil:.2f} kg ✨")
    except:
        label_hasil.config(text="⚠️ Masukkan angka ya!")

# Setup GUI
root = tk.Tk()
root.title("Planet Calculator 🌌")
root.geometry("350x300")
root.configure(bg="#2a0055")  # ungu gelap

# Judul
tk.Label(root, text="🌟 Beratmu di Planet 🌟", bg="#2a0055", fg="white",
         font=("Arial", 14, "bold")).pack(pady=10)

# Input
tk.Label(root, text="Masukkan berat di Bumi (kg):", bg="#2a0055", fg="pink", font=("Arial", 12)).pack()
entry = tk.Entry(root, font=("Arial", 12), bg="#550077", fg="white")
entry.pack(pady=5)

# Dropdown planet
pilihan = tk.StringVar()
pilihan.set("Mars")
tk.OptionMenu(root, pilihan, "Mars", "Jupiter", "Venus", "Saturnus").pack(pady=5)

# Tombol
tk.Button(root, text="Hitung 🚀", font=("Arial", 12), bg="#8800cc", fg="white", command=hitung_berat).pack(pady=10)

# Hasil
label_hasil = tk.Label(root, text="", bg="#2a0055", fg="white", font=("Arial", 12))
label_hasil.pack(pady=10)

# Hiasan
tk.Label(root, text="✨🌙⭐", font=("Arial", 16), bg="#2a0055", fg="white").pack()

root.mainloop()
