class Datum:
    def __init__(self, data, group):
        self.data = data
        self.group = group


class ColumnDistributions:
    def __init__(self, setosa, virginica, versicolor, setosa_df, virginica_df, versicolor_df):
        self.setosa = setosa
        self.virginicia = virginica
        self.versicolor = versicolor
        self.setosa_df = setosa_df
        self.virginica_df = virginica_df
        self.versicolor_df = versicolor_df
