import tkinter as tk
import time
from datetime import datetime
import winsound

# alarm fonksiyonu
def check_alarm():
    current_time = datetime.now().strftime("%H:%M")
    if current_time == alarm_time.get():
        winsound.Beep(1000, 1000)  # Alarm sesi
        label_alarm.config(text="ALARM: Time's Up!", fg="red")
    else:
        label_alarm.config(text="Set Alarm", fg="black")
    root.after(1000, check_alarm)  # 1 saniye sonra tekrar kontrol et

# zamanlayıcı fonksiyonu
def start_timer():
    try:
        timer_seconds = int(entry_timer.get()) * 60  # Dakikayı saniyeye çevir
        while timer_seconds > 0:
            minutes, seconds = divmod(timer_seconds, 60)
            time_str = f"{minutes:02}:{seconds:02}"
            label_timer.config(text=time_str)
            root.update()
            time.sleep(1)
            timer_seconds -= 1
        winsound.Beep(1000, 1000)  # Zamanlayıcı bittiğinde alarm sesi
        label_timer.config(text="Time's Up!", fg="red")
    except ValueError:
        label_timer.config(text="Invalid input", fg="red")

# ana pencere
root = tk.Tk()
root.title("Electronic Alarm Clock & Timer")

# saat bölümü
label_time = tk.Label(root, font=("Helvetica", 48), fg="black")
label_time.pack()

# alarm bölümü
alarm_time = tk.StringVar()
label_alarm = tk.Label(root, text="Set Alarm (HH:MM)", font=("Helvetica", 16))
label_alarm.pack()

entry_alarm = tk.Entry(root, textvariable=alarm_time, font=("Helvetica", 16))
entry_alarm.pack()

# zamanlayıcı bölümü
label_timer = tk.Label(root, text="00:00", font=("Helvetica", 32), fg="black")
label_timer.pack()

entry_timer = tk.Entry(root, font=("Helvetica", 16))
entry_timer.pack()

button_start_timer = tk.Button(root, text="Start Timer", font=("Helvetica", 16), command=start_timer)
button_start_timer.pack()

# saat güncellemesi
def update_time():
    current_time = time.strftime("%H:%M:%S")
    label_time.config(text=current_time)
    root.after(1000, update_time)  # 1 saniye sonra tekrar güncelle

update_time()

# alarm kontrol fonksiyonunu başlat
check_alarm()

# pencereyi çalıştır
root.mainloop()

