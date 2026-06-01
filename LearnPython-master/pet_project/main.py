import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import shutil
import time
import threading


class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class DoublyNode:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None


class Queue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def is_empty(self):
        return self.head is None

    def put(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def get(self):
        if self.is_empty():
            return None
        target_data = self.head.value
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        self.count -= 1
        return target_data


class Stack:
    def __init__(self):
        self.top = None
        self.count = 0

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self.count += 1

    def pull(self):
        if self.is_empty():
            return None
        target_data = self.top.value
        self.top = self.top.next
        self.count -= 1
        return target_data


class Deque:
    def __init__(self):
        self.left = None
        self.right = None
        self.count = 0

    def is_empty(self):
        return self.left is None

    def Rput(self, data):
        new_node = DoublyNode(data)
        if self.is_empty():
            self.left = new_node
            self.right = new_node
        else:
            new_node.prev = self.right
            self.right.next = new_node
            self.right = new_node
        self.count += 1

    def Lget(self):
        if self.is_empty():
            return None
        target_data = self.left.value
        self.left = self.left.next
        if self.left is None:
            self.right = None
        else:
            self.left.prev = None
        self.count -= 1
        return target_data

    def to_list(self):
        res = []
        curr = self.left
        while curr:
            res.append(curr.value)
            curr = curr.next
        return res


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("System Optimizer & Search")
        self.root.geometry("850x550")

        self.undo_stack = Stack()
        self.log_deque = Deque()

        self.quarantine_dir = os.path.join(os.getcwd(), "_quarantine")
        if not os.path.exists(self.quarantine_dir):
            os.makedirs(self.quarantine_dir)

        self.main_frame = ttk.Frame(self.root, padding="10")
        self.main_frame.pack(fill="both", expand=True)

        self.control_frame = ttk.Frame(self.main_frame)
        self.control_frame.pack(fill="x", pady=(0, 10))

        ttk.Label(self.control_frame, text="Директория сканирования:").grid(row=0, column=0, sticky="w")
        self.dir_entry = ttk.Entry(self.control_frame, width=50)
        self.dir_entry.grid(row=0, column=1, padx=5, sticky="we")
        ttk.Button(self.control_frame, text="Обзор...", command=self.browse_dir).grid(row=0, column=2, padx=5)

        ttk.Label(self.control_frame, text="Имя файла (для поиска):").grid(row=1, column=0, sticky="w", pady=5)
        self.file_entry = ttk.Entry(self.control_frame, width=50)
        self.file_entry.grid(row=1, column=1, padx=5, pady=5, sticky="we")

        self.btn_frame = ttk.Frame(self.control_frame)
        self.btn_frame.grid(row=2, column=0, columnspan=3, pady=10, sticky="w")

        self.search_btn = ttk.Button(self.btn_frame, text="Найти файл", command=lambda: self.start_task("search"))
        self.search_btn.pack(side="left", padx=(0, 10))

        self.junk_btn = ttk.Button(self.btn_frame, text="Найти мусор (.tmp, .log)",
                                   command=lambda: self.start_task("junk"))
        self.junk_btn.pack(side="left")

        self.results_frame = ttk.LabelFrame(self.main_frame, text="Результаты сканирования", padding="5")
        self.results_frame.pack(fill="both", expand=True)

        self.results_listbox = tk.Listbox(self.results_frame, selectmode=tk.EXTENDED)
        self.results_listbox.pack(side="left", fill="both", expand=True)

        self.scrollbar = ttk.Scrollbar(self.results_frame, orient="vertical", command=self.results_listbox.yview)
        self.scrollbar.pack(side="right", fill="y")
        self.results_listbox.config(yscrollcommand=self.scrollbar.set)

        self.action_frame = ttk.Frame(self.main_frame)
        self.action_frame.pack(fill="x", pady=10)

        self.select_all_btn = ttk.Button(self.action_frame, text="Выбрать все", command=self.select_all_items)
        self.select_all_btn.pack(side="left", padx=(0, 10))

        self.delete_btn = ttk.Button(self.action_frame, text="Удалить выбранное", command=self.delete_selected)
        self.delete_btn.pack(side="left", padx=(0, 10))

        self.restore_btn = ttk.Button(self.action_frame, text="Восстановить последнее", command=self.restore_last)
        self.restore_btn.pack(side="left")

        self.log_frame = ttk.LabelFrame(self.main_frame, text="Журнал действий", padding="5")
        self.log_frame.pack(fill="x")

        self.log_label = ttk.Label(self.log_frame, text="Готово к работе", font=("Consolas", 9))
        self.log_label.pack(anchor="w")

        self.add_log("Программа запущена")

    def browse_dir(self):
        selected = filedialog.askdirectory()
        if selected:
            self.dir_entry.delete(0, tk.END)
            self.dir_entry.insert(0, selected)

    def add_log(self, message):
        time_str = time.strftime("%H:%M:%S")
        full_msg = f"[{time_str}] {message}"
        self.log_deque.Rput(full_msg)
        if self.log_deque.count > 5:
            self.log_deque.Lget()

        log_text = "\n".join(self.log_deque.to_list())
        self.log_label.config(text=log_text)

    def start_task(self, mode):
        start_dir = self.dir_entry.get().strip()
        if not start_dir or not os.path.exists(start_dir):
            messagebox.showerror("Ошибка", "Выберите существующую директорию")
            return

        self.search_btn.config(state="disabled")
        self.junk_btn.config(state="disabled")
        self.results_listbox.delete(0, tk.END)

        if mode == "search":
            target = self.file_entry.get().strip().lower()
            if not target:
                self.search_btn.config(state="normal")
                self.junk_btn.config(state="normal")
                return
            self.add_log(f"Начат поиск файла: {target}")
            threading.Thread(target=self.scan_fs, args=(start_dir, target, "search"), daemon=True).start()
        else:
            self.add_log("Начат поиск системного мусора")
            threading.Thread(target=self.scan_fs, args=(start_dir, "", "junk"), daemon=True).start()

    def scan_fs(self, start_dir, target, mode):
        q = Queue()
        q.put(start_dir)
        found_count = 0
        junk_exts = [".tmp", ".log", ".bak", ".old"]

        while not q.is_empty():
            curr_dir = q.get()
            try:
                for item in os.listdir(curr_dir):
                    full_path = os.path.join(curr_dir, item)
                    if os.path.isdir(full_path):
                        q.put(full_path)
                    else:
                        match = False
                        if mode == "search" and target in item.lower():
                            match = True
                        elif mode == "junk":
                            _, ext = os.path.splitext(item.lower())
                            if ext in junk_exts:
                                match = True

                        if match:
                            self.results_listbox.insert(tk.END, full_path)
                            found_count += 1
                            if found_count >= 200:
                                break
            except PermissionError:
                continue

            if found_count >= 200:
                break

        self.add_log(f"Сканирование завершено. Найдено объектов: {found_count}")
        self.search_btn.config(state="normal")
        self.junk_btn.config(state="normal")

    def select_all_items(self):
        self.results_listbox.select_set(0, tk.END)

    def delete_selected(self):
        selection = self.results_listbox.curselection()
        if not selection:
            return

        deleted_batch = []

        for index in sorted(selection, reverse=True):
            file_path = self.results_listbox.get(index)
            if not os.path.exists(file_path):
                self.results_listbox.delete(index)
                continue

            timestamp = str(int(time.time() * 1000))
            safe_name = f"{timestamp}_{index}_{os.path.basename(file_path)}"
            quarantine_path = os.path.join(self.quarantine_dir, safe_name)

            try:
                shutil.move(file_path, quarantine_path)
                deleted_batch.append((file_path, quarantine_path))
                self.results_listbox.delete(index)
            except Exception:
                pass

        if deleted_batch:
            self.undo_stack.push(deleted_batch)
            self.add_log(f"Удалено файлов: {len(deleted_batch)}")

    def restore_last(self):
        if self.undo_stack.is_empty():
            self.add_log("Корзина пуста, нечего восстанавливать")
            return

        batch = self.undo_stack.pull()
        if batch:
            restored_count = 0
            for orig_path, quar_path in batch:
                if os.path.exists(quar_path):
                    try:
                        os.makedirs(os.path.dirname(orig_path), exist_ok=True)
                        shutil.move(quar_path, orig_path)
                        restored_count += 1
                    except Exception:
                        pass

            if restored_count > 0:
                self.add_log(f"Восстановлено файлов: {restored_count}")
            else:
                self.add_log("Не удалось восстановить файлы")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()