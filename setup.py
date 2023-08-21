from pathlib import Path

import setuptools


ROOT_DIRECTORY = Path(__file__).parent.resolve()

setuptools.setup(
    name='tesstrain',
    description='Training utils for Tesseract',
    long_description=(ROOT_DIRECTORY / 'README.md').read_text(encoding='utf-8'),
    long_description_content_type='text/markdown',
    url='https://github.com/stefan6419846/tesstrain_package',
    packages=setuptools.find_packages(),
    include_package_data=True,
    license='Apache Software License 2.0',
    author='Tesseract contributors',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Image Recognition',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Typing :: Typed',
    ],
    keywords='Tesseract,tesseract-ocr,OCR,optical character recognition',

    python_requires='>=3.8,<4',
    install_requires=[
        'tqdm',
    ],
    extras_require={
        'dev': [
            'mypy',
            'types-tqdm',
        ]
    },

    entry_points={
        'console_scripts': [
        ],
    },
)
