# Issue 3529: ATLAS.spkg: reapply the PowerPC detection fix

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-06-28 10:07:49

Assignee: mabshoff


```
Maybe I advanced a little in this problem. I found that your patch 
ATLAS-3.8.1-ppc-g4-7447-detect-fix.patch is not applied in sage. After 
applying this patch, it can detect architecture PPCG4. Here are the 
result with atlas-3.8.1.p2 in 3.0.4.alpha1:
---------------------------------------
OS configured as Linux (1)

Assembly configured as GAS_PPC (4)

Bad VECFLAG value=0, ierr=0, ln2='VECFLAG=0
'

Vector ISA Extension configured as   (0,0)

Architecture configured as  PPCG4 (4)

Bad CPU MHZ value=0, ierr=0, ln2='CPU MHZ=0
'

Clock rate configured as 0Mhz
-----------------------------------

and

-----------------------------
real    62m10.407s
user    47m47.740s
sys     4m38.025s
Successfully installed atlas-3.8.1.p2
-------------------------------

For comparison (atlas-3.8.1p1 in sage-3.0.3) I need long time:
-------------------------
real    450m35.791s
user    371m58.504s
sys     16m33.417s
Successfully installed atlas-3.8.1.p1
-----------------------------------------

Thanks
Bin 
```



---

Comment by mabshoff created at 2008-06-28 10:07:56

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-07-07 05:31:38

The spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.0.4/alpha2/atlas-3.8.1.p3.spkg

has a patched archinfo.c which now properly detects the G4 in question.

Cheers,

Michael


---

Comment by was created at 2008-07-07 05:42:52

positive review as explained in irc.


---

Comment by mabshoff created at 2008-07-07 05:46:43

Merged in Sage 3.0.4.alpha2


---

Comment by mabshoff created at 2008-07-07 05:46:43

Resolution: fixed
