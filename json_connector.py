import pandas as pd


class JSONConnector:

    def load(self, file_path):

        return pd.read_json(file_path)
