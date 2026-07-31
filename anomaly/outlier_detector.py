class OutlierDetector:

    def detect(self, dataframe, column):

        q1 = dataframe[column].quantile(0.25)

        q3 = dataframe[column].quantile(0.75)

        iqr = q3 - q1

        lower = q1 - 1.5 * iqr

        upper = q3 + 1.5 * iqr

        return dataframe[
            (dataframe[column] < lower) |
            (dataframe[column] > upper)
      ]
