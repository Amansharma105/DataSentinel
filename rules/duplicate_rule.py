class DuplicateRule:

    def validate(self, dataframe):

        return dataframe.duplicated().sum()
