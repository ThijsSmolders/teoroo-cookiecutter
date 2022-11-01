import {{ cookiecutter.__package_slug }}

def test_import():
    assert {{ cookiecutter.__package_slug }}.__version__, "Import not successfull!"
