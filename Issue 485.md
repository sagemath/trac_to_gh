# Issue 485: SAGElite -- release a first version of SAGE Lite

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-08-23 18:21:02

Assignee: was

CC:  was

SAGElite will be a pure-python package that is kept completely and automatically in sync with the main SAGE distribution.  The code will not be separate.  When releasing a new version of SAGE, the script spkg-distlite will be run in the SAGE_ROOT/devel/sage/sage directory, resulting in a pure-python sagelite package, which will also be posted at the sage website.  This will have some
sort of automated testing, though I'm not sure what at present.

Components that will initially be in SAGElite:
  1. The SAGE interfaces (to gap, pari, etc).
  2. The SAGE notebook.

Components that may eventually be added to SAGElite:
  1. DSage
  2. Plotting
  3. Calculus (depend on the user having Maxima installed)
  
Specific tasks that remain:
  1. package data or otherwise for the data/extcode/notebook stuff. 
  2. get notebook to actually work (issue with object loading and saving)
 


---

Comment by was created at 2007-08-23 19:49:48

It would also be a great idea to make a stand-alone version of SAGE-lite, which
includes just the spkg's needed to build SAGE lite, but doesn't depend on the user
having Python installed on their computer.  This would be something that is vastly
easier and faster to build from source than current SAGE, would be easier to port
to Windows, etc.


---

Comment by pdehaye created at 2007-08-23 21:38:46

how would the version numbering work? exactly in parallel with sage? if it's all automatically released, it would have to, no?


---

Comment by jason created at 2009-11-19 22:43:51

What's the status on this?


---

Comment by was created at 2009-11-19 22:49:30

I think that sagenb *is* sagelite, as far as I'm concerned.  So this closes it: http://nb.sagemath.org/


---

Comment by was created at 2009-11-19 22:49:30

Resolution: fixed
