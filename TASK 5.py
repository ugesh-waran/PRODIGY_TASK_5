import cv2
from pyzbar.pyzbar import decode
import webbrowser
from tkinter import Tk, Label, Button, StringVar

# GUI setup
root = Tk()
root.title("QR Code Scanner")
root.geometry("400x200")

result_text = StringVar()
result_text.set("Scan a QR Code")

label = Label(root, textvariable=result_text, font=("Arial", 14), wraplength=350)
label.pack(pady=20)

def open_link():
    data = result_text.get()
    if data.startswith("http://") or data.startswith("https://"):
        webbrowser.open(data)

def start_scanner():
    cap = cv2.VideoCapture(0)
    found = False
    while True:
        _, frame = cap.read()
        decoded_objs = decode(frame)

        for obj in decoded_objs:
            data = obj.data.decode('utf-8')
            result_text.set(f"Scanned: {data}")
            found = True
            cap.release()
            cv2.destroyAllWindows()
            return

        cv2.imshow("QR Scanner - Press Q to quit", frame)
        if cv2.waitKey(1) & 0xFF == ord('q') or found:
            break

    cap.release()
    cv2.destroyAllWindows()

# Buttons
scan_btn = Button(root, text="Start Scanning", font=("Arial", 12), command=start_scanner)
scan_btn.pack(pady=10)

open_btn = Button(root, text="Open Link", font=("Arial", 12), command=open_link)
open_btn.pack()

root.mainloop()
