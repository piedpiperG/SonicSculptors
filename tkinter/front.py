import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import pygame
import audio_processing  # 导入音频处理模块


class GUI(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("SonicSculptor音频处理系统")
        self.geometry("500x300")

        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill=tk.BOTH)

        self.page1 = tk.Frame(self.notebook)
        self.page2 = tk.Frame(self.notebook)
        self.page3 = tk.Frame(self.notebook)

        self.notebook.add(self.page1, text="欢迎使用")
        self.notebook.add(self.page2, text="歌声转换")
        self.notebook.add(self.page3, text="评分")

        self.create_page1()
        self.create_page2()
        self.create_page3()

    def create_page1(self):
        label = tk.Label(self.page1, text="欢迎使用SonicSculptor音频处理系统！", justify='center')
        label.place(relx=0.5, rely=0.5, anchor='center')

        next_button = tk.Button(self.page1, text="下一页", command=self.show_page2)
        next_button.place(relx=1, rely=1, anchor='se', x=-10, y=-10)

    def create_page2(self):
        def upload_file():
            filepath = filedialog.askopenfilename(filetypes=[("WAV files", "*.wav")])
            if filepath:
                messagebox.showinfo("上传成功", f"已上传文件: {filepath}")
                self.filepath = filepath
                self.file_uploaded.set(True)
                check_inputs()

        def select_option():
            selected_option = self.choice_var.get()
            messagebox.showinfo("选择成功", f"已选择选项: {selected_option}")
            self.option_selected.set(True)
            check_inputs()

        def check_inputs():
            if self.file_uploaded.get() and self.option_selected.get():
                self.process_button.config(state=tk.NORMAL)
                self.next_button.config(state=tk.NORMAL)
            else:
                self.process_button.config(state=tk.DISABLED)
                self.next_button.config(state=tk.DISABLED)

        def update_progress(progress):
            self.progressbar['value'] = progress

        def process_complete():
            messagebox.showinfo("处理完成", "音频处理完成，请点击下一页查看。")
            self.process_button.config(state=tk.NORMAL)

        self.file_uploaded = tk.BooleanVar(value=False)
        self.option_selected = tk.BooleanVar(value=False)

        upload_button = tk.Button(self.page2, text="上传文件", command=upload_file)
        upload_button.pack(side=tk.LEFT, padx=10, pady=10)

        choices = ["选项1", "选项2", "选项3", "选项4", "选项5"]
        self.choice_var = tk.StringVar()
        self.choice_var.set(choices[0])

        option_menu = tk.OptionMenu(self.page2, self.choice_var, *choices)
        option_menu.pack(side=tk.LEFT, padx=10, pady=10)

        select_button = tk.Button(self.page2, text="选择", command=select_option)
        select_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.process_button = tk.Button(self.page2, text="处理", command=self.process_audio, state=tk.DISABLED)
        self.process_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.next_button = tk.Button(self.page2, text="下一页", command=self.show_page3, state=tk.DISABLED)
        self.next_button.pack(side=tk.RIGHT, padx=10, pady=10)

        self.progressbar = ttk.Progressbar(self.page2, mode='determinate')
        self.progressbar.pack(side=tk.LEFT, padx=10, pady=10)

    def create_page3(self):
        def close_window():
            self.destroy()

        def play_audio():
            if hasattr(self, "processed_filepath"):
                pygame.mixer.init()
                pygame.mixer.music.load(self.processed_filepath)
                pygame.mixer.music.play()
                play_button.config(state=tk.DISABLED)
                stop_button.config(state=tk.NORMAL)

        def stop_audio():
            if pygame.mixer.get_init():
                pygame.mixer.music.stop()
                stop_button.config(state=tk.DISABLED)
                play_button.config(state=tk.NORMAL)

        def finish_rating():
            rating = rating_scale.get()
            messagebox.showinfo("评分完成", f"您给系统的评分是: {rating}")
            close_window()

        rating_label = tk.Label(self.page3, text="请为系统评分（满分5星）:")
        rating_label.pack(padx=10, pady=10)

        rating_scale = tk.Scale(self.page3, from_=0, to=5, orient=tk.HORIZONTAL, tickinterval=1)
        rating_scale.pack(padx=10, pady=10)

        finish_button = tk.Button(self.page3, text="完成评分", command=finish_rating)
        finish_button.pack(side=tk.RIGHT, padx=10, pady=10)

        play_button = tk.Button(self.page3, text="播放", command=play_audio)
        play_button.pack(side=tk.LEFT, padx=10, pady=10)

        stop_button = tk.Button(self.page3, text="暂停", command=stop_audio, state=tk.DISABLED)
        stop_button.pack(side=tk.LEFT, padx=10, pady=10)

    def show_page2(self):
        self.notebook.select(self.page2)

    def show_page3(self):
        self.notebook.select(self.page3)

    def process_audio(self):
        if not hasattr(self, "filepath"):
            messagebox.showerror("错误", "请先上传文件。")
            return

        if not self.file_uploaded.get() or not self.option_selected.get():
            messagebox.showerror("错误", "请先选择文件和选项。")
            return

        processed_filepath = audio_processing.process_audio(self.filepath, self.choice_var.get())
        messagebox.showinfo("处理完成", "音频处理完成，请下载文件。")
        self.process_button.config(state=tk.NORMAL)

        self.processed_filepath = processed_filepath


if __name__ == "__main__":
    app = GUI()
    app.mainloop()
