from setuptools import setup, find_packages
setup(
    name="spain-economic-impact-database-2020-2024",
    version="1.0.0",
    description="This dataset compiles key macroeconomic and financial indicators for Spain covering the period 2020&",
    author="de la Serna, Juan Moisés",
    url="https://github.com/juanmoisesd/spain-economic-impact-database-2020-2024",
    packages=find_packages(),
    install_requires=["pandas>=1.3.0","requests>=2.26.0"],
    python_requires=">=3.7",
    classifiers=["Programming Language :: Python :: 3","License :: OSI Approved :: MIT License","Topic :: Scientific/Engineering"],
    keywords="cc0, citation, dataset, development-economics, economic-indicators, economics, fair-data, financial-markets, gdp, inflation, juan-moises-de-la-serna, macroeconomics, open-data, open-science, orcid, research, spain, tourism, unemployment, zenodo, zenodo, open-data",
)