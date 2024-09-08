# Financial-Data-Analysis-for-IDA

Given a dataset with 1.28 million rows and 30 columns, 70% of the data was used for analysis, focusing solely on financial aspects and omitting temporal variables. Streamlined the dataset by discarding irrelevant columns and removing rows with null values in two specific columns—resulting in the elimination of only two rows. This preprocessing was accomplished using a Python script, which ultimately generated a refined CSV file containing only essential information.

Subsequently, an empty database was established, and six tables were created from the CSV file using the SQLite module in Python. These tables were structured to eliminate violations of Boyce-Codd Normal Form (BCNF), ensuring database normalization.

For further data manipulation, Valentino Studio was utilized to export these tables into Excel files. These Excel files were then imported into PostgreSQL for comprehensive analysis, enhancing the versatility and depth of the financial evaluation.