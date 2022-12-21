# Issue 2183: scipy and special functions

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2008-02-16 23:14:55

Assignee: was

CC:  ncalexan

In the thread "[sage-support] Bessel argument order"
http://blog.gmane.org/gmane.comp.mathematics.sage.support/page=20
Micheal suggested replacing all "#random's" by "..." and
William seconded this. Then William suggested adding the scip option to
the functions implemented. This has been done as well.
The patch passes "sage -t" has some examples added and some
docstring typos fixed. The patch is attached.


---

Attachment


---

Comment by mabshoff created at 2008-02-16 23:26:51

David,

please export a single patch next time since this is a single commit only. It makes review on the command line easier and in case of rejects makes it possible to edit the patch by hand.

You should also add an indicator like "[with patch|bundle, needs review]" so that people are aware that there is a patch.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-16 23:27:52

There is also no reason not to still try to get this into 2.10.2, so for something as simple as this it is always recommended to assign against the current milestone.

Cheers,

Michael


---

Comment by ncalexan created at 2008-02-18 19:48:15

There are some typos in the opening docstring.

The tests don't always make it clear that scipy agrees with the previous implementations, which is what I was looking for.

I say apply.


---

Comment by mabshoff created at 2008-02-18 20:42:58

I see two typos in the initial docstring and will fix those after I apply the bundle.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-18 20:46:22

Resolution: fixed


---

Comment by mabshoff created at 2008-02-18 20:46:22

Merged in Sage 2.10.2.alpha1
