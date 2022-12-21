# Issue 2901: rewrite load_session and save_session to use much better modern techniques (in particular merge the notebook and non-notebook implementations)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-13 01:42:04

Assignee: cwitty

Basically, I know a lot more about how to write Python/Cython code than I used to, so i can write these functions in a way that is (1) vastly better, and (2) will be easily doctested, and (3) work in (almost) the same way in the notebook or command line. 

This depends on the patch up at #2883.  #2883 should be applied then the code attached to this patch, once this patch is accepted.

I've separated this out from #2883, since #2883 really *must* get applied, and the code here should be, but it's really a separate issue, and more nontrivial.


---

Attachment


---

Comment by was created at 2008-04-13 04:02:11

Patch is up.   This basically replaces a bunch of terrifying ugly undocumented miserable scary code (umh, that I wrote) by nice modern well-documented code.


---

Comment by ncalexan created at 2008-04-13 04:08:02

I am not enough of a notebook user to test this thoroughly, but the code is good and the documentation is good.  I say apply immediately!

One quibble: could the module comment make it clear why this is in Cython and not Python?  I think there's a locals() trick at play, but it should be made clear none-the-less.


---

Comment by mabshoff created at 2008-04-13 16:33:03

Ok, I tracked down the issue for the reject of hunk two in worksheet.py. It expects:

```
if t.startswith('load_session'):
    filename = self.hunt_file(filename)
```

But the file contains:

```
filename = self.hunt_file(filename)
```

I am deleting hunk two as is and then apply the rest of the patch.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-13 16:35:19

Merged in Sage 3.0.alpha5


---

Comment by mabshoff created at 2008-04-13 16:35:19

Resolution: fixed
