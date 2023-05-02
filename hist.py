import pandas as pd
import matplotlib.pyplot as plt
import pprint

pp = pprint.PrettyPrinter(indent=4)

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv('Order-LD_FRC-1_Intervals-4_ESA_ID-ESA#1.csv', parse_dates=['start_time'], dtype={'duration': 'float64'})

# Convert duration column to timedelta format
df['duration'] = pd.to_timedelta(df['duration'], unit='s')


# Sort the DataFrame by start time
#df = df.sort_values(by='start_time')

# Fill in missing start times
prev_end_time = pd.Timestamp.min
for i, row in df.iterrows():
    if pd.isna(row['start_time']):
        if not pd.isnull(prev_end_time):
            df.at[i, 'start_time'] = prev_end_time
        else:
            df.at[i, 'start_time'] = df.at[i-1 ,'start_time'] + df.at[i-1 ,'duration']
            
    prev_end_time = row['start_time'] + row['duration']


# Group the intervals by interruptibility
groups = df.groupby('interruptible')

pp.pprint(df)

# Generate a histogram for each group
fig, ax = plt.subplots(figsize=(16, 6))
for interruptible, group in groups:
    # Set the color of the bars based on interruptibility
    color = 'gray' if interruptible else 'blue'
    
    # Compute the width of the bars as the duration in hours
    width = group['duration'].dt.seconds / 3600 / 24
    
    # Plot the intervals as bars
    ax.bar(
        group['start_time'],  # x values are the start times
        group['power'],  # y values are the power
        width=width,  # width is the duration in hours
        align='edge',  # align the bars to the left edge of the start time
        alpha=0.5,  # set the transparency of the bars to 50%
        color=color,  # set the color of the bars based on interruptibility
        label='Interruptible' if interruptible else 'Non-Interruptible'
    )   

# Add labels and legend
ax.set_xlabel('Start Time (UTC)')
ax.set_ylabel('Power (kW)')
ax.set_title('Interval Power Profile')
ax.legend()
plt.xticks(rotation=45)

# Set the y-axis to be logarithmic
ax.set_yscale('log')

# Add x-axis at 0
ax.axhline(y=0, color='black', linestyle='--', linewidth=1)

# Save the plot to file
plt.savefig('intervals.png', dpi=300)
