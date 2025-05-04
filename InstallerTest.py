import tkinter as tk
from PIL import ImageTk, Image
from tkinter.ttk import Style, Checkbutton

def apply_system_theme(checkbuttons):
    try:
        style.theme_use("vista")  # Стандартная тема Windows Vista
        root.update_idletasks()   # Применение настроек мгновенно
    except Exception as e:
        print(f"Ошибка при применении темы: {e}")

    # Общий стиль
    style.configure("TCheckbutton", background="#FFFFFF", foreground="black", font=("Segoe UI", 10))
    style.map("TCheckbutton", background=[("selected", "#ADD8E6")], indicatorsize=[12])

    # Поддерживаем другие платформы
    for btn in checkbuttons:
        btn.state(["!disabled"])
        btn.style = "TCheckbutton"

def on_accept():
    global button_accept
    if button_accept["text"] == "Принять":
        # Меняем изображение и удаляем старый контент
        label_image.config(image=install_photo)
        label_title.destroy()
        label_license.destroy()
        
        # Обновляем текст кнопки
        button_accept.config(text="Далее")
        
        # Новое содержимое после нажатия
        frame_install_options = tk.Frame(root, bg="#FFFFFF")
        frame_install_options.pack(fill="both", expand=True)
        
        # Инструкция
        label_new = tk.Label(frame_install_options, text="Выберите, что хотите установить:", font=("Segoe UI", 16), bg="#FFFFFF")
        label_new.pack(pady=(10, 5))
        
        # Список флажков (чекбоксов)
        check_buttons = []
        
        var_classic_menu = tk.BooleanVar(value=False)
        check_classic_menu = Checkbutton(frame_install_options, text="Классическое контекст. меню с Acrylic", variable=var_classic_menu)
        check_classic_menu.pack(anchor="w", padx=20)
        check_buttons.append(check_classic_menu)
        
        var_start_menu = tk.BooleanVar(value=False)
        check_start_menu = Checkbutton(frame_install_options, text="Улучшенное Start Menu, а именно прозрачность.", variable=var_start_menu)
        check_start_menu.pack(anchor="w", padx=20)
        check_buttons.append(check_start_menu)
        
        var_drag_fix = tk.BooleanVar(value=False)
        check_drag_fix = Checkbutton(frame_install_options, text="Исправление перетаскивания 22H2+", variable=var_drag_fix)
        check_drag_fix.pack(anchor="w", padx=20)
        check_buttons.append(check_drag_fix)
        
        var_accent_colorizer = tk.BooleanVar(value=False)
        check_accent_colorizer = Checkbutton(frame_install_options, text="AccentColorizer", variable=var_accent_colorizer)
        check_accent_colorizer.pack(anchor="w", padx=20)
        check_buttons.append(check_accent_colorizer)
        
        var_fluent_msgbox = tk.BooleanVar(value=False)
        check_fluent_msgbox = Checkbutton(frame_install_options, text="FluentMsgBox - Fluent окна ошибок, предупреждений и просто сообщений.", variable=var_fluent_msgbox)
        check_fluent_msgbox.pack(anchor="w", padx=20)
        check_buttons.append(check_fluent_msgbox)
        
        # Автоматически применяем стиль Windows
        apply_system_theme(check_buttons)
    else:
        pass  # Последующие шаги можно добавить сюда

# Центровка окна
def center_window(window):
    window.update_idletasks()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    size = tuple(int(_) for _ in window.geometry().split('+')[0].split('x'))
    x = screen_width / 2 - size[0] / 2
    y = screen_height / 2 - size[1] / 2
    window.geometry("%dx%d+%d+%d" % (size + (x, y)))

# Основная программа
if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("700x500")
    root.resizable(False, False)
    root.title("Mod11 Installer")
    root.configure(bg="#FFFFFF")  # Белый фон

    center_window(root)  # Центральное размещение окна

    # Подготавливаем изображения
    img_eula = Image.open('eula.png').resize((250, 240), Image.LANCZOS)
    eula_photo = ImageTk.PhotoImage(img_eula)

    img_install = Image.open('install.png').resize((250, 200), Image.LANCZOS)
    install_photo = ImageTk.PhotoImage(img_install)

    # Логотип слева
    label_image = tk.Label(root, image=eula_photo, bg="#FFFFFF")
    label_image.pack(side="left", padx=(10, 20))

    # Панель с текстом
    frame_text = tk.Frame(root, bg="#FFFFFF")
    frame_text.pack(side="right", fill="both", expand=True)

    # Заголовок "Лицензия"
    label_title = tk.Label(frame_text, text="Лицензия", font=("Segoe UI Semibold", 16), bg="#FFFFFF")
    label_title.pack(pady=(10, 5))

    # Текст лицензии
    license_text = """
    1. Данный софт предоставляется \"Как есть\" и он полностью бесплатный.\n\n
    2. Автор не несёт ответственности за любой ущерб, включая баги,\nнеправильную установку и всё, что может вызвать повреждения ОС или модификаций.
    """

    label_license = tk.Label(frame_text, text=license_text, justify='left', wraplength=350, bg="#FFFFFF")
    label_license.pack(padx=10, pady=10)

    # Кнопка "Принять"
    button_accept = tk.Button(frame_text, text="Принять", command=on_accept, bg="#EFEFEF", fg="black", width=10, height=1, cursor="hand2")
    button_accept.pack(side="bottom", anchor="se", pady=(0, 10), padx=(0, 10))

    # Начальное выполнение
    root.mainloop()
