# Polza Agency — Тестовое задание: Вайбкодер-аутричер

## Что внутри

| Файл | Описание |
|------|----------|
| `collection_tsk2.csv` | База 50 B2B-компаний (Россия) |
| `tsk2_personalized.csv` | 50 компаний + персонализация |
| `email chain - sheets.csv` | Цепочка из 3 холодных писем |
| `tsk4.csv` | База Polza (15 компаний) |
| `tsk4_personalized.csv` | 15 компаний + персонализация + найденные ошибки |
| `personalize.py` | Генератор промптов для Claude |
| `step2and4.py` | Слияние ответов Claude с CSV |
| `prompts_for_claude.txt` | Пример промптов (Task 2) |
| `claude_output_tsk2.txt` | Ответ Claude (Task 2) |
| `claude_output_tsk4.txt` | Ответ Claude (Task 4) |
| `task5_llm_stack.md` | Мой LLM-стек |

## Инструменты

- Python 3
- Claude (веб-интерфейс)
- Apollo.io (сбор базы)
- Google Sheets

## Запуск

```bash
# Сгенерировать промпты для Claude
py personalize.py

# Объединить ответ Claude с CSV
py step2and4.py
