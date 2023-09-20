#!/bin/bash

# Функція для встановлення необхідних системних пакетів та Python 3.10
setup_system() {
    sudo apt update
    sudo apt upgrade -y
    sudo apt install python3.10 python3.10-venv python3-pip git -y
}

# Функція для налаштування сервера та встановлення необхідних компонентів
setup_server() {
    # Тут ви можете додати інші налаштування сервера, які вам потрібні

    # Приклад: встановлення бази даних SQLite
    sudo apt install sqlite3 -y
}

# Функція для встановлення проекту з репозиторію Git
install_project() {
    # Замініть URL репозиторію на свій
    git clone https://github.com/Hant0-0/telegram_bot_test.git
    cd core

    # Створення віртуального середовища
    python3.10 -m venv venv
    source venv/bin/activate

    # Встановлення залежностей
    pip install -r requirements.txt

    # Виконання міграцій бази даних (якщо використовуєте Django)
    python manage.py migrate
}

# Функція для оновлення проекту з репозиторію Git
update_project() {
    cd core
    git pull origin master
}

# Основний виконавчий код
echo "Налаштування сервера..."
setup_system
setup_server

echo "Встановлення та налаштування проекту..."
install_project

echo "Проект був успішно встановлений та налаштований."

# Інструкції для користувача
echo "Для оновлення проекту в майбутньому використовуйте команду: ./update_project.sh"
