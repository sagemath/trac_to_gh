# Issue 7076: SageNB -- Do ReST introspection on a `worksheet_process`

Issue created by migration from Trac.

Original creator: timdumol

Original creation time: 2009-09-29 19:48:30

Assignee: boothby

Keywords: sagenb notebook

This increases security (prevents a DoS by introspecting constantly), and ensures that it is done in a separate process (which may be in an entirely different server)


---

Attachment

Reimplements introspection.


---

Comment by was created at 2009-09-29 20:14:06

Resolution: fixed


---

Comment by was created at 2009-09-29 20:14:06

I've applied this to the notebook.
