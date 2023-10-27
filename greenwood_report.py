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


fig, ax = plt.subplots(figsize=(15, 8))

# Manually set your annotations of events here
# Check date_list to match index to event date (for instance, 47 equates March 11, 2020)
# Note that events may occur on non-trading days

#Greenwwod

ax.annotate('February 16:\nMason Greenwood\nsigns a new four-year\ncontract with\nManchester United',
            xy=(date_list[11], price_series[11]),
            xycoords='data',
            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black
            xytext=(45, 170),
            textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black
            va='center',
            ha='right',
            fontsize=8)

ax.annotate('January 22: Greenwood is arrested\non suspicion of rape and assault.\nUnited announces he won\'t \nfeature or train "until further notice"',
            xy=(date_list[247], price_series[247]),
            xycoords='data',
            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black
            xytext=(0, -40),
            textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black
            va='center',
            ha='right',
            fontsize=8)

ax.annotate('February 1: Greenwood is further arrested\non suspicion of sexual assault\n and making threats to kill',
            xy=(date_list[254], price_series[254]),
            xycoords='data',
            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black
            xytext=(87, 150),
            textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black
            va='center',
            ha='right',
            fontsize=8)

ax.annotate('October 15: Greenwood is arrested\nover allegations of breaching bail conditions.\nUnited notes criminal charges brought by the CPS',
            xy=(date_list[431], price_series[431]),
            xycoords='data',
            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black
            xytext=(20, 100),
            textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black
            va='center',
            ha='right',
            fontsize=8)

ax.annotate('October 17: Greenwood\nappears at Manchester&Salford\nMagistrates\' Court,\nremanded in custody',
            xy=(date_list[432], price_series[432]),
            xycoords='data',
            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black
            xytext=(77, -50),
            textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black
            va='center',
            ha='right',
            fontsize=8)


ax.annotate('November 21: Greenwood appears at Manchester Crown Court,\na provisional trial date is set for November 27, 2023',
            xy=(date_list[457], price_series[457]),
            xycoords='data',
            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black
            xytext=(270, -65),
            textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black
            va='center',
            ha='right',
            fontsize=8)

ax.annotate('February 2: The CPS\ndiscontinues criminal proceedings\nagainst Greenwood due t\nwithdrawal of key witnesses\nand new material',
            xy=(date_list[506], price_series[506]),
            xycoords='data',
            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black
            xytext=(100, -120),
            textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black
            va='center',
            ha='right',
            fontsize=8)

ax.annotate('August 16: United\'s CEO Richard Arnold\ntold the club\'s executive leadership\nthat United was planning\nto bring back Greenwood',
            xy=(date_list[640], price_series[640]),
            xycoords='data',
            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black
            xytext=(50, 85),
            textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black
            va='center',
            ha='right',
            fontsize=8)

ax.annotate('September 1: Greenwood joined La Liga (Spain) club\nGetafe on loan for the 2023–24 season',
            xy=(date_list[652], price_series[652]),
            xycoords='data',
            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black
            xytext=(50, -100),
            textcoords='offset points',
            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black
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
plt.plot(date_list, price_series, color='black')

# Display the plot
plt.show()