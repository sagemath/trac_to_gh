# Issue 4454: bug in preparser

Issue created by migration from https://trac.sagemath.org/ticket/4454

Original creator: ggrafendorfer

Original creation time: 2008-11-06 15:25:38

Assignee: cwitty

CC:  robertwb boothby

sage 3.1.4 on a 32-bit core duo

consider a file 'time.sage' with the following content:

def func(time = 5):
    time = RDF(time)
    return time

loading this file then yields following error:

sage: load time.sage
------------------------------------------------------------
   File "/home/georg/.sage/temp/HILBERT/4119/_home_georg_Daten_Sync_Software_Sage_Experimente_time_time_sage_0.py", line 7
     __time__=misc.cputime(); __wall__=misc.walltime();  = RDF(time); print     "Time: CPU %.2f s, Wall: %.2f s"%(misc.cputime(__time__), misc.walltime(__wall__))
                                                         ^
SyntaxError: invalid syntax

WARNING: Failure executing file: </home/georg/.sage/temp/HILBERT/4119/_home_georg_Daten_Sync_Software_Sage_Experimente_time_time_sage_0.py>


If one quits the space between 'time' and '=' in the second line of 'time.sage' it works as expected.
Defining this function directly on the sage prompt also works as expected.


---

Comment by ggrafendorfer created at 2008-11-06 15:29:42

I don't know why in the final view it looks like this, of course the 'return time' part of the second line of the function definition should be a separate line.


---

Comment by mabshoff created at 2008-11-06 22:04:56

Changing priority from minor to major.


---

Comment by mabshoff created at 2008-11-06 22:06:08

Hi,

you need to use "`" and "`" to get verbatim output - see also the main trac page. It would also be useful to have a more descriptive summary since as is "bug in preparser" is not very detailed :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-11 07:53:51

This is still a problem despite numerous preparser bugs being fixed during SD 12:

```
sage: load time.sage
------------------------------------------------------------
   File "/scratch/mabshoff/dot_sage/temp/sage.math.washington.edu/4348/_scratch_mabshoff_sage_3_3_rc0_time_sage_1.py", line 8
     __time__=misc.cputime(); __wall__=misc.walltime();  = RDF(time); print         "Time: CPU %.2f s, Wall: %.2f s"%(misc.cputime(__time__), misc.walltime(__wall__))
                                                         ^
SyntaxError: invalid syntax

WARNING: Failure executing file: </scratch/mabshoff/dot_sage/temp/sage.math.washington.edu/4348/_scratch_mabshoff_sage_3_3_rc0_time_sage_1.py>
```



---

Comment by robertwb created at 2009-02-11 07:57:00

Have you verified that this is not taken care of by #5106?


---

Comment by mhansen created at 2009-06-04 23:35:27

This has been fixed by #5106:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: load time.sage
sage: func()
5.0
sage: func(10)
10.0
```



---

Comment by mhansen created at 2009-06-04 23:35:27

Resolution: invalid
