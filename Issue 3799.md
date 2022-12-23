# Issue 3799: degree sequence should not be a single integer in graph_database

Issue created by migration from https://trac.sagemath.org/ticket/3799

Original creator: rlm

Original creation time: 2008-08-10 10:04:30

Assignee: rlm

CC:  rlm

This is part of Jason Grout's formatting of his database, but it should be translated to and from a sequence of integers for the user.


---

Comment by ekirkman created at 2008-08-14 00:46:28

this patch inspired a full graph database re-write.  Coming soon!


---

Attachment


---

Comment by ekirkman created at 2008-09-22 11:16:50

This patch should be stable for review, and it includes some definite improvements.  There will be more database enhancements coming, but they'll deserve their own tickets.  Oops -- one more patch coming with doctest fixes...


---

Attachment


---

Comment by rlm created at 2008-09-22 15:45:06

Due to the new restrictions on incoming patches, this can't be merged until all of the functions added/modified have doctests. This includes `verify_type, verify_operator, construct_skeleton, _apply_format, _apply_plot,` and maybe others. For discussion, if nothing else, I challenge `No doctest is intentional.` in `database.py`.

Perhaps this could be reworded/more specific (and you don't need to shout, I can hear you ;-) ):

```
# WORD ON THE STREET IS THAT SQLITE IS RETARDED ABOUT
# *ALTER TABLE* COMMANDS... SO MEANWHILE WE ACCOMPLISH THIS
# BY CREATING A TEMPORARY TABLE.  SUGGESTIONS FOR SPEEDUP ARE
# WELCOME.  (OR JUST SEND A PATCH...)
```


Why was the copyright statement removed from `graph_database.py`? Remember that these statements protect our code!


---

Attachment

Attached another patch to address the problems mentioned.


---

Attachment


---

Comment by rlm created at 2008-09-29 22:06:47

Looks good to me.


---

Comment by mabshoff created at 2008-09-29 23:29:05

Resolution: fixed


---

Comment by mabshoff created at 2008-09-29 23:29:05

Merged all four patches in Sage 3.1.3.alpha2
