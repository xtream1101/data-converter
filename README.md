# Data Converter

## WIP...DO NOT USE YET

Convert data files between different formats


### Install
Python: `pip install data-converter`  
Brew: `coming soon...`


### Ways to use

#### Command line
```
$ data-converter -h
usage: data-converter [-h] -t TO input_file

Convert data files

positional arguments:
  input_file      File to convert from

optional arguments:
  -h, --help      show this help message and exit
  -t TO, --to TO  Format to convert to
```

#### Import in python
```python
import data_converter

# Convert one format to another. Ex. csv --> json
output_path = data_converter.convert("~/some/data/file.csv", "json")
print(output_path)  # Print the full path of the new json file

# Read in any supported data format into a python object
data = data_converter.csv_helper.read_file("~/some/data/test.csv")

```


### Currently supported file types
- json
- csv
