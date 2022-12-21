# Issue 3676: [with patch, needs review] Refactor graph isom code.

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-07-19 00:07:34

Assignee: rlm

CC:  boothby

Keywords: graphs

After this patch, `graph_isom` will be essentially obsolete. Brought to the GNU General Public by Google, Inc.


---

Attachment


---

Comment by wdj created at 2008-07-19 05:27:47

FYI, I got the following test failure:


```
wdj`@`hera:~/sagefiles/sage-3.0.4.rc0$ ./sage -t  devel/sage/sage/rings/finite_field_ntl_gf2e.pyx
sage -t  devel/sage/sage/rings/finite_field_ntl_gf2e.pyx    **********************************************************************
File "/home/wdj/sagefiles/sage-3.0.4.rc0/tmp/finite_field_ntl_gf2e.py", line 170:
    sage: k.modulus()
Expected:
    x^17 + x^16 + x^15 + x^10 + x^8 + x^6 + x^4 + x^3 + x^2 + x + 1
Got:
    x^17
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_2
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wdj/sagefiles/sage-3.0.4.rc0/tmp/.doctest_finite_field_ntl_gf2e.py
         [2.9 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage/sage/rings/finite_field_ntl_gf2e.pyx
Total time for all tests: 2.9 seconds
```



---

Comment by mabshoff created at 2008-07-19 13:20:48

David,

the above doctest is a known issue and orthogonal to rlm's code. See #3634 for the patch that likely caused this.

Cheers,

Michael


---

Comment by wdj created at 2008-07-19 13:51:21

Okay. I was just trying to help out with the doctesting, that's all. Seems like it tests fine then.


---

Attachment

It's so... readable...


---

Attachment


---

Comment by rlm created at 2008-08-06 17:43:32

The patches here may depend on #3703.


---

Attachment


---

Attachment

I can flatten those last three if desired...


---

Comment by mabshoff created at 2008-08-10 20:19:08

Once this ticket is merged #3786 should be next.

Cheers,

Michael


---

Attachment


---

Comment by ncalexan created at 2008-08-11 18:35:49

`3676-ncalexan-docstring-changes.patch` changes some documentation to be clearer.

I am happy with this patch, save for a missing module docstring.  rlmiller will write said docstring, explaining programming API to his code, and then this is ready for showtime.


Apply all patches in order.


---

Comment by boothby created at 2008-08-11 22:07:14

Looks good to me.


---

Comment by rlm created at 2008-08-12 01:11:46

The last patch is a flattened version of the previous ones, together with a recipe for implementing other objects. It should be finally ready to go. Apply only the last patch.


---

Comment by rlm created at 2008-08-12 01:29:42

Apply only this patch (please do not delete the others!)


---

Attachment

rlm and I have gone back and forth on this and I think it's great.  I say apply!


---

Comment by mabshoff created at 2008-08-12 05:00:53

Merged in Sage 3.1.alpha2


---

Comment by mabshoff created at 2008-08-12 05:00:53

Resolution: fixed
