# Issue 2350: The 2.10.2 behavior of show(list) should instead be available via plot(list, array=True)

Issue created by migration from https://trac.sagemath.org/ticket/2350

Original creator: jason

Original creation time: 2008-02-29 01:45:04

Assignee: was

show changed behavior in 2.10.2, which surprised lots of people.

 * revert show to the previous behavior.

 * plot(list) does what it currently does (i.e., superimpose the plots)

 * plot(list, array=True) does what show does in 2.10.2 (i.e., put the
plots into an array).

 * change the docs to show() to more clearly reflect the purpose of the
function.



---

Comment by jason created at 2008-02-29 01:45:17

Changing status from new to assigned.


---

Comment by jason created at 2008-02-29 01:45:17

Changing assignee from was to jason.


---

Comment by jason created at 2008-03-03 20:05:07

The ticket that introduced the mentioned changes is #1908


---

Attachment


---

Comment by jason created at 2008-03-03 22:42:00

show-revert.patch takes care of the first item listed above.  Please don't close this ticket, though, as I'd like to do the rest of the items too.


---

Comment by jason created at 2008-03-03 22:42:07

Changing type from defect to enhancement.


---

Comment by jason created at 2008-03-03 22:59:22

see #2380 for the remainder of the items; you can close this one after applying the patch.


---

Comment by mabshoff created at 2008-03-03 23:38:42

Merged in Sage 2.10.3.rc1


---

Comment by mabshoff created at 2008-03-03 23:38:42

Resolution: fixed


---

Comment by mabshoff created at 2008-03-04 00:09:42

Oops, forgot to change the status in the summary.

Cheers,

Michael
