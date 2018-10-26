import pytest


@pytest.fixture(scope='session')
def dummie_csv():
    return """col1,col2,col3
val1,val2,val3
val11,val12,val13"""