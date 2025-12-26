# Python Quick Reference

## Common Commands
```bash
# Activate virtual environment
source .venv/bin/activate


# Install packages
pip install package_name
pip install -r requirements.txt

# Check installed packages
pip list
pip show package_name

# Format code
black script.py
black .  # Format all files

# Check code quality
flake8 script.py

# Run tests
pytest
pytest tests/test_file.py
```

## Python Basics Cheat Sheet

### Variables & Types
```python
# Numbers
x = 42          # int
y = 3.14        # float

# Strings
name = "Python"
multiline = """Multi
line string"""

# Lists (mutable)
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

# Tuples (immutable)
coords = (10, 20)

# Dictionaries
person = {"name": "Alice", "age": 25}
person["city"] = "NYC"

# Sets
unique_nums = {1, 2, 3, 3}  # {1, 2, 3}
```

### Control Flow
```python
# If statements
if x > 0:
    print("positive")
elif x < 0:
    print("negative")
else:
    print("zero")

# For loops
for item in fruits:
    print(item)

for i in range(5):  # 0 to 4
    print(i)

# While loops
count = 0
while count < 5:
    print(count)
    count += 1

# List comprehension
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
```

### Functions
```python
# Basic function
def greet(name):
    return f"Hello, {name}!"

# With type hints
def add(a: int, b: int) -> int:
    return a + b

# Default arguments
def power(base, exp=2):
    return base ** exp

# *args and **kwargs
def print_all(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key}: {value}")
```

### File I/O
```python
# Read file
with open("file.txt", "r") as f:
    content = f.read()
    # or line by line
    for line in f:
        print(line.strip())

# Write file
with open("file.txt", "w") as f:
    f.write("Hello, World!\n")

# Append to file
with open("file.txt", "a") as f:
    f.write("More text\n")
```

### Error Handling
```python
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
finally:
    print("This always runs")
```

### Working with APIs (requests)
```python
import requests

# GET request
response = requests.get("https://api.example.com/data")
if response.status_code == 200:
    data = response.json()

# POST request
data = {"key": "value"}
response = requests.post("https://api.example.com/endpoint", json=data)

# With headers
headers = {"Authorization": "Bearer token"}
response = requests.get("https://api.example.com/data", headers=headers)
```

### Pandas Basics
```python
import pandas as pd

# Create DataFrame
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6]
})

# Read CSV
df = pd.read_csv("data.csv")

# Basic operations
df.head()           # First 5 rows
df.info()           # Column info
df.describe()       # Statistics
df['column'].mean() # Column average

# Filter
filtered = df[df['A'] > 2]

# Write to CSV
df.to_csv("output.csv", index=False)
```

### Environment Variables (.env)
```python
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Access variables
api_key = os.getenv("API_KEY")
database_url = os.getenv("DATABASE_URL", "default_value")
```

### Testing with pytest
```python
# In test_example.py
def add(a, b):
    return a + b

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

# Run: pytest
```

## Useful Built-in Functions
```python
len(obj)           # Length of object
type(obj)          # Type of object
str(obj)           # Convert to string
int(obj)           # Convert to integer
list(obj)          # Convert to list
sum(iterable)      # Sum of items
max(iterable)      # Maximum value
min(iterable)      # Minimum value
sorted(iterable)   # Return sorted list
enumerate(iter)    # Get index and value
zip(iter1, iter2)  # Combine iterables
```

## String Methods
```python
s = "  Hello, World!  "
s.strip()          # "Hello, World!"
s.lower()          # "  hello, world!  "
s.upper()          # "  HELLO, WORLD!  "
s.replace("World", "Python")
s.split(",")       # ["  Hello", " World!  "]
",".join(["a", "b", "c"])  # "a,b,c"
"test" in s        # False
s.startswith("  H") # True
```
