# Issue 6412: [with patch, needs review] Getting Singular's cputime does not work with negative argument

Issue created by migration from https://trac.sagemath.org/ticket/6412

Original creator: SimonKing

Original creation time: 2009-06-25 17:53:48

Assignee: SimonKing

CC:  malb

Keywords: cputime Singular

In some application, I accidentally had a negative argument `t` to `singular.cputime(t)`. Actually I don't know how this came, but anyway: This lead to a Traceback, since `t` is inserted into a string: 'timer-%d'%t

Of coure, if t has a minus sign, Singular complains.
Easy solution: Put brackets aroung %d.

Without the patch:

```
sage: singular.cputime(-7)
---------------------------------------------------------------------------
RuntimeError                              Traceback (most recent call last)

/home/SimonKing/.sage/temp/sage.math.washington.edu/18981/_home_SimonKing__sage_init_sage_0.py in <module>()

/usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/singular.pyc in cputime(self, t)
    677         """
    678         if t:
--> 679             return float(self.eval('timer-%d'%(int(1000*t))))/1000.0
    680         else:
    681             return float(self.eval('timer'))/1000.0

/usr/local/sage/local/lib/python2.5/site-packages/sage/interfaces/singular.pyc in eval(self, x, allow_semicolon, strip, **kwds)
    547
    548         if s.find("error") != -1 or s.find("Segment fault") != -1:
--> 549             raise RuntimeError, 'Singular error:\n%s'%s
    550
    551         if get_verbose() > 0:

RuntimeError: Singular error:
   ? --(`int`) failed
   ? expected --(`identifier`)
   ? error occurred in STDIN line 19: `timer--7000;`
```


With the patch:

```
sage: singular.cputime(-70)
70.060000000000002
```


It will certainly hardly ever occur that people call the cputime with a negative starting point, but why not fix a corner case?



---

Comment by SimonKing created at 2009-06-25 17:54:23

Allow negative arguments for singular.cputime()


---

Attachment

Looks good.


---

Comment by boothby created at 2009-06-26 17:43:23

Resolution: fixed
