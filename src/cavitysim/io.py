import pandas as pd


def _split_top_line(inline):
    return [v.strip().strip('"').strip() for v in inline.strip().split(",")]


def _check_indicator(indicator, expected, full_line, help_str):
    if indicator != expected:
        raise AssertionError(
            f"Expected {help_str} line to start with {expected}, got: {full_line}"
        )


def _get_no_header_lines(header_line):
    indicator, value = _split_top_line(header_line)

    _check_indicator(indicator, "Header Size", header_line, "header")

    try:
        return int(value)
    except ValueError:
        print(f"Couldn't convert value in header line, {value}, to an integer")
        raise


def _get_model_name(inline):
    indicator, value = _split_top_line(inline)
    _check_indicator(indicator, "Model Name", inline, "model name")

    return value


def _get_comment(inline):
    indicator, value = _split_top_line(inline)
    _check_indicator(indicator, "Comment", inline, "comment")

    return value


def _get_settings_key_value(inline):
    raw_split = [v.strip().strip('"').strip() for v in inline.strip().split(",")]

    for i in range(len(raw_split)):
        try:  # try converting to int
            raw_split[i] = int(raw_split[i])
            continue  # if it worked, move to the next item in the list
        except ValueError:
            pass

        try:  # try converting to float
            raw_split[i] = float(raw_split[i])
            continue
        except ValueError:
            pass

        # none of the conversions worked, do nothing

    return raw_split[0], raw_split[1:]


def read_octascope_output(filepath):
    """
    Read octascope output

    Parameters
    ----------
    filepath : str
        Filepath from which to read the data

    Returns
    -------
    dict
        Dictionary containing the read data. The keys are:

            - ``Header Size``: The size of the header in the data file

            - ``Model Name``: [Rusty halp]

            - ``Comment``: [Rusty halp]

            - ``settings``: A pandas ``DataFrame`` containing information about
                            the settings used in each channel. The columns are
                            each different channel whilst the index is the
                            different settings e.g. ``SampleRate``, ``HUnit``.

            - ``data``: A pandas ``DataFrame`` containing the data from each
                        channel. Each row is a different channel and the index
                        is the different times.
    """
    with open(filepath, "r") as fh:
        header_line = fh.readline()
        no_header_lines = _get_no_header_lines(header_line)

        model_name = _get_model_name(fh.readline())
        comment = _get_comment(fh.readline())

        # we've already read top three lines
        remaining_header_lines = no_header_lines - 3

        raw_settings = {}
        for i in range(remaining_header_lines):
            key, value = _get_settings_key_value(fh.readline())
            raw_settings[key] = value

    try:
        settings = pd.DataFrame(raw_settings)
    except ValueError:
        print("settings lines don't all have the same length")
        raise

    settings = settings.set_index("TraceName")
    settings.index.name = "Channel"
    settings = settings.T

    data = pd.read_csv(
        filepath, skiprows=no_header_lines, header=None, index_col=0
    ).dropna(axis=1)
    try:
        data.columns = settings.columns
    except ValueError:
        print("settings columns don't match data columns")
        raise

    data.index.name = "Time"

    output = {
        "header": {
            "Header Size": no_header_lines,
            "Model Name": model_name,
            "Comment": comment,
        },
        "settings": settings,
        "data": data,
    }

    return output
