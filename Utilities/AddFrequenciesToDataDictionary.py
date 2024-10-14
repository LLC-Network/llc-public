import pandas as pd
import numpy as np

######### DESCRIPTION #########
# This script takes, as inputs, XLSX files containing:
#  - the scan report produced by WhiteRabbit after scanning a dataset;
#  - the data dictionary containing the description of the variables
#    contained in the dataset (in any order; there can be either more
#    entries in the data dictionary than records in the dataset or viceversa).
#
# It outputs another XLSX file (<dataDictionaryName>_withFreqs.xlsx), namely
# the data dictionary with the addition of a "frequency_percent" column, reporting
# on the percentage of observations in the dataset for which that variable is not
# missing. Frequencies can help users realize on which variables they should focus
# more in the mapping procedure. To do so, simply order the variables by frequencies
# on USAGI interface.

######### SCRIPT PARAMETERS #########
# Define paths to scan report file (XLSX)
scanreportPath = '../Dati_esempio/Policlinico_prova300924/campioni schede/'
scanreportName = 'ScanReport_pre-ospedalizzazione.xlsx'
# Define path to data dictionary file (XLSX)
dictionaryPath = '../Dati_esempio/Policlinico_prova300924/DataDictionary/'
dictionaryName = '01-COVIDNetwork_DataDictionary_2022-07-27 (3).xlsx'
variableFieldName = 'Variable / Field Name'

######### SCRIPT BODY (DO NOT MODIFY) #########
# Load the Excel files into dataframes (needs openpyxl)
dfScanReport = pd.read_excel(scanreportPath+scanreportName)
dfDictionary = pd.read_excel(dictionaryPath+dictionaryName)

# Map the position of each label in dfScanReport['Field'] to dfDictionary['Variable / Field Name']
posLabelsScan = np.array([])
posLabelsDict = np.array([])
matchedLabels = []
nonMatchedLabels = []
for posScan in range(dfScanReport.shape[0]):
    label = dfScanReport['Field'].iloc[posScan].lstrip('\ufeff') #lstrip is needed to remove the BOM character from
                                                                 #the first variable name in case the CSV inputted to
                                                                 #WhiteRabbit was UTF-8-encoded
    posDict = np.where(dfDictionary[variableFieldName]==label)[0]
    if len(posDict) >0:
        posLabelsDict = np.append(posLabelsDict, posDict)
        posLabelsScan = np.append(posLabelsScan, posScan)
        matchedLabels.append(label)
    else:
        nonMatchedLabels.append(label)

posLabelsScan = posLabelsScan.astype(int)
posLabelsDict = posLabelsDict.astype(int)

#### Da sistemare la parte da qui in poi!!!

# Add a column to the data dictionary with the frequencies of empty values in the
# positions of the labels in the scan report
dfDictionary['frequencies_percent'] = float(0) # Initialize the column with zeros
dfDictionary.loc[posLabelsDict, 'frequencies_percent'] = (1 - dfScanReport['Fraction empty'].iloc[posLabelsScan].values) * 100

# Replace the .xlsx extension with _withFreqs.xlsx
newDictionaryName = dictionaryName.replace('.xlsx','_withFreqs.xlsx')

# Save dfDictionary to a new Excel file
dfDictionary.to_excel(dictionaryPath+newDictionaryName, index=False)

# Print a summary of the results
print(f'\n---- INFO:\nOf the {dfScanReport.shape[0]} variables in the scan report, {len(posLabelsDict)} have a corresponding entry in the data dictionary.')
if len(nonMatchedLabels) > 0:
    print(f'The following variables have no match in the data dictionary:\n{nonMatchedLabels}')
print('----\n')