## Essential IT Skills Course

## Description
Forecasting Temperature by Single Exponential Smoothing Model through Python

## Abstract
In our real life, there are many factors that we want to estimate their value in the future. We wish to have some simple yet reliable methods to make a reasonable guess of these unknown values. There are several existing methodologies, such as linear regression and time series analysis. To provide a lightweight method for short-term predictions without requiring complex models, we adopted the exponential smoothing method to forecast the future  weather in the next 10 days. The program is written in Python, using user-provided temperature data and a customizable smoothing coefficient (α) to generate predictions.

## Model
<img width="468" height="260" alt="image" src="https://github.com/user-attachments/assets/3bad5a78-64fb-4a9b-8e9d-3960aa2b76da" />

## Methodology
Algorithm Steps:

a.	Initialize with the first observed value.

b.	Iteratively compute smoothed values using the SES equation.

c.	Generate the forecast for the next period.

## Data 
Input:
1.	Smoothing coefficient (between 0 and 1).
2.	The temperatures (Unit: °C) of the last X days (decided by the user)
❖	Lower bound: -50°C
❖	Upper bound: 60°C

Output
1.	List of smoothed temperature values
2.	Forecast for the temperature in the next day
3.	Data visualization

## Contact
Group members:
Chan Ronny Ryan (3036217087)
Poon Brian (3036058493)
