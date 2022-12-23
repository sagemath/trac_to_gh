# Issue 4355: Port latex/asciiArt output for tableaux and all friends from MuPAD-Combinat

Issue created by migration from https://trac.sagemath.org/ticket/4355

Original creator: nthiery

Original creation time: 2008-10-24 00:53:04

Assignee: mhansen

CC:  sage-combinat boussica

The latex method for tableaux was written in a rush during Sage Days 7
to get the latex output for crystals. This is a partial quick port of
the TeX method we use in MuPAD-Combinat in the general case of
"ObjectsWith2DBoxedRepresentation" which includes everything from
partitions, tableaux, skew tableaux, ribbons tableaux, to rigged
configurations, or other things that can be drawn with symbols in an
array, and some horizontal and vertical delimiters, like mazes. 

A class which inherits from ObjectsWith2DBoxedRepresentation just has
to implement a method that fills appropriately an array for the
symbols, and another for the delimiters, and it gets for free 2D ascii
art, latex, ... output.  See:

http://mupad-combinat.svn.sourceforge.net/viewvc/mupad-combinat/trunk/MuPAD-Combinat/lib/DOMAINS/CATEGORY/CombinatorialClassWith2DBoxedRepresentation.mu?revision=7455&view=markup

For a few samples of the produced 2d ascii art, you can have a look
at:

http://mupad-combinat.sourceforge.net/doc/en/output_Combinat/asciiArt.html

(note: the pictures are broken unless you use a fixed font).

It as proven to be a handy tool, for the zillion of tableaux-like
classes, so a good candidate for porting.

First straightforward step: LaTeX output

Second step: ascii art output. This may require a bit more thinking,
since there is not yet (?) a general framework for ascii art in Sage.


---

Comment by bump created at 2008-10-24 03:24:33

I have added two patches tableaux_output.patch and tableaux_output1.patch with the aim of fixing the latex output for tableaux. This is particularly important for CrystalOfTableaux tex output which is a main way of viewing crystals. For discussion see this thread:

http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/3fff0cbc6b44b483?hl=en#


---

Comment by bump created at 2008-10-24 03:29:35

Changing type from enhancement to defect.


---

Comment by bump created at 2008-10-24 03:29:35

I changed the type from "enhancement" to "defect" since the existing code is actually broke. Nicolas envisions an enhancement here but in the meantime perhaps we can at least make the existing code work correctly.


---

Comment by bump created at 2008-10-24 11:36:20

Since what Nicolas is proposing is clearly different from the problems the patches addresses, I created a new ticket at #4362 and changed the type of this one back to enhancement.


---

Comment by bump created at 2008-10-24 11:36:20

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2008-10-24 11:42:59

I have deleted both of Dan's patches and moved them over to the new ticket so that things are kept simple :)

Cheers,

Michael


---

Comment by tscrim created at 2012-01-16 06:23:52

I have completed a portion of part 1 in ticket #12314.

Travis


---

Comment by git created at 2014-05-02 09:09:15

Branch pushed to git repo; I updated commit sha1. New commits:
