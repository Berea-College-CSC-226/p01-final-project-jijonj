# CSC226 Final Project

## Instructions

Exclamation Marks indicate action items; you should remove these emoji as you complete/update the items which 
  they accompany. (This means that your final README should have no  ️in it!)

**Author(s)**: Julio Jijon

**Google Doc Link**: https://docs.google.com/document/d/1nyi6LlV4pHktY3rm4gYhRnUOrsHA9QXdYZ3fIJDYF7c/edit?usp=sharing

---

## References 
Throughout this project, you have likely used outside resources. Reference all ideas which are not your own, 
and describe how you integrated the ideas or code into your program. This includes online sources, people who have 
helped you, AI tools you've used, and any other resources that are not solely your own contribution. Update as you go.

---

## Milestone 1: Setup, Planning, Design

**Title**: `Piano.io`

**Purpose**: `A playable piano that can be played with the computer keyboard.`

**Source Assignment(s)**: `chapter_6_suite.py, hw05_funky_functions.py, hw08_genes.py, hw09_upc_classes.py`

**CRC Card(s)**:
  - Create a CRC card for each class that your project will implement.
  - See this link for a sample CRC card and a template to use for your own cards (you will have to make a copy to edit):
    [CRC Card Example](https://docs.google.com/document/d/1JE_3Qmytk_JGztRqkPXWACJwciPH61VCx3idIlBCVFY/edit?usp=sharing)
  - Tables in markdown are not easy, so we suggest saving your CRC card as an image and including the image(s) in the 
    README. You can do this by saving an image in the repository and linking to it. See the sample CRC card below - 
    and REPLACE it with your own:

![CRC Card that I created](image\Screenshot 2024-11-13 212702.png)

**Branches**: This project will **require** effective use of git. 

Each partner should create a branch at the beginning of the project, and stay on this branch (or branches of their 
branch) as they work. When you need to bring each others branches together, do so by merging each other's branches 
into your own, following the process we've discussed in previous assignments: 

```
    Branch 1 name: jijonj
    Branch 2 name: _____________
```
---

## Milestone 2: Code Setup and Issue Queue

Most importantly, keep your issue queue up to date, and focus on your code. 🙃

Reflect on what you’ve done so far. How’s it going? Are you feeling behind/ahead? What are you worried about? 
What has surprised you so far? Describe your general feelings. Be honest with yourself; this section is for you, not me.

```
    the key binds is the thing that is worrying me
```

---

## Milestone 3: Virtual Check-In

Indicate what percentage of the project you have left to complete and how confident you feel. 

**Completion Percentage**: `55%`

**Confidence**: Describe how confident you feel about completing this project, and why. Then, describe some 
  strategies you can employ to increase the likelihood that you'll be successful in completing this project 
  before the deadline.

```
    even though my percentage is not where I want it to be, I still believe I can complete most of the things that I want to implement into the program.
    I believe if that I assign more time into the interface of the program and focus less on more complex code, that I will complete the majority of my program.
```

---

## Milestone 4: Final Code, Presentation, Demo

### User Instructions
In a paragraph, explain how to use your program. Assume the user is starting just after they hit the "Run" button 
in PyCharm. 

```
Once you hit the "Run" button in PyCharm, a window will open with a graphical piano interface. 
You can interact with the piano by pressing the piano keys displayed on the screen or by using your computer's keyboard. 
Each key corresponds to a musical note, and when you press a key, the associated sound will play. 
The program allows you to choose between different piano types (such as "Grand" or "Electric") from the menu bar, which changes the sound of the notes. 
You can also highlight major or minor scales by selecting a root note from the menu, and the program will color the corresponding keys to indicate the notes of the scale.
If you'd like to reset the colors or change the piano type, you can use the buttons at the top of the window. To reset the key colors to their default, click "Reset Key Colors."

```

### Errors and Constraints
Every program has bugs or features that had to be scrapped for time. These bugs should be tracked in the issue queue. 
You should already have a few items in here from the prior weeks. Create a new issue for any undocumented errors and 
deficiencies that remain in your code. Bugs found that aren't acknowledged in the queue will be penalized.

### Reflection
In three to four well-written paragraphs, address the following (at a minimum):
- Why did you select the project that you did?
- How closely did your final project reflect your initial design?
- What did you learn from this process?
- What was the hardest part of the final project?
- What would you do differently next time, knowing what you know now?
- (For partners) How well did you work with your partner? What made it go well? What made it challenging?

```
	I selected the project of creating a piano GUi interface. I selected this project because I love making music and thought that it would be a great learning experience by combining two things that I enjoy. 
	Music has always been a big part of my life, whether through playing instruments or creating sounds, and I’ve always wanted to explore how technology can enhance the musical experience.This project seemed like a perfect way to challenge myself while doing something I truly enjoy.
	
	In terms of how my final project reflected my initial design, I would say that it looked similar to what I first imagined it as. I do wish that it looked a little bit cleaner though since I am a person who loves aesthetics. 
	Besides that,  I did stick to the initial design but also added a couple other features, like changing keyboard types.
	
	Throughout the project, I learned a lot about Tkinter and how to use audio files in Python. Before starting, I had only a basic understanding of graphical user interfaces and hadn’t worked much with playing sound through code. 
	This project gave me the opportunity to explore the various components of Tkinter, such as buttons, labels, and menus. I also gained experience with handling external audio files, learning how to integrate them into a Python program and manage playback with the help of libraries like playsound. 
	
	The hardest part of the project was the keybinds. Everything that I tried was not working correctly. I went through the internet for help but had no luck. However, Dr. Heggen was able to correctly implement one keybind and help me with handling multiple key presses at one time. 
	Overall that was the hardest part of the entire project. 
	
	Knowing what I know now, I would do more research on Tkinter before starting the actual interface. I remember when I first started coding the program, I was confused about the implementation of the buttons.
	I would also figure out which audio Python library would best suit my program since I didn’t take a lot of time researching which library would be the best for my program. 


```