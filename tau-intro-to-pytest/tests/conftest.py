import pytest

from stuff.accum import Accumulator

@pytest.fixture
def accum():
    yield Accumulator()
    print("DONE with the test!")

@pytest.fixture
def accum2():
    return Accumulator()