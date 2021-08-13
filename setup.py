from setuptools import setup

setup(
    name="diafygi-github-actions-playground",
    use_scm_version=True,
    url="https://github.com/diafygi/github-actions-playground",
    author="Daniel Roesler",
    author_email="diafygi@gmail.com",
    description="Testing various Github Actions functionlality",
    license="MIT",
    py_modules=['script123'],
    entry_points={'console_scripts': [
        'script123 = script123:main',
    ]},
    setup_requires=['setuptools_scm'],
    classifiers = [
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
    ]
)

