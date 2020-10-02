from setuptools import setup

setup(
        name="toopy",
        version="0.1",
        py_modules=["too"],
        install_requires=[
            "Click",
            "pyyaml",
        ],
        entry_points="""
            [console_scripts]
            toopy=too:cli
        """,
)
