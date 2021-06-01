import pandas as pd
import matplotlib.pyplot as plt

def obesity(excelfile="Obes-phys-acti-diet-eng-2014-tab.xls", nogui = False):
    data = pd.ExcelFile(excelfile)
    print(data.sheet_names)

    # Read section 7.1 from the Excel file

    # Define the columns to be read
    columns1 = ['year', 'total', 'males', 'females']

    data_gender = data.parse('7.1', skiprows=4, skipfooter=14, names=columns1)
    #print data_gender

    # Remove the N/A from the data
    data_gender.dropna(inplace = True)
    #print data_gender

    data_gender.set_index('year', inplace=True)

    # Plot all
    data_gender.plot()
    if not nogui:
        plt.show()


    # Read 2nd section, by age
    data_age  = data.parse('7.2', skiprows=4, skipfooter=14)
    print(data_age)

    # Rename unames to year
    data_age.rename(columns={'Unnamed: 0': 'Year'}, inplace=True)

    # Drop empties and reset index
    data_age.dropna(inplace=True)
    data_age.set_index('Year', inplace=True)

    #plot
    data_age.plot()
    if not nogui:
        plt.show()

    # Plotting everything cause total to override everything. So drop it.
    # Drop the total column and plot
    data_age_minus_total = data_age.drop('Total', axis = 1)
    data_age_minus_total.plot()
    if not nogui:
        plt.show()
        plt.close()

    #Plot children vs adults
    data_age['Under 16'].plot(label = "Under 16")
    data_age['25-34'].plot(label = "25-34")
    plt.legend(loc="upper right")
    if not nogui:
        plt.show()

    return data_age['Total'][1]


if __name__ == "__main__":
    obesity()