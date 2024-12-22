import os
import tkinter as tk
from tkinter import messagebox, filedialog

class FileManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Manager")
        self.root.geometry("400x200")
        
        # Метки и поле ввода для названия файла
        self.label = tk.Label(root, text="Введите название файла с расширением .txt:")
        self.label.pack(pady=10)
        
        self.file_name_entry = tk.Entry(root, width=40)
        self.file_name_entry.pack(pady=5)
        
        self.create_button = tk.Button(root, text="Подтвердить", command=self.check_file)
        self.create_button.pack(pady=10)
        
        self.action_frame = tk.Frame(root)
        self.action_frame.pack(pady=10)

    def check_file(self):
        file_name = self.file_name_entry.get()
        
        if not file_name.endswith('.txt'):
            messagebox.showerror("Ошибка", "Файл должен иметь расширение .txt")
            return
        
        if not os.path.exists(file_name):
            self.ask_create_file(file_name)
        else:
            self.show_action_options(file_name)
    
    def ask_create_file(self, file_name):
        result = messagebox.askyesno("Файл не найден", f"Файл '{file_name}' не найден. Хотите создать его?")
        if result:
            try:
                open(file_name, 'w').close()  # Создание пустого файла
                messagebox.showinfo("Успех", f"Файл '{file_name}' создан.")
                self.show_action_options(file_name)
            except Exception as e:
                messagebox.showerror("Ошибка", f"Не удалось создать файл: {e}")
        else:
            self.file_name_entry.delete(0, tk.END)  # Очищаем поле ввода
    
    def show_action_options(self, file_name):
        # Очистка старых элементов управления
        for widget in self.action_frame.winfo_children():
            widget.destroy()
        
        tk.Label(self.action_frame, text="Выберите действие:").pack(pady=5)
        
        tk.Button(self.action_frame, text="Чтение файла", command=lambda: self.read_file(file_name)).pack(pady=2)
        tk.Button(self.action_frame, text="Редактировать файл", command=lambda: self.edit_file(file_name)).pack(pady=2)
        tk.Button(self.action_frame, text="Назад", command=self.reset).pack(pady=2)
    
    def read_file(self, file_name):
        read_mode = messagebox.askquestion("Режим чтения", "Читать весь файл (Yes) или построчно (No)?")
        
        try:
            with open(file_name, 'r') as file:
                if read_mode == 'yes':
                    content = file.read()
                    messagebox.showinfo("Содержание файла", content)
                else:
                    lines = file.readlines()
                    for line in lines:
                        messagebox.showinfo("Чтение построчно", line.strip())
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при чтении файла: {e}")
    
    def edit_file(self, file_name):
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Редактирование файла")
        edit_window.geometry("400x200")
        
        tk.Label(edit_window, text="Введите текст для добавления в файл:").pack(pady=10)
        
        self.text_entry = tk.Text(edit_window, height=5, width=40)
        self.text_entry.pack(pady=5)
        
        tk.Button(edit_window, text="Сохранить текст", command=lambda: self.save_text(file_name, edit_window)).pack(pady=10)
    
    def save_text(self, file_name, edit_window):
        text = self.text_entry.get("1.0", tk.END).strip()
        
        if text == '/end':
            edit_window.destroy()
            return
        
        try:
            with open(file_name, 'a') as file:
                file.write(text + '\n')
            messagebox.showinfo("Успех", "Текст успешно добавлен в файл.")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Ошибка при записи в файл: {e}")
        
        edit_window.destroy()
    
    def reset(self):
        self.file_name_entry.delete(0, tk.END)
        for widget in self.action_frame.winfo_children():
            widget.destroy()

# Создание окна
root = tk.Tk()
app = FileManagerApp(root)
root.mainloop()