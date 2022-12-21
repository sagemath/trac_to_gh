# Issue 8804: Bring plot/plot3d/parametric_surface.pyx to 100% doctest coverage

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2010-04-28 15:20:22

Assignee: mvngu

CC:  robertwb

Bring plot/plot3d/parametric_surface.pyx to 100% doctest coverage.


---

Comment by kcrisman created at 2010-04-29 20:14:18

Based on Sage 4.4


---

Comment by kcrisman created at 2010-04-29 20:27:03

Changing status from new to needs_review.


---

Attachment

Also fixes a few inconsistencies with formula for MobiusStrip that wasn't used and dual() that I checked with robertwb.


---

Attachment


---

Comment by mvngu created at 2010-05-10 00:58:41

The patch [trac_8804-param-surface-docs.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8804/trac_8804-param-surface-docs.patch) is OK by me. I have added a reviewer patch that fixes some typos, add the parametric surface module to the reference manual, and fixes to get the module to build and resolve all warnings. So only my patch needs review by anyone but me.


---

Comment by kcrisman created at 2010-05-10 15:51:37

This looks okay, but I'm not sure how to test the documentation building and looking right.  Also, just for my information, when do we need r""" and when is """ sufficient?    Also, apparently the input for init goes in the class definition - is that right?  My apologies, I didn't realize that.


---

Comment by mvngu created at 2010-05-10 21:15:10

Replying to [comment:3 kcrisman]:
> This looks okay, but I'm not sure how to test the documentation building and looking right. 

A quick-and-dirty way is to rebuild as follows from SAGE_ROOT:


```sh
./sage -b main
./sage -docbuild reference html
```


If you really want to be thorough, you could delete the whole output directory resulting from building the Sage documentation and then rebuild the whole reference manual again. This would take much longer than the above quick-and-dirty way, but it sure is more thorough. From SAGE_ROOT, do:


```sh
rm -rf devel/sage-main/doc/output/
./sage -b main
./sage -docbuild reference html
```




> Also, just for my information, when do we need r""" and when is """ sufficient?  

We need `r"""` when the docstring contains LaTeX escapes, i.e. LaTeX macros that start with a backslash character. In most other cases, `"""` is sufficient. For example, if your docstring contains something like 


```
\sin(x)^2 + \cos(x)^2 = 1
```


then your docstring must be delimited with `r"""`. For safety, I always use `r"""`.




>  Also, apparently the input for init goes in the class definition - is that right? 

At the moment, that is the case because docstrings for methods and functions whose names start with an underscore don't show up on the reference manual. So full documentation for the constructor `__init__` are recommended to be in the class docstring. That way, documentation relating to the constructor, including its input and output documentation, shows up on the reference manual.


---

Comment by kcrisman created at 2010-05-11 13:45:17

Okay, looks great and still passes tests.


---

Comment by kcrisman created at 2010-05-11 13:45:17

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-05-12 22:49:51

Resolution: fixed
