import numpy as np
import random
import matplotlib.pyplot as plt

class input_data:

    def __init__(self):
        self.InputFile = open("MakoInterviewPack/input.csv")

    def __del__(self):
        self.InputFile.close()
        
    def ReadNextLine(self):
        self.RawData = self.InputFile.readline().split(",")
            
    def PrintValues(self):
        print(self.RawData)
        

Data = input_data()
for i in range(0,100):
    Data.ReadNextLine()
    Data.PrintValues()


