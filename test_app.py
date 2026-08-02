from app import app


def test_header_is_present():
    """Test 1: Check header component is present in the app layout."""
    layout_str = str(app.layout)
    assert "Soul Foods — Pink Morsels Visualiser" in layout_str


def test_visualisation_is_present():
    """Test 2: Check graph component is present in the app layout."""
    layout_str = str(app.layout)
    assert "sales-line-chart" in layout_str


def test_region_picker_is_present():
    """Test 3: Check region filter component is present in the app layout."""
    layout_str = str(app.layout)
    assert "region-filter" in layout_str