import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(x=df['Year'], y=df['CSIRO Adjusted Sea Level'])


    # Create first line of best fit
    first = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    x_first = range(df['Year'].min(),2051,1)
    y_first = x_first*first.slope + first.intercept

    plt.plot(x_first,y_first)

    # Create second line of best fit
    second_data = df.loc[df['Year']>=2000]
    second = linregress(second_data['Year'], second_data['CSIRO Adjusted Sea Level'])
    x_second = range(second_data['Year'].min(),2051,1)
    y_second = x_second*second.slope + second.intercept

    plt.plot(x_second,y_second)

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()