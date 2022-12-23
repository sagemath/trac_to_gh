# Issue 4373: doctest failure in sage/algebras/group_algebra.py on 32 bit platforms

Issue created by migration from https://trac.sagemath.org/ticket/4373

Original creator: mabshoff

Original creation time: 2008-10-27 05:35:02

Assignee: mabshoff

CC:  mhansen


```
sage -t  devel/sage/sage/algebras/group_algebra.py          
********************************************************************** 
File "/home/jaap/downloads/sage-3.2.alpha0/tmp/group_algebra.py", line 230: 
     sage: OG(FormalSum([ (1, G(2)), (2, RR(0.77)) ]), check=False) 
Expected: 
     [2 0] 
     [0 2] + 2*0.770000000000000 
Got: 
     2*0.770000000000000 + [2 0] 
     [0 2] 
**********************************************************************
```



---

Comment by mabshoff created at 2008-10-28 12:54:53

David,

since this is your patch any clue what is going on here?

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-28 12:55:04

Changing priority from major to blocker.


---

Attachment


---

Comment by davidloeffler created at 2008-10-28 13:31:52

Changing status from new to assigned.


---

Comment by davidloeffler created at 2008-10-28 13:31:52

The failed doctest was just verifying that the "check" flag could be disabled, by using this to create a bogus group algebra element that is a formal sum of things that aren't in the right group. The string representation of such an element depends on the sort order of the elements, which is completely arbitrary and subject to changing between platforms, hence the failure here.

All that's really needed is to check that the method runs; it's inconceivable that it could run but not give the expected answer. So I've uploaded a 1-line patch that marks the doctest with "# random".

(I didn't use the "#64-bit" and "#32-bit" flags as then it would just break again next time someone changed the sort order of real numbers versus integer matrices, which is bound to happen before long.)


---

Comment by davidloeffler created at 2008-10-28 13:31:52

Changing assignee from mabshoff to davidloeffler.


---

Comment by mabshoff created at 2008-10-28 13:41:01

Ok, I think in that situation then #random is warranted. But could you please replace the patch by a version that adds the explanation you just gave on the ticket why this fails so that in the future people looking at that doctest understand why. It would also be nice to mention this ticket number in the string, i.e. "the issue was also discussed at #4373".

Mike: FYI since you also had some comments about this code.

Cheers,

Michael


---

Attachment

ok, here it is again, with a more informative comment on the doctest.


---

Comment by mabshoff created at 2008-10-28 15:49:07

Two small issues: The explanation should be before the doctest and indented and the '#' in the docstring needs to be escaped. I will take care of both small issues. 

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-28 16:24:17

Resolution: fixed


---

Comment by mabshoff created at 2008-10-28 16:24:17

Merged in Sage 3.2.alpha2
