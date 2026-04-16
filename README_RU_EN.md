# Prolog Learning - Tool for training LLM models

## Overview / Overview

Prolog Learning is a comprehensive tool for testing and training LLM models on Prolog code. It provides scripts and utilities for fine-tuning language models to understand and generate Prolog code.

Prolog Learning - this is a comprehensive tool for testing and training LLM models on Prolog code. It provides scripts and utilities for fine-tuning language models to understand and generate Prolog code.

---

## 🚀 Установка / Installation

### **Русский / Russian**

#### **Требования / Requirements**
- VSCode 1.74.0+ или Windsurf
- Python 3.8+
- MLX LM библиотека
- Виртуальное окружение mlx_venv

#### **Автоматическая установка / Automatic Installation**
```bash
# Установка в оба редактора
./install_universal.sh

# Установка только в VSCode
./install_vsix.sh

# Установка только в Windsurf
./install_to_windsurf.sh
```

#### **Ручная установка / Manual Installation**
```bash
# Создать папку расширения
mkdir -p ~/.vscode/extensions/prolog-learning-extension

# Копировать файлы
cp vscode_extension/extension.js ~/.vscode/extensions/prolog-learning-extension/
cp vscode_extension/package.json ~/.vscode/extensions/prolog-learning-extension/
cp vscode_extension/README.md ~/.vscode/extensions/prolog-learning-extension/

# Для Windsurf
mkdir -p ~/.windsurf/extensions/prolog-learning-extension
cp vscode_extension/* ~/.windsurf/extensions/prolog-learning-extension/
```

---

### **English**

#### **Requirements**
- Python 3.8+
- MLX LM library
- Virtual environment mlx_venv
- Command line terminal

#### **Automatic Setup**
```bash
# Setup virtual environment
python -m venv mlx_venv
source mlx_venv/bin/activate

# Install MLX LM
pip install mlx-lm

# Prepare training data
python prepare_prolog_data.py
```

#### **Manual Setup**
```bash
# Create virtual environment
python -m venv mlx_venv
source mlx_venv/bin/activate

# Install dependencies
pip install mlx-lm

# Prepare data
python prepare_prolog_data.py

# Start training
./train_prolog.sh
```

---

## 🎮 Использование / Usage

### **Русский / Russian**

#### **Запуск расширения / Launch Extension**
1. Откройте VSCode или Windsurf
2. Нажмите `Ctrl+Shift+P`
3. Введите: `Show Prolog Testing Panel`
4. Нажмите Enter

#### **Доступные функции / Available Functions**
- 🚀 **Run Complete Test** - полный цикл тестирования и обучения
- ⚡ **Quick Test** - быстрая проверка текущей модели
- 📊 **View Report** - просмотр отчета сравнения
- 📝 **Before/After Training** - доступ к файлам результатов

#### **Полный рабочий процесс / Complete Workflow**
```bash
# Запустить полный цикл
./full_comparison_workflow.sh

# Или через расширение
# 1. Run Complete Test
# 2. Дождаться завершения всех этапов
# 3. Посмотреть отчет в training_comparison_report.md
```

#### Available Scripts
- **full_comparison_workflow.sh** - complete testing and training cycle
- **train_prolog.sh** - model training only
- **prepare_prolog_data.py** - data preparation
- **generate_comparison.py** - generate comparison reports

#### Complete Workflow
```bash
# Run complete cycle
./full_comparison_workflow.sh

# Monitor progress
# 1. Training phase (1000 iterations)
# 2. Before/after testing
# 3. Report generation
# 4. View results in training_comparison_report.md
```

---

### English

### Основные файлы / Main Files
```
ProLogLearning/
|
|-- examples/                  # Prolog code examples
|   |-- basic_prolog.pl       # Basic predicates
|   |-- lists_prolog.pl       # List operations
|   |-- hello.pl              # Hello World
|   |-- arith.pl              # Church numerals & arithmetic
|
|-- data/                      # Training data
|   |-- train.jsonl           # Training dataset
|
|-- Scripts & Tools
|   |-- train_prolog.sh        # Training script
|   |-- full_comparison_workflow.sh  # Complete workflow
|   |-- generate_comparison.py # Report generation
|   |-- prepare_prolog_data.py # Data preparation
|
|-- Results
|   |-- before_training_results.txt
|   |-- after_training_results.txt
|   |-- training_comparison_report.md
```

---

## Настройка обучения / Training Configuration

### **Русский / Russian**

