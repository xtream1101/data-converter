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
usage: data-converter [-h] -i INPUT_FILE -t TO [-o [OUTPUT_FILE]]
                      [-c CHUNK_SIZE]

Convert data files

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT_FILE, --input-file INPUT_FILE
                        File to convert
  -t TO, --to TO        Output format
  -o [OUTPUT_FILE], --output-file [OUTPUT_FILE]
                        Output file
  -c CHUNK_SIZE, --chunk-size CHUNK_SIZE
                        Max rows per output file
```

Examples:
`~/Downloads/test.csv` -> `new_data.json`  
`$ data-converter -i=~/Downloads/test.csv -t=json -o=new_data.json`  

`~/Downloads/test.csv` -> `test.json`  
`$ data-converter -i=~/Downloads/test.csv -t=json -o=test.json` or `$ data-converter -i=~/Downloads/test.csv -t=json -o=`  
If you leave the output as a blank string (`-o=`) then it will take the full path of the input file and change the file extension to the output data type.

`~/Downloads/test.csv` -> `json` output in the terminal  
`$ data-converter -i=~/Downloads/test.csv -t=json`  
If you do not even use the argument `-o`, then the converted data will be sent to `stdout` (the terminal) which then can be piped (`|`) into anything you want without creating a new file.


#### Import in python
```python
import data_converter

# The output file argument in any example can either be a path string a file object, or nothing (terminal output).
# Pass in the keyword arg `chunk_size=n` (n is the num of rows to store in each file)
# to any `convert` or `write_file` function. This will return a list of files that the data is chunked up into.

# Convert one format to another. Ex. csv --> json
output_path = data_converter.convert('/some/data/file.csv', 'json', '/new_file.json')
print(output_path)  # Print the full path of the new json file `/new_file.json`

# Leave the output file as a blank string to save the file in the same location as the input but with a new extension
output_path = data_converter.convert('/some/data/file.csv', 'json', '')
print(output_path)  # Print the full path of the new json file `/some/data/file.json`

# Dont pass in any output path and it will output the new file contents to stdout
output = data_converter.convert('/some/data/file.csv', 'json')
# output will be a file object created by stdout

# Read in any supported data format into a python object
data = data_converter.csv_helper.read_file('~/some/data/test.csv')

# Or write the data to any file like object in python
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

# This will return the StringIO object back containg the data
data = data_converter.csv_helper.write_file([[1,2,3],[4,5,6]], StringIO(), header=False)

```

#### Arguments for each file type
- **json**
    - **Reading/Converting from**
        - N/A
    - **Writing/Converting to**
        - N/A

- **csv**
    - **Reading/Converting from**
        - **has_header** _(bool)_ - _Default: True_ - The first row in the csv is the header
    - **Writing/Converting to**
        - **has_header** _(bool)_ - _Default: True_ - Write first row to the csv as the header

### Currently supported file types
- json
- csv
