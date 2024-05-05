import tkinter as tk


class FloatingButton:
    def __init__(self, master):
        self.master = master
        self.floating_buttons = []  # List to store references to the floating buttons

        master.title("Floating Button")

        # Set window attributes for floating effect
        master.attributes('-topmost', True)
        master.overrideredirect(True)

        # Position the window
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        self.x = screen_width - 120
        self.y = screen_height - 120
        master.geometry('50x50+{}+{}'.format(self.x, self.y))

        # Create the button
        self.image = tk.PhotoImage(
            file=r"C:\Users\Vedo\Desktop\Coinis kurs\Fillio\assets\icons\main_button.png")
        self.button = tk.Button(master, image=self.image,
                                command=self.onButtonClick)
        self.button.pack()

        # Bind mouse events for moving the button
        self.button.bind("<Control-Button-1>", self.start_move)
        self.button.bind("<ButtonRelease-1>", self.stop_move)
        self.button.bind("<B1-Motion>", self.on_motion)

        self.move = False
        self.prev_x = None
        self.prev_y = None

    def onButtonClick(self):
        print("Button clicked!")
        # Check if floating buttons are already created
        if self.floating_buttons:
            # If floating buttons exist, destroy them and clear the list
            for floating_button in self.floating_buttons:
                floating_button.destroy()
            self.floating_buttons.clear()
        else:
            # Create four new floating buttons
            for i in range(1, 5):
                new_window = tk.Toplevel(self.master)
                new_window.overrideredirect(True)
                new_window.geometry(
                    '50x50+{}+{}'.format(self.x - i * 60, self.y - 60))
                image_path = rf"C:\Users\Vedo\Desktop\Coinis kurs\Fillio\assets\icons\icon{i}.png"
                if i == 1:
                    self.img1 = tk.PhotoImage(file=image_path)
                    new_button = tk.Button(
                        new_window, image=self.img1, command=self.onButtonClick)
                if i == 2:
                    self.img2 = tk.PhotoImage(file=image_path)
                    new_button = tk.Button(
                        new_window, image=self.img2, command=self.onButtonClick)
                if i == 3:
                    self.img3 = tk.PhotoImage(file=image_path)
                    new_button = tk.Button(
                        new_window, image=self.img3, command=self.onButtonClick)
                if i == 4:
                    self.img4 = tk.PhotoImage(file=image_path)
                    new_button = tk.Button(
                        new_window, image=self.img4, command=self.onButtonClick)
                new_button.pack(side="left")
                self.floating_buttons.append(new_window)

    def start_move(self, event):
        self.move = True
        self.prev_x = event.x_root
        self.prev_y = event.y_root

    def stop_move(self, event):
        self.move = False

    def on_motion(self, event):
        if self.move:
            delta_x = event.x_root - self.prev_x
            delta_y = event.y_root - self.prev_y
            self.x += delta_x
            self.y += delta_y
            self.master.geometry('50x50+{}+{}'.format(self.x, self.y))
            self.prev_x = event.x_root
            self.prev_y = event.y_root


if __name__ == "__main__":
    root = tk.Tk()
    app = FloatingButton(root)
    root.mainloop()
