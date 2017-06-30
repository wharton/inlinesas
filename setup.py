try:
    from setuptools import setup
except ImportError:
    from distuils.core import setup

setup(
        name="inlinesas",
        version='0.0.5',
        description="Run SAS code from within a Python script.",
        author="Joe Dougherty",
        author_email="josepd@wharton.upenn.edu",
        url="https://wrds-web.wharton.upenn.edu/wrds/",
        packages=['inlinesas'],
        )

