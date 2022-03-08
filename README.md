# Scientific productivity from a gender perspective during the Covid-19 pandemic: classification and analysis via machine learning
### Produtividade científica na perspectiva de gênero durante a pandemia do Covid-19: classificação e análise via aprendizado de máquina

<div>
  <img src="https://github.com/TheGabrielSN/Gender-Classification-in-Academic-Papers/blob/main/image3.png" width="250" height="200">
  <img src="https://github.com/TheGabrielSN/Gender-Classification-in-Academic-Papers/blob/main/image4.png" width="250" height="200">
</div>

<div>
  <img src="https://github.com/TheGabrielSN/Gender-Classification-in-Academic-Papers/blob/main/image1.png" width="250" height="200">
  <img src="https://github.com/TheGabrielSN/Gender-Classification-in-Academic-Papers/blob/main/image2.png" width="250" height="200">
</div>

## Requirements 

```bash
$ pip install requirements.txt
```

## Dataset 🎲
---
  ### 1. For training 
   Brasil.io [click here](https://data.brasil.io/dataset/genero-nomes/nomes.csv.gz)

  ### 2. For classification
   Lattes Platform scraped data [click here](https://github.com/TheGabrielSN/Gender-Classification-in-Academic-Papers/blob/main/web-scraping-from-lattes/dataLattes.csv)
#### 📄 The format of the  file .csv: 
  | index |	primeiro_nome | nome_completo  | formacao | titulo | ano |
  |---- |---- |----- | ----- | ------ | ------ |

   
---

## Results 

  1. [BiLSTM](https://github.com/TheGabrielSN/Gender-Classification-in-Academic-Papers/blob/main/notebooks/BiLSTM_Classify_Lattes.ipynb)
  2. [1D CNN](https://github.com/TheGabrielSN/Gender-Classification-in-Academic-Papers/blob/main/notebooks/CNN_Classify_Lattes.ipynb)
  3. [SVM](https://github.com/TheGabrielSN/Gender-Classification-in-Academic-Papers/blob/main/notebooks/SVM_Classify_Lattes.ipynb)
