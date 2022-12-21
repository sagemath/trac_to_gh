# Issue 5324: notebook -- %time block bug

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-02-20 20:00:08

Assignee: boothby

If you create a block like this:

```
%time 
2+2
```

in the notebook, then you get the following output:

```
Traceback (click to the left for traceback)
...
NameError: name 'time' is not defined
```


IMPORTANT: There is a single space right immediately after %time in the input!  Without the space things are fine. 


---

Comment by mhansen created at 2009-02-20 21:07:22

Changing status from new to assigned.


---

Comment by mhansen created at 2009-02-20 21:07:22

Changing assignee from boothby to mhansen.


---

Comment by jason created at 2009-05-30 07:18:11

mhansen says this is fixed at #5564.


---

Comment by mvngu created at 2009-08-26 19:59:59

Ticket #5564 has been closed because it addresses many issues. The issues it addresses are also considered by other tickets. If anyone is working on this ticket, please refer to #5564 for code and inspiration.


---

Comment by was created at 2009-11-09 02:03:51

Note that the problem isn't just with %time, but with any % modes.


---

Attachment


---

Comment by was created at 2009-11-09 02:13:43

Changing status from new to needs_review.


---

Comment by mhampton created at 2009-11-09 03:14:56

Changing status from needs_review to positive_review.


---

Comment by mhampton created at 2009-11-09 03:14:56

Looks good and seems to fix the problem.  What's the point of setting i=-1 in the patch?  Is that just so i is defined as an integer if text has no elements when reaching the line: return "\n".join(text[i:]).strip()?  Setting i = 0 would seem to make slightly more sense, if so.  I'm just curious, that doesn't seem like enough of an issue to block a positive review.


---

Comment by was created at 2009-11-09 17:12:07

> Is that just so i is defined as an integer if text has no elements when 
> reaching the line: return

Yes.    splitlines and split('\n') have different semantics.  I changed to splitlines in anticipation of windows. 

You're right, using i=0 makes more sense, though of course won't make any difference since in this special case the list we're slicing is empty.


---

Attachment


---

Comment by was created at 2009-11-09 17:19:03

Resolution: fixed
