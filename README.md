# [Brazilian scientific productivity from a gender perspective during the Covid-19 pandemic: classification and analysis via machine learning](https://ieeexplore.ieee.org/document/10015223/)

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

### How to cite: 

R. C. B. Rego, G. d. S. Nascimento, D. E. d. L. Rodrigues, S. M. Nascimento and V. M. L. Silva, ["Brazilian scientific productivity from a gender perspective during the Covid-19 pandemic: classification and analysis via machine learning,"](https://ieeexplore.ieee.org/document/10015223) in IEEE Latin America Transactions, vol. 21, no. 2, pp. 302-309, Feb. 2023, doi: 10.1109/TLA.2023.10015223.

### Bibitex: 

```bash
@ARTICLE{10015223,

  author={Rego, Rosana Cibely B. and Nascimento, Gabriel da Silva and Rodrigues, Davi Emmanuel de Lima and Nascimento, Samara Martins and Silva, Verônica Maria L.},

  journal={IEEE Latin America Transactions}, 

  title={Brazilian scientific productivity from a gender perspective during the Covid-19 pandemic: classification and analysis via machine learning}, 

  year={2023},

  volume={21},

  number={2},

  pages={302-309},

  doi={10.1109/TLA.2023.10015223}}
```

