import pandas as pd

def read_excel(file_path, sheet_name):
    assert fpath.split('.')[-1] == 'xlsx', "read xlsx file only."
    xls = pd.ExcelFile(file_path)

    return pd.read_excel(xls, sheet_name)


if __name__ == "__main__":
    fpath = '/Users/jeanchung/DailyPNL.xlsx'
    sheet = 'logs'
    df = read_excel(fpath, sheet)

   # print(df.iloc[6:9]["Unnamed: 2"])
    pass

