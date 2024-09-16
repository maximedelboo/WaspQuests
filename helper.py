import pandas as pd

# Load the CSV file
file_path = 'C:\\Users\\maxim\\AppData\\Local\\Simba\\Includes\\WaspQuests\\questNames.csv'
df = pd.read_csv(file_path)

# Display the content to understand its structure
df.head()

import os
import sys

# Function to convert a string to camelCase
def to_camel_case_without_apostrophe(s):
    s = s.replace("'", "")  # Remove apostrophes
    s = s.split()
    return s[0].lower() + ''.join(word.capitalize() for word in s[1:])


# Process each name in the dataframe
names = df['Tutorial Island']
print(names)

# Directory to save the files
output_dir = 'setups'
os.makedirs(output_dir, exist_ok=True)

# Create a .simba file for each name in camelCase
for name in names:
    camel_case_name = to_camel_case_without_apostrophe(name)
    file_name = f"{camel_case_name}.simba"
    file_path = os.path.join(output_dir, file_name)
    with open(file_path, 'w') as file:
        file.write(f"{{$IFNDEF WQ_OSR}}\n\t{{$I WaspQuests/osr.simba}}\n{{$ENDIF}}")

output_dir

# Get the base directory of the current Python instance
base_dir = sys.path[0]
print(base_dir)
print(os.listdir(output_dir))

absolute_output_dir = os.path.abspath(output_dir)
print(absolute_output_dir)

file_path = 'osr2.simba'
lines = []
with open(file_path, 'w') as file:
    for name in names:
        fullcaps_name = to_camel_case_without_apostrophe(name).upper()
        camel_case_name = to_camel_case_without_apostrophe(name) + '.simba'
        lines.append(f'{{$I setups/{camel_case_name}.simba}}\n')
    
    file.writelines(lines)
