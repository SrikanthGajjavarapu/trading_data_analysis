***Trading Data Analysis***

This Python script combines and analyzes trading data from multiple CSV files. The data is assumed to contain information about closed positions in financial trading, including key identifiers, exit times, symbols, entry prices, quantities, and profits/losses (PnL).

***Part 1: Combining Data from CSV Files***

The script starts by importing the necessary libraries, including pandas for data manipulation and glob for file path pattern matching. It then performs the following steps:

File Selection: The script uses glob to select CSV files from the 'SampleData/' directory, specifically those containing 'closePosition' in the filename.

Data Concatenation: It initializes an empty DataFrame (combined_data) and iterates through the selected files, reading and preprocessing data. Relevant columns ('Key', 'ExitTime', 'Symbol', 'EntryPrice', 'Quantity', 'Pnl') are selected, and a new 'Date' column is created from the 'ExitTime' column. The individual DataFrames are concatenated into the main DataFrame.

Save Combined Data: The combined DataFrame is saved to a new CSV file named 'combined_closePosition.csv'.

***Part 2: Analyzing Trading Statistics***

The script defines a function part2(path) to analyze trading statistics. It reads the combined data, calculates various statistics such as total trades, unique days, average trades per day, total PnL, profit trades, and loss trades. The results are then written to a text file named 'combined_stats.txt'.

***Part 3: Analyzing Winning and Losing Streaks***

The script defines a function part3(path) to analyze winning and losing streaks. It reads the combined data, sorts it by 'ExitTime', and calculates individual winning and losing streaks for each trading symbol. It then prompts the user to input a value (n) for the top winning/losing streaks.

The top winning and losing streaks are calculated and written to a text file named 'combined_winning_losing.txt'. For each streak, the script includes the number of trades, start and end dates, and the total PnL of the streak.

***Running the Script***

The main block of the script checks if it's the main module and, if so, executes part2 and part3 on the 'combined_closePosition.csv' file.

***Requirements***

Python
pandas library
Usage
Place your CSV files in the 'SampleData/' directory.
Ensure that the required libraries (pandas and glob) are installed.
Run the script.

Note: The script assumes well-formatted CSV files with the specified column names. Adjustments may be needed based on the actual structure of your trading data.# trading_data_analysis
