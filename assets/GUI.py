import tkinter as tk
import pyperclip
from assets.aiResponse import message_validation
from assets.image_text_detect import screenshot_to_text
import pyautogui as pg


def withdraw_app(self):
    self.master.withdraw()
    for window in root.winfo_children():
        if isinstance(window, tk.Toplevel):
            window.withdraw()


def deiconify_app(self):
    self.master.deiconify()
    for window in root.winfo_children():
        if isinstance(window, tk.Toplevel):
            window.deiconify()


class FloatingButton:
    def __init__(self, master):
        self.master = master
        self.floating_buttons = []  # List to store references to the floating buttons
        # Use StringVar to store the state
        self.settings_window = None
        self.formBoarder = tk.StringVar(value="1")
        # Variable to control the spawning of input and output form window
        self.spawn_forms = tk.StringVar(value="1")
        self.prompt_advisory = tk.StringVar(value="0")
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
            file=r"Fillio\assets\icons\main_button.png")
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
        # print("Button clicked!")
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
                image_path = rf"Fillio\assets\icons\icon{
                    i}.png"
                if i == 1:
                    self.img1 = tk.PhotoImage(file=image_path)
                    new_button = tk.Button(
                        new_window, image=self.img1, command=self.excuse)
                if i == 2:
                    self.img2 = tk.PhotoImage(file=image_path)
                    new_button = tk.Button(
                        new_window, image=self.img2, command=self.accept)
                if i == 3:
                    self.img3 = tk.PhotoImage(file=image_path)
                    new_button = tk.Button(
                        new_window, image=self.img3, command=self.shortly_summarized)
                if i == 4:
                    self.img4 = tk.PhotoImage(file=image_path)
                    new_button = tk.Button(
                        new_window, image=self.img4, command=self.reject)
                if i == 5:
                    settings_button_path = r"Fillio\assets\icons\settings.png"
                    self.imgSettingsButton = tk.PhotoImage(
                        file=settings_button_path)
                    new_button = tk.Button(
                        new_window, image=self.imgSettingsButton, command=self.settings)
                if i == 6:
                    exit_button_path = r"Fillio\assets\icons\exit.png"
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
                new_window.overrideredirect(self.formBoarder.get() == "0")
                new_window.geometry(
                    "530x330+{}+{}".format(self.x - 450, self.y - 450))

                # Background color
                new_window.configure(bg="#242424")

                # Text input field
                self.text_input = tk.Entry(new_window)
                self.text_input.pack(pady=5, fill=tk.X)

                input_button_frame = tk.Frame(new_window)
                input_button_frame.pack()

                # Create a button to clear input
                clear_input_button = tk.Button(
                    input_button_frame, text="Clear Input", command=self.clearInput)
                clear_input_button.pack(side="left")

                # Create a button to submit input
                submit_button = tk.Button(
                    input_button_frame, text="Submit", command=self.submitInput)
                submit_button.pack(side="left")

                # Create the text output field
                self.text_output = tk.Text(new_window, height=3, width=20)
                self.text_output.pack(fill=tk.BOTH, expand=True)

                # Create a frame for output text and buttons
                output_frame = tk.Frame(new_window)
                output_frame.pack()

                # Create a button to clear output
                clear_output_button = tk.Button(
                    output_frame, text="Clear Output", command=self.clearOutput)
                clear_output_button.pack(side="left")

                # Create a button to copy output
                copy_output_button = tk.Button(
                    output_frame, text="Copy Output", command=self.copyOutput)
                copy_output_button.pack(side="left")

                # Add the new window to the list of floating buttons
                self.floating_buttons.append(new_window)

    def clearInput(self):
        # Clear the input field
        self.text_input.delete(0, tk.END)

    def clearOutput(self):
        # Clear the output field
        self.text_output.delete(1.0, tk.END)

    def excuse(self):
        withdraw_app(self)
        try:
            message = screenshot_to_text()
        except Exception as e:
            if self.spawn_forms.get() == "1":
                self.text_output.insert(tk.END,
                                        f"\nScreenshot failed by exception: {e}\n ")

        if self.prompt_advisory.get() == "1":
            try:
                if self.spawn_forms.get() == "1":
                    self.text_input.insert(tk.END, message + ' --excuse--')
            except:
                if self.spawn_forms.get() == "1":
                    self.text_output.insert(
                        tk.END, "\nScreenshot failed or canceled or blank\n")
        else:
            self.submitToAi(message, ' --excuse--')
        deiconify_app(self)

    def accept(self):
        withdraw_app(self)
        try:
            message = screenshot_to_text()
        except Exception as e:
            if self.spawn_forms.get() == "1":
                self.text_output.insert(tk.END,
                                        f"\nScreenshot failed by exception: {e}\n ")

        if self.prompt_advisory.get() == "1":
            try:
                if self.spawn_forms.get() == "1":
                    self.text_input.insert(tk.END, message + ' --acception--')
            except:
                if self.spawn_forms.get() == "1":
                    self.text_output.insert(
                        tk.END, "\nScreenshot failed or canceled or blank\n")
        else:
            self.submitToAi(message, ' --acception--')
        deiconify_app(self)

    def shortly_summarized(self):
        withdraw_app(self)
        try:
            message = screenshot_to_text()
        except Exception as e:
            self.text_output.insert(tk.END,
                                    f"\nScreenshot failed by exception: {e}\n ")

        if self.prompt_advisory.get() == "1":
            try:
                self.text_input.insert(
                    tk.END, message + ' --shortly summarized--')
            except:
                self.text_output.insert(
                    tk.END, "\nScreenshot failed or canceled or blank\n")
        else:
            self.submitToAi(message, ' --shortly summarized--')
        deiconify_app(self)

    def reject(self):
        withdraw_app(self)
        try:
            message = screenshot_to_text()
        except Exception as e:
            if self.spawn_forms.get() == "1":
                self.text_output.insert(tk.END,
                                        f"\nScreenshot failed by exception: {e}\n ")

        if self.spawn_forms.get() == "1" and self.prompt_advisory.get() == "1":
            try:
                self.text_input.insert(tk.END, message + ' --rejection--')
            except:
                self.text_output.insert(
                    tk.END, "\nScreenshot failed or canceled or blank\n")
        else:
            self.submitToAi(message, ' --rejection--')
        deiconify_app(self)

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
                "150x100+{}+{}".format(self.x - 400, self.y - 150))
            self.settings_window.configure(bg="#242424")

            # Check button to toggle formBorder
            check_button = tk.Checkbutton(self.settings_window, text="Form Border", variable=self.formBoarder,
                                          onvalue="1", offvalue="0", command=self.toggleFormBorder)
            check_button.configure(bg="yellow")
            check_button.pack()

            # Check button to toggle spawn_forms
            spawn_button = tk.Checkbutton(self.settings_window, text="Spawn Forms", variable=self.spawn_forms,
                                          onvalue="1", offvalue="0", command=self.toggleFormBorder)
            spawn_button.configure(bg="yellow")
            spawn_button.pack()

            # Check button to turn on prompt advisory
            if self.spawn_forms.get() == "1":
                prompt_advisory_button = tk.Checkbutton(
                    self.settings_window, text="Prompt Advisory", variable=self.prompt_advisory, onvalue="1", offvalue="0", command=self.toggleFormBorder)
                prompt_advisory_button.configure(bg="yellow")
                prompt_advisory_button.pack()

    def toggleFormBorder(self):
        self.settings_window.destroy()
        if self.spawn_forms.get() == "0":
            self.prompt_advisory.set("0")
        # Force update of the application to reflect the changes
        # self.master.update_idletasks()

    def submitInput(self):
        # Get input from the input field
        input_text = self.text_input.get()

        # Clear the input field
        self.text_input.delete(0, tk.END)

        # Put the input text in the output field
        self.submitToAi(input_text)

    def submitToAi(self, prompt, option=''):
        if prompt == -1 or prompt == '':
            if self.spawn_forms.get() == "1":
                self.text_output.insert(
                    tk.END, "\nScreenshot failed or canceled or blank\n")
            return

        response = message_validation(prompt + option)
        if self.spawn_forms.get() == "1":
            self.text_output.insert(
                tk.END, f"\n{response}\n")
        pyperclip.copy(response)
        pg.hotkey('ctrl', 'v')
        pg.hotkey('ctrl', 'a')

    def copyOutput(self):
        # Get text from the output field
        output_text = self.text_output.get(1.0, tk.END)

        # Copy text to clipboard
        pyperclip.copy(output_text.strip())

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


root = tk.Tk()
app = FloatingButton(root)
