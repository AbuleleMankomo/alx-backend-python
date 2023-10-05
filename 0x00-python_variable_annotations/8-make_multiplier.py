#!/usr/bin/env python3
'''Task  module.
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Creates multiplier function.
    '''
    return lambda x: x * multiplier
