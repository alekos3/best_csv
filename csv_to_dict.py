__author__ = "Alexios Nersessian"
__email__ = "nersessian@gmail.com"
__version__ = "v1"

"""
MIT License

Copyright (c) 2023 Alexios Nersessian

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

def csv_to_dict(file_name:str, column_as_key:int) -> dict:
    """
    Pass the filename and column number of the CSV file that you would like to make the keys in the
    dictionary. For example Column One is 1 and Column five is 5.
              usage: csv_to_dict("example.csv", 2)
    :param file_name: string
    :param column_as_key: integer
    :return: dictionary
    """
    information_dict = {}
    tmp_dict = {}
    keys = []

    try:
        # Open the CSV file
        with open(file_name, 'r') as f:
            raw = f.readlines()

        for i, line in enumerate(raw):
            tmp = line.replace("\n", "").split(",")

            if i > 0:
                for x, key in enumerate(keys):
                    tmp_dict[key] = tmp[x+1]
                information_dict[tmp[column_as_key-1]] = tmp_dict

            else:
                for field in tmp:
                    keys.append(field)
                keys.pop(0)
            tmp_dict = {}

        return information_dict

    except Exception as e:
        print(e)
        return {"Error": e}
