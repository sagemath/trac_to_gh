# Issue 2807: line 26 of c_lib/src/interrupt.c is probably wrong

Issue created by migration from Trac.

Original creator: dmharvey

Original creation time: 2008-04-05 14:50:26

Assignee: cwitty

Line 26 of c_lib/src/interrupt.c says:


```
 if ( _signals.mpio && 1 ) {
```


it should probably be


```
if ( _signals.mpio & 1 ) {
```




---

Attachment


---

Comment by dmharvey created at 2008-04-05 15:03:48

I've made a patch, have no idea if it will work.


```
[10:45am] dmharvey: that's #2807
[10:46am] mabshoff: Well, let's hope we close more tickets today than we open.
[10:46am] dmharvey: I can easily close that one, but I wonder if it will introduce strange bugs....
[10:46am] malb: this line means: we always use Sage's signal handler
[10:47am] malb: which isn't too bad apparently if it handles all the signals we come across ;-)
[10:47am] malb: it probably won't change much
[10:47am] dmharvey: i will make a patch
```



---

Comment by mabshoff created at 2008-04-05 15:48:31

Patch is correct and passes doctests. Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-05 15:49:09

Resolution: fixed


---

Comment by mabshoff created at 2008-04-05 15:49:09

Merged in Sage 3.0.alpha2
