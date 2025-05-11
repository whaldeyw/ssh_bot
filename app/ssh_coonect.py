import paramiko
from aiogram import Router, F
from aiogram.types import Message
from dotenv import load_dotenv
import asyncio
import os

load_dotenv()
router_ssh = Router()

def run_ssh_command(command: str) -> str:
    """Синхронная функция для выполнения SSH-команд."""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(
            hostname=os.getenv('host'),
            username=os.getenv('user_name'),
            password=os.getenv('password_host'),
            #key_filename=os.getenv('key_filename')#При использовании ssh_key
        )

        stdin, stdout, stderr = ssh.exec_command(command)
        output = stdout.read().decode().strip()
        error = stderr.read().decode().strip()
        return output if output else error or "Команда выполнена."
    except Exception as e:
        return f"Ошибка: {e}"
    finally:
        ssh.close()


@router_ssh.message(F.text == 'Создать папку')
async def handle_create_folder(message: Message):
    """Создает папку на сервере через SSH."""
    command = "mkdir -p /root/my_new_folder"

    # Запускаем в отдельном потоке, чтобы не блокировать бота
    result = await asyncio.to_thread(run_ssh_command, command)
    await message.answer(f"Результат:\n{result}")


@router_ssh.message(F.text.startswith("/cmd "))
async def handle_custom_command(message: Message):
    """Выполняет любую команду после /cmd."""
    user_command = message.text.split("/cmd ")[1]
    if not user_command:
        await message.answer("Укажите команду, например: /cmd ls /")
        return

    result = await asyncio.to_thread(run_ssh_command, user_command)
    await message.answer(f"Результат:\n{result}")

#Обработчик команд и текса которого нет в хэндлерах
@router_ssh.message(F.text)
async def message(message: Message):
    await message.answer(f"Воспользуйтесь кнопкой или используйте команды linux, например:  /cmd ls / ")


@router_ssh.message(~F.text)
async def handle_non_text(message: Message):
    if message.photo:
        await message.answer("📷 Фото не поддерживаются! Воспользуйтесь кнопкой или используйте команды linux, например:  /cmd ls /")
    elif message.voice:
        await message.answer("🎤 Голосовые сообщения не принимаются. Воспользуйтесь кнопкой или используйте команды linux, например:  /cmd ls /")
    elif message.sticker:
        await message.answer("😺 Стикеры милые, но бот работает только с текстом. Воспользуйтесь кнопкой или используйте команды linux, например:  /cmd ls /")
    else:
        await message.answer("❌ Неподдерживаемый формат сообщения. Воспользуйтесь кнопкой или используйте команды linux, например:  /cmd ls /")