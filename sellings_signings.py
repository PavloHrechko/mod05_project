import datetimefrom matplotlib import pyplot as pltfrom main import get_date_list, read_price_datastock_symbol = 'MANU' # Stock symbol# Set time periodstart_date = datetime.datetime(2018, 7, 25)end_date = datetime.datetime(2022, 10, 1)interval = 'd' # Date interval, by default daily ('d')# Import price series and list of trading daystry:    date_list = get_date_list(stock_symbol, start_date, end_date, interval=interval)    price_series = read_price_data(stock_symbol, start_date, end_date, interval=interval)except:    print('Import failed')fig, ax = plt.subplots(figsize=(15, 8))# Manually set your annotations of events here# Check date_list to match index to event date (for instance, 47 equates March 11, 2020)# Note that events may occur on non-trading days#Sellings and Signingsax.annotate('10 August 2018: Fred signed from\nShakhtar Donetsk for £52 million',            xy=(date_list[13], price_series[13]),            xycoords='data',            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black            xytext=(180, 50),            textcoords='offset points',            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black            va='center',            ha='right',            fontsize=8)ax.annotate('1 January 2019: Paul Pogba\nsigned a new contract\nwith Manchester United',            xy=(date_list[130], price_series[130]),            xycoords='data',            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black            xytext=(57, -80),            textcoords='offset points',            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black            va='center',            ha='right',            fontsize=8)ax.annotate('8 August 2019: Harry Maguire signed\nfrom Leicester City for £80 million',            xy=(date_list[262], price_series[262]),            xycoords='data',            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black            xytext=(76, 100),            textcoords='offset points',            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black            va='center',            ha='right',            fontsize=8)ax.annotate('28 August 2020: Donny van de Beek\nsigned from Ajax for £39.1 million',            xy=(date_list[529], price_series[529]),            xycoords='data',            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black            xytext=(65, 110),            textcoords='offset points',            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black            va='center',            ha='right',            fontsize=8)ax.annotate('10 March 2021: Marcus Rashford\nsigned a new contract\nwith Manchester United',            xy=(date_list[661], price_series[661]),            xycoords='data',            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black            xytext=(50, 100),            textcoords='offset points',            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black            va='center',            ha='right',            fontsize=8)ax.annotate('31 July 2021: Raphael Varane\nsigned from Real Madrid\nfor £40 million',            xy=(date_list[760], price_series[760]),            xycoords='data',            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black            xytext=(60, -70),            textcoords='offset points',            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black            va='center',            ha='right',            fontsize=8)ax.annotate('14 August 2021: Jadon Sancho\nsigned from Borussia Dortmund\nfor £73 million',            xy=(date_list[770], price_series[770]),            xycoords='data',            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black            xytext=(55, 130),            textcoords='offset points',            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black            va='center',            ha='right',            fontsize=8)ax.annotate('31 January 2022:\nBruno Fernandes\nsigned a new contract\nwith Manchester United',            xy=(date_list[887], price_series[887]),            xycoords='data',            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black            xytext=(50, 100),            textcoords='offset points',            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black            va='center',            ha='right',            fontsize=8)ax.annotate('12 April 2022: Erik ten Hag\nappointed as new\nManchester United manager',            xy=(date_list[943], price_series[943]),            xycoords='data',            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black            xytext=(0, -60),            textcoords='offset points',            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black            va='center',            ha='right',            fontsize=8)ax.annotate('21 June 2022:\nChristian Eriksen\nsigned as a free agent',            xy=(date_list[984], price_series[984]),            xycoords='data',            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black            xytext=(40, 120),            textcoords='offset points',            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black            va='center',            ha='right',            fontsize=8)ax.annotate('22 August 2022:\nCasemiro signed\nfrom Real Madrid\nfor €70 million',            xy=(date_list[1027], price_series[1027]),            xycoords='data',            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black            xytext=(133, -10),            textcoords='offset points',            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black            va='center',            ha='right',            fontsize=8)# Customize the color themeax.set_facecolor('white')  # Set background color to whiteax.spines[['top', 'right', 'bottom', 'left']].set_color('black')  # Set axis spines to blackax.yaxis.label.set_color('black')  # Set y-axis label color to blackax.xaxis.label.set_color('black')  # Set x-axis label color to black# Set options for the interactive plotfig.canvas.toolbar_visible = Falsefig.canvas.resizable = False# Set labelsplt.title('Stock price {}'.format(stock_symbol), fontdict={'fontsize': 15, 'color': 'black'})  # Set title color to blackplt.xlabel('Date', fontdict={'fontsize': 15, 'color': 'black'})  # Set label color to blackplt.ylabel('Adj. close price', fontdict={'fontsize': 15, 'color': 'black'})  # Set label color to black# Plot annotated price series with a red lineplt.plot(date_list, price_series, color='black')# Display the plotplt.show()