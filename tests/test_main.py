
import pytest
from scrapy.selector import Selector
from scrapy.selector.unified import SelectorList

from scrapy_rowspan_colspan_contents_copied.main import extract


@pytest.fixture()
def selector_list():
    f = open("tests/index.html", "r")
    html = f.read()
    _selector_list = Selector(text=html).xpath('//table')
    return _selector_list


def test_main(selector_list):
    cleaned = extract(selector_list)
    assert isinstance(cleaned, list)
    assert isinstance(cleaned[0], SelectorList)

    # Test without converting SelectorList passed.
    max_length = len(max(cleaned, key=len))
    assert all(len(item) == max_length for item in cleaned)
