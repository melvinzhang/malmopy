AI concepts with Python and Malmo

Target audience is 15 - 18 years old with basic python knowledge

Duration: 5 sessions, each 2 hours

Prior knowledge assumed: primitive data types, list, function, concept of
object, loop, conditionals, string manipulation

Should not require: OOP

Put malmo on Desktop for ease of starting Minecraft

Session 1
  Concept of an agent
    sense the environment
    make decision
    act on the environment
    repeat
  Motivation: controlling a robot interacting with the world
    self-driving cars, vacuum cleaner robot, etc
  Introduction to Malmo
    https://www.microsoft.com/en-us/research/project/project-malmo/
    https://www.youtube.com/watch?v=KkVj_ddseO8
  Simple exercise to create an agent
    tutorial_4 - reach the diamond block in the center
    tutorial_5 - reach the diamond block, avoid the lava

Session 2
  Line following task
    related to self driving cars, they need to drive within the lane
    follow the earth, everywhere else is lava

Session 3
  Exploring a maze
    search and rescue mission
    tutorial_7
    implement left hand rule
    what are the limitations of left hand rule?
  Exploring an open area to collect diamonds
    systematic exploration
    open area with some obstacles inside
    motivation: vacuum cleaner robot

Session 4
   

Session 5


-----

continuous movement commands
  move [-1,1]
    -1 is backwards
  turn [-1,1]
    -1 is full speed left
  pitch [-1,1]
    -1 pitch camera upwards
  jump 1/0 
    1 starts jumping, 0 stops
  crouch 1/0
  attach 1/0
  use 1/0

/time set 1000 
  1000 is start of day
  13000 is start of sunset

-----

Collaborative AI challenge in Malmo
https://www.microsoft.com/en-us/research/academic-program/collaborative-ai-challenge/

AI Course
http://home.wlu.edu/~levys/courses/cs315f2007/
http://homepage.cs.uri.edu/faculty/hamel/courses/2015/spring2015/csc481/

CS 175: Projects in AI in Minecraft
http://sameersingh.org/courses/aiproj/sp17/index.html

AzureCraft AI
https://blogs.msdn.microsoft.com/uk_faculty_connection/2017/05/23/azure-craft-a-hack-for-kids-and-parents-to-learn-ai-programming/
1 - 1.30: Lab 2 - Automating Minecraft with Python
1.30 - 2.15: Lab 3 - First steps in Malmo
2.15 - 3.00: Lab 4 - Building and updating a Malmo map
3.00 - 4.00: Lab 5 - Putting it all together, walking a Maze faster with rewards!

NASA's lesson plan for teaching robotics
https://www.nasa.gov/audience/foreducators/robotics/lessonplans/index.html

Reeborg's world (web-based 2D robot simulator, allows both text and blocks)
http://reeborg.ca
