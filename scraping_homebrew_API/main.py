import json
import time
import requests
import csv

packages_url = "https://formulae.brew.sh/api/formula.json"

request = requests.get(packages_url)
packages_json = request.json()

print(len(packages_json))

packages_name = (package["name"] for package in packages_json)

# The url above have no analytics data for installation. 
# However, https://formulae.brew.sh/api/formula/a2ps.json API has analytics data for a2ps data
# Hence we try to find a way to grab the "package name" and then input it into the url.

homebrew_data_list = []

t1 = time.perf_counter()

for package_name in packages_name:
    package_url = f"https://formulae.brew.sh/api/formula/{package_name}.json"

    request = requests.get(package_url)
    package_json = request.json()

    name = package_json["name"]
    description = package_json["desc"]
    homepage = package_json["homepage"]

    metrics = ["install", "install_on_request"]
    metrics_period = ["30d", "90d", "365d"]

    total_metric_data = []
    total_metric_names = []
    for metric in metrics:
        for period in metrics_period:
            metric_data = package_json["analytics"][metric][period][package_name]
            metric_name = "num_" + metric + "_" + period
            total_metric_data.append(metric_data)
            total_metric_names.append(metric_name)

    generated_date = package_json["generated_date"]

    field_names = ["name", "description", "homepage", *total_metric_names, "generated_date"]
    field_values = [name, description, homepage, *total_metric_data, generated_date]
    
    key_value_pair = {}
    for item, value in zip(field_names, field_values):
        key_value_pair[item] = value
    
    homebrew_data_list.append(key_value_pair)

    time.sleep(request.elapsed.total_seconds())
    print(f"Got response in {request.elapsed.total_seconds()}")

t2 = time.perf_counter()

print(f"Total time it takes to get all data is {t2 - t1} seconds")
with open("homebrew_packages_data.csv", "w", encoding="utf8") as file:
    field_names = ["name", "description", "homepage", *total_metric_names, "generated_date"]
    writer = csv.DictWriter(file, fieldnames= field_names)
    writer.writeheader()
    writer.writerows(homebrew_data_list)

