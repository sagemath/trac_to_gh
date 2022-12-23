# Issue 315: wizard database and interface for notebook and commandline

Issue created by migration from https://trac.sagemath.org/ticket/315

Original creator: TimothyClemans

Original creation time: 2007-03-10 23:42:32

Assignee: was

When the new calculus package comes online, it would be nice if there were wizards that could me through what I wanted to do. For the commandline maybe there could say a wizard for starting up the notebook. If I used it, I would be asked different questions based on do I want a public notebook, advanced, simple, name, description, etc. Once I answered all the questions, the wizard would return me back to the commandline and have all the code I need ready for me to execute. This wizard interface would have a menu that I could call using "WizMode()". In fact there could even a special SAGE commandline interface from the start based on a config file in the user's home directory. So I if I had the config file saying I wanted this, then I would see a greeting followed by a nice menu. This would be good for me if say I wanted to let a friend, who didn't know anything about programming or SAGE, use my laptop to work on their homework. Also it could be nice to use the wizard interface as a tutorial system since the user would see the output code. 


---

Comment by was created at 2007-03-21 23:08:36

Changing assignee from was to TimothyClemens.


---

Comment by was created at 2007-03-21 23:10:45

I think this is basically just a Python question.  One can write interactive Python programs
that use SAGE as a library...
