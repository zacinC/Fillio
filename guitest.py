import tkinter as tk
import tkinter.messagebox
import pyperclip


class FloatingButton:
    def __init__(self, master):
        self.master = master
        self.floating_buttons = []  # List to store references to the floating buttons
        # Use StringVar to store the state
        self.settings_window = None
        self.formBoarder = tk.StringVar(value="0")
        # Variable to control the spawning of input and output form window
        self.spawn_forms = tk.StringVar(value="1")
        master.title("Floating Button")

        # Set window attributes for floating effect
        master.attributes('-topmost', True)
        master.overrideredirect(True)

        # Position the window
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()
        self.x = screen_width - 120
        self.y = screen_height - 120
        master.geometry(f'50x50+{self.x}+{self.y}')

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
        if self.floating_buttons:
            # If floating buttons exist, destroy them and clear the list
            for floating_button in self.floating_buttons:
                floating_button.destroy()
            self.floating_buttons.clear()
        else:
            # Create four new floating buttons
            for i in range(1, 7):
                new_window = tk.Toplevel(self.master)
                new_window.overrideredirect(True)
                new_window.geometry(
                    '50x50+{}+{}'.format(self.x - i * 60, self.y - 60))
                image_path = rf"C:\Users\Vedo\Desktop\Coinis kurs\Fillio\assets\icons\icon{
                    i}.png"
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
                if i == 5:
                    settings_button_path = r"C:\Users\Vedo\Desktop\Coinis kurs\Fillio\assets\icons\settings.png"
                    self.imgSettingsButton = tk.PhotoImage(
                        file=settings_button_path)
                    new_button = tk.Button(
                        new_window, image=self.imgSettingsButton, command=self.settings)
                if i == 6:
                    exit_button_path = r"C:\Users\Vedo\Desktop\Coinis kurs\Fillio\assets\icons\exit.png"
                    self.imgExitbutton = tk.PhotoImage(file=exit_button_path)
                    new_button = tk.Button(
                        new_window, image=self.imgExitbutton, command=root.destroy)

                new_button.pack(side="left")
                self.floating_buttons.append(new_window)

            # Check if spawn_forms is True before creating "Floating Text" window
            new_window = None
            if self.spawn_forms.get() == "1":
                new_window = tk.Toplevel(self.master)
                new_window.title("Floating Text")
                new_window.attributes('-topmost', True)
                # Use StringVar to check the value
                new_window.overrideredirect(self.formBoarder.get() == "1")
                new_window.geometry(
                    "350x200+{}+{}".format(self.x - 250, self.y - 300))

                # Background color
                new_window.configure(bg="#242424")

                # Text input field
                self.text_input = tk.Entry(new_window)
                self.text_input.pack(pady=5, fill=tk.X)

                # Button to submit input
                submit_button = tk.Button(
                    new_window, text="Submit", command=self.submitInput)
                submit_button.pack(pady=5)

                # Text output field
                self.text_output = tk.Text(new_window, height=3, width=20)
                self.text_output.pack(fill=tk.BOTH, expand=True)

                # Button to copy output
                copy_button = tk.Button(
                    new_window, text="Copy Output", command=self.copyOutput)
                copy_button.pack(pady=5)

                # Add the new window to the list of floating buttons
                self.floating_buttons.append(new_window)

    def settings(self):
        if self.settings_window and tk.Toplevel.winfo_exists(self.settings_window):
            # If settings window is already open, close it
            self.settings_window.destroy()
            self.settings_window = None
        else:
            # Create a new settings window
            self.settings_window = tk.Toplevel(self.master)
            self.settings_window.title("Settings")
            self.settings_window.attributes('-topmost', True)
            self.settings_window.overrideredirect(True)
            self.settings_window.geometry(
                "150x70+{}+{}".format(self.x - 400, self.y - 150))
            self.settings_window.configure(bg="#242424")

            # Check button to toggle formBorder
            check_button = tk.Checkbutton(self.settings_window, text="Form Border", variable=self.formBoarder,
                                          onvalue="1", offvalue="0", command=self.toggleFormBorder)
            check_button.pack()

            # Check button to toggle spawn_forms
            spawn_button = tk.Checkbutton(self.settings_window, text="Spawn Forms", variable=self.spawn_forms,
                                          onvalue="1", offvalue="0", command=self.toggleFormBorder)
            spawn_button.pack()

    def toggleFormBorder(self):
        self.settings_window.destroy()
        # Force update of the application to reflect the changes
        # self.master.update_idletasks()

    def submitInput(self):
        # Get input from the input field
        input_text = self.text_input.get()

        # Clear the input field
        self.text_input.delete(0, tk.END)

        # Put the input text in the output field
        self.text_output.insert(tk.END, f"{input_text}\n")

    def copyOutput(self):
        # Get text from the output field
        output_text = self.text_output.get(1.0, tk.END)

        # Copy text to clipboard
        pyperclip.copy(output_text.strip())

        # Show confirmation message
        tkinter.messagebox.showinfo(
            "Copy Output", "Output copied to clipboard!")

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
