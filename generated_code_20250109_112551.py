# Task: Write a script to extract data from JSON and create summary reports

```python
import json
import pandas as pd

# Load the JSON data into a Python dictionary
with open('data.json') as f:
    data = json.load(f)

# Create a pandas DataFrame from the JSON data
df = pd.DataFrame(data)

# Group the data by the 'category' column and calculate the mean of the 'value' column for each group
summary = df.groupby('category').agg({'value': 'mean'})

# Print the summary report
print(summary)
```