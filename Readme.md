📌 Описание проекта
Этот Telegram-бот позволяет авторизованным пользователям выполнять команды на удалённом сервере прямо из чата Telegram. 
Бот обеспечивает безопасное выполнение команд с логированием действий.

🌟 Основные функции
🔐 Авторизация пользователей по паролю который хранится в .env

💻 Выполнение ssh-команд на сервере

📋 Просмотр результатов выполнения команд

📝 Логирование всех действий

⚙️ Установка и настройка
Требования
Python 3.8+

Сервер с доступом к Telegram API

Аккаунт в Telegram с созданным ботом через @BotFather

Установка
bash
git clone https://github.com/whaldeyw/ssh_bot.git
cd ssh_bot

Настройка
Создайте файл .env в корне проекта:

PASSWORD = 'secret_password' #пароль для авторизации

TG_TOKEN = ваш_токен_бота    #без кавычек

host= 'ваш ip адрес сревера'

user_name="имя вашего пользователя"

password_host="ваш пароль от сервера"  

key_filename= # путь к ключу, например "/home/user/.ssh/id_rsa"


🚀 Запуск бота
1. docker
docker build --tag name:ssh_bot .     #создаем образ/create images

docker run --restart=always -it --name ssh_bot -d name_images   #создаем контейнер с автоматическим рестартом контенера 
                                                                 при перезагрузке  сервера
2. Создайте виртуальное окружение  
Linux/macOS:
bash
python3 -m venv venv
Активируйте виртуальное окружение
source venv/bin/activate
Установите зависимости 
pip install -r requirements.txt
Запустите бота
python3 run.py

Windows:
bash
python -m venv venv
Активируйте виртуальное окружение
venv\Scripts\activate
Установите зависимости 
pip install -r requirements.txt
Запустите бота
python run.py



                                                                 



