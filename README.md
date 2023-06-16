# CS160PythonProjects
This repository was created for my high school computer science class in 2023. It was made to keep track of the code I wrote throughout the entirety of the course.

## Description
Python was the language utlized most heavily within these projects, however minor C++ was used when [coding in Arduino](https://github.com/pyanpyan/CS160PythonProjects/blob/main/sketch_may2a.ino). 
* The files ending in Flag.py were simple constructions of country flags that I created with turtle. These were some of the very first creations I made in python, and were also what helped me gain a better understanding of for loops and how to communicate with computers on a basic level.
* [RockPaperScissorsAI.py](https://github.com/pyanpyan/CS160PythonProjects/blob/main/RockPaperScissorsAI.py) contains a very simple AI that plays rock paper scissors with the user. It "learns" by adding whichever option it beats you with to the list it pulls its options from. For example, if the computer beats you with paper, the list becomes ["rock", "paper", "scissors", "paper"]. The randomization method shuffles the options like one would shuffle a deck of cards, however it becomes very manual when written in python. As of June 2023, it is the most advanced project I have made with python thus far. 
* [sketch_may2a.ino](https://github.com/pyanpyan/CS160PythonProjects/blob/main/sketch_may2a.ino) contains code for an Arduino I programmed for a simple breadboard project. To summarize, the breadboard contained three LEDs, one potentiometer, and an Arduino Nano. The goal was to get the potentiometer to gradually turn on each LED as I turned the dial to the right. 

## Dependencies
Arduino IDE is required to run [sketch_may2a.ino](https://github.com/pyanpyan/CS160PythonProjects/blob/main/sketch_may2a.ino) along with proper breadboard configuration. The rest of the files simply require a python instllation and a text editor to run. 
