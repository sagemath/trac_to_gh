# Issue 2783: notebook -- ocassional "crap" in output like this   print "\x01r\x01e580"

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-04-02 22:17:45

Assignee: boothby

Hi,

I was very embarrassed while teaching today since maybe 15 times I got
crap like this in the output from the notebook:

```
print "\x01r\x01e580"
```


This is from the synchronization code that *I* wrote.  It "should" never happen.  Anyways it does -- but of course only when 40 people are watching you :-(.  Anyways, to solve this ticket should mean to simply look at that synchro code again, think about it, and rewrite it in a way that is _more_ robust. 

William


---

Comment by TimothyClemans created at 2008-09-08 14:11:03

According to the ticket description the ticket should be marked as invalid since it's past June 1st.


---

Comment by mabshoff created at 2008-09-08 18:00:58

Resolution: invalid


---

Comment by mabshoff created at 2008-09-08 18:00:58

Oh well: invalid.


---

Comment by was created at 2008-09-09 01:13:14

Changing status from closed to reopened.


---

Comment by was created at 2008-09-09 01:13:14

Resolution changed from invalid to 


---

Comment by was created at 2008-09-09 01:13:14

I am reopening this since I am able to systematically replicate it now.  All you have to do is
use rpy from the notebook, and right after that this crap appears. 


{{
import rpy
rpy.std([1..1000])
///
print "\x01r\x01e96"
288.67499025720952
}}


---

Comment by was created at 2008-09-09 01:13:35


```
{{ 
import rpy rpy.std([1..1000]) 
/// 
print "\x01r\x01e96" 288.67499025720952 
}}
```



---

Comment by mabshoff created at 2008-09-09 02:20:34

Any chance this could be related to using a terminal which has trouble with dealing with the escape characters related to color? We had similar issues with sage0 and IPython.

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-22 00:19:27

Isn't this likely some issue with escape character sequences from colored output being printed?

Cheers,

Michael


---

Comment by was created at 2008-09-22 00:55:58

> Isn't this likely some issue with escape character sequences from colored output being printed?

I doubt it.  rpy is a C-library interface to R.

Those special looking \x01r characters are synchronization control characters that Sage itself (in the file worksheet.py) puts in the output stream. 

William


---

Comment by mabshoff created at 2008-09-22 00:58:15

ok, good to know.

Cheers,

Michael


---

Comment by boothby created at 2009-01-22 00:28:46

I still see these pop up sporadically, and I can't reproduce it reliably.  Initial ticket said "mark as invalid by June 1, 2008", which is long past.  Thoughts?


---

Comment by timdumol created at 2009-11-15 17:19:37

Has anyone had this problem recently?


---

Comment by was created at 2009-11-18 09:36:28

No, and using rpy2 instead doesn't produce it.  Moreover, I completely rewrote from scratch the pexpect interfaces to use a much better way of synchronizing IO.  The crap mentioned in this ticket was from the old way of synchronizing IO.   So I'm closing this as fixed.


---

Comment by was created at 2009-11-18 09:36:28

Resolution: fixed
