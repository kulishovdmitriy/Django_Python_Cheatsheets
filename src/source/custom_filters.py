import re


def highlight_code(text):
    # Убираем переносы строк внутри многострочных конструкций с точками
    text = re.sub(r'(from\s+\.\w+)\s*\n\s*(import\s+\w+)', r'\1 \2', text)
    text = re.sub(r'(from\s+\w+)\s*\n\s*(import\s+\w+)', r'\1 \2', text)

    # Убираем переносы строк после строки с кодом и заменяем на пробел
    text = re.sub(r'([^\n]+)\n+', r'\1 ', text)

    # Добавляем перенос строки только перед "class"
    text = re.sub(r'(?<!\n)\bclass\s+', r'\nclass ', text)

    # Добавляем пустую строку перед "ЗАКЛЮЧЕНИЕ"
    text = re.sub(r'(?<!\n)\bЗАКЛЮЧЕНИЕ\b', r'\n\nЗАКЛЮЧЕНИЕ\n\n', text)

    # Объединяем строки, если они начинаются и заканчиваются на дефис
    text = re.sub(r'(?<!\n)-\s*(.*?)\n-\s*(.*)', r'- \1 \2', text)

    # Оборачиваем команды терминала в теги <pre><code> для выделения
    command_pattern = (r"\b(sudo|apt|pip|python|git|newgrp|docker|docker-compose|curl|gunicorn|export|bind|debug|toolbar|"
                       r"ls|cd|INSTALLED_APPS|INTERNAL_IPS)\s+[^\n]*")

    text = re.sub(command_pattern, r'<pre><code>\g<0></code></pre>', text)

    # Замена для оборачивания кода Python в теги <pre><code> для многострочного кода
    python_pattern = r"(class\s+\w+.*?:|def\s+\w+.*?:|from\s+\w+.*|import\s+\w+.*|[ ]{4}.*)"
    highlighted_text = re.sub(python_pattern, r'<pre><code>\1</code></pre>', text)

    # Регулярное выражение для ключевых слов Python
    keyword_pattern = r"\b(class|def|import|from|return|for|if|else|elif|try|except|with|as|while|break|continue)\b"

    # Выделение ключевых слов Python с помощью <span> и классов
    highlighted_text = re.sub(keyword_pattern, r'<span class="keyword">\1</span>', highlighted_text)

    return highlighted_text
