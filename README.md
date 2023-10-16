# best_csv

This library converts a csv file to a Python dictionary. "So what!?!?" you may ask :). This library does it better, more efficienty and greatly improves your querry times over the built in csv Python library. The built in csv Python library has a lookup complexity 
of O(n) where runtime grows directly in proportion to n; best_csv has a lookkup complexity of O(1) which means that it takes a constant time to lookup regardless of the dataset size.

Now, this library might not be ideal for all csv datasets but is great for datasets that have a a column that we can use as a unique identifier for any given row of information. For example, if we have a dataset of employees and each row is an employee record we can use the employee IDs as the key for any given employee in the dictionary. 

The statndard Python csv library will create a list of dicts so if you want to search for specific employee IDs you have to potentialy loop though all of the dataset to find the employee you want; whereas with best_csv you simply call the employee ID you need without having to loop through the dataset. This is great if you have massive datasets and you are running multiple querries.




## Installation

Use the package manager pip to install dnac_device_list.

```bash
  pip install best_csv
```
    
## Usage/Examples


```python
import best_csv

# Headers in employee_data.csv
# User Id,First Name,Last Name,Email,Phone,Date of birth,Job Title

# Convert your csv to dict with column 1 as the unique key for any given row.
result = best_csv.csv_to_dict("employee_data.csv", 1)


print(result['AB123']) # Print info of Employee ID AB123

```


## result['AB123'] print simulation

```
{'First Name': 'Wesley', 'Last Name': 'Chung', 'Email': 'wcab123s@acme.org', 'Phone': '(280)277-4903', 'Date of birth': '1953-04-21', 'Job Title': 'Security Engineer'}

```


## Authors

- [@Alexios Nersessian](https://github.com/alekos3)

