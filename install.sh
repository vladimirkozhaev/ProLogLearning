# Создаем и активируем виртуальное окружение
python3 -m venv mlx_venv
source mlx_venv/bin/activate

# Устанавливаем необходимые библиотеки
pip install -U mlx-lm huggingface_hub