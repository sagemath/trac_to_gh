# Issue 6098: 3d bezier path plotting

Issue created by migration from https://trac.sagemath.org/ticket/6098

Original creator: ekirkman

Original creation time: 2009-05-21 02:19:19

Assignee: ekirkman

CC:  rlm mhansen




---

Comment by ekirkman created at 2009-05-21 02:34:22

This picture was created with input sage: bezier3d([This is the Trac macro ** that was inherited from the migration called with arguments (0,0,0),)](https://trac.sagemath.org/wiki/WikiMacros#-macro))


---

Attachment

Referee edit


---

Comment by ncalexan created at 2009-06-13 21:26:36

Unfortunately, against 4.0.2.alpha0:


```
----------------------------------------------------------------------

The following tests failed:

        sage -t -long devel/sage/sage/plot/plot3d/shapes2.py # 4 doctests failed
        sage -t -long devel/sage/sage/plot/plot3d/shapes2.py # 4 doctests failed
        sage -t -long devel/sage/sage/plot/bezier_path.py # 2 doctests failed
----------------------------------------------------------------------
```



---

Comment by rlm created at 2009-07-13 21:11:31

Apply only this patch


---

Attachment

It was completely trivial to get this patch working again. I did the work while Emily watched over my shoulder. If one positive review isn't enough, then you have two! :)


---

Comment by mvngu created at 2009-07-16 16:08:43

Oops... ignore the patch `trac_6098-reviewer.patch`. Just to let people know, only the patch `trac_6098-rebased.patch` has been merged in sage-4.1.1-alpha0. I can't close this ticket because I don't have the privilege to do so. Sorry, folks :-(


---

Comment by mvngu created at 2009-07-16 21:18:09

Resolution: fixed
