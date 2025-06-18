# ft_package

A simple Python package that provides utility functions for list operations.

## Installation

```bash
pip install ft_package
```

## Usage

```python
from ft_package import count_in_list

my_list = [1, 2, 3, 4, 5]
needle = 2
count = count_in_list(my_list)
print(f"The list contains {count} times the element {needle}.")
```

## Functions

### count_in_list

Return the occurence number of `needle` in `lst`.

**Parameters:**
- `lst` (list): The list to count elements from
- `needle` (Any): The element to search in the list

**Returns:**
- `int`: The number of elements `needle` in the list

## License
MIT