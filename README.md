# Lasso Regression Model for Financial Factor Analysis
This project implements a Lasso regression model to analyze the relationship between the S&amp;P 500 Total Return Index (SP500TR) and various financial factors, such as World Equities, High Yield Bonds, Currency Protection, and Inflation Protection

# Key Features
Data Acquisition: Fetches daily adjusted close prices of selected financial assets using the yfinance library.
Return Calculation: Computes daily returns and calculate by subtracting Inflation Protection.
Lasso Regression:  Lasso regression with cross-validation to determine the best panilty parameter (alpha).
Factor Loadings: Displays the factor loadings, offering insights into which factors most significantly affect the S&P 500 Total Return Index.
Correlation Analysis: Generates a correlation matrix and calculates the Variance Inflation Factor (VIF) to check for multicollinearity among factors.
Model Evaluation: Includes R² score, cross-validation performance, and residual plot.
