# Issue 7437: the optional gnuplotpy-1.7.p3 spkg doesn't build at all since with switched to python-2.6

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-11-12 05:04:19

Assignee: tbd


```
Traceback (most recent call last):
  File "setup.py", line 17, in <module>
    from __init__ import __version__
  File "/home/sage/sage/spkg/build/gnuplotpy-1.7.p3/src/__init__.py", line 167, in <module>
    from PlotItems import PlotItem, Func, File, Data, GridData
  File "/home/sage/sage/spkg/build/gnuplotpy-1.7.p3/src/PlotItems.py", line 88
    'with' : lambda self, with: self.set_string_option(
                             ^
SyntaxError: invalid syntax
Error installing gnuplotpy.

real    0m0.159s
user    0m0.024s
sys     0m0.124s
sage: An error occurred while installing gnuplotpy-1.7.p3
```



---

Comment by was created at 2009-11-12 05:10:24


```
mhansen:
There is a new upstream release for that.
[9:07pm] mhansen:
I'm not sure if it fixes that issue though.
mhansen:
Yep, it should (looking at SVN).
```



---

Comment by aapitzsch created at 2014-08-13 22:28:38

Changing status from new to needs_review.


---

Comment by aapitzsch created at 2014-08-13 22:28:38

Works for me with Python 2.7.8 and current optional gnuplotpy-1.8 (on linux).


---

Comment by vbraun created at 2014-10-25 21:44:22

Resolution: worksforme
