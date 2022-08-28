# Brazilian scientific productivity from a gender perspective during the Covid-19 pandemic: classification and analysis via machine learning

#### IEEE Latin America Transactions
### Produtividade científica na perspectiva de gênero durante a pandemia do Covid-19: classificação e análise via aprendizado de máquina

<div>
  <img src="https://github.com/TheGabrielSN/Gender-Classification-in-Academic-Papers/blob/main/figures/image3.png" width="250" height="200">
  <img src="https://github.com/TheGabrielSN/Gender-Classification-in-Academic-Papers/blob/main/figures/image4.png" width="250" height="200">
</div>

## Prerequisites

What things you need to have to be able to run:

  * Python 3.6 +
  * Pip 3+
  * VirtualEnvWrapper is recommended but not mandatory

## Requirements 

```bash
$ pip install requirements.txt
```
## Bot 
  * [Web scraping](https://github.com/TheGabrielSN/gender-classification-scientific-productivity/tree/main/web-scraping-from-lattes)

## Dataset 🎲
  * For training 
  
   Brasil.io [click here](https://data.brasil.io/dataset/genero-nomes/nomes.csv.gz)

  * For classification
  
   Lattes Platform scraped data [click here](https://github.com/TheGabrielSN/Gender-Classification-in-Academic-Papers/blob/main/web-scraping-from-lattes/dataLattes.csv)
#### 📄 The format of the  scraped data file .csv: 
  | index |	primeiro_nome | nome_completo  | formacao | titulo | ano |
  |---- |---- |----- | ----- | ------ | ------ |


## Trained models
  * [BiLSTM](https://github.com/TheGabrielSN/gender-classification-scientific-productivity/tree/main/machine-learning-models/deep-learning-models/BiLSTM/Model)
  * [1D CNN](https://github.com/TheGabrielSN/gender-classification-scientific-productivity/tree/main/machine-learning-models/deep-learning-models/1D-CNN/Model)
  * [SVM](https://github.com/TheGabrielSN/gender-classification-scientific-productivity/tree/main/machine-learning-models/SVM/Models)

## Results 

  * [BiLSTM](https://github.com/TheGabrielSN/Gender-Classification-in-Academic-Papers/blob/main/notebooks/BiLSTM_Classify_Lattes.ipynb)
  * [1D CNN](https://github.com/TheGabrielSN/Gender-Classification-in-Academic-Papers/blob/main/notebooks/CNN_Classify_Lattes.ipynb)
  * [SVM](https://github.com/TheGabrielSN/Gender-Classification-in-Academic-Papers/blob/main/notebooks/SVM_Classify_Lattes.ipynb)

Output file format .csv

 |	primeiro_nome | nome_completo  | gender |
  |---- |---- |----- | 

* Some wrong name classification:  
[clik here](https://github.com/TheGabrielSN/gender-classification-scientific-productivity/blob/main/notebooks/results/Classifica%C3%A7%C3%A3o_incorreta_todos.csv)
---


<div>
  <img src="https://github.com/TheGabrielSN/Gender-Classification-in-Academic-Papers/blob/main/figures/graphical-abstract.png" width="650" height="400">
</div>

