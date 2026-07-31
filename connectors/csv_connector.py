import pandas as pd


class CSVConnector:

    def load(self, file_path):

        return pd.read_csv(file_path)
