
import pandas as pd
import logging as log
from PyQt5 import QtCore, QtGui

def DataFormat(dataclass):
    # supply pd data object, formats/completes dataset

    if 'FT' not in dataclass:
        dataclass['FT'] = dataclass['IF']
        for i in range(1, len(dataclass)):
            dataclass.at[i, 'FT'] += dataclass['FT'][i-1]

    elif 'IF' not in dataclass:
        dataclass['IF'] = dataclass['FT']
        for i in range(len(dataclass)-1, 0, -1):
            dataclass.at[i, 'IF'] -= dataclass['IF'][i-1]

    if 'FI' not in dataclass:
        dataclass['FI'] = pd.Series(0)
        for i in range(len(dataclass)):
            IF = dataclass['IF'][i]
            dataclass.at[i, 'FI'] = 1/IF if IF > 0 else 'inf'

    else:
        log.info('Input data does not contain IF or FT')

    return dataclass  # either just run method or set var to method result


def LaplaceTest(dataclass):	 # returns series object of size dataclass.size
                            # with laplace values
    laplace = pd.Series(0)  # 0 gives workable series

    for i in range(2, len(dataclass)):
        cur_sum = sum(dataclass['FT'][1:i])
        laplace[i] = ((((1/(i-1))*cur_sum) - (dataclass['FT'][i]/2)) /
                      (dataclass['FT'][i]*(1/(12*(i-1))**(0.5))))

    return pd.DataFrame({'FN': dataclass['FN'], 'LT': laplace})


def AverageTest(dataclass):
    avg = pd.Series(0)

    for i in range(len(dataclass)):
        avg[i] = sum(dataclass['IF'][0:i+1])/(i+1)


    return pd.DataFrame({'FN': dataclass['FN'], 'RA': avg})


class PandasModel(QtCore.QAbstractTableModel):
    def __init__(self, data, parent=None):
        QtCore.QAbstractTableModel.__init__(self, parent)
        self._data = data

    def rowCount(self, parent=None):
        return len(self._data.values)

    def columnCount(self, parent=None):
        return self._data.columns.size
    
    def data(self, index, role=QtCore.Qt.DisplayRole):
        if index.isValid():
            if role == QtCore.Qt.DisplayRole:
                return QtCore.QVariant(str(
                    self._data.values[index.row()][index.column()]
                ))
        return QtCore.QVariant()