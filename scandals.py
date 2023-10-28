import datetimefrom matplotlib import pyplot as pltfrom main import get_date_list, read_price_datastock_symbol = 'MANU' # Stock symbol# Set time periodstart_date = datetime.datetime(2016, 5, 1)end_date = datetime.datetime(2023, 10, 27)interval = 'd' # Date interval, by default daily ('d')# Import price series and list of trading daystry:    date_list = get_date_list(stock_symbol, start_date, end_date, interval=interval)    price_series = read_price_data(stock_symbol, start_date, end_date, interval=interval)except:    print('Import failed')num = 1for date in date_list:    print(num, " - ", date)    num+=1fig, ax = plt.subplots(figsize=(15, 8))# Manually set your annotations of events here# Check date_list to match index to event date (for instance, 47 equates March 11, 2020)# Note that events may occur on non-trading days#Scandalsax.annotate('12 May  2016: Bastian Schweinsteiger\naccused of being drunk\nand disorderly on a flight',            xy=(date_list[10], price_series[10]),            xycoords='data',            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black            xytext=(120, 110),            textcoords='offset points',            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black            va='center',            ha='right',            fontsize=8)ax.annotate('10 July 2017: Paul Pogba\naccused of racism by Patrice Evra',            xy=(date_list[300], price_series[300]),            xycoords='data',            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black            xytext=(90, -50),            textcoords='offset points',            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black            va='center',            ha='right',            fontsize=8)ax.annotate('25 August 2018: Romelu Lukaku\naccused of tax evasion',            xy=(date_list[585], price_series[585]),            xycoords='data',            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black            xytext=(70, 50),            textcoords='offset points',            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black            va='center',            ha='right',            fontsize=8)ax.annotate('30 March 2019: Marcus Rashford\naccused of cheating on his\ngirlfriend with a reality TV star',            xy=(date_list[733], price_series[733]),            xycoords='data',            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black            xytext=(95, 80),            textcoords='offset points',            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black            va='center',            ha='right',            fontsize=8)ax.annotate('17 September 2020: Paul Pogba\naccused of using witchcraft\nto curse Kylian Mbappe',            xy=(date_list[1104], price_series[1104]),            xycoords='data',            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black            xytext=(50, 130),            textcoords='offset points',            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black            va='center',            ha='right',            fontsize=8)ax.annotate('20 April 2021: Harry Maguire\narrested and charged with\nassaulting police officers\nin Greece',            xy=(date_list[1251], price_series[1251]),            xycoords='data',            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black            xytext=(60, -110),            textcoords='offset points',            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black            va='center',            ha='right',            fontsize=8)ax.annotate('20 October 2023:\nAlejandro Garnacho\naccused of sexual assaul',            xy=(date_list[1882], price_series[1882]),            xycoords='data',            bbox=dict(boxstyle="square", fc="none", ec="red"),  # Set edge color to black            xytext=(30, -50),            textcoords='offset points',            arrowprops=dict(arrowstyle='->', color='red'),  # Set arrow color to black            va='center',            ha='right',            fontsize=8)# Customize the color themeax.set_facecolor('white')  # Set background color to whiteax.spines[['top', 'right', 'bottom', 'left']].set_color('black')  # Set axis spines to blackax.yaxis.label.set_color('black')  # Set y-axis label color to blackax.xaxis.label.set_color('black')  # Set x-axis label color to black# Set options for the interactive plotfig.canvas.toolbar_visible = Falsefig.canvas.resizable = False# Set labelsplt.title('Stock price {}'.format(stock_symbol), fontdict={'fontsize': 15, 'color': 'black'})  # Set title color to blackplt.xlabel('Date', fontdict={'fontsize': 15, 'color': 'black'})  # Set label color to blackplt.ylabel('Adj. close price', fontdict={'fontsize': 15, 'color': 'black'})  # Set label color to black# Plot annotated price series with a red lineplt.plot(date_list, price_series, color='black')# Display the plotplt.show()