## Python Functions

List of Commonly Used Functions:

range():

- Generates a sequence of numbers
- excludes the stop value
- Can specify start, stop, and step values
  - Example: `range(0, 10, 2)` generates [0, 2, 4, 6, 8]
  - `range(5)` generates [0, 1, 2, 3, 4]
  - `range(1, 10, 2)` generates [1, 3, 5, 7, 9]
  - `range(10, 0, -1)` generates [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
  - `range(0, 0, 1)` generates []

enumerate():

- Adds a counter to an iterable and returns it as an enumerate object
- Commonly used in for-loops to get both index and value
- Example: `for i, value in enumerate(['a', 'b', 'c']):` gives (0, 'a'), (1, 'b'), (2, 'c')

len():

- Returns the number of items in an iterable
- Commonly used to get the size of lists, strings, etc.
- Example: `len([1, 2, 3])` returns 3

set():

- Creates a set object, which is an unordered collection of unique elements
- Commonly used to remove duplicates from a list
- Example: `set([1, 2, 2, 3])` returns {1, 2, 3}
