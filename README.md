# malmopy: a Python library for working with Project Malmo

[Project Malmo](https://github.com/Microsoft/malmo) comes with MalmoPython, which is a Python wrapper around a C++ library.

The C++ API is directly exposed using Boost.Python.

This library aims to provide a more Pythonic API by providing a higher level abstraction around common tasks.

![](http://melvinzh.sdf.org/cliff-loop.gif)

## Installation

Copy src/malmopy.py and put it together with MalmoPython.so.

## API

### Initialization

```python
malmo = malmopy.Malmo()
```

### Start a mission from mission xml file

```python
malmo.start_mission('missions/cliff_walking_1.xml')
```

### Movement

```python
# move forward 1m
malmo.move()

# turn left
malmo.turn_left()

# turn right
malmo.turn_right()
```

### Control loop

```python
for obs in malmo.observations():
    # agent policy
