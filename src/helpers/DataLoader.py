import pandas as pd


class DataLoader:
    def __init__(self, path):  # Constructor y arguemnto
        self.path = path  # path del objeto y path del metodo

    def load_data(self):
        data = pd.read_csv(self.path)
        return data
