import pandas as pd
import matplotlib.pyplot as plt


def make_dataframe_from_csv(file):
    dataframe = pd.read_csv(file, delimiter=',', encoding='latin-1')
    dataframe.columns = ['ChecklistId', 'Date', 'SpeciesCode', 'Name', 'Amount']
    return dataframe


def order_dataframe_by_amount(dataframe, column):
    result = dataframe.groupby(column)['Amount'].sum()
    return result


def make_bar_plot_by_day(dataframe):
    dataframe.plot.bar(x='Name', y='Amount', title='Amount of birds on a certain day')
    plt.show()


print(make_dataframe_from_csv("data/observations.csv"))
print(order_dataframe_by_amount(make_dataframe_from_csv("data/observations.csv"), "Name"))
print(make_bar_plot_by_day(make_dataframe_from_csv("data/observations.csv")))
