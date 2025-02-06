import pandas as pd
from pandas.api.extensions import ExtensionDtype
from typing_extensions import TypeAlias

from pandas._typing import (
    ArrayLike,
    DtypeObj,
    npt,
)

from pandas.core.dtypes.inference import (
    is_array_like as is_array_like,
    is_bool as is_bool,
    is_complex as is_complex,
    is_dict_like as is_dict_like,
    is_file_like as is_file_like,
    is_float as is_float,
    is_hashable as is_hashable,
    is_integer as is_integer,
    is_iterator as is_iterator,
    is_list_like as is_list_like,
    is_named_tuple as is_named_tuple,
    is_number as is_number,
    is_re as is_re,
    is_re_compilable as is_re_compilable,
    is_scalar as is_scalar,
)

_ArrayOrDtype: TypeAlias = (
    ArrayLike | npt.DTypeLike | pd.Series | pd.DataFrame | pd.Index | ExtensionDtype
)

def is_object_dtype(arr_or_dtype: _ArrayOrDtype) -> bool: ...
def is_datetime64_dtype(arr_or_dtype: _ArrayOrDtype) -> bool: ...
def is_timedelta64_dtype(arr_or_dtype: _ArrayOrDtype) -> bool: ...
def is_dtype_equal(source, target) -> bool: ...
def is_string_dtype(arr_or_dtype: _ArrayOrDtype) -> bool: ...
def is_integer_dtype(arr_or_dtype: _ArrayOrDtype) -> bool: ...
def is_signed_integer_dtype(arr_or_dtype: _ArrayOrDtype) -> bool: ...
def is_unsigned_integer_dtype(arr_or_dtype: _ArrayOrDtype) -> bool: ...
def is_datetime64_any_dtype(arr_or_dtype: _ArrayOrDtype) -> bool: ...
def is_datetime64_ns_dtype(arr_or_dtype: _ArrayOrDtype) -> bool: ...
def is_timedelta64_ns_dtype(arr_or_dtype: _ArrayOrDtype) -> bool: ...
def is_numeric_dtype(arr_or_dtype: _ArrayOrDtype) -> bool: ...
def is_float_dtype(arr_or_dtype: _ArrayOrDtype) -> bool: ...
def is_bool_dtype(arr_or_dtype: _ArrayOrDtype) -> bool: ...
def is_extension_array_dtype(arr_or_dtype: _ArrayOrDtype) -> bool: ...
def is_complex_dtype(arr_or_dtype: _ArrayOrDtype) -> bool: ...
def is_any_real_numeric_dtype(arr_or_dtype: _ArrayOrDtype) -> bool: ...
def pandas_dtype(dtype: object) -> DtypeObj: ...
