# Issue 2655: [with patch, needs review] Cython circular cdef imports

Issue created by migration from https://trac.sagemath.org/ticket/2655

Original creator: gfurnish

Original creation time: 2008-03-23 16:09:37

Assignee: gfurnish

CC:  robertwb

This patch allows circular cdef imports in Cython.
It also modifies cython exceptions to also print the line number in the C code.
Furthermore the patch begins modifications to seperate module creation from module global execution, which will potentially be useful as Cython starts to employ more optimizations.   
This patch is required for the symbolics overhaul.


---

Attachment


---

Comment by gfurnish created at 2008-03-23 16:10:46

Changing status from new to assigned.


---

Attachment

Do not apply 9612.patch, apply 9612.2 patch instead.  It removed several debug printf statements.


---

Attachment

New patch, apply this one *only*.  Removes more commented code.


---

Comment by gfurnish created at 2008-03-23 18:38:43

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2008-03-23 19:13:05

Mhh, shouldn't this go to the Cython mailing list?

Cheers,

Michael


---

Comment by robertwb created at 2008-03-26 11:19:18

I am looking into this, but so far it looks good.


---

Comment by was created at 2008-03-28 06:58:26

Could you post some samples here that don't work with Cython now, but do with your patch applied?


---

Comment by robertwb created at 2008-03-30 11:11:08

This wasn't near as scary of a patch as I had first supposed, good work. I merged it into Cython.


---

Attachment

Fix for clear.pyx issue


---

Comment by robertwb created at 2008-04-04 05:00:09

Merged upstream.


---

Comment by gfurnish created at 2008-04-04 19:33:59

Fixes doctests for cython 0.9.6.13


---

Attachment


```
This has the new repository hierarchy, so you won't be able to pull
from the online -devel ones. If no one reports any bugs in then I
will release tomorrow.

http://sage.math.washington.edu/home/robertwb/cython/

- Robert
```



---

Comment by mabshoff created at 2008-04-04 20:28:07

The spkg at

http://sage.math.washington.edu/home/robertwb/cython/cython-0.9.6.13.spkg

contains a BUILD directory. I removed it and got the size down to about 100kb over 0.9.6.12.

Cheers,

Michael


---

Comment by robertwb created at 2008-04-04 20:32:15

Thanks. This will be removed before the final release.


---

Comment by mabshoff created at 2008-04-04 21:24:00

Resolution: fixed


---

Comment by mabshoff created at 2008-04-04 21:24:00

Merged in Sage 3.0.alpha1


---

Comment by robertwb created at 2008-04-04 22:43:54

Just to confirm, does this mean in the cython-0.9.6.13.spkg from above (minus the build directory) so I needn't make a separate ticket for the new Cython?


---

Comment by mabshoff created at 2008-04-04 22:49:06

Replying to [comment:15 robertwb]:
> Just to confirm, does this mean in the cython-0.9.6.13.spkg from above (minus the build directory) so I needn't make a separate ticket for the new Cython? 

Correct. The ticket's credit and description reflects this.

Cheers,

Michael


---

Comment by robertwb created at 2008-04-08 08:48:08

The spkg up at 

http://sage.math.washington.edu/home/robertwb/cython/

turns c line numbers back on, and has a minor fix for external class declarations (which didn't show up in the Sage codebase, but did for other poeple).


---

Comment by mabshoff created at 2008-04-08 09:22:59

Hi Robert,

I have merged the latest (April 8th) cython.spkg. I saw the message on the Cython mailing list, so I am not surprised that it did come. But I would recommend opening [or reopening] a ticket and also bumping the version number to p0 to reflect this change.

Cheers,

Michael
