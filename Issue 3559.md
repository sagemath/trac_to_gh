# Issue 3559: [with patch; needs review] sage timeup script

Issue created by migration from https://trac.sagemath.org/ticket/3559

Original creator: was

Original creation time: 2008-07-06 08:20:37

Assignee: tbd

Credit goes to Andrew Dalke, Mike Hansen, and William Stein (a little)


---

Attachment


---

Comment by mabshoff created at 2008-07-06 10:58:52

Changing keywords from "" to "editor_mhansen".


---

Comment by mabshoff created at 2008-07-06 10:58:52

Since Mike is getting the author's permission so we can include this I am making him editor. Feel free to decline :)

Cheers,

Michael


---

Comment by mhansen created at 2008-07-06 17:02:11


```
    I was wondering if you'd be
    willing to release your code under a GPL compatible license so that we
    can include it with Sage to do regression testing with every release.


Certainly.

If you believe that

 This work written by Andrew Dalke and released into the public domain
 in 2008.  No copyright protection is asserted.

is sufficient then there you go.  Else

 Copyright Andrew Dalke, 2008. This software is provided 'as-is', without
 any express or implied warranty. In no event will the author be held
 liable for any damages arising from the use of this software.

 Permission is granted to anyone to use this software for any purpose,
 including commercial applications, and to alter it and redistribute it
 freely, subject to no restriction.

I honestly think that the code needs enough modifications to be usable in SAGE or another tool that nothing of my code will remain.

Now if had access to the code I wrote for a client, that would be much cooler.  It saved the imports to a format that kcachegrind could visualize.  :)

Cheers,


                               Andrew
                               dalke@dalkescientific.com
```



---

Attachment


---

Comment by mabshoff created at 2008-07-06 17:18:06

Positive review. I think this is a nice start and will greatly help to keep the import time down.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-06 18:11:58

Merged both patches in Sage 3.0.4.alpha2


---

Comment by mabshoff created at 2008-07-06 18:11:58

Resolution: fixed
