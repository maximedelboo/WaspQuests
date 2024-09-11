# WaspQuests

This library in meant as an extension to the SLR-T and WaspLib modules for Simba, which are open source frameworks for developing scripts for Oldschool Runescape. It features a framework for developing bots that function in a sequential manner, rather than in a loop, like traditional bots you would develop using the WaspLib and SLR-T modules. The most obvious application of sequential tasks in the game is solving quests, but there exist many other application, like solving clue steps or solving various minigames that are too complex for a singular loop. Besides this, the library also comes with all the quests that are currently solved. To access the currently solved quests, install the library as explained below and run the `QuestSolver.simba` script. 

### Installation
To install this library, download it and place it in the Includes folder in a folder named 'WaspQuests', just like the other libraries.

### Sequential tasks
As said before, this library focusses specifically on solving sequential tasks. This is fundamentally different from most other bots you will see developed for the game. Most bots written for SLR-T and WaspLib are what you call **Finite State Machines (FSM)**, where you can determine the current state of the machine from the given context, and then you enact a certain logic based on that detected state. This library focusses on another type of automation machine, called the **Sequential State Machine**. Rather than only taking the input of the current context and figuring out what to do from there, this machine knows its 'history' so to say and makes decisions based on that. How does this work in practice? The script has a given set of steps to perform, where each step has a clear terminal condition, determining success or failure. Success means your system is ready to perform the next task in the sequence, whereas failure means you can retry the current step and then hopefully reach the terminal condition. 

This last part is very fundamental: the only way to make a sequential system robust is to have steps that are firstly (and obviously) completable from the current state, but also have a clear success condition **and** are repeatable from the beginning of the step to hopefully reach the desired terminal condition.

OSRS quests satisfy these rules by design, because they always have this structure of repeatability and clear success conditions. Therefore, it makes sense to solve quests in this way, rather than trying to use a FSM like with regular bots. The success of quest bots relies on the sucessfull detection of terminal condition steps. If you succeed in this task, your quest bots will be very reliable and robust.

### How does WaspQuests help with creating Sequential State Machines?
WaspQuests has an entire framework to support solving sequential state machines. It does this by providing many basic step types that are very common in quest steps, ranging from solving conversations to interacting with objects, to walking to certain spots or looting items of the ground. Each of these basic step types have their own standard pre-programmed terminal condition, which are obvious for said step type, but you always have the freedom to supply a custom terminal condition and you also have the freedom to add any extra actions to the step that do not influence the terminal condition. If you create a quest in this way where you supply the steps and terminal conditions, the library has the necessary framework to execute all these steps.
