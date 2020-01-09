import os.path

import numpy as np
import pandas as pd
import pytest

from cavitysim.io import read_octascope_output

# first column is time
# next columns are channels
# read header into dictionary with keys model name, comment, settings (settings is a dataframe)


def test_read_octascope_output(test_data_dir):
    source_csv_fullpath = os.path.join(test_data_dir, "test_scope_raw.csv")

    exp_settings = pd.DataFrame(
        [
            [1, 1],
            [1250, 1250],
            ["V", "V"],
            [1250000.0, 1250000.0],
            [8.000000e-07, 8.000000e-07],
            [-9.992000e-04, -9.992000e-04],
            ["s", "s"],
            [1250, 1250],
            [1, 1],
            ["2019/11/26", "2019/11/26"],
            ["12:33:56.100895200", "12:33:56.100895200"],
        ],
        index=[
            "BlockNumber",
            "BlockSize",
            "VUnit",
            "SampleRate",
            "HResolution",
            "HOffset",
            "HUnit",
            "DisplayBlockSize",
            "DisplayPointNo",
            "Date",
            "Time",
        ],
        columns=["CH1", "CH3"],
    )

    res = read_octascope_output(source_csv_fullpath)

    assert res["header"]["Header Size"] == 15
    assert res["header"]["Model Name"] == "DLM4000"
    assert res["header"]["Comment"] == ""

    pd.testing.assert_frame_equal(res["settings"], exp_settings)

    # test first value
    np.testing.assert_allclose(res["data"].loc["CH1", -999.20000e-06], 0.241e-03)
    # test second value
    np.testing.assert_allclose(res["data"].loc["CH3", -999.20000e-06], 121.88e-03)
    # test middle value
    np.testing.assert_allclose(res["data"].loc["CH1", -20.000000e-06], 0.084e-03)
    # test last value
    np.testing.assert_allclose(res["data"].loc["CH3", 0.0], 120.03e-03)

    assert False


@pytest.mark.parametrize(
    "source_csv",
    ("test_scope_1_column.csv", "test_scope_2_columns.csv", "test_scope_9_columns.csv"),
)
def test_read_octascope_output_variable_columns(source_csv, test_data_dir):
    source_csv_fullpath = os.path.join(test_data_dir, source_csv)
    assert os.path.isfile(source_csv_fullpath), f"{source_csv_fullpath} does not exist"
    assert False
