class NullRule:

    def validate(self, dataframe):

        return dataframe.isnull().sum()
