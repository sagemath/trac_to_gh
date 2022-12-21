# Issue 2365: [with patch, needs review] with sage -wthread, attach runs code in wrong thread on subsequent loads

Issue created by migration from Trac.

Original creator: cwitty

Original creation time: 2008-03-02 00:51:38

Assignee: was

This is a tricky bug to explain... the description of the bug is a lot more complicated than the patch, and reproducing the bug requires wxPython.

With "sage -wthread", ipython creates and deals with multiple Python threads.  All the Sage code (along with all wxPython code) runs in the main, original thread; ipython creates its own new thread to deal with the command line interaction (the "sage: " prompt).  When you type in a command, all the command line editing, preparsing, etc., runs in this new ipython thread; then the final command is shipped over to the main thread for execution.

This interacts poorly with the current implementation of Sage's "attach" command.  When you attach a file, it is loaded in the main thread.  When you then modify the file (and run the preparser to trigger a reload of the file, for example by simply pressing Enter), the file is loaded in the ipython command-line-processing thread.

For most code, this makes no difference... it doesn't matter what thread is used to load the code.  However, wxPython code must run in the main thread, so if the attached file runs wxPython code in the ipython thread, bad things will happen (often, perhaps always, Sage will crash).

You can test that the combination of "sage -wthread" and attach does the wrong thing as follows:

Create a file attach-thread.py with the following contents:

```
import thread
print "Current thread is: %d" % thread.get_ident()
```


Then run "sage -wthread".  You can then run a session much like the following:

```
sage: attach attach-thread.py
Current thread is: -1210038080
sage: !touch attach-thread.py
sage: 
Current thread is: -1246987376
sage: thread.get_ident()
-1210038080
```

Your thread identifiers will be different; the important thing is that the first and third numbers are the same, and the second is different, showing the bug.  Without -wthread, the bug does not appear.

My patch ensures that when an attached file is changed, the command to reload the file gets shipped across to the main thread and executed there, rather than being executed in the ipython thread.  Here's what the above session looks like after my patch (still with -wthread):

```
sage: attach attach-thread.py
Current thread is: -1210521408
sage: !touch attach-thread.py
sage: 
Current thread is: -1210521408
sage: thread.get_ident()
-1210521408
```

All three numbers are the same, so the bug is gone.

This patch does not have a doctest; the above process for replicating the bug seems too difficult to automate.  Sorry!


---

Attachment

This seems good.


---

Comment by mabshoff created at 2008-03-03 12:25:59

Merged in Sage 2.10.3.rc1. This patch is low risk for people who do not use the thread option, so I am also fine with it.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-03 12:25:59

Resolution: fixed
