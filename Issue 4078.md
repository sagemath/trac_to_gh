# Issue 4078: [with patch, needs review] evaluate all has sometimes erratic behavior

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-09-08 13:52:56

Assignee: boothby


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

Attachment

See this thread: http://groups.google.com/group/sage-support/browse_thread/thread/2bb639b190728393/50bf3da4522eaa63?lnk=gst&q=%22evaluate+all%22#50bf3da4522eaa63


---

Comment by was created at 2008-09-09 01:45:48

I strongly agree with this fix.


---

Comment by mabshoff created at 2008-09-09 02:40:25

Merged in Sage 3.1.2.rc1


---

Comment by mabshoff created at 2008-09-09 02:40:25

Resolution: fixed


---

Comment by boothby created at 2008-09-09 20:49:44

I don't like how this was done.  On a slow net connection, (or, if your wireless connection breaks) this can cause the entire browser (or browser window, or just the tab) to completely lock up.  *bad*
