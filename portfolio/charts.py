import json
import sys
from flask import Markup

class ChartTypes():
    """ Add additional chart types here as they are used.
    """
    LINE = 'line'
    BUBBLE = 'bubble'


class Chart:


    def __init__(self, type):
        self.chart_dict = {}

        self.set_chart_type(type)

        # Configuration Options
        self.chart_dict['options'] = {}
        self.chart_dict['data'] = {}
        self.chart_dict['data']['datasets'] = []


    def set_chart_type(self, type):
        """ The chart type. This should probably come from an enum of some kind.
        """
        self.chart_dict['type'] = type


    def set_labels(self, labels):
        """ A list of labels to use for the chart.
        """
        self.chart_dict['data']['labels'] = labels


    def set_options(self, options_dict):
        """ Dictionary of options for the chart.
        """
        self.chart_dict['options'] = options_dict


    def set_single_option(self, key, value):
        self.chart_dict['options'][key] = value


    def create_dataset(self, label, backgroundColor, borderColor, data):
        """ Create a dataset to append to the chart's datasets for display.
        """
        dataset = {}
        dataset['label'] = label
        dataset['backgroundColor'] = backgroundColor
        dataset['borderColor'] = borderColor
        dataset['data'] = data

        return dataset


    def add_dataset(self, dataset):
        self.chart_dict['data']['datasets'].append(dataset)


    def create_and_add_dataset(self, label, bgColor, borderColor, data):
        self.add_dataset(self.create_dataset(label, bgColor, borderColor, data))


    def get_nonescaped_json(self):
        """ Get JSON representation of the chart without Autoescaping
        by wrapping the JSON string in a Markup object.
        """
        return Markup(self.get_chart_json())


    def get_chart_json(self):
        """ Get the JSON representation of the chart.
        """
        return json.dumps(self.chart_dict, separators=(',', ':'))
