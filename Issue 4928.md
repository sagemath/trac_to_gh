# Issue 4928: Create Sage 3.2.3 release notes

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-01-02 23:16:37

Assignee: mabshoff

As the summary says :)

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-10 01:16:02

Please comment on needed fixes.

Cheers,

Michael


---

Comment by mabshoff created at 2009-01-10 01:16:02

Changing status from new to assigned.


---

Attachment


---

Comment by GeorgSWeber created at 2009-01-13 08:21:39

Only one remark:

In the introductory text, it is said "... 71 Open Source Packages ...". The count of spkgs is beyond 90 (93 I think), but that is not a one-to-one relation, of course.

Is that number "71" to be updated? (If it should, but is not going to be updated, that would be still fine for me.)


---

Comment by was created at 2009-01-13 14:51:55

> The count of spkgs is beyond 90 (93 I think), but that is 
> not a one-to-one relation, of course.

wstein`@`sage:~/sage/spkg/standard$ ls *.spkg |wc -l
88

But I'm not convinced every spkg counts as an "open source package".  Are any of these spkg's "open source packages":

elliptic_curves-0.1.spkg
examples-3.2.3.spkg
extcode-3.2.3.spkg

Definitely 71 should increase though, e.g., since new spkg's like docutils-0.5.spkg have been added to sage since I computed that 71 number.


---

Comment by mabshoff created at 2009-01-19 04:49:03

I have checked and 3.2.3 has 89 spkgs. Of those six are not 

```
doc
elliptic_curves
examples
extcode
scripts
polytopes_db
```

Open source projects IMHO. So let's use the number 83 for now.

I am attaching a final version of the release notes shortly.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2009-01-19 05:10:12

Resolution: fixed


---

Comment by mabshoff created at 2009-01-19 05:10:12

Merged in Sage 3.2.3 - a little late, but it is finally in :)

Cheers,

Michael
