#!/bin/bash
echo "Запуск тестів Pytest..."
pytest --html=report.html --self-contained-html
if [ $? -ne 0 ]; then
    echo "Тести не пройшли!"
    exit 1
fi

echo "Перевірка стилю коду Flake8..."
flake8 . --format=html --htmldir=flake-report
if [ $? -ne 0 ]; then
    echo "Перевірка стилю коду не пройшла!"
    exit 1
fi

echo "Pipeline успішно виконано!"