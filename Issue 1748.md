# Issue 1748: Passing the ipython argument '-wthread' at startup

Issue created by migration from https://trac.sagemath.org/ticket/1748

Original creator: jsp

Original creation time: 2008-01-10 15:14:41

Assignee: was

From the thread in gg:sage-devel: Enthought mayavi2 as a library


```
My question: Is there a better way to pass the argument "-wthread" to ipython?
And than run the real sage.

What I do is a kind of cheating: ipython comes back with the prompt
sage:

So it looks like sage but it isn't.

Jaap

```




```
Yes, the issue is really that I explained myself poorly to Jaap.  He's running

import IPython
IPython.Shell.IPShellWX().mainloop()

Inside an already started Sage session.  But at the exit of that
mainloop(), ipython will tear down the threading support (absolutely
necessary for WX to work without blocking the interactive console).
That mainloop is hooked into the WX event loop, so it can't really be
restarted.

The solution is to have Sage start ipython with the wthread option, if
you want full Sage support.  As a starter, you can test this. Make a
little file that's simply

#!/path/to/sage/python
import IPython
IPython.Shell.IPShellWX().mainloop()


make it executable, and run it *standalone* in a sage-sh configured
shell.  This standalone ipython is equivalent to running

ipython -wthread

and will simply exit at the end.  If that works and closes without
crashing, then someone more familiar than myself with how sage starts
itself can then offer an option for sage to fire up ipython with
'-wthread' at startup.  This will ensure that the threads cleanup only
happens when sage itself exits, not in the middle of the enclosing
Sage session.

My originally incomplete explanation led Jaap to have a main event
loop inside another one.  That's always bad news.

I hope this is now clearer.

Cheers,

f

```


This worked for me.


---

Comment by cwitty created at 2008-03-01 01:35:30

Changing assignee from was to cwitty.


---

Comment by cwitty created at 2008-03-01 01:35:30

Changing status from new to assigned.


---

Comment by cwitty created at 2008-03-01 01:35:30

I can think of a couple of ways to handle this.  One is for sage (specifically, the sage-sage script) to automatically detect whether wxPython has been installed, and if so, automatically start ipython with the -wthread argument.  Another is to have "sage -wthread" pass the thread argument on to ipython.

I'm willing to create either of these patches.  I would prefer the former, just because it's simpler for the user, as long as the -wthread argument has no bad side effects.  I've been running with -wthread myself for a few weeks now (hardcoded by editing sage-sage to add -wthread unconditionally), and have noticed no problems; but that's just one user and one machine.

Any thoughts on which option is better?


---

Attachment


---

Comment by cwitty created at 2008-03-01 20:02:12

This patch makes "sage -wthread" pass the -wthread argument to ipython.  (It also adds support for -gthread, -qthread, -q4thread, and -pylab.)


---

Comment by mabshoff created at 2008-03-01 21:28:41

Patch looks good to me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-01 21:29:04

Resolution: fixed


---

Comment by mabshoff created at 2008-03-01 21:29:04

Merged in Sage 2.10.3.rc1
