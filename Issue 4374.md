# Issue 4374: Numerical noise doctest failure in sage/tests/book_stein_ent.py

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-10-27 17:12:43

Assignee: mabshoff

CC:  craigcitro


```
sage -t  devel/sage/sage/tests/book_stein_ent.py 
********************************************************************** 
File "/local/jec/sage-3.1.4/tmp/book_stein_ent.py", line 5056: 
    : g2.complex_embedding() 
Expected: 
    -2.2360679775 + 3.33066907388e-16*I 
Got: 
    -2.2360679775 + 3.83970199386e-16*I 
********************************************************************** 
```



---

Comment by mabshoff created at 2008-10-27 17:15:46

On an Itanium I am seeing the following numerical results:

```
sage -t  devel/sage/sage/tests/book_stein_ent.py            
**********************************************************************
File "/home/mabshoff/build-3.2.a1/sage-3.2.alpha1-cleo/tmp/book_stein_ent.py", line 5056:
    : g2.complex_embedding()
Expected:
    -2.2360679775 + 3.33066907388e-16*I
Got:
    -2.2360679775 + 5.38810057558e-16*I
**********************************************************************
```



---

Comment by mabshoff created at 2008-10-27 17:15:46

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-10-27 18:07:43

And from a G5 running OSX 10.4:

```
sage -t  devel/sage/sage/tests/book_stein_ent.py            
**********************************************************************
File "/Users/mabshoff/sage-3.2.alpha1/tmp/book_stein_ent.py", line 5056:
    : g2.complex_embedding()
Expected:
    -2.2360679775 + 3.33066907388e-16*I
Got:
    -2.2360679775 + 5.38810057558e-16*I
**********************************************************************
```



---

Comment by mabshoff created at 2008-10-27 18:14:34

Craig,

since William mentioned you were cleaning up those files feel free to take ownership here.

Cheers,

Michael


---

Comment by craigcitro created at 2008-10-27 19:47:28

Changing assignee from mabshoff to craigcitro.


---

Comment by craigcitro created at 2008-10-27 19:47:28

Changing status from assigned to new.


---

Attachment

The attached patch fixes the above issues, as well as cleaning up the files `book_stein_ent.py` and `book_stein_modform.py`. I'll keep an eye out for any new numerical noise that pops up during testing ...


---

Comment by craigcitro created at 2008-10-27 19:47:36

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-10-27 20:04:01

Positive review. Tests pass on Itanium and the G5. All the other changes look good, too, and also take care of the coverage problem.

Cheers,

Michael


---

Comment by mabshoff created at 2008-10-27 20:05:28

Resolution: fixed


---

Comment by mabshoff created at 2008-10-27 20:05:28

Merged in Sage 3.2.alpha2
