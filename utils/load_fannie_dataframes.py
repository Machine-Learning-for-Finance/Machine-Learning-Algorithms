import pandas as pd
from .data import AcquisitionColumnNames, PerformanceColumnNames


def load_dataframes_fannie(aqcuisition: str,
                           performance: str,
                           *args, **kwargs) -> (pd.DataFrame, pd.DataFrame):
    """

    :param aqcuisition:
    :param performance:
    :param args:
    :param kwargs:
    :return:
    """
    acquisition_df = pd.read_csv(
        aqcuisition,
        names=AcquisitionColumnNames,
        header=None,
        sep="|"
    )

    performance_df = pd.read_csv(
        performance,
        names=PerformanceColumnNames,
        header=None,
        sep="|"
    )

    return acquisition_df, performance_df
