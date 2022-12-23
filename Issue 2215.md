# Issue 2215: if p is a permutation, matrix(p) should call p.to_matrix()

Issue created by migration from https://trac.sagemath.org/ticket/2215

Original creator: jason

Original creation time: 2008-02-19 22:37:39

Assignee: was

CC:  sage-combinat

it seems like matrix(thing) should usually work if we can think of "thing" as a matrix.  In this case, we even already have a p.to_matrix() function.


---

Comment by mhansen created at 2008-02-20 03:45:49

The fix to this would be to add a _matrix_ method to Permutation_class ( which can call .to_matrix() )


---

Comment by mhansen created at 2008-02-20 03:45:49

Changing component from algebraic geometry to combinatorics.


---

Comment by mhansen created at 2008-02-20 03:45:49

Changing status from new to assigned.


---

Comment by mhansen created at 2008-02-20 03:45:49

Changing priority from major to minor.


---

Comment by mhansen created at 2008-02-20 03:45:49

Changing assignee from was to mhansen.


---

Attachment

I created an hg bundle which modifies this patch. It makes it such that 
perm -> matrix(perm) is consistent with the corresponding map on perm gp
elements and respects multiplication. It passes sage -t but sage -testall failed
in *many* places, though none which seemed related to this patch.


---

Comment by wdj created at 2008-02-20 18:20:23

The bundle was too large to attach (if that makes any sense). It is posted to
http://sage.math.washington.edu/home/wdj/patches/perms-mat_20-02-2008.hg


---

Comment by mabshoff created at 2008-02-20 18:25:40

The bundle is against the *2.10.1 release*, ergo reverts all patches and bundle from the roughly 120 tickets closed so far against 2.10.2. Please export the commits you made after applying Mike Hansen's 2215.patch and attach those to the tickets.

To reiterate a message which I should be pushing on sage-devel: bundles are evil, especially for single commits.

Cheers,

Michael


---

Comment by wdj created at 2008-02-20 18:43:29

(a) I have no idea how I used 2.10.1 instead of 2.10.2.a1.
(b) I am missing something. Use patches not bundles? I don't even know how to make
a patch. I am used to following http://www.sagemath.org/doc/html/prog/node72.html
Is there a corresponding list of commands for patches?


---

Comment by mabshoff created at 2008-02-20 18:53:09

To quote from that page:

```
You can make all changes in the repository you're working in as a bundle by
typing hg_sage.bundle('mybundle') (this creates an hg bundle mybundle.hg). 
Alternatively, you can export any particular changeset as plain text 
patches by typing hg_sage.export(...); note that each individual changeset 
is recorded as a different patch. hg_sage.export(...) needs at least the 
argument revs - integer or list of integers (revision numbers); use the 
hg_sage.log() function to see them. An optional second argument is a 
'patch_filename', default is '(changeset_revision_number).patch'.
```

The command `hg_sage.bundle('mybundle')` creates a bundle against the current main repo, which is at 2.10.1. Use `hg_sage.export(...)` with the right commit numbers, which `hg_sage.log()` does tell you.

Cheers,

Michael


---

Attachment


---

Comment by wdj created at 2008-02-20 19:05:28

Thanks! Please see attached.


---

Comment by mabshoff created at 2008-02-20 19:12:25

I guess you are giving Mike's patch a positive review. If so please change the summary from "[with patch, needs review]" to "[with patch, with positive review]". It also looks like I need to apply only the second patch?

Cheers,

Michael


---

Comment by wdj created at 2008-02-20 21:09:37

Yes, only the 2nd one.


---

Comment by mhansen created at 2008-02-20 21:42:37

I don't like that matrix(p) and p.to_matrix() will give out different things.  In the documentation for to_matrix(), I specifically said that matrix multiplication will only agree with the permutation  multiplication when the multiplication is not done "English-style".  The proper way to change things would be to modify to_matix() and its documentation, and make sure other things don't break.


---

Comment by wdj created at 2008-02-20 23:46:28

I tried to figure out to_matrix but failed. It seemed to me that it was
implicitly using a global variable, permutation_options or something like that.
I though global variables were Bad. Is there a reason not to use optional
parameters instead? Anyway, I think the matrix command of a permutation
should agree with the the matrix command of a permutation, when regarded as an element
of permutation group.


---

Comment by craigcitro created at 2008-06-20 04:28:39

Changing keywords from "" to "editor_mhansen".


---

Attachment

Is anyone in favor of invalidating this? It seems to have hung around forever.

Cheers,

Michael


---

Comment by mhansen created at 2010-07-10 16:48:38

I've posted an email to sage-combinat-devel asking for additional inpu.


---

Comment by chapoton created at 2018-08-11 19:50:52

Changing status from needs_work to needs_review.


---

Comment by tscrim created at 2018-08-11 21:34:28

Changing status from needs_review to positive_review.


---

Comment by embray created at 2018-11-08 16:14:09

Resolution: wontfix
