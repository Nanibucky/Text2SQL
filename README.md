# Text2SQL Using Mistral-7B

Convert natural language to SQL queries using fine-tuned and optimized Mistral-7B models.

## Models Available
- [Full Model (Mistral-7B-Text2SQL)](https://huggingface.co/tharun66/Mistral-7B-Text2SQL)
- [Optimized GGUF Model](https://huggingface.co/tharun66/mistral-sql-gguf)

## Model Details
- Base Architecture: Mistral 7B
- Task: Natural Language to SQL Translation
- Optimization Method: GGUF Quantization (Q8_0)
- Size Reduction: 27.01GB → 7.2GB
- Performance: 80% accuracy on complex queries

## Features
- Fine-tuned with PEFT and LoRA adaptation
- Optimized for both cloud and edge deployment
- Evaluation loss: 0.4643
- CPU inference support via llama.cpp

## Repository Structure