#### **Подготовка данных / Data Preparation**
```bash
# Подготовить данные из .pl файлов
python prepare_prolog_data.py

# Проверить результат
cat data/train.jsonl
```

#### **Настройка параметров обучения / Training Parameters**
```bash
# Редактировать train_prolog.sh
vim train_prolog.sh

# Основные параметры:
--model mlx-community/Qwen1.5-0.5B-Chat-4bit
--train_data data/train.jsonl
--iters 1000
--learning_rate 2e-5
--adapter_path prolog_adapters
```

---

### **English**

#### **Data Preparation**
```bash
# Prepare data from .pl files
python prepare_prolog_data.py

# Check result
cat data/train.jsonl
```

#### **Training Parameters**
```bash
# Edit train_prolog.sh
vim train_prolog.sh

# Main parameters:
--model mlx-community/Qwen1.5-0.5B-Chat-4bit
--train_data data/train.jsonl
--iters 1000
--learning_rate 2e-5
--adapter_path prolog_adapters
```

---

## 📊 Анализ результатов / Results Analysis

### **Русский / Russian**

#### **Файлы результатов / Result Files**
- `before_training_results.txt` - ответы модели до обучения
- `after_training_results.txt` - ответы модели после обучения
- `training_comparison_report.md` - детальный отчет сравнения

#### **Метрики качества / Quality Metrics**
- **Relevance** - релевантность ответов
- **Keywords found** - количество найденных ключевых слов
- **Improvement Rate** - процент улучшения

---

### **English**

#### **Result Files**
- `before_training_results.txt` - model responses before training
- `after_training_results.txt` - model responses after training
- `training_comparison_report.md` - detailed comparison report

#### **Quality Metrics**
- **Relevance** - response relevance
- **Keywords found** - number of keywords found
- **Improvement Rate** - improvement percentage

---

## 🐛 Troubleshooting

### **Русский / Russian**

#### **Расширение не работает / Extension Not Working**
```bash
# Проверить установку
./check_installation.sh

# Переустановить
./uninstall_extension.sh
./install_universal.sh

# Запустить с отладкой
./launch_windsurf_debug.sh
```

#### **Проблемы с обучением / Training Issues**
```bash
# Проверить виртуальное окружение
source mlx_venv/bin/activate

# Проверить данные
python prepare_prolog_data.py

# Запустить обучение вручную
./train_prolog.sh
```

---

### **English**

#### **Extension Not Working**
```bash
# Check installation
./check_installation.sh

# Reinstall
./uninstall_extension.sh
./install_universal.sh

# Launch with debug
./launch_windsurf_debug.sh
```

#### **Training Issues**
```bash
# Check virtual environment
source mlx_venv/bin/activate

# Check data
python prepare_prolog_data.py

# Run training manually
./train_prolog.sh
```

---

## 🔄 Обновление / Updates

### **Русский / Russian**
```bash
# Обновить расширение
cp vscode_extension/* ~/.vscode/extensions/prolog-learning-extension/

# Обновить Windsurf
cp vscode_extension/* ~/.windsurf/extensions/prolog-learning-extension/

# Перезапустить редактор
open -a "Visual Studio Code"  # или Windsurf
```

### **English**
```bash
# Update extension
cp vscode_extension/* ~/.vscode/extensions/prolog-learning-extension/

# Update Windsurf
cp vscode_extension/* ~/.windsurf/extensions/prolog-learning-extension/

# Restart editor
open -a "Visual Studio Code"  # or Windsurf
```

---

## 📚 Дополнительные ресурсы / Additional Resources

### **Документация / Documentation**
- [MLX LM Documentation](https://github.com/ml-explore/mlx-lm)
- [Prolog Tutorial](https://www.swi-prolog.org/pldoc/man?section=quickstart)
- [VSCode Extension API](https://code.visualstudio.com/api)

### **Примеры кода / Code Examples**
- `examples/basic_prolog.pl` - базовые предикаты
- `examples/lists_prolog.pl` - работа со списками
- `examples/arith.pl` - Church numerals и арифметика
- `examples/hello.pl` - Hello World

---

## 📝 Лицензия / License

MIT License - свободное использование и модификация

---

## 🤝 Поддержка / Support

### **Русский / Russian**
- Создать Issue в репозитории проекта
- Проверить раздел Troubleshooting
- Использовать отладочные скрипты

### **English**
- Create Issue in project repository
- Check Troubleshooting section
- Use debug scripts

---

**🎉 Готов к использованию! / Ready to use!**
