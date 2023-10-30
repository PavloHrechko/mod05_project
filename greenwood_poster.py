import datetime

from matplotlib import pyplot as plt

from main import get_date_list, read_price_data

stock_symbol = 'MANU' # Stock symbol

# Set time period
start_date = datetime.datetime(2022, 1, 1)
end_date = datetime.datetime(2023, 10, 1)
interval = 'd' # Date interval, by default daily ('d')

# Import price series and list of trading days
try:
    date_list = get_date_list(stock_symbol, start_date, end_date, interval=interval)
    price_series = read_price_data(stock_symbol, start_date, end_date, interval=interval)
except:
    print('Import failed')


# num = 1
# for date in date_list:
#     print(num, " - ", date)
#     num+=1

fig, ax = plt.subplots(figsize=(15, 8))

# Manually set your annotations of events here
# Check date_list to match index to event date (for instance, 47 equates March 11, 2020)
# Note that events may occur on non-trading days

#Greenwwod

ax.annotate('February 1: Greenwood is further arrested',
            xy=(date_list[21], price_series[21]),
            xycoords='data',
            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black
            xytext=(197, 150),
            textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black
            va='center',
            ha='right',
            fontsize=12)

ax.annotate('November 21: Greenwood appears\nat Manchester Crown Court',
            xy=(date_list[224], price_series[224]),
            xycoords='data',
            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black
            xytext=(-20, 45),
            textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black
            va='center',
            ha='right',
            fontsize=12)

ax.annotate('September 1: Greenwood joined Getafe on loan',
            xy=(date_list[419], price_series[419]),
            xycoords='data',
            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black
            xytext=(50, -80),
            textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black
            va='center',
            ha='right',
            fontsize=12)


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