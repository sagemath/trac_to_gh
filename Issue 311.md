# Issue 311: Update sage -t testing structure

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2007-03-07 19:01:16

Assignee: ncalexan

Keywords: test examples run

The current testing architecture could use some spring cleaning.

ncalexan has started updating it, with the first cut having:

 * better error reporting
 * more flexible importing, so that, for example, a test can import its current file without full sage scoping
 * a Python API so testing is integrated into the SAGE shell (and into the notebook, although this is not particularly powerful at this time)

Secondary tools might make it:

 * easier to order the tests in some way, such as most recently modified or last failing test first
 * easy to mine the examples for documenting
 * possible to generate statistics and other useful tidbits from the existing examples

If you're interested in a particular feature, please let ncalexan know.



---

Comment by ncalexan created at 2007-03-07 19:01:31

Changing type from defect to enhancement.


---

Comment by ncalexan created at 2007-03-07 19:01:40

Changing status from new to assigned.


---

Comment by ncalexan created at 2007-03-08 18:23:07

Request: it would be nice if Ctrl-C was better behaved.


---

Comment by mabshoff created at 2007-09-10 02:44:42

What is the status here? It has been a while.

Cheers,

Michael


---

Comment by mabshoff created at 2008-03-16 09:02:24

We should break this ticker up in bits that we want to get done and close this ticker as invalid since it is a hodgepodge of various things.

Cheers,

Michael


---

Comment by gfurnish created at 2008-03-21 16:09:33

Resolution: invalid


---

Comment by gfurnish created at 2008-03-21 16:09:33

I have moved the Python API request to #2630.  #679 provides statistics and better error reporting.  I am closing this as the rest of the items are too vague to create individual tickets for.


---

Comment by mabshoff created at 2008-03-21 21:43:38

Do not invalidate tickets like this since it is certainly a borderline case. Me not objecting in IRC is *not* approval ;)

Cheers,

Michael
