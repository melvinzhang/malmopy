---
author: Melvin Zhang
title: Intro to AI with Project\ Malmo 
date: 24th June, 2018
---

# Fictional Robots

![](r2d2.jpg){height=500px}

---

![](data.jpg){height=500px}

---

![](rosie.jpg){height=500px}


# Real life Robots


![](kofu.jpg){height=500px}

---

![](cleaner.jpg){height=500px}

---

![](agv.jpg){height=500px}


# Intelligent Agent 

![](AI-agent-and-environment.jpg){height=500px}

# Project Malmo

![https://github.com/Microsoft/malmo](ProjectMalmo.jpg)

# Sample mission

![](malmo.gif)

# Collaborative agent

![](collab-task.png)

# Activity 1: Using MalmoPy

```python
import MalmoPy

malmo = MalmoPy.Malmo()
malmo.start_mission('mission1.xml')
# turn right
malmo.turn(1)
# move forward
malmo.move(1)
# turn left
malmo.turn(-1)
```

# Activity 2: Reacting to the world


```python
for obs in malmo.observations():
    print(obs)
    malmo.move(1)
```


# Activity 3: Navigating the world
