#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)
```python
    a = 0 
    while (a < n * n * n):          # O(3n)
      a = a + n * n                 # O(n)
```
Answer = O(n)

b)
```python
    sum = 0
    for i in range(n): O(n)             # O(n * (1 + (log n)))
      j = 1 # O(1)                  # O(n * log n)
      while j < n: # O(log n)       # O(n log n) 
        j *= 2
        sum += 1
```
Answer = O(n log n)

c)
```python
    def bunnyEars(bunnies):
      if bunnies == 0:
        return 0                        # Will only run based on the number
                                        # of bunnies so runtime will increase
      return 2 + bunnyEars(bunnies-1)   # linearly to the size of n
```                                     
Answer = O(n)                           


## Exercise II


