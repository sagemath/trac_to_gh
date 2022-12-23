# Issue 2030: hg_[doc|extcode|scripts] docstring is wrong about the repo

Issue created by migration from https://trac.sagemath.org/ticket/2030

Original creator: mabshoff

Original creation time: 2008-02-02 05:17:15

Assignee: tba


```
[05:58] <mabshoff> The docstring for hg_scripts also seems to be wrong, i.e.
[05:58] <mabshoff>         Most commands are directly provided as member functions.  However,
[05:58] <mabshoff>         you can use the full functionality of hg, i.e.,
[05:58] <mabshoff>                 hg_sage("command line arguments")
[05:58] <mabshoff>         is *exactly* the same as typing
[05:58] <mabshoff>                 cd <SAGE_ROOT>/devel/sage/ && hg command line arguments
[05:59] <mabshoff> Same for hg_extcode and hg_doc
```



---

Comment by was created at 2008-02-02 06:26:57


```
22:24 < wstein> #2030 - what's wrong with the hg docstrig?
22:25 < wstein> I couldn't figure that out from the ticket desc.
22:25 < mabshoff> All of them say to cd into $SAGE_LOCAL/deve/sage
22:25 < mabshoff> while the repos are in different places.
22:25 < wstein> I think it's a "generic" docstring.
22:25 < wstein> All the hg_* objects are instances of a generic hg object.
22:25 < mabshoff> Ok, so is it fixable? Or is it invalid?
22:26 < wstein> It should be fixed.
22:26 < wstein> It might be kind of hard / unnatural.
22:26 < wstein> However, if it is really confusing it should be changed.
22:26 < mabshoff> Well, we could list all four repos in the generic docstring.
22:26 < wstein> Or at least the docstring could be made much clearer to emphasize this subtle point.
22:26 < wstein> Exactly
```



---

Comment by mhansen created at 2008-09-19 07:31:16

Changing status from new to assigned.


---

Comment by mhansen created at 2008-09-19 07:31:16

Changing assignee from tba to mhansen.


---

Attachment


---

Comment by mabshoff created at 2008-12-03 11:32:21

Hmmm, the second patch seems to be the same as the first one, but I would guess you accidentally did not post the second one.

Thoughts?

Cheers,

Michael


---

Comment by was created at 2008-12-06 22:36:19

Patch looks good (and is fun/clever).    Maybe Mike just hit submit twice by accident.


---

Comment by mabshoff created at 2008-12-08 11:20:30

Merged in Sage 3.2.2.alpha1


---

Comment by mabshoff created at 2008-12-08 11:20:30

Resolution: fixed
