# Issue 2292: segfault in AbelianGroups

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2008-02-24 15:16:16

Assignee: joyner

wdj`@`wooster:~/wdj/sagefiles/sage-2.10.2.rc0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.2, Release Date: 2008-02-22                      |
| Type notebook() for the GUI, and license() for information.        |
sage: G.<a,b> = AbelianGroup(2)
sage: a/b
/home/wdj/wdj/sagefiles/sage-2.10.2.rc0/local/bin/sage-sage: line 212: 31402 Segmentation fault      (core dumped) sage-ipython -c "$SAGE_STARTUP_COMMAND;" "$`@`"

On the other hand, this seems to be okay in perm_groups_named:

wdj`@`wooster:~/wdj/sagefiles/sage-2.10.2.rc0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.2, Release Date: 2008-02-22                      |
| Type notebook() for the GUI, and license() for information.        |
sage: G = SymmetricGroup(5)
sage: G.gens()
((1,2,3,4,5), (1,2))
sage: a,b = G.gens()
sage: a/b
(2,3,4,5)


---

Comment by wdj created at 2008-02-24 15:18:43

This is a more readable version:


```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.2, Release Date: 2008-02-22                      |
| Type notebook() for the GUI, and license() for information.        |
sage: G.<a,b> = AbelianGroup(2)
sage: a/b
/home/wdj/wdj/sagefiles/sage-2.10.2.rc0/local/bin/sage-sage: line 212: 31402 Segmentation fault      (core dumped) sage-ipyt on -c "$SAGE_STARTUP_COMMAND;" "$`@`"
```



```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10.2, Release Date: 2008-02-22                      |
| Type notebook() for the GUI, and license() for information.        |
sage: G = SymmetricGroup(5)
sage: G.gens()
((1,2,3,4,5), (1,2))
sage: a,b = G.gens()
sage: a/b
(2,3,4,5)
sage:
```



---

Comment by wdj created at 2008-02-24 18:15:05

I think I can fix this. I'm running tests on the patch now. The patch will hopefully also fix
http://trac.sagemath.org/sage_trac/ticket/2293


---

Attachment


---

Attachment

I attached the patch and the bundle, so the reviewer can use either one. Passed the tests and fixes
http://trac.sagemath.org/sage_trac/ticket/2293


---

Comment by mhansen created at 2008-02-27 22:19:45

Works for me in 2.10.3.alpha0.


---

Comment by mabshoff created at 2008-02-27 23:07:36

David: Please add the issue that caused the bug as a doctest, especially in case of segfaults. mhansen is adding a doctest in this case.

Cheers,

Michael


---

Comment by mabshoff created at 2008-02-27 23:07:55

Resolution: fixed


---

Comment by mabshoff created at 2008-02-27 23:07:55

Merged in Sage 2.10.3.rc0


---

Attachment

Merged 2292-doctest.patch (due to unknown parent via GNU patch), but credited to mhansen via hg commit
