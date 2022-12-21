# Issue 7410: Strings sometimes truncated in notebook mode.

Issue created by migration from Trac.

Original creator: AJonsson

Original creation time: 2009-11-08 10:41:45

Assignee: boothby

Noticed that some strings are truncated when viewed by print. Example:

```
G=graphs.Grid2dGraph(2,9)
S=G.graph6_string()
print S
print G.graph6_string()
```

We expect this to print the same string two times, but when this code is evaluated in the notebook, this is what is printed:

```
QhCGGC`@`_A?c`@`C`@`A?__GC`@`?OC?_G
QhCGGC`@`_A?c`@`C`@`A?__GC`@`?OC?
```

The former is the correct answer, the latter removes the last two characters for some reason.

This only happens in the notebook(tested on alpha.sagenb.org for Ubuntu, Debian and Windows XP, with browsers Firefox and IE). When the code above is run in the terminal without a notebook, it works as expected. Running './sage -notebook' also displays the error. This is all tested with Sage 4.2.


---

Comment by mpatel created at 2009-12-14 17:41:58

This may be fixed by #7666.


---

Comment by mpatel created at 2009-12-14 17:45:28

Possibly related: #7663.


---

Comment by mpatel created at 2010-01-18 04:31:52

#7648's patch (alone!) gives the correct answer.  If I'm right, please close this ticket when #7648 and #7663 merge.


---

Comment by mpatel created at 2010-01-18 04:33:42

#7648's patch (alone!?) gives the correct answer.  If I'm right, please close this ticket when #7648 and #7663 merge.


---

Comment by timdumol created at 2010-01-19 03:12:29

Resolution: duplicate


---

Comment by timdumol created at 2010-01-19 03:12:29

Works with sagenb-0.6.
