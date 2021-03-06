# This file auto-generated by `generate_schema_interface.py`.
# Do not modify this file directly.

import traitlets as T
from ..baseobject import BaseObject
from .formula import Formula


class Transform(BaseObject):
    """Wrapper for Vega-Lite Transform definition.
    
    Attributes
    ----------
    calculate: List(Formula)
        Calculate new field(s) using the provided expresssion(s).
    filter: Unicode
        A string containing the filter Vega expression.
    filterNull: Bool
        Filter null values from the data.
    """
    calculate = T.List(T.Instance(Formula, help="""Formula object for calculate."""), allow_none=True, default_value=None, help="""Calculate new field(s) using the provided expresssion(s).""")
    filter = T.Unicode(allow_none=True, default_value=None, help="""A string containing the filter Vega expression.""")
    filterNull = T.Bool(allow_none=True, default_value=None, help="""Filter null values from the data.""")
    
    def __init__(self, calculate=None, filter=None, filterNull=None, **kwargs):
        kwds = dict(calculate=calculate, filter=filter, filterNull=filterNull)
        kwargs.update({k:v for k, v in kwds.items() if v is not None})
        super(Transform, self).__init__(**kwargs)