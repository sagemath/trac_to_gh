# Issue 1987: [with patch] unintuitive return values for "forall" and "exists"

Issue created by migration from https://trac.sagemath.org/ticket/1987

Original creator: nbruin

Original creation time: 2008-01-30 22:28:41

Assignee: cwitty

The names of "forall" and "exists" suggest that these are predicates that can be used where a conditional is needed. In fact, doing so does not result in an error but in unintended results:
`len([ i for i in [1..300] if forall(prime_divisors(i),lambda i: i<10)])`
returns
`300`
which does not reflect the apparent meaning of the expression. The proper result is returned by inserting an index:
`len([ i for i in [1..300] if forall(prime_divisors(i),lambda i: i<10)[0]])`
which returns
`82`

I would suggest an optional parameter to "forall" and "exists", say, witness=True to return a second return value giving the index. The default should be index=False in my opinion.


---

Comment by nbruin created at 2008-01-30 23:14:16

As Mike Hansen points out, use python natives "all" and "any" instead. Patch should probably not be merged.


---

Attachment

Patch to fix docstrings of forall and exists to refer to Python natives.


---

Comment by nbruin created at 2008-02-01 02:02:36

Patch now changed to fix docstrings of "forall" and "exists". Please do consider this change for inclusion, so that other people have an easier time finding the more appropriate python natives.


---

Comment by was created at 2008-02-01 03:02:56

I made some comments on sage-devel.  This patch should definitely be included
though, even if none of my comments are addressed.


---

Comment by mabshoff created at 2008-02-15 23:51:32

The patch has sat in trac for about two weeks now. William suggested to merge, but maybe Nils has some more input?

Cheers,

Michael


---

Comment by cremona created at 2008-02-16 20:37:29

This patch can _certainly_ be applied as is, since it just adds some useful info to docstrings.

The only remaining issues from the sage-devel discussion that I can see are some odd timing issues.  But that does not seem a reason to hold back on this.


---

Comment by mabshoff created at 2008-02-16 20:44:55

Ok, I consider John's review to be a positive one. Changing the subject accordingly. The patch applies cleanly against my current 2.10.2.alpha1 buil.d


---

Comment by mabshoff created at 2008-02-16 20:45:58

Resolution: fixed


---

Comment by mabshoff created at 2008-02-16 20:45:58

Merged in Sage 2.10.2.alpha1
