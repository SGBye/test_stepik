# Django-DRF-Celery-Rabbit-Vue-Docker-docker-compose project

Фронт и бэк проекта, который позволяет пользователю отправлять задания на проверку на внешний сервис.

# Как запустить?
Спулить проект и выполнить 
```docker-compose up --build```

# Что можно улучшить?
- Весь фронтенд. Написал, как умею, вроде бы что-то даже работает.

- Добавить документацию - swagger, PlantUML схемы и т.д.

- Можно сделать простенький CI с тестами и заливкой документов на сервер.

- Можно сделать разные docker-compose.yml и файлы с переменными окружения для разных сред разработки - локалки, дева и прода.

- Обсудить варианты флоу на бэкенде, потому что из ТЗ было не совсем ясно :(

- Добавить авторизацию. В своём отдельном проекте у меня есть готовый вариант JWT авторизации с обновлениями токенов и инвалидацией, однако в ТЗ такой задачи не стояло, поэтому на бэке кое-где есть достаточно странные места.

**NB!** Я реализовал тот вариант на бэке, который показался мне уместным, такой подход я хотя бы могу обосновать. Возможно, есть более оптимальные пути.



