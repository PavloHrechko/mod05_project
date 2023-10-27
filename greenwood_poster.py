import datetime

from matplotlib import pyplot as plt

from main import get_date_list, read_price_data

stock_symbol = 'MANU' # Stock symbol

# Set time period
start_date = datetime.datetime(2021, 2, 1)
end_date = datetime.datetime(2023, 10, 1)
interval = 'd' # Date interval, by default daily ('d')

# Import price series and list of trading days
try:
    date_list = get_date_list(stock_symbol, start_date, end_date, interval=interval)
    price_series = read_price_data(stock_symbol, start_date, end_date, interval=interval)
except:
    print('Import failed')

num = 1
for date in date_list:
    print(num , " " , date)
    num+=1

fig, ax = plt.subplots(figsize=(15, 8))

# Manually set your annotations of events here
# Check date_list to match index to event date (for instance, 47 equates March 11, 2020)
# Note that events may occur on non-trading days

#Greenwwod

ax.annotate('16 February 2021',
            xy=(date_list[11], price_series[11]),
            xycoords='data',
            bbox=dict(boxstyle="square", fc="none", ec="black"),  # Set edge color to black
            xytext=(45, 170),
            textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='black'),  # Set arrow color to black
            va='center',
            ha='right',
            fontsize=15)

ax.annotate('22 January 2022',
            xy=(date_list[247], price_series[247]),
            xycoords='data',
            bbox=dict(boxstyle="square", fc="none", ec="black"),  # Set edge color to black
            xytext=(0, -40),
            textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='black'),  # Set arrow color to black
            va='center',
            ha='right',
            fontsize=8)

ax.annotate('1 February 2022',
            xy=(date_list[254], price_series[254]),
            xycoords='data',
            bbox=dict(boxstyle="square", fc="none", ec="black"),  # Set edge color to black
            xytext=(87, 150),
            textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='black'),  # Set arrow color to black
            va='center',
            ha='right',
            fontsize=8)

ax.annotate('15 October 2022',
            xy=(date_list[431], price_series[431]),
            xycoords='data',
            bbox=dict(boxstyle="square", fc="none", ec="black"),  # Set edge color to black
            xytext=(20, 100),
            textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='black'),  # Set arrow color to black
            va='center',
            ha='right',
            fontsize=8)

ax.annotate('17 October 2022',
            xy=(date_list[432], price_series[432]),
            xycoords='data',
            bbox=dict(boxstyle="square", fc="none", ec="black"),  # Set edge color to black
            xytext=(77, -50),
            textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='black'),  # Set arrow color to black
            va='center',
            ha='right',
            fontsize=8)


ax.annotate('21 November 2022',
            xy=(date_list[457], price_series[457]),
            xycoords='data',
            bbox=dict(boxstyle="square", fc="none", ec="black"),  # Set edge color to black
            xytext=(270, -65),
            textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='black'),  # Set arrow color to black
            va='center',
            ha='right',
            fontsize=8)

ax.annotate('2 February 2023',
            xy=(date_list[506], price_series[506]),
            xycoords='data',
            bbox=dict(boxstyle="square", fc="none", ec="black"),  # Set edge color to black
            xytext=(100, -120),
            textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='black'),  # Set arrow color to black
            va='center',
            ha='right',
            fontsize=8)

ax.annotate('16 August 2023',
            xy=(date_list[640], price_series[640]),
            xycoords='data',
            bbox=dict(boxstyle="square", fc="none", ec="black"),  # Set edge color to black
            xytext=(50, 85),
            textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='black'),  # Set arrow color to black
            va='center',
            ha='right',
            fontsize=8)

ax.annotate('1 September 2023',
            xy=(date_list[652], price_series[652]),
            xycoords='data',
            bbox=dict(boxstyle="square", fc="none", ec="black"),  # Set edge color to black
            xytext=(50, -100),
            textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='black'),  # Set arrow color to black
            va='center',
            ha='right',
            fontsize=8)

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
plt.plot(date_list, price_series, color='red')

# Display the plot
plt.show()