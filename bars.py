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
