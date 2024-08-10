import yfinance as yf
import pandas as pd
from sklearn.linear_model import Lasso
from sklearn.model_selection import GridSearchCV
from sklearn.preprocessing import StandardScaler
import numpy as np

# Define the updated symbols including Currency Protection and other factors
symbols = {
    'SP500TR': '^SP500TR',
    'WorldEquities': 'ACWI',  # MSCI All Country World Index
    'HighYield': 'HYG',       # iShares iBoxx $ High Yield Corporate Bond ETF
    'CurrencyProtection': 'FXE',  # Currency Protection ETF
    'TIPS': 'TIP',            # iShares TIPS Bond ETF
    'NominalTreasuries': 'IEF',  # 7-10 Year Treasury Bonds ETF
    '10YearUSTreasuries': '^TNX'
}

start_date = "2023-01-01"
end_date = "2023-12-31"

# Load the data
data = {symbol: yf.download(ticker, start=start_date, end=end_date, interval='1d')['Adj Close'] for symbol, ticker in symbols.items()}

# Convert to DataFrame
df = pd.DataFrame(data)

# Calculate returns
returns = df.pct_change().dropna()

# Calculate Inflation Protection factor
returns['InflationProtection'] = returns['TIPS'] - returns['NominalTreasuries']

# Define features (x) and target (y)
x = returns.drop(columns=['SP500TR', 'TIPS', 'NominalTreasuries'])  # Dropping additional columns not needed
y = returns['SP500TR']

# Scale the features
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)

# Define the Lasso model with GridSearchCV to find the best alpha
alphas = np.logspace(-12, np.log(0.001), base=np.exp(1), num=100)
lassoTest = Lasso(fit_intercept=True)
tuned_parameters = [{'alpha': alphas}]
clf = GridSearchCV(lassoTest, tuned_parameters, cv=5, refit=True)
clf.fit(x_scaled, y)

# Best model and alpha
lassoBest = clf.best_estimator_
alphaBest = clf.best_params_['alpha']

# Display the results
def display_factor_loadings(intercept, coefs, factor_names):
    print("Intercept: ", intercept)
    for factor, coef in zip(factor_names, coefs):
        print(f"Factor: {factor}, Loading: {coef}")

# Display factor loadings (coefficients)
display_factor_loadings(lassoBest.intercept_, lassoBest.coef_, x.columns.tolist())
