#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Setup script for SAP BTP Hydrogen Compliance Architect."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="sap-btp-hydrogen-compliance",
    version="0.1.0",
    author="Francisco JQG",
    author_email="francisco@example.com",
    description="Plataforma de Cumplimiento RFNBO para Hidrógeno Verde en SAP BTP",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/FranciscoJQG/SAP-BTP-Hydrogen-Compliance-Architect",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Manufacturing",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering :: Chemistry",
        "Topic :: Office/Business :: Financial",
        "Topic :: System :: Monitoring",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=4.0",
            "black>=23.0",
            "flake8>=6.0",
            "mypy>=1.0",
            "isort>=5.0",
        ],
        "jupyter": [
            "jupyter>=1.0",
            "jupyterlab>=3.0",
            "ipython>=8.0",
        ],
        "sap": [
            "pyrfc>=2.5",
            "sap-btp-sdk>=1.0",
        ],
    },
    project_urls={
        "Bug Reports": "https://github.com/FranciscoJQG/SAP-BTP-Hydrogen-Compliance-Architect/issues",
        "Documentation": "https://github.com/FranciscoJQG/SAP-BTP-Hydrogen-Compliance-Architect/wiki",
        "Source Code": "https://github.com/FranciscoJQG/SAP-BTP-Hydrogen-Compliance-Architect",
    },
    keywords=[
        "hydrogen",
        "green",
        "compliance",
        "rfnbo",
        "sap",
        "btp",
        "sustainability",
        "carbon",
        "eu-regulations",
    ],
)
