## Интернет магазин "Shop-tech" на фреймворке Django

### Описание проекта:

Это мой pet-project, который я создаю, пока изучаю фреймворк Django, а также всё, что касается веб-разработки, а именно:
HTML, CSS, JavaScript.

### Используемые технологии:

- python
- Django
- pillow
- ipython

### Как запустить проект?:

1. Клонируйте проект с GitHub себе на ПК:

2. Создайте и активируйте виртуальное окружение:

- Инструкция для работы через виртуальное окружение - poetry:
  Создает виртуальное окружение -> Активирует виртуальное окружение -> Установить зависимости:

```text
poetry init
poetry shell
poetry install
```

- Инструкция для активации виртуального окружения - pip:
  Создает виртуальное окружение:

```text
python3 -m venv venv
```

Активирует виртуальное окружение:

```text
source env/bin/activate              # для Linux и Mac
source env\Scripts\activate          # для Windows
source env\Scripts\activate.bat      # для Windows
```

Установить зависимости:

```text
pip install -r requirements.txt
```

3. В корне проекта есть файл ".env.sample". Переименуйте его в ".env" и внесите в этот файл информацию
   о созданной вами базе (название, пароль и т.д.), а также информацию о данных admin, данные почтового сервера и т.д.
- О настройке почты smtp: 
[Настройка почтового сервиса SMTP ](https://proghunter.ru/articles/setting-up-the-smtp-mail-service-for-yandex-in-django)

4. Создайте базу данных postgresql.

5. Создаем таблицы в БД:

```text
python manage.py migrate
```

6. При необходимости заполните базу данных тестовыми данными следующей командой:

```text
python manage.py fill_db
```

7. Установите Redis:

  - Linux команда:
   ```text
   sudo apt install redis; 
  или 
  sudo yum install redis;
   ```

  - macOS команда:
   ```text
   brew install redis;
   ```

  Windows инструкция:
  - [Перейти на Redis docs](https://redis.io/docs/install/install-redis/install-redis-on-windows/)

8. Запустите проект:

```text
python manage.py runserver
```

9. Перейдите по адресу вашего локального компьютера в браузере:

```text
http://127.0.0.1:8000
```