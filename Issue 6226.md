# Issue 6226: developer's guide: sections on formatting docstrings and trac guidelines

Issue created by migration from https://trac.sagemath.org/ticket/6226

Original creator: mvngu

Original creation time: 2009-06-05 15:18:00

Assignee: tba

Keywords: developer's guide

We need to add to the developer's guide some information about docstring formatting in ReST, and how to build the Sage standard documentation. The developer's guide also needs to document further detailed guidelines when working on tickets.


---

Comment by mvngu created at 2009-06-05 15:21:03

based on Sage 4.0.1.rc1


---

Attachment

The patch `trac_6226.patch` fixes some typos in the developer's guide. It also adds sections on formatting documentation using ReST. The information on that is taken from the Sage wiki at



http://wiki.sagemath.org/combinat/HelpOnTheDoc



written by Florent Hivert. The patch also adds guidelines on the trac server and working on tickets. These guidelines were written by Michael Abshoff and can be found at 



http://wiki.sagemath.org/TracGuidelines



So authorship credit should be shared with Michael Abshoff and Florent Hivert.


---

Comment by jhpalmieri created at 2009-06-05 19:43:55

Comments: very nice overall.  I have a second patch, to be applied on top of yours, which deals with a few small issues:

in producing_patches.rst, `hg_sage.patch(...)` and `hg_sage.apply(...)` are not synonyms, and it sounds like that a bit.  Also, you've deleted one reference to the "doc" repository, but there's another (two lines after "Sage includes these Mercuruial repositories").

in sage_manuals.rst: as far as I can tell, you don't need to run `sage -b` when producing new versions of any manual other than the reference manual: just edit the files and run `sage -docbuild tutorial html` or whatever.  There are a few typos, too.

in trac.rst: I thought that a few of the lines from the wiki were more appropriate for a wiki page than a formal piece of documentation, so I removed them.

I give your patch a positive review, so if you're happy with mine, the whole thing is ready to go.


---

Comment by jhpalmieri created at 2009-06-05 19:44:20

Changing assignee from tba to mvngu.


---

Attachment


---

Attachment

The patch `trac_6226_part2.patch` looks good to me. After applying `trac_6226.patch` and `trac_6226_part2.patch` to Sage 4.0.1.rc2 and re-reading the developer's guide, I noticed more typos. These are fixed in `trac_6226-part3.patch`. If it gets positive review, then the patches on this ticket should be applied in the following order:
 1. `trac_6226.patch`
 1. `trac_6226_part2.patch`
 1. `trac_6226-part3.patch`


---

Comment by ncalexan created at 2009-06-13 23:03:51

Resolution: fixed
