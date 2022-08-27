# American Express Default Prediction
Team Member: **Jarad Angel**, **Meredith Wang**

Date: Aug - Sep 2022

<a href="#"><img alt="Python" src="https://img.shields.io/badge/Python-013243.svg?logo=python&logoColor=white"></a>
<a href="#"><img alt="Pandas" src="https://img.shields.io/badge/Pandas-150458.svg?logo=pandas&logoColor=white"></a>
<a href="#"><img alt="NumPy" src="https://img.shields.io/badge/Numpy-2a4d69.svg?logo=numpy&logoColor=white"></a>
<a href="#"><img alt="seaborn" src="https://img.shields.io/badge/seaborn-65A9A8.svg?logo=pandas&logoColor=white"></a>
<a href="#"><img alt="sklearn" src="https://img.shields.io/badge/sklearn-4b86b4.svg?logo=scikitlearn&logoColor=white"></a>
<a href="#"><img alt="SciPy" src="https://img.shields.io/badge/SciPy-1560bd.svg?logo=scipy&logoColor=white"></a>

Whether out at a restaurant or buying tickets to a concert, modern life counts on the convenience of a credit card to make daily purchases. It saves us from carrying large amounts of cash and also can advance a full purchase that can be paid over time. How do card issuers know we’ll pay back what we charge? That’s a complex problem with many existing solutions—and even more potential improvements, to be explored in this competition.

**Credit default prediction** is central to managing risk in a consumer lending business. Credit default prediction allows lenders to optimize lending decisions, which leads to a better customer experience and sound business economics. Current models exist to help manage risk. But it's possible to create better models that can outperform those currently in use.

# Business Goals
▪️ Apply our machine learning skills to predict credit default.

▪️ Leverage an industrial scale data set to build a machine learning model that challenges the current model in production.

# Timeline
▪️ May 25, 2022 - Start Date.

▪️ August 17, 2022 - Entry Deadline. You must accept the competition rules before this date in order to compete.

▪️ August 17, 2022 - Team Merger Deadline. This is the last day participants may join or merge teams.

▪️ August 24, 2022 - Final Submission Deadline.

# Data Context
Training, validation, and testing datasets include time-series behavioral data and anonymized customer profile information.

# Initial Questions

# Data Dictionary

# Process
#### :one:   Data Acquisition

<details>
<summary> Gather data from mySQL database</summary>

- Create env.py file to establish connection to mySQL server

- Use **telco_churn** database in the mySQL server

- Write query to join useful tables to gather all data about the customers:  <u>customers, contract_types, payment_types, internet_service_types </u>
     ```sh
     SELECT * FROM customers JOIN contract_types USING (contract_type_id) JOIN payment_types ON customers.payment_type_id = payment_types.payment_type_id JOIN internet_service_types ON customers.internet_service_type_id = internet_service_types.internet_service_type_id
     ```
</details>

<details>
<summary> acqure.py</summary>

- Create acquire.py and user-defined function `get_telco_data()` to gather data from mySQL
     ```sh
     def get_telco_data():
     
     if os.path.isfile('telco.csv'):
        df = pd.read_csv('telco.csv', index_col=0)
    else:
        df = new_telco_data()
        df.to_csv('telco.csv')
        
    return df
    ```
- Import [acquire.py](acquire.py)

- Test acquire function

- Calling the function, and store the table in the form of dataframe
    ```sh
    df = acquire.get_telco_data()
    ```
</details>

#### :two:   Data Preparation

<details>
<summary> Data Cleaning</summary>

- **Missing values: null values are dropped** (total_charges)
     ```sh
    df['total_charges'] = df['total_charges'].str.strip()
    df = df[df.total_charges != '']
    ```
- **Data types: object is converted to the numeric datatype** (total_charges)
     ```sh
     df['total_charges'] = df.total_charges.astype(float)
     ```
- **Dummy variables: created dummy variables for binary and non-binary categorical variables**

- **Duplicate columns: duplicated columns are dropped**

- Create function `prep_telco` to clean and prepare data with steps above

- Import [prepare.py](prepare.py)

- Test prepare function

- Call the function, and store the cleaned data in the form of dataframe
</details>

<details>
<summary> Data Splitting</summary>

- Create function `split_telco_data()` to split data into **train, validate, test**

- Test prepare function

- Check the size of each dataset
     ```sh
     train.shape, validate.shape, test.shape
     ```
- Call the function, and store the 3 data samples separately in the form of dataframe
     ```sh
     train, validate, test = prepare.split_telco_data(df)
     ```
</details>

#### :three:   Exploratory Analysis


#### :four:    Statistical Testing & Modeling
- Conduct T-Test for categorical variable vs. numerical variable

- Conduct Chi^2 Test for categorical variable vs. categorical variable

- Conclude hypothesis and address the initial questions

#### :five:    Modeling Evaluation


# Steps to Reproduce
- [x] 
- [x] Clone the repo
- [x] 
- [x] 
- [x] 


# Key Findings
▪️

▪️ 

▪️ 

▪️

▪️

# Recommendations
▪️

▪️ 

▪️ 
