#!/bin/bash

# Activate virtual environment
source mlx_venv/bin/activate

# Название базовой квантованной модели (4-bit)
MODEL="mlx-community/Qwen1.5-0.5B-Chat-4bit"

# Запуск процесса обучения
python -m mlx_lm.lora \
  --model $MODEL \
  --train \
  --data ./data \
  --iters 200 \
  --batch-size 1 \
  --num-layers 8 \
  --max-seq-length 512 \
  --learning-rate 2e-5 \
  --adapter-path ./prolog_adapters