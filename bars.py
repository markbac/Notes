I am plotting bars as below. My width of the bars appear to be wrong (far too wide). The start tiem is UTS, e.g 2023-02-01 11@42:18.451204+00:00

What is wrong

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
this is my dataset
                        start_time        duration    power  interruptible
0 2023-02-01 11:43:18.451204+00:00 0 days 01:00:00   3000.0          False
1 2023-02-01 12:43:18.451204+00:00 0 days 03:00:00      0.0          False
2 2023-02-01 15:43:18.451204+00:00 0 days 01:00:00  10000.0          False
