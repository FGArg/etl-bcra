import pytest
import pandas as pd
from dags.etl_bcra.transform_series import transform_series


@pytest.fixture
def actual_series():
    return pd.DataFrame({
        'fecha': ['2024-10-01', '2024-10-02', '2024-10-03', '2024-10-04', '2024-10-05'],
        'res_int': [25000.0, 26000.0, 27000.0, 28000.0, 29000.0],
        'tc_min':  [1000.0, 1001.0, 1002.0, 1003.0, 1004.0],
        'tasa_just': [900.0, 901.0, 902.0, 903.0, 904.0],
    })


@pytest.fixture
def new_series():
    return pd.DataFrame({
        'fecha': ['2024-10-04', '2024-10-05', '2024-10-06'],
        'res_int': [28000.0, 29000.0, 30000.0],
        'tc_min':  [1010.0, 1011.0, 1012.0],
        'tasa_just': [910.0, 911.0, 912.0],
    })


@pytest.fixture
def expected_series():
    return pd.DataFrame({
        'fecha': ['2024-10-01', '2024-10-02', '2024-10-03', '2024-10-04', '2024-10-05', '2024-10-06'],
        'res_int': [25000.0, 26000.0, 27000.0, 28000.0, 29000.0, 30000.0],
        'tc_min':  [1000.0, 1001.0, 1002.0, 1010.0, 1011.0, 1012.0],
        'tasa_just': [900.0, 901.0, 902.0, 910.0, 911.0, 912.0],
    })


@pytest.fixture
def new_series_with_duplicates():
    return pd.DataFrame({
        'fecha': ['2024-10-04', '2024-10-05', '2024-10-06', '2024-10-06'],
        'res_int': [28000.0, 29000.0, 30000.0, 30000.0],
        'tc_min':  [1010.0, 1011.0, 1012.0, 1012.0],
        'tasa_just': [910.0, 911.0, 912.0, 912.0],
    })


def test_transform_series_with_none(new_series):
    df_updated = transform_series(None, new_series)
    expected = new_series.copy()
    pd.testing.assert_frame_equal(df_updated, expected)


def test_transform_series_with_new_dates(actual_series, new_series, expected_series):
    df_updated = transform_series(actual_series, new_series)
    expected = expected_series.sort_values('fecha').reset_index(drop=True)
    pd.testing.assert_frame_equal(df_updated, expected)


def test_transform_series_with_duplicates(actual_series, new_series_with_duplicates, expected_series):
    df_updated = transform_series(actual_series, new_series_with_duplicates)
    expected = expected_series.sort_values('fecha').reset_index(drop=True)
    pd.testing.assert_frame_equal(df_updated, expected)
