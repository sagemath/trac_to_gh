# Issue 47: make it easy to turn off preparser

Issue created by migration from Trac.

Original creator: anonymous

Original creation time: 2006-09-13 09:26:37

Assignee: somebody

It's "from sage.all import *".  But then I'm being dumb, since that
just turns the preparser back on. 

The preparser in SAGE is activated in misc/interpreter.py in this line:

# Rebind this to be the new IPython prefilter:
InteractiveShell.prefilter = sage_prefilter

If you comment that one line out, then restart SAGE (with sage -br) you'll 
get a SAGE that has no preparsing at all by default.  Yet all the library
code
should work fine and you have the sage library functions available by
default.

That sounds reasonable. I undid the preparser.py change and commented out the
suggested line in interpreter.py. With a few basic tests everything seems OK.

I guess the default int is now a Python int, but that is okay for what I'm working on
right now. 

Thanks for sorting this out.


---

Comment by mabshoff created at 2008-03-16 07:53:05

Resolution: fixed


---

Comment by mabshoff created at 2008-03-16 07:53:05

This has been possible for a while now:

```
sage: preparser(False)
sage: 2^2
0
sage: preparser(True)
sage: 2^2
4
```

Hence I am closing the ticket.

Cheers,

Michael
