# Issue 525: Get Pete Chvany's build notes into the SAGE docs.

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-08-30 03:06:42

Assignee: tba




---

Attachment

SAGe build notes


---

Comment by mabshoff created at 2007-08-30 10:36:46

From Section 10:

```
The call to bison will probably go away in future versions of SAGE, but at present (version 2.7.3, version 2.8) it is helpful to force install bison as part of preparing the ground for later packages.
```

This issue has been resolved.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-20 06:55:36

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-04-20 06:55:36

Changing assignee from tba to mabshoff.


---

Comment by jhpalmieri created at 2008-09-26 18:09:56

Is this ticket still relevant? If so, can someone explain its purpose to me? Who is the target audience for the attached document?

For example, the document says 'These instructions assume a basic level of Unix command-line fluency.' But in this case, how much of this needs to be explained?

For another example, it seems like a bad idea (items 3 and 4) to delete the old copy of sage, at least not until you're sure that the new one doesn't break things (the way the notebook was somewhat broken for a few releases). If we want instructions like this somewhere (in the installation guide, I suppose), I would not include them as is...


---

Comment by mabshoff created at 2008-09-26 19:08:16

Replying to [comment:3 jhpalmieri]:

Hi John,

> Is this ticket still relevant? If so, can someone explain its purpose to me? Who is the target audience for the attached document?

I don't think so.

> For example, the document says 'These instructions assume a basic level of Unix command-line fluency.' But in this case, how much of this needs to be explained?
> 
> For another example, it seems like a bad idea (items 3 and 4) to delete the old copy of sage, at least not until you're sure that the new one doesn't break things (the way the notebook was somewhat broken for a few releases). If we want instructions like this somewhere (in the installation guide, I suppose), I would not include them as is...

They do suggest outright bad things like building Sage with sudo privileges. It is much, much better to build Sage as a user, -bdist and then move the result into a user accessible location. Another bad thing it to give the sage script an absolute patch since these days the location of a link is automatically resolved.

Consequently: closed as wontfix.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-26 19:08:39

wontfix as explained above.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-26 19:08:39

Resolution: wontfix
