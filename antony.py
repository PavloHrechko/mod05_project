import datetime

from matplotlib import pyplot as plt

from main import get_date_list, read_price_data

stock_symbol = 'MANU' # Stock symbol

# Set time period
start_date = datetime.datetime(2022, 8, 1)
end_date = datetime.datetime(2023, 10, 25)
interval = 'd' # Date interval, by default daily ('d')

# Import price series and list of trading days
try:
    date_list = get_date_list(stock_symbol, start_date, end_date, interval=interval)
    price_series = read_price_data(stock_symbol, start_date, end_date, interval=interval)
except:
    print('Import failed')

fig, ax = plt.subplots(figsize=(15, 8))

# Manually set your annotations of events here
# Check date_list to match index to event date (for instance, 47 equates March 11, 2020)
# Note that events may occur on non-trading days

#Antony

ax.annotate('September 1: Antony transferred\nfrom Ajax to Manchester United\nfor €95 000 000',
            xy=(date_list[24], price_series[24]),
            xycoords='data',
            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black
            xytext=(84, 100),
            textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black
            va='center',
            ha='right',
            fontsize=10)


ax.annotate('June 7: Antony faced\nallegations of violence\nagainst women',
            xy=(date_list[215], price_series[215]),
            xycoords='data',
            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black
            xytext=(0, 150),
            textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black
            va='center',
            ha='right',
            fontsize=10)

ax.annotate('September 4: Antony was dropped\nfrom the Brazil national team',
            xy=(date_list[275], price_series[275]),
            xycoords='data',
            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black
            xytext=(-180, -70),
            textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black
            va='center',
            ha='right',
            fontsize=10)

ax.annotate('September 8: Two more women make\nallegations of violence against Anthony',
            xy=(date_list[279], price_series[279]),
            xycoords='data',
            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black
            xytext=(-60, -140),
            textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black
            va='center',
            ha='right',
            fontsize=10)

ax.annotate('September 10: Antony\nwas given a leave of absence\nby Manchester United',
            xy=(date_list[280], price_series[280]),
            xycoords='data',
            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black
            xytext=(90, -90),
            textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black
            va='center',
            ha='right',
            fontsize=10)

ax.annotate('September 29: Anthony returned to\nManchester United and Brazil  selection',
            xy=(date_list[280], price_series[280]),
            xycoords='data',
            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black
            xytext=(100, 140),
            textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black
            va='center',
            ha='right',
            fontsize=10)

# Customize the color theme
ax.set_facecolor('white')  # Set background color to white
ax.spines[['top', 'right', 'bottom', 'left']].set_color('black')  # Set axis spines to black
ax.yaxis.label.set_color('black')  # Set y-axis label color to black
ax.xaxis.label.set_color('black')  # Set x-axis label color to black

# Set options for the interactive plot
fig.canvas.toolbar_visible = False
fig.canvas.resizable = False

# Set labels
plt.title('Stock price {}'.format(stock_symbol), fontdict={'fontsize': 15, 'color': 'black'})  # Set title color to black
plt.xlabel('Date', fontdict={'fontsize': 15, 'color': 'black'})  # Set label color to black
plt.ylabel('Adj. close price', fontdict={'fontsize': 15, 'color': 'black'})  # Set label color to black

# Plot annotated price series with a red line
plt.plot(date_list, price_series, color='black')

# Display the plot
plt.show()