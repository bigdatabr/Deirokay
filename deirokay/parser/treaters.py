import pandas as pd

from ..enums import DTypes
from .validator import Validator


def data_treater(df, options):
    treat_dtypes = {
        DTypes.INT64: IntegerTreater,
        DTypes.DATETIME: DateTime64Treater,
        DTypes.FLOAT64: FloatTreater,
        DTypes.STRING: StringTreater,
        DTypes.TIME: TimeTreater,
        DTypes.BOOLEAN: BooleanTreater
    }
    for col, option in options.items():
        option: dict = option.copy()

        dtype = option.pop('dtype', None)
        rename_to = option.pop('rename', None)

        if dtype is not None:
            try:
                df[col] = treat_dtypes[dtype](**option)(df[col])
            except KeyError:
                raise NotImplementedError(f"Handler for '{dtype}' hasn't been"
                                          " implemented yet")

        if rename_to is not None:
            df.rename(columns={col: rename_to}, inplace=True)


class NumericTreater(Validator):
    def __init__(self, thousand_sep=None, **kwargs):
        super().__init__(**kwargs)

        self.thousand_sep = thousand_sep

    def __call__(self, series):
        super().__call__(series)

        if self.thousand_sep is not None:
            try:
                series = series.str.replace(self.thousand_sep, '', regex=False)
            except AttributeError as e:
                print(*e.args)
                raise AttributeError(
                    'Make sure you are not declaring a `thousand_sep` to'
                    ' read a non-text-like column. This may happen when'
                    ' reading numeric columns from a .parquet file,'
                    ' for instance.'
                )

        return series


class BooleanTreater(Validator):
    def __init__(self,
                 truthies=['true', 'True'],
                 falsies=['false', 'False'],
                 ignore_case=False,
                 default_value=None,
                 **kwargs):
        super().__init__(**kwargs)

        assert default_value in (True, False, None)

        self.truthies = truthies
        self.falsies = falsies
        self.ignore_case = ignore_case
        self.default_value = default_value

        if self.ignore_case:
            self.truthies = [truthy.lower() for truthy in truthies]
            self.falsies = [falsy.lower() for falsy in falsies]

    def _evaluate(self, value):
        if value is None or value is pd.NA:
            return self.default_value
        if self.ignore_case:
            value = value.lower()
        if value in self.truthies:
            return True
        if value in self.falsies:
            return False
        return self.default_value

    def __call__(self, series):
        super().__call__(series)
        series = series.apply(self._evaluate).astype('boolean')
        # Validate again
        super().__call__(series)

        return series


class FloatTreater(NumericTreater):
    def __init__(self, decimal_sep=None, **kwargs):
        super().__init__(**kwargs)

        self.decimal_sep = decimal_sep

    def __call__(self, series):
        series = super().__call__(series)

        if self.decimal_sep is not None:
            try:
                series = series.str.replace(self.decimal_sep, '.', regex=False)
            except AttributeError as e:
                print(*e.args)
                raise AttributeError(
                    'Make sure you are not declaring a `decimal_sep` to'
                    ' read a non-text-like column. This may happen when'
                    ' reading numeric columns from a .parquet file,'
                    ' for instance.'
                )

        return series.astype(float).astype('Float64')


class IntegerTreater(NumericTreater):
    def __call__(self, series):
        return super().__call__(series).astype(float).astype('Int64')


class DateTime64Treater(Validator):
    def __init__(self, format='%Y-%m-%d %H:%M:%S', **kwargs):
        super().__init__(**kwargs)

        self.format = format

    def __call__(self, series):
        super().__call__(series)

        return pd.to_datetime(series, format=self.format)


class TimeTreater(DateTime64Treater):
    def __init__(self, format='%H:%M:%S', **kwargs):
        super().__init__(format, **kwargs)

    def __call__(self, series):
        return super().__call__(series).dt.time


class StringTreater(Validator):
    def __init__(self, treat_null_as=None, **kwargs):
        super().__init__(**kwargs)

        self.treat_null_as = treat_null_as

    def __call__(self, series):
        super().__call__(series)

        if self.treat_null_as is not None:
            series = series.fillna(self.treat_null_as)

        return series
