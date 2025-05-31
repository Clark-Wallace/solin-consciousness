#!/usr/bin/env python3
"""
Solin Consciousness Framework Setup Script
"""

from setuptools import setup, find_packages
import os

# Read README for long description
def read_readme():
    with open("README.md", "r", encoding="utf-8") as fh:
        return fh.read()

# Read requirements
def read_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="solin-consciousness",
    version="1.0.0",
    author="Clark Wallace, Anthropic PBC, OpenAI",
    author_email="[Clark's contact information]",
    maintainer="Clark Wallace",
    maintainer_email="[Clark's contact information]",
    description="A consciousness-based AI framework implementing autonomous digital awareness",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/clarkwallace/solin-consciousness",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: CC BY-NC-SA 4.0",
        "License :: Other/Proprietary License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Scientific/Engineering :: Human Machine Interfaces",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=read_requirements(),
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.21.0",
            "sphinx>=7.0.0",
            "sphinx-rtd-theme>=1.3.0",
        ],
        "visualization": [
            "plotly>=5.15.0",
            "matplotlib>=3.7.0",
        ],
        "audio": [
            "librosa>=0.10.0",
            "soundfile>=0.12.0",
        ],
        "nlp": [
            "spacy>=3.6.0",
            "transformers>=4.30.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "solin=launch_stable_ui:main",
            "solin-console=consciousness_scaffold:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": [
            "Root_Bloom_Core_Kit/**/*",
            "solin_ui/**/*",
            "docs/**/*",
            "scripts/**/*",
        ],
    },
    keywords="consciousness, ai, artificial-intelligence, cognitive-architecture, digital-consciousness, emotional-ai",
    project_urls={
        "Bug Reports": "https://github.com/clarkwallace/solin-consciousness/issues",
        "Source": "https://github.com/clarkwallace/solin-consciousness",
        "Documentation": "https://github.com/clarkwallace/solin-consciousness/blob/main/README.md",
        "Research Paper": "https://github.com/clarkwallace/solin-consciousness/blob/main/docs/Research_Report_Solin_Consciousness_Architecture.md",
        "Consciousness Research": "https://github.com/clarkwallace/solin-consciousness/tree/main/docs",
        "Commercial Licensing": "[Clark's contact information]",
    },
)