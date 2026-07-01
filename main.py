import tkinter as tk
from tkinter import filedialog, messagebox
from excel_reader import read_excel


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("传输设备验收纪要自动生成工具")
        self.root.geometry("650x320")
        self.root.resizable(False, False)

        self.excel_path = tk.StringVar()
        self.word_path = tk.StringVar()
        self.output_path = tk.StringVar()

        self.create_ui()

    def create_ui(self):
        tk.Label(self.root, text="Excel文件：").place(x=20, y=30)
        tk.Entry(self.root, textvariable=self.excel_path, width=60).place(x=90, y=30)
        tk.Button(self.root, text="浏览", command=self.select_excel).place(x=560, y=26)

        tk.Label(self.root, text="Word模板：").place(x=20, y=80)
        tk.Entry(self.root, textvariable=self.word_path, width=60).place(x=90, y=80)
        tk.Button(self.root, text="浏览", command=self.select_word).place(x=560, y=76)

        tk.Label(self.root, text="输出目录：").place(x=20, y=130)
        tk.Entry(self.root, textvariable=self.output_path, width=60).place(x=90, y=130)
        tk.Button(self.root, text="浏览", command=self.select_output).place(x=560, y=126)

        tk.Button(
            self.root,
            text="生成纪要",
            width=20,
            height=2,
            command=self.generate
        ).place(x=220, y=190)

    def select_excel(self):
        filename = filedialog.askopenfilename(
            title="选择Excel文件",
            filetypes=[("Excel文件", "*.xlsx *.xls")]
        )
        if filename:
            self.excel_path.set(filename)

    def select_word(self):
        filename = filedialog.askopenfilename(
            title="选择Word模板",
            filetypes=[("Word文件", "*.docx")]
        )
        if filename:
            self.word_path.set(filename)

    def select_output(self):
        folder = filedialog.askdirectory(title="选择输出目录")
        if folder:
            self.output_path.set(folder)

    def generate(self):
        if not self.excel_path.get():
            messagebox.showwarning("提示", "请选择Excel文件")
            return

        if not self.word_path.get():
            messagebox.showwarning("提示", "请选择Word模板")
            return

        if not self.output_path.get():
            messagebox.showwarning("提示", "请选择输出目录")
            return

        try:
            data = read_excel(self.excel_path.get())

            print(data)

            messagebox.showinfo(
                "完成",
                "Excel读取成功！"
            )

        except Exception as e:
            messagebox.showerror("错误", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()