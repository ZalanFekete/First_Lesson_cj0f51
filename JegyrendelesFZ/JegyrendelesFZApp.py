import tkinter as tk
from datetime import datetime
from tkinter import messagebox
from osztalyFZ import TicketFZ


class App:
    def __init__(self, master):
        self.master = master
        self.master.title("Jegyfoglalás")
        self.master.geometry("500x600")


        tk.Label(master, text="Név:", fg="green", font=("Arial", 10, "bold")).pack(pady=(20, 5))
        self.name_entry = tk.Entry(self.master, width=30)
        self.name_entry.pack(pady=5)

        tk.Label(master, text="Cél:", fg="green", font=("Arial", 10, "bold")).pack(pady=(10, 5))
        self.destination_entry = tk.Entry(self.master, width=30)
        self.destination_entry.pack(pady=5)

        tk.Label(master, text="Dátum (ÉÉÉÉ-HH-NN):", fg="green", font=("Arial", 10, "bold")).pack(pady=(10, 5))
        self.date_entry = tk.Entry(master, width=30)
        self.date_entry.pack(pady=5)


        self.save_button = tk.Button(self.master, text="Mentés TXT-be", command=self.save_to_txtFZ)
        self.save_button.pack(pady=3)

        self.clear_button = tk.Button(self.master, text="Adatok törlése", bg="green", fg="white",
                                      width=12, command=self.clear_listFZ)
        self.clear_button.pack(pady=3)

        self.add_button = tk.Button(self.master, text="Hozzáadás", bg="green", fg="white",
                                    width=12, command=self.add_ticketFZ)
        self.add_button.pack(pady=3)


        self.output_box = tk.Text(master, width=50, height=10)
        self.output_box.pack(padx=10, pady=20)

        self.tickets = []



    def save_to_txtFZ(self):
        if not self.tickets:
            messagebox.showwarning("Figyelem", "Nincs mit elmenteni!")
            return

        try:
            with open("jegyek.txt", "w", encoding="utf-8") as file:
                for ticket in self.tickets:
                    file.write(str(ticket) + "\n\n")

            messagebox.showinfo("Siker", "A jegyek sikeresen elmentve a jegyek.txt fájlba!")
        except Exception as e:
            messagebox.showerror("Hiba", f"Hiba történt mentés közben:\n{e}")

    def clear_listFZ(self):
        self.output_box.delete("1.0", tk.END)

    def add_ticketFZ(self):
        name = self.name_entry.get().strip()
        destination = self.destination_entry.get().strip()
        date = self.date_entry.get().strip()


        if name == "" or destination == "" or date == "":
            messagebox.showerror("Hiba", "Minden mezőt ki kell tölteni!")
            return

        if not all(ch.isalpha() or ch.isspace() for ch in name):
            messagebox.showerror("Hiba", "A név nem tartalmazhat számot vagy speciális karaktert!")
            self.name_entry.delete(0, tk.END)
            return

        if not all(ch.isalpha() or ch.isspace() for ch in destination):
            messagebox.showerror("Hiba", "A cél nem tartalmazhat számot vagy speciális karaktert!")
            self.destination_entry.delete(0, tk.END)
            return

        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Hiba", "A dátum formátuma hibás! Használj ÉÉÉÉ-HH-NN formátumot.")
            self.date_entry.delete(0, tk.END)
            return


        ticket = TicketFZ(name, destination, date)
        self.tickets.append(ticket)


        self.output_box.tag_config("green", foreground="green")
        self.output_box.tag_config("yellow", foreground="orange")
        self.output_box.tag_config("red", foreground="red")


        info = (
            f"Utas: {ticket.name} → Cél: {ticket.destination}\n"
            f"Dátum: {ticket.date} | Ár: {ticket.price} Ft\n"
        )
        self.output_box.insert(tk.END, info)


        if ticket.delay < 25:
            tag = "green"
        elif ticket.delay < 35:
            tag = "yellow"
        else:
            tag = "red"

        delay_text = f"Késés: {ticket.delay} perc — {ticket.delay_type}\n\n"
        self.output_box.insert(tk.END, delay_text, tag)


        self.name_entry.delete(0, tk.END)
        self.destination_entry.delete(0, tk.END)
        self.date_entry.delete(0, tk.END)



if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()