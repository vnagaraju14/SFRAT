import pandas as pd
import sys

class Failure_DataSet:
	def __init__(self, Data_Set):
		self.data_if={}
		self.data_ft={}
		self.data={}

		if Data_Set.name == 'FT':
			self.data_ft = Data_Set
			for idx in range(len(Data_Set)):
				self.data_if[idx] = Data_Set[idx] - Data_Set[idx - 1] if idx > 0 else Data_Set[idx]
			self.data_if = pd.Series(self.data_if, name='IF')
			
		elif Data_Set.name == 'IF':
			self.data_if = Data_Set
			for idx in range(len(Data_Set)):
				self.data_ft[idx] = Data_Set[idx] + self.data_ft[idx - 1] if idx > 0 else Data_Set[idx]
			self.data_ft = pd.Series(self.data_ft, name='FT')
		self.data['IF'] = self.data_if
		self.data['FT'] = self.data_ft


spreadsheet = pd.read_excel(sys.argv[1])		#supply file name as first arg 
dataset = Failure_DataSet(spreadsheet['IF'])	#example, can change to IF or FT
print(dataset.data['FT'])						#show new created FT branch
