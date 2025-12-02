from dash.testing.application_runners import import_app


def test_header_exists(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    # Assert the <h1> header exists
    dash_duo.wait_for_element("h1", timeout=10)
    header = dash_duo.find_element("h1")
    assert header.text == "Pink Morsel"


def test_visualization_exists(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    # Assert graph with id="sales-chart" exists
    dash_duo.wait_for_element("#sales-chart", timeout=10)
    graph = dash_duo.find_element("#sales-chart")
    assert graph is not None


def test_region_picker_exists(dash_duo):
    app = import_app("app")
    dash_duo.start_server(app)

    # Assert component with id="region-filter" exists
    dash_duo.wait_for_element("#region-filter", timeout=10)
    region_picker = dash_duo.find_element("#region-filter")
    assert region_picker is not None
