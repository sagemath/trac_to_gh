# Issue 6044: Enhanced reduction modulo ideals of number fields

Issue created by migration from https://trac.sagemath.org/ticket/6044

Original creator: mtaranes

Original creation time: 2009-05-15 09:24:14

Assignee: somebody

CC:  cremona

Keywords: number fields, ideals

1. Modify "residues" function so that it returns a canonical set of coset representatives.

2. New "reduce" function for number field ideals that returns the canonical reduced representative of a given integral element: I.reduce(f) is an element of the set of representatives returned by I.residues(). 

3. Have "inverse_mod" working for integral elements of a number field without having to coerce to the ring of integers (using existing  functionality for order elements)


Patch based on 3.4.2 to follow soon.


---

Comment by mabshoff created at 2009-05-15 14:47:21

This is unlikely to make it into Sage 4.0, so bumping it to 4.0.1.

Cheers,

Michael


---

Comment by cremona created at 2009-05-15 14:52:23

Replying to [comment:1 mabshoff]:
> This is unlikely to make it into Sage 4.0, so bumping it to 4.0.1.
> 
> Cheers,
> 
> Michael
No problem, though it is likely to have been reviewed within a day or two!


---

Attachment

Here is the patch, with the new functions, etc, and corrections for the docstrings that were affected by the change in the 'residues' function.


---

Attachment


---

Comment by cremona created at 2009-05-20 11:55:59

The patch applies fine to 4.0.alpha0, and all tests in sage/rings/number_field pass.

There are some small glitches in the docstrings:  in inverse_mod() in the first line, N should be I.  In reduce(), there is a formatting problem which I think would go away if a space is inserted after the second ` in `I`=self, and later on the single backquotes aroung small_residue should be double.  Ans some small indentation issues (which aer oly seen as problematical when docbuild is used).

I fixed these things in the review patch (which also fixes a few minor documentation issues I noticed that are nothing to do with this ticket as such), but someone else should look at this too.


---

Comment by davidloeffler created at 2009-06-10 10:49:47

Rebased to 4.0.1 and folded into one patch


---

Attachment

Good stuff; it will be much more efficient to use hermite form rather than smith form in residues, besides being more canonical.

I have rebased the patch to 4.0.1, and checked that it commutes with #5842 and #6188. All tests in sage/rings/number_field pass still (on a 32-bit machine), as do those in sage/doc/en/bordeaux_2008 (which have a habit of catching out unwary number theory patch authors). 

This one has been in limbo for three weeks because the trac reports of patches with review / needing review / etc are done using text searches of the summary field, and thus "with review, needs second opinion" doesn't get picked up. I guess it would be safer to set it to "needs review", but this strikes me as conclusive proof that we need to change the way we use trac -- this is the *fifth* ticket I've spotted today which has been in limbo because of a slightly unusual summary string.


---

Comment by cremona created at 2009-06-10 17:30:30

Many thanks for spotting this and delivering it out of limbo, especially as you had to rebase it.  I have a habit of forgetting all about my own patches once I have put them up for review (and wish trac had an option to filter out those tickets which I had added a patch to which were still open).

As for SNF  v. HNF it was just my stupidity in the first place which caused us to use SNF.   HNF is particularly efficient since that's the form pari stores ideals in anyway.


---

Comment by ncalexan created at 2009-06-13 20:46:05

Resolution: fixed
