# Issue 4060: Polyhedra don't handle real coordinates properly

Issue created by migration from Trac.

Original creator: mhampton

Original creation time: 2008-09-04 13:44:12

Assignee: mhampton

Keywords: polyhedra

Dear All,

I have a question related to the polyhedra module.
When I define a polyhedron using float rather than integer
coordinates, I get a weird behavior from the vert_to_ieq function.
For example, if I type something like this:

p = [[1.1, 2.2], [3.3, 4.4]]
vert_to_ieq(p, cdd_type="real") 


---

Attachment


---

Comment by mhampton created at 2008-09-04 20:38:20

Changing assignee from mhampton to somebody.


---

Comment by mhampton created at 2008-09-04 20:38:20

OK, I think I have resolved this problem.  I added a doctest to the Polyhedron class to test this.


---

Comment by mhansen created at 2008-09-19 00:43:15

This looks good to me.


---

Comment by mabshoff created at 2008-09-19 03:20:08

Resolution: fixed


---

Comment by mabshoff created at 2008-09-19 03:20:08

Merged in Sage 3.1.3.alpha0
