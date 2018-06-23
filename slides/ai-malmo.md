---
author: Melvin Zhang
title: Intro to AI with Project\ Malmo
date: 24th June, 2018
---

# Fictional Robots

![](r2d2.jpg){height=500px}

---

![](david.jpg){height=500px}

---

![](rosie.jpg){height=500px}


# Real life Robots


![](kofu.jpg){height=500px}

---

![](cleaner.jpg){height=500px}

---

![](agv.jpg){height=500px}


# Intelligent Agent

![](control.jpg){height=500px}

# Project Malmo

![https://github.com/Microsoft/malmo](ProjectMalmo.jpg)

# Missions

![](malmo.gif)

# Activity 1: Moving around

Run `src/movement.py`. Edit it so that the agent moves to where the diamond is.
```python
import MalmoPy

malmo = MalmoPy.Malmo()
malmo.start_mission('missions/cliff_walking_1.xml')
# turn right
malmo.turn(1)
# move forward
malmo.move(1)
# turn left
malmo.turn(-1)
```

# Activity 2: Reacting to the world


![](control.jpg){height=500px}

---

Edit `src/reacting.py` and help the agent get to the diamond block.

```python
for obs in malmo.observations():
    floor = obs['floor']

    # (0,1) means in front
    # (-1,0) is to the left
    # (1,0) is to the right

    # front is a string description of the block
    front = floor[(0,1)]

    # implement the following logic:
    # if not lava in front
    #   move forward
    # else
    #   turn left
```

# Activity 3: Navigating the world

![](patrol.webp){height=500px}

---

Edit `src/patrol.py` and help the agent patrol the platform.

```python
for obs in malmo.observations():
    floor = obs['floor']

    # (0,1) means in front
    # (-1,0) is to the left
    # (1,0) is to the right

    # front is a string description of the block
    front = floor[(0,1)]

    # implement the following logic:
    #   patrol the platform in a clockwise direction by
    #   keeping the lava to your left
```

# A collaborative mission

![](collab-task.png)

# An open problem

![](survive.png)

Create an agent that learns how to survive in the game and eventually reach a diamond block.

# Recap

![](control.jpg){height=500px}
