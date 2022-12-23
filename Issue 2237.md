# Issue 2237: plot options for turning off randomness in sampling x data and turning off adaptive plotting

Issue created by migration from https://trac.sagemath.org/ticket/2237

Original creator: jason

Original creation time: 2008-02-20 22:56:44

Assignee: was

In doing animations like in http://groups.google.com/group/sage-support/browse_thread/thread/8e2edf8165e9ded2

the adaptive plotting and the randomness added to the x-sample points is very annoying, creating a wiggling graph in the animation.  We ought to have options to plot to turn these things off so that we can get the same graph over and over again.


---

Comment by cwitty created at 2008-02-21 02:19:37

Another idea would be for animate to use the same random offsets in each plot in the animation.


---

Comment by was created at 2008-02-21 06:58:11

See trac #2244 that implements an option to turn off randomness in plotting.

This ticket should likely be marked as a dupe.


---

Comment by was created at 2008-02-21 06:58:11

Resolution: duplicate
