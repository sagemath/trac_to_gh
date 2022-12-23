# Issue 482: ideals for improving the SAGE tutorial

Issue created by migration from https://trac.sagemath.org/ticket/482

Original creator: was

Original creation time: 2007-08-23 01:25:54

Assignee: was

CC:  mvngu kcrisman

Here are some ideas from a user for improving the SAGE tutorial:

 * 2nd para of abstract: point reader to the official python tutorial for syntax issues
 * section 5 "programming": mention X? and X?? again
 * why doesn't "print?" work?  "attach?"
 * why does att[tab] give me attr and not "attach"?
 * Why does "time for M in L:" break. 
 * Putting cputime(t) alone by itself in the script doesn't print anything.  Why? (Because you have to put "print cputime(t)")
 * In many cases using xrange instead of range can be vastly better
 * nohup sage file.sage > out&   # very useful
 * How to change a .sage file to a .spyx file:
    1. Profile your file.sage file with %prun -- premature optimization is root of all evil
    2. Start with file.py instead of file.sage.
    3. Use "from sage.all import stuff you need" at the top
    4. Consider cdef'ing classes, cdef'ing methods, and cdef'ing variables.


---

Comment by mabshoff created at 2008-09-26 09:17:20

Unless somebody thinks that anything here is still usefull I will close this ticket in the near future. 

Cheers,

Mihcaek


---

Comment by AlexGhitza created at 2008-09-27 02:28:32

Some comments, based on 3.1.3.alpha1:

 * attach? does work (so fixed)
 * print? does not work (so still an issue)
 * att[tab] gives attach, not attr (so fixed)
 * the following works when written on one line:

```
sage: time for i in range(10000): a = i^2
CPU times: user 0.02 s, sys: 0.00 s, total: 0.02 s
Wall time: 0.02 s
```

 * however, I cannot see how to make it work with a for loop spread over several lines

Several of the other suggestions seem more appropriate for the FAQ (on the wiki) than for the tutorial (e.g. the cputime issue, the "use screen instead of nohup").  I think it is a good idea to mention screen somewhere in the tutorial, as well as a section about converting from .sage to .spyx.  I am happy to write a small paragraph about the former, but I'm not the right person for the latter.

I've opened #4204 regarding screen, and someone who agrees that the "sage 2 spyx" section should exist should open a ticket for that.  Maybe there should also be a ticket for "print?".  Then we can close this ancient and somewhat vague ticket.


---

Comment by mabshoff created at 2008-09-27 02:41:04

Replying to [comment:6 AlexGhitza]:
> Someone who agrees that the "sage 2 spyx" section should exist should open a ticket for that.

Isn't that covered by Cython already? What exactly would the goal of that section be?

> Maybe there should also be a ticket for "print?".  Then we can close this ancient and somewhat vague ticket.

Well, that is really a Python issue. I do not recall it ever coming up.

Cheers,

Michael


---

Comment by mvngu created at 2009-06-27 00:43:03

CC'ing myself.


---

Comment by mmezzarobba created at 2015-01-28 15:50:12

See also #9790.
