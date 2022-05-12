# Importance and Efficiency Prediction 

# Overview
The notebook  **Importance and Efficiency Prediction.ipynb** loads the test data: **x_test.csv** (encoded features), **y_test.csv** (target efficiencies), and the trained model **xgb**, to compute the importance of chromatin accessibility parameter relative to the context-sequence, and predict the efficiency of the test data (dummy encoded, i.e. the following representation denotes that the first base is C).

 |1_A                          |1_C                   |1_G                           |1_T                                 
|----------------|-----------|------------|----------------|-------
|0            |1           |0    |0


# System Requirements
> Software dependencies
- pandas == 1.0.5
- joblib == 0.16.0
- scipy == 1.5.0
- matplotlib  ==  3.2.2
- seaborn  ==  0.11.1

>  OS Requirements

- The package has been tested on macOS Big Sur Version 11.5.2.

# Instructions:
1. Install python packages:
	change to the directory where  _requirements.txt_  is located and run
```python
	pip install -r requirements.txt
```
2. Run the demo Jupyter Notebook _Importance and Efficiency Prediction.ipynb_.
	- It would take 1 to 2 mins to get the outputs.
