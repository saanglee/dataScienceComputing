
# Overview 
- Goal: In this competition, we challenge you to predict the rate of stock fluctuation using all the machine learning techniques we have covered so far in the course.
- test.csv is Test Stock Market Dataset: dataset with all stock information but without label
- train.csv is Train Stock Market Dataset: dataset with all stock information and label
- sample_submission is sample submission dataset. you should follow this format. 
    • id - id of test.csv
    • label- predicted label
    • Label column must be in integer type.

 
# Data set
- id: De-identified key column for the original name of the stock.
- 현재가: Closing price of the each stock.
- 전일비: Absolute price difference between the previous day's closing price and the given day's closing price.
- 액면가: The price per share determined when a company goes public (IPO). Typically, it refers to a fixed price written on the stock certificate at the initial issuance of the stock.
- 시가총액: The indicator used to evaluate the value of a listed company or corporation by multiplying the stock price by the number of shares issued. Note the values are expressed in units of 100 million Korean won.
- 상장주식수: The total number of shares that a company has registered and made available for trading when it goes public on the KOSPI or KOSDAQ market.
- 외국인비율: The proportion of stock trading conducted by foreign investors out of the total trading volume.
- 거래량: The quantity of the traded stocks for a given day.
- PER: Price-to-Earnings Ratio. It is a financial metric used to evaluate a company's valuation relative to its earnings. The PER is calculated by dividing the market price per share of a company's stock by its earnings per share (EPS).
- ROE: Return on Equity. In the stock market, ROE is a financial ratio that measures the profitability and efficiency of a company in generating profits from its shareholders' equity. It is calculated by dividing the company's net income by its average shareholders' equity.

- label:
    - 0 : Decreased
    - 1 : Remained the same
    - 2 : Increased


