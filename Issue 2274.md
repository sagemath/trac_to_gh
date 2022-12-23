# Issue 2274: guava->python, 1

Issue created by migration from https://trac.sagemath.org/ticket/2274

Original creator: wdj

Original creation time: 2008-02-23 02:50:35

Assignee: rlm

For various reasons, ease of maintenance among others, the coding theory functions in SAGE which are GAP wrappers for GUAVA functions will be moved over to pure Python/SAGE. This is just a "first installment". In this patch (to be attached once the testall suite is completed)

HammingCode, CyclicCode, dual_code, put_standard_form,

are moved over and the simple function LinearCodeFromCheckMatrix is added.
The amusing utility function "permutation_action" is needed, which provides a
(left) action of SymmetricGroup(n) on a list/vector/sequence/matrix of
length n.


---

Comment by wdj created at 2008-02-23 14:46:10

The bundle was too large to post for some reason. It is at
http://sage.math.washington.edu/home/wdj/patches/coding_23-02-2008.hg
Modified were the files 
all.py (moved HammingCode from guava to code_constructions, etc)
linear_code.py (rewrote standard_form and dual_code in python, so they do not call GAP)
guava.py (deleted HammingCode and CyclicCode)
code_constructions.py (added pure python functions HammingCode, CyclicCodeFromGeneratorPolynomial, CyclicCodeFromCheckPolynomial, LinearCodeFromCheckMatrix, and some utility functions)


---

Comment by wdj created at 2008-02-23 14:48:52

I'm sorry, I should add that this passes sage -testall, except for the file const.tex. I'll fix this separately. (There is no way I know of to create a mercurial bundle containing both code patches and doc fixes.)


---

Comment by mabshoff created at 2008-02-23 15:01:15

I am dubious about any bundle larger than a couple dozen kilobytes, especially for something like this. In comparison David Roe's padics bundle topped out at about 150kb with a hundred+ commits. I will have a look, but it sounds like you need to do this again with a clean 2.10.2 and your code applied.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-23 15:03:29

Replying to [comment:2 wdj]:
> I'm sorry, I should add that this passes sage -testall, except for the file const.tex. I'll fix this separately. (There is no way I know of to create a mercurial bundle containing both code patches and doc fixes.)

Since the code for documentation and the sage library are in different repos you cannot submit a bundle that contains changesets from both repos. I would also plead you once more to use the export command, if needed via the command line, i.e. `hg export $CHANGESET` because there are clearly some issues with the way you do bundle :(

Cheers,

Michael


---

Comment by wdj created at 2008-02-23 15:11:50

I don't know how to export a doc bundle (and I've tried many different ways). I'm attaching the patch, just in case.


---

Attachment


---

Comment by wdj created at 2008-02-23 15:18:34

I just figured out how to export a doc bundle to a patch. It's actually obvious and easy, so I don't know what the problem was before. It is attached too. 

Can you tell me if these are acceptable or if they need to be redone?


---

Attachment


---

Comment by mabshoff created at 2008-02-23 15:20:20

Replying to [comment:5 wdj]:
> I don't know how to export a doc bundle (and I've tried many different ways). I'm attaching the patch, just in case.

The patch looks good and does apply cleanly against my 2.10.3.alpha0. That isn't a formal review, just a technical observation. The reason the bundle is so large because William hasn't pushed out the changes from 2.10.2 to the repos and it contains every commit from 2.10.1 onward. So in the end it is all William's fault :)

To export the doc patch go into `$SAGE_ROOT/devel/doc` and us hg to do an `hg export tip` (at least for the last commit). You can do the same using Sage's hg interface to the doc repo, i.e. do `hg_doc.log()` to see the changelog.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-23 15:22:17

Replying to [comment:6 wdj]:
> I just figured out how to export a doc bundle to a patch. It's actually obvious and easy, so I don't know what the problem was before. It is attached too. 
> 
> Can you tell me if these are acceptable or if they need to be redone?

I can now see that we crossed paths while I wrote the answer to your initial question. Both patches look correct and apply cleanly against my current repo. So once they get positively reviewed (by rlm?) they can go in.

Cheers,

Michael


---

Comment by rlm created at 2008-02-24 19:21:14

- I noticed that you changed many instances of `from blah import *` to `from blah import one_specific_thing`. Awesome!
- Since you did testall, I just tested the `sage/coding` module, and everything seems fine.
- I strongly support the move from Guava to Python for this functionality. Tom Boothby and I are going to start working on something similar for permutation groups (not just elements).


---

Comment by mabshoff created at 2008-02-25 02:29:34

Resolution: fixed


---

Comment by mabshoff created at 2008-02-25 02:29:34

Both patches merged in Sage 2.10.3.alpha0
