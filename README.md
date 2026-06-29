# Financial Sentiment Analysis

A course project comparing traditional machine learning methods and Transformer-based models for financial sentiment classification.

The task is to classify financial text into three sentiment categories:

* Positive
* Neutral
* Negative

## Project Overview

This project builds a text classification pipeline for financial sentiment analysis. It includes data preprocessing, exploratory analysis, traditional machine learning baselines, Transformer-based models, model comparison, error analysis, robustness testing, and out-of-distribution evaluation.

The repository is a cleaned version of an academic project. Raw data files, trained model weights, and generated outputs are not included.

## Methods

### Traditional Machine Learning

* TF-IDF feature extraction
* Logistic Regression
* Linear SVM
* Multinomial Naive Bayes
* SMOTE for class imbalance handling

### Transformer-based Models

* FinBERT
* BERT-base
* DistilBERT / RoBERTa variants
* Zero-shot classification with BART-large-MNLI
* Optional LoRA / quantization experiments

### Evaluation

The project compares models using:

* Accuracy
* Macro-F1
* Class-level performance
* Training time
* Inference latency
* Robustness under noisy text input
* Out-of-distribution behaviour on financial news

## Project Structure

```text
financial-sentiment-analysis/
├── README.md
├── requirements.txt
├── config.py
├── main.py
├── preprocessing.py
├── eda_analysis.py
├── ml_pipeline.py
├── transformer_pipeline.py
├── additional_models.py
├── lora_pipeline.py
├── zero_shot.py
├── ensemble.py
├── error_analysis.py
├── ood_evaluation.py
├── robustness.py
└── evaluation.py
```

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the full pipeline:

```bash
python main.py
```

To use a local dataset, configure the data path through an environment variable:

```bash
export STAT8307_DATA=/path/to/data.csv
```

The expected input file should contain financial text and sentiment labels.

## Notes on Data and API Keys

Raw data, trained model files, and generated result files are not included in this repository.

The OOD evaluation module can optionally use NewsAPI. The API key should be configured locally through an environment variable:

```bash
export NEWSAPI_KEY=your_api_key_here
```

No API keys or private data are included in this repository.

## Dependencies

Main libraries used in this project include:

* pandas, numpy
* scikit-learn, imbalanced-learn
* torch, transformers
* peft, bitsandbytes
* nltk
* matplotlib, seaborn, wordcloud
* umap-learn
* statsmodels
* newsapi-python
