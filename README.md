# easy_habr_spider_with_stats

Простой хабр парсер с аданизом данных

# Подготовка:

 - установить python3.6
 - virtualenv -p python3.6 venv
 - sourve venv/bin/activate
 - pip install -r requirements.txt
 
# Запуск:

 # - python3.6 -m main gather - Сбор данных с сохранением в json
 # - python3.6 -m main transform - Трансформация данных из json в табличный csv
 # - python3.6 -m main stats - Вывод некоторой статистики данных
 
 Вы можете спарсить любой другой хаб, просто заменив ссылки на нужный хаб в файле habr_spider.py в переменной 'allowed_domains' и 'start_urls'
 
 Использовал:
  - python3.6
  - scrapy
  - pandas
  - subprocess
  
 
Специально для Otus.ru в качестве дз.

https://youtu.be/huQK5OuEGIo - ссылка на процесс работы скрипта
