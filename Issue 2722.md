# Issue 2722: [with patch; needs trivial review] interact -- a doctest problem

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-03-29 17:43:25

Assignee: boothby


```
>  Fedora 7 32 bits:
>  
>  sage -t  devel/sage-main/sage/server/notebook/interact.py   **********************************************************************
>  File "interact.py", line 1420:
>      sage: slider([1, 'x', 'abc', 2/3], None, None, 3, 'alpha')
>  Expected:
>      Slider: alpha [abc--|1|---1]
>  Got:
>      Slider: alpha [2/3--|1|---x]
>  **********************************************************************
>  1 items had failures:
>     1 of   3 in __main__.example_62
>  ***Test Failed*** 1 failures.
>  For whitespace errors, see the file .doctest_interact.py
>           [2.4 s]


Good catch.  The right fix is to change the input that causes
that failure to:
   sage: slider([1, 'x', 'abc', 2/3], None, None, 'abc', 'alpha')

This was caused by a change in the definition of the slider
function, which results in extreme cases in system-specific
behavior.  
```



---

Attachment


---

Comment by was created at 2008-03-29 17:51:05

Changing priority from major to blocker.


---

Comment by jsp created at 2008-03-29 18:40:12

This worked for me on Fedora 7 32 bits.



```
[jaap`@`paix sage-2.11.alpha2]$ ./sage -t  devel/sage-main/sage/server/notebook/interact.py
sage -t  devel/sage-main/sage/server/notebook/interact.py   
         [3.6 s]
 
----------------------------------------------------------------------
All tests passed!

```



Jaap


---

Comment by mabshoff created at 2008-03-29 18:50:43

Merged in Sage 2.11.rc0


---

Comment by mabshoff created at 2008-03-29 18:50:43

Resolution: fixed
