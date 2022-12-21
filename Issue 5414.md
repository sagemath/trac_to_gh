# Issue 5414: notebook help: the live documentation list are broken after the doc removal

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2009-03-01 21:17:39

Assignee: boothby

CC:  mhansen jhpalmieri

The notebook help screen has links to the reference manual and so on. Those links point to the doc repo where the static html lives. Once #5410 is done those links should be fixed to point to the new static html.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-09 19:48:33

The documentation links mostly work once the needed html documentation has been created, i.e.

```
./sage -docbuild reference html
./sage -docbuild tutorial html
./sage -docbuild developer html
./sage -docbuild constructions html
```

The only thing not working after that is the "Fast Static Versions of the Documentation" link from the main help page.

Cheers,

Michael


---

Attachment


---

Attachment


---

Comment by mhansen created at 2009-03-11 05:24:03

Changing status from new to assigned.


---

Comment by mhansen created at 2009-03-11 05:24:03

Changing assignee from boothby to mhansen.


---

Comment by mabshoff created at 2009-03-11 05:28:21

Positive review.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2009-03-11 06:25:22

Resolution: fixed


---

Comment by mabshoff created at 2009-03-11 06:25:22

Merged all three patches in Sage 3.4.final.

Cheers,

Michael


---

Comment by jhpalmieri created at 2009-03-11 17:03:02

Does this depend on another ticket?  If not, trac_5414-install.diff has the line 

```
"$SAGE_LOCAL/bin"/sage-docbuild --jsmath all html
```

and I don't see a file sage-docbuild anywhere.  Should it be "sage -docbuild"?


---

Comment by mhansen created at 2009-03-11 17:29:11

Hi John,

Actually, mabshoff and I fixed that bit in person so that it does the right thing.  But, you're right, it should be "$SAGE_ROOT"/sage -dodbuild.  We'll post the actual diff here in a sec.

--Mike
