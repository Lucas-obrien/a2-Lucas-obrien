[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/9EhCNjHp)
# CP1404 Assignment 2 - Song List 2.0 by Lucas O'Brien

A Python project with GUI and Console programs that (re)use classes to manage a list of songs to learn.

# Project Reflection

## 1. How long did the entire project (assignment 2) take you?

The entire project took around 3 days, coding the classes and reworking assignment 1 took the least amount of time; around three to four hours.
Constructing the app took the longest, around eight hours. After completing the bulk of the project on the 12/11, I spent most of my time cleaning and updating DRY code

## 2. What are you most satisfied with?

Being able to use classes effectively in my code. 
Specifically the second part of the assignment, adapting the first assignment to the class.
Changing the code to work in a cleaner way gave me a clear view of how classes work and why they should be used.

## 3. What are you least satisfied with?

I was least satisfied with some of the coding structures, the functions with error checking feels wrong to use,
given that a try/except could be used in place of repeating if statements.

## 4. What worked well in your development process?

Repeated testing of code, going step by step until the correct outputs were achieved.
Iterating through each problem allowed me to focus on errors and incorrect code as I went, rather than building the whole app and then forcing it to work afterward.

## 5. What about your process could be improved the next time you do a project like this?

My commits were lacking, I had tunnel vision during building the app; I had completed the entire build without committing at several milestones.
To fix this, I would set more TODOs in the code to remind myself to stop, commit, then continue.

## 6. Describe what learning resources you used and how you used them.

I frequently referenced the CP1404 slides, particularly the Kivy Demos. 
I believe this resource is critical to completing this project, learning Kivy in a short period of time in addition to regular class work would be near impossible.
I also made use of previous practicals, given that all of what is required in the assignment is taught in class, searching through my own practical work to find relevant code structures made the assignment significantly easier.

## 7. Describe the main challenges or obstacles you faced and how you overcame them.

The biggest hurdle I faced during the assignment was how to associate a button to a specific object. 
This was the challenge that took the longest time to figure out. After going through the majority of the Kivy demos, I saw that the guitars_app.py had what I needed.
In this demo I saw that you could create any variable as you would as normal and assign a value to it (in the demo, temp_button.guitar = guitar was used).
After I found this, testing it by assigning it the song object essentially broke the wall I was stuck at and the remainder of the project was completed within a few hours.

## 8. Briefly describe your experience using classes and if/how they improved your code.

I definitely can see how classes can improve your code, the readability and re-usability was noticeable during the rework of assignment 1.
There is a significant decrease in the length of code needed once the csv data was converted into a song object.
Once the object was initialised, I no longer needed to reference the index of values, I could just call the specific value that I wanted.
