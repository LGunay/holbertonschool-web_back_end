#!/usr/bin/env python3
'''Python - Variable Annotations'''
from typing import List, Union


def to_kv(k: str, v: Union[int, float]) -> tuple[str, float]:
    '''tuple'''
    return (k, v**2)
