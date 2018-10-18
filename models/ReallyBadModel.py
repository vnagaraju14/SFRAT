#This is a template model
# it doesnt pay any attention to the data provided
# it just returns a linear regression from
# the first point to the last point

import pandas as pd
import numpy as np

class ReallyBadModel():
    def __init__(self):
        self.name = "Really Bad Model"

    def crunch(self, data):
        m =  data["FN"].iloc[-1] - data["FN"][0]
        m /= data["FT"].iloc[-1] - data["FT"][0]
        out = pd.DataFrame({
        "X": np.linspace(0, data["FT"].iloc[-1], 100),
        "Y": -1 * m * np.linspace(0, data["FT"].iloc[-1], 100)
        + data["FN"].iloc[-1],
        })
        return out
