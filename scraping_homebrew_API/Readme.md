# PROJECT DESCRIPTION

The purpose of this project is to fetch installation data from homebrew's API -- a package manager for MacOS. With this data, It is possible to analyze the number of packages avalaible in homebrew's repository, the number of installations in 30-day, 90-day and 1-year period of all installed packages, top "n" number of installed packages for specific period, the package with the largest number of differential between number of install and number of install on request for the packages.

This numbers are particularly important to allow homebrew get to know the most popular packages on its repository, It can also help apple to get to ensure that this popular packages works seamlessly on apple phones in order to reduce customer complaints and consequently improves customer satisfaction.

# ETL Description

`main.py` file is used to build the programs used for pulling data from homebrew's API. The total time to it took to fetch over 6000 data points from the source API is 6805.85168 seconds (2 hours). Finally, the data is written to `homebrew_packages_data.csv` file.