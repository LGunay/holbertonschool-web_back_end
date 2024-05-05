#!/usr/bin/env python3
"""Async Comprehensions"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    '''async_comprehension'''
    for i in async_generator():
        random = i
        return random