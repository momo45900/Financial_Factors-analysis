# Lasso Regression Model for Financial Factor Analysis

This project implements a Lasso regression model to analyze the relationship between the S&P 500 Total Return Index (SP500TR) and various financial factors, such as World Equities, High Yield Bonds, Currency Protection, and Inflation Protection.

## Key Features

- **Data Acquisition**: Fetches daily adjusted close prices of selected financial assets using the `yfinance` library.
- **Return Calculation**: Computes daily returns and calculates Inflation Protection.
- **Lasso Regression**: Performs Lasso regression with cross-validation to determine the best penalty parameter (alpha).
- **Factor Loadings**: Displays the factor loadings, offering insights into which factors most significantly affect the S&P 500 Total Return Index.
- **Correlation Analysis**: Generates a correlation matrix and calculates the Variance Inflation Factor (VIF) to check for multicollinearity among factors.
- **Model Evaluation**: Includes R² score, cross-validation performance, and a residual plot.

## Data Loading

Historical price data is downloaded from Yahoo Finance for the selected symbols:

- **WorldEquities**: `ACWI` (MSCI All Country World Index)
- **HighYield**: `HYG` (High Yield Corporate Bond ETF)
- **CurrencyProtection**: `FXE` (Currency Protection ETF)
- **TIPS**: `TIP` (iShares TIPS Bond ETF)
- **NominalTreasuries**: `IEF` (7-10 Year Treasury Bonds ETF)

The data is converted into a Pandas DataFrame for further analysis.

## Return Calculation

Daily returns for each symbol are calculated. An Inflation Protection factor is derived by subtracting Nominal Treasuries returns from TIPS returns.

## Model Training

- Features and target variables are defined, with scaling applied to the features.
- A Lasso regression model is trained using `GridSearchCV` to find the optimal alpha value.

### Output

The script outputs the intercept and factor loadings as follows:

Intercept: [0.0009876933029975444]
Factor: WorldEquities, Loading: [0.0009876933029975444]
Factor: HighYield, Loading: [0.0]
Factor: CurrencyProtection, Loading: [-0.0011081486154325439]
Factor: 10YearUSTreasuries, Loading: [0.0]
Factor: InflationProtection, Loading: [0.0]


**Economic Interpretation**: From an economic standpoint, the results make sense as the S&P 500 (a broad U.S. equity index) might not be heavily influenced by High Yield bonds, 10-Year Treasuries, or certain inflation protection measures directly. The positive correlation with World Equities could reflect global equity market movements.

## Correlation Analysis

- **Correlation Matrix**: A correlation matrix is created to visualize the relationships between the factors.

    ![Correlation Matrix](path_to_correlation_matrix_image.png)

- **Variance Inflation Factor (VIF)**: The VIF is calculated to check for multicollinearity:

    ```
    Factor               VIF
    -------------------------
    WorldEquities       3.140960
    HighYield           3.524403
    CurrencyProtection  1.507104
    10YearUSTreasuries  2.929273
    InflationProtection 2.087047
    ```

## Model Evaluation

The model's performance is evaluated using the R² score, and a residual plot is generated:

- **Residual Plot**:

    ![Residual Plot](path_to_residual_plot.png)

- **R² Score**: [R² Score Value]

- **Cross-Validation R² Scores**: [0.93184481 0.93392989 0.94369063 0.96668209 0.94933958]
- **Average CV R² Score**: 0.9450974019275595

**Evaluation Notes**:
- A high R² score (close to 1) suggests a good fit. If it’s low, the model may not be capturing much of the variance in the S&P 500 returns.
- The residual plot should show no obvious patterns; if it does, the model may be missing some structure in the data.
- Cross-validation scores should be consistent and reasonably high, indicating that the model generalizes well.
