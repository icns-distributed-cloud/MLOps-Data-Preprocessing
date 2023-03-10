from fastapi import BackgroundTasks

from app.models.exceptions import *
from app.internal.restAPI import *

from scipy.stats import pearsonr

import os
import pandas as pd
import numpy as np
import time

def load_csv_data(filename):
    try:
        df = pd.read_csv(filename, encoding='gbk')
    except FileNotFoundError as e:
        raise NotFoundDataEx(ex=e)
    except Exception as e:
        raise APIException(ex=e)
    return df


def save_csv_data(df, filename):
    try:
        df.to_csv(filename, index=False)
    except Exception as e:
        raise APIException(ex=e)
    return filename, True


def valid_columns(columns, origin_columns):
    try:
        for column in columns:
            if column not in origin_columns:
                raise NotFoundColumnEx()
    except Exception as e:
        raise APIException(ex=e)


def get_pearsonr(data, columns):
    origin_columns = data.columns

    pearson_dict = {}
    for column in columns:
        for origin_column in origin_columns:
            pearsonr(data[column], data[origin_column])


def save_mini_data(file_path, source, target, db_id, nrows=50, is_origin=False):
    try:
        path, file_name = os.path.split(file_path)
        save_path = change_path(path, source, target)
 
        df = pd.read_csv(file_path, nrows=nrows)
        
        if is_origin == True:
            save_csv_data(df, f'{save_path}/{db_id}_{file_name}')
            mini_path = f'{save_path}/{db_id}_{file_name}'
        else:
            save_csv_data(df, f'{save_path}/{file_name}')
            mini_path = f'{save_path}/{file_name}'

        mini_path = mini_path.replace('./', '')
        update_readpre_path(db_id, mini_path)

        print(mini_path)
    except Exception as e:
        raise APIException(ex=e)
    return mini_path


def change_path(path, source, target):
    path = path.replace(source, target)

    return path