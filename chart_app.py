import justpy as jp
import pandas

data = pandas.read_csv("cars.csv")
weight_average = data.groupby(['Weight']).mean()

char_def = """
{
    chart: {
        type: 'spline',
        inverted: false
    },
    title: {
        text: 'Car weight by model'
    },
    subtitle: {
        text: 'According to the car statistics'
    },
    xAxis: {
        reversed: false,
        title: {
            enabled: true,
            text: 'Weight'
        },
        labels: {
            format: '{value} kg'
        },
        accessibility: {
            rangeDescription: 'Range: 0 to 80 km.'
        },
        maxPadding: 0.05,
        showLastLabel: true
    },
    yAxis: {
        title: {
            text: 'Model number'
        },
        labels: {
            format: '{value}'
        },
        accessibility: {
            rangeDescription: 'Range: -90°C to 20°C.'
        },
        lineWidth: 2
    },
    legend: {
        enabled: false
    },
    tooltip: {
        headerFormat: '<b>{series.name}</b><br/>',
        pointFormat: '{weight_average.index} : {point.y} model'
    },
    plotOptions: {
        spline: {
            marker: {
                enable: false
            }
        }
    },
    series: [{
        name: 'Car weigth and model',
        data: [[0, 15], [10, -50], [20, -56.5], [30, -46.5], [40, -22.1],
            [50, -2.5], [60, -27.7], [70, -55.7], [80, -76.5]]
    }]
}
"""


def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of Course Reviews",
                 classes="text-h3 text-center q-pt-md")
    p1 = jp.QDiv(a=wp, text="These graghs represent course review analysis")
    hc = jp.HighCharts(a=wp, options=char_def)

    hc.options.xAxis.categories = list(weight_average.index)
    hc.options.series[0].data = list(weight_average['Model'])

    return wp


jp.justpy(app)
