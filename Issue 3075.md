# Issue 3075: notebook -- add a "test" option

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-05-01 22:28:27

Assignee: boothby

Click Action ---> Test and all cells will be evaluated and their output compared with the output last time.  Any time the output differs both outputs are shown with the bad one in RED.

Or something like that...


---

Comment by was created at 2008-05-01 22:28:36

Changing type from defect to enhancement.


---

Comment by was created at 2008-05-02 17:26:24


```
10:13 < mabshoff> And I have been slipping in FreeBSD fixes when no one was looking ;)
10:16 < jason|log> okay, "flaky" == in one cell, I have a=[] and i=1, the next I have a.append(i).  
                   Evaluate all sometimes gives me an error in the second cell and says that 'a' is not 
                   defined.
10:16 < jason|log> I can't reproduce it on sage.math in the few minutes I tried.
10:18 < jason|log> wstein: could the problem be the asynchronous requests to evaluate the cells?  One 
                   request gets ahead of another sometimes?
10:19 < jason|log> (not in the sending, but in the server receiving the requests?)
10:19 < wstein> Yes, that is possible.
10:20 < wstein> The right fix would be to make a single "evaluateall" command that gets sent
10:20 < wstein> to the notebook server.
10:20 < wstein> Right now a stupid evaluate_all javascript function calls evaluate_cell on each cell.
```



---

Comment by mhansen created at 2008-09-08 01:29:08

Changing status from new to assigned.


---

Comment by mhansen created at 2008-09-08 01:29:08

Changing assignee from boothby to mhansen.


---

Comment by mhansen created at 2008-09-08 01:33:34

This patch fixes the problems with evaluate all.


---

Comment by TimothyClemans created at 2008-09-08 11:23:04

The patch by mhansen doesn't add a "test" option, so I think it should be on a different ticket.


---

Comment by mhansen created at 2008-09-08 13:54:32

I made #4078.

Do we even really want this feature for the notebook?  I'd vote for marking this ticket as invalid.


---

Comment by TimothyClemans created at 2008-09-08 13:58:56

I don't want it.


---

Comment by mhansen created at 2009-01-22 13:03:19

Resolution: invalid
