import pandas as pd

class Excel():
    def __init__(self,file):
        self.file = file 

    def read_file(self):
        self.df = pd.read_csv(self.file)  
        return self.df

    def count(self):
        cols = self.df.shape(1)
        rows = self.df.shape(0)
        return cols, rows
