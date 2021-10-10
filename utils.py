import pandas as pd

def formatExcel(fileName):
    dfs = pd.read_excel(f'{fileName}.xlsx', sheet_name=None)
    writer = pd.ExcelWriter(f'{fileName}.xlsx', engine='xlsxwriter')
    for sheetname, df in dfs.items():  # loop through `dict` of dataframes
        df.to_excel(writer, sheet_name=sheetname, index=False)  # send df to writer
        worksheet = writer.sheets[sheetname]  # pull worksheet object
        for idx, col in enumerate(df):  # loop through all columns
            series = df[col]
            max_len = max((
                series.astype(str).map(len).max(),  # len of largest item
                len(str(series.name))  # len of column name/header
                )) + 3  # adding a little extra space
            worksheet.set_column(idx, idx, max_len)  # set column width
    writer.save()

def exportToExcel(data, fileName):
    writer = pd.ExcelWriter(f'{fileName}.xlsx', engine = 'xlsxwriter')
    data.to_excel(writer, index=False)
    writer.save()
    writer.close()

    formatExcel(fileName)