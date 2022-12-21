# Issue 8153: [with patch] typo in documentation

Issue created by migration from Trac.

Original creator: zimmerma

Original creation time: 2010-02-02 16:08:03

Assignee: mvngu

trivial patch


---

Attachment

Is this up for review?


---

Comment by zimmerma created at 2010-02-02 20:52:21

> Is this up for review? 

yes it should be easy :-)


---

Comment by zimmerma created at 2010-02-02 20:52:21

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-02-02 21:20:07

before applying 13535.patch


---

Attachment

after applying 13535.patch


---

Attachment

based on Sage 4.3.2.alpha1


---

Attachment

after applying trac_8153-plot-doc.patch


---

Comment by mvngu created at 2010-02-02 21:30:26

The attachment [13535.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8153/13535.patch) actually removes Sphinx formatting of a block of example code. See [before.png](http://trac.sagemath.org/sage_trac/attachment/ticket/8153/before.png) for the situation before applying [13535.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8153/13535.patch). The image [after.png](http://trac.sagemath.org/sage_trac/attachment/ticket/8153/after.png) shows the situation after applying [13535.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8153/13535.patch). Perhaps [trac_8153-plot-doc.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8153/trac_8153-plot-doc.patch) is the effect you originally wanted to achieve? See [after2.png](http://trac.sagemath.org/sage_trac/attachment/ticket/8153/after2.png) for the result of applying [trac_8153-plot-doc.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8153/trac_8153-plot-doc.patch).


---

Comment by zimmerma created at 2010-02-02 22:11:25

> Perhaps  trac_8153-plot-doc.patch is the effect you originally wanted to achieve? 

no, since with the tty interface of Sage we still get two ':':

```
sage: plot?
...
        We plot the sin function::
...
```



---

Comment by jhpalmieri created at 2010-02-03 02:38:31

The double colons are an essential part of the documentation, and they are ubiquitous.   mvngu's pictures show what happens when you change them, and it's not good.  Meanwhile, see #8161 for a patch which changes all double colons to single ones when displaying docstrings using the command-line interface.  That ticket will "fix" the issue raised here.

I think this ticket should be closed as "wontfix".


---

Comment by mvngu created at 2010-02-03 02:42:54

Resolution: wontfix


---

Comment by mvngu created at 2010-02-03 02:42:54

Closing this ticket as "wontfix". See #8161 for a follow-up ticket.
