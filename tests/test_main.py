
import pytest
from scrapy.selector import Selector

from scrapy_rowspan_colspan_contents_copied.main import extract


@pytest.fixture()
def selector_list():
    f = open("tests/index.html", "r")
    html = f.read()
    _selector_list = Selector(text=html).xpath('//table')
    return _selector_list

@pytest.fixture()
def selector():
    f = open("tests/index.html", "r")
    html = f.read()
    _selector = Selector(text=html).xpath('//table')
    return _selector


class TestMain:

    def test_main(self, selector_list):

        cleaned = extract(selector_list)
        assert isinstance(cleaned, list)
        assert isinstance(cleaned[0], list)
        max_length = len(max(cleaned, key=len))
        assert all(len(item) == max_length for item in cleaned)

