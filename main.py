import pandas as pd
import glob

# Part 1: Combining Data from CSV Files
files_routes = glob.glob('SampleData/*')
# Filtering files containing 'closePosition' in the filename
close_position = [file for file in files_routes if 'closePosition' in file]
# Initialize an empty DataFrame to combine data
combined_data = pd.DataFrame()
# Loop through selected files, read and preprocess data, and concatenate to the main DataFrame
for path in close_position:
    df = pd.read_csv(path)
    # Selecting relevant columns
    df = df[['Key', 'ExitTime', 'Symbol', 'EntryPrice', 'Quantity', 'Pnl']]
    # Converting 'ExitTime' to datetime and Extracting date from it,creating new date column
    df['ExitTime'] = pd.to_datetime(df['ExitTime'])
    df['Date'] = df['ExitTime'].dt.date
    # Concatenate the current DataFrame to the main DataFrame
    combined_data = pd.concat([combined_data, df], ignore_index=True)
# Save the combined data to a CSV file
combined_data.to_csv('combined_closePosition.csv', index=False) 

# Part 2: Analyzing Trading Statistics
def part2(path):
    # Read the combined data
    combined_data = pd.read_csv(path)
    total_trades = len(combined_data)
    unique_days = len(combined_data['Date'].unique())
    average_trades = total_trades / unique_days
    total_pnl = combined_data['Pnl'].sum()
    profit_trades = (combined_data['Pnl'] > 0).sum()
    loss_trades = (combined_data['Pnl'] <= 0).sum()
    # Write the statistics to a text file
    with open('combined_stats.txt', 'w') as file:
        file.write(f'Total trades: {total_trades}\n')
        file.write(f'Unique days: {unique_days}\n')
        file.write(f'Average trades: {average_trades:.2f}\n')
        file.write(f'Total Pnl: {total_pnl:.2f}\n')
        file.write(f'Profit Trades: {profit_trades}\n')
        file.write(f'Loss Trades: {loss_trades}\n')

# Part 3: Analyzing Winning and Losing Streaks
def part3(path):
    combined_data = pd.read_csv(path)
    # Sorting the data by 'ExitTime'
    combined_data.sort_values('ExitTime',inplace=True)
    # Function to calculate individual winning and losing streaks
    def calculate_individual_streaks(group):
        group['WinningStreak'] = (group['Pnl'] > 0).astype(int)
        group['LosingStreak'] = (group['Pnl'] <= 0).astype(int)
        # Calculate cumulative streaks
        group['WinningStreak'] = group['WinningStreak'].groupby(
            (group['WinningStreak'] != group['WinningStreak'].shift()).cumsum()
        ).cumsum()
        group['LosingStreak'] = group['LosingStreak'].groupby(
            (group['LosingStreak'] != group['LosingStreak'].shift()).cumsum()
        ).cumsum()

        return group
     # Apply the streak calculation function grouped by 'Symbol'
    combined_data = combined_data.groupby('Symbol').apply(calculate_individual_streaks)
    # Taking input from user for the top winning/losing streaks
    n = int(input("Enter the value of n for top winning/losing streaks: "))
    # Calculate and print the top winning and losing streaks
    top_winning_streaks = combined_data[combined_data['Pnl'] > 0].groupby('WinningStreak').agg({
        'Key': 'count',
        'ExitTime': ['min', 'max'],
        'Pnl': 'sum'
    }).nlargest(n, ('Pnl', 'sum'))
    top_losing_streaks = combined_data[combined_data['Pnl'] <= 0].groupby('LosingStreak').agg({
        'Key': 'count',
        'ExitTime': ['min', 'max'],
        'Pnl': 'sum'
    }).nsmallest(n, ('Pnl', 'sum'))
     # writing the results to a text file
    with open('combined_winning_losing.txt', 'w') as file:
        file.write("Top winning streaks\n")
        for i, (index, row) in enumerate(top_winning_streaks.iterrows(), 1):
            file.write(f"{i}) No. of Trades: {row[('Key', 'count')]} "
                       f"Start Date - End Date: {row[('ExitTime', 'min')]} - {row[('ExitTime', 'max')]} "
                       f"Pnl of Streak: {row[('Pnl', 'sum')]:.2f}\n")

        file.write("\nTop losing streaks\n")
        for i, (index, row) in enumerate(top_losing_streaks.iterrows(), 1):
            file.write(f"{i}) No. of Trades: {row[('Key', 'count')]} "
                       f"Start Date - End Date: {row[('ExitTime', 'min')]} - {row[('ExitTime', 'max')]} "
                       f"Pnl of Streak: {row[('Pnl', 'sum')]:.2f}\n")


if __name__ == "__main__":
    # Executing part2 and part3
    part2('combined_closePosition.csv')
    part3('combined_closePosition.csv')





