import logging
import sys
import subprocess
from transform import to_csv
from make_stats import stats


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    logger.info("Work started")

    if sys.argv[1] == 'gather':

        # Ниже представлен вызов парсера Scrapy с аргументом,
        # который заворачивает спарсенную дату в json.
        # Вы можете изменить формат сsv на любой удобный для вас (csv/xml).
        # Достаточно лишь изменить в переменной args формат файла,
        # указанный в конце списка, а именно 'data.json'

        args = ['scrapy', 'crawl', 'habr', '-o', 'data.json']
        subprocess.Popen(args)


    elif sys.argv[1] == 'transform':
        to_csv()

    elif sys.argv[1] == 'stats':
        stats()

    logger.info("work ended")
