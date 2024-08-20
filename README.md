## Развертка проекта

```bash
cp example.env .env
```
```bash
sudo docker-compose up -d
```
```bash
pipenv install
```
```bash
pipenv shell
```
```bash
python backend/manage.py makemigrations
```
```bash
python backend/manage.py migrate
```
```bash
python backend/manage.py createsuperuser
```
```bash
python backend/manage.py runserver
```

**Сваггер с эндами для всех четырех заданий доступен по /api/docs/**
