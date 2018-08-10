from matplotlib import pyplot as plt

def make_chart_simple_line_chart(plt):
    years = [1950, 1960, 1970, 1980, 1990, 2000, 2010]
    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3]

    plt.plot(years, gdp, color='green', marker='o', linestyle='solid')
    plt.title('Nominal GDP')
    plt.ylabel('Billions of $')
    plt.show()

def make_chart_simple_bar_chart(plt):
    pass

def make_chart_histogram(plt):
    pass

def make_chart_misleading_y_axis(plt, mislead=True):
    pass

def make_chart_several_line_charts(plt):
    pass

def make_scatterplot_axes(plt, equal_axes=False):
    pass

def make_chart_pie_chart(plt):
    pass

if __name__ == '__main__':
    make_chart_simple_line_chart(plt)
    make_chart_simple_bar_chart(plt)
    make_chart_histogram(plt)
    make_chart_misleading_y_axis(plt, mislead=True)
    make_chart_misleading_y_axis(plt, mislead=False)
    make_chart_several_line_charts(plt)
    make_chart_scatterplot_axes(plt, equal_axes=False)
    make_chart_scatterplot_axes(plt, equal_axes=True)
    make_chart_pie_chart(plt)
