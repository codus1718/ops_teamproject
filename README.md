# ops_teamproject

## 2. Algorithm part
### 2-1. initial test
Date: 2023-11-20
1. Basic data preprocessing, visualization, and EDA
  - line chart
  - histogram
2. Check whether the data is stationary or not.
  - Dickey-Fuller Test
3. Estimating and Eliminating Trend
  - Exponential Weighted Moving Average
  - Differencing
4. Basic data prediction(failed due to wrong starting point(train test data split))
- LSTM(Arima: Auto Regressive Integrated Moving Average)

### 2-2. Time Series Analysis Initial
Date: 2023-11-24
1. Prediction using autoTS(Auto Time Series)

### 2-3. Time Series Analysis 
Date: 2023-11-29
1. Prediction using pmdarima(auto_arima)
2. Prediction using neural prophet but failed

### 2-4. Time Series Analysis 
Date: 2023-11-30
1. Prediction using neural prophet
2. Neuralprophet with the sophisticated train but overfitted
3. Basic analysis & visualization using Brent Oil data

### 2-5. Time Series Analysis 
Date: 2023-12-01
1. Visualization
2. Prediction using neural prophet
3. Saved forecast model using pickle
4. Model RMSE:139.6
5. Model Loss:0.017

### 2-5. Time Series Analysis Validation 
Date: 2023-12-01
1. Prediction using neural prophet
2. Train validation data split ratio of 9:1
3. Validation RMSE:192
4. Model RMSE:147
5. Model Loss:0.19

### 2-6. GPVP(Gasoline Price Visualization&Prediction) 
Date: 2023-12-05
1. Trimmed down the whole process of data analysis, visualization, and prediction
2. Used saved pickle model for the fast deployment
