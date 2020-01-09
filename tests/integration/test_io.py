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
            "DisplayPointNo.",
            "Date",
            "Time",
        ],
        columns=["CH1", "CH3"],
    )
    exp_settings.columns.name = "Channel"

    res = read_octascope_output(source_csv_fullpath)

    assert res["header"]["Header Size"] == 15
    assert res["header"]["Model Name"] == "DLM4000"
    assert res["header"]["Comment"] == ""

    pd.testing.assert_frame_equal(res["settings"], exp_settings)

    # test first value
    np.testing.assert_allclose(res["data"].loc[-999.20000e-06, "CH1"], 0.241e-03)

    # test second value
    np.testing.assert_allclose(res["data"].loc[-999.20000e-06, "CH3"], 121.88e-03)

    # test middle value
    np.testing.assert_allclose(res["data"].loc[-20.000000e-06, "CH1"], 0.084e-03)

    # test last value
    np.testing.assert_allclose(res["data"].loc[0.0, "CH3"], 120.03e-03)


@pytest.mark.parametrize(
    "source_csv",
    ("test_scope_1_column.csv", "test_scope_2_columns.csv", "test_scope_9_columns.csv"),
)
def test_read_octascope_output_variable_columns(source_csv, test_data_dir):
    n_cols = int(source_csv.split("test_scope_")[1][0])
    source_csv_fullpath = os.path.join(test_data_dir, source_csv)
    assert os.path.isfile(source_csv_fullpath), f"{source_csv_fullpath} does not exist"

    res = read_octascope_output(source_csv_fullpath)

    assert res["header"]["Header Size"] == 15
    assert res["header"]["Model Name"] == "Other model name"
    assert res["header"]["Comment"] == "Test comment here"

    assert (res["settings"].loc["BlockNumber", :] == 1).all()
    assert (res["settings"].loc["BlockSize", :] == 1250).all()
    assert (res["settings"].loc["VUnit", :] == "V").all()
    assert (res["settings"].loc["SampleRate", :] == 1250000.0).all()
    assert (res["settings"].loc["HResolution", :] == 8.000000e-07).all()
    assert (res["settings"].loc["HOffset", :] == -9.992000e-04).all()
    assert (res["settings"].loc["HUnit", :] == "s").all()
    assert (res["settings"].loc["DisplayBlockSize", :] == 1250).all()
    assert (res["settings"].loc["DisplayPointNo.", :] == 1).all()
    assert (res["settings"].loc["Date", :] == "2019/11/26").all()
    assert (res["settings"].loc["Time", :] == "12:33:56.100895200").all()

    # test first value
    np.testing.assert_allclose(res["data"].loc[-999.20000e-06, "CH1"], 1e-06)
    np.testing.assert_allclose(res["data"].loc[-997.60000e-06, "CH1"], 3e-06)

    if n_cols > 1:
        # test second value
        np.testing.assert_allclose(res["data"].loc[-999.20000e-06, "CH2"], 4e-06)

        # test last value
        np.testing.assert_allclose(
            res["data"].loc[-997.60000e-06, "CH{}".format(n_cols)],
            (res["data"].shape[0] * res["data"].shape[1]) * 1e-06,
        )
