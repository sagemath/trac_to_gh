# Issue 3730: Sage scripts ending with .py

Issue created by migration from Trac.

Original creator: tabbott

Original creation time: 2008-07-27 03:37:25

Assignee: tba

Debian's automated Python byte-compilation tool determines what's a python script based on whether it has extention .py (yeah, I know, pretty lame), and is apparently stupid enough to look in /usr/share/doc/sagemath/examples for things needing byte-compilation.

Unfortunately, /usr/share/doc/sagemath/examples/example.py is a .py with a #!/usr/bin/sage and which apparently isn't entirely valid python (the last line causes the byte-compiler to fail):


```
Compiling /usr/share/sagemath/examples/example.py ...
  File "/usr/share/sagemath/examples/example.py", line 62
    time factor(Integer(2)**Integer(127)-Integer(1))
              ^
SyntaxError: invalid syntax
```


The corresponding file example.sage seems to not exist, so I'm not sure what the story with that file is.


---

Comment by tabbott created at 2008-07-27 04:28:17

To be clear, I think this is the only instance of this problem in the distribution.


---

Comment by kcrisman created at 2012-06-01 18:05:41

Given that the examples/ directory is gone, this is no longer valid.


---

Comment by kcrisman created at 2012-06-01 18:05:41

Changing status from new to needs_review.


---

Comment by kcrisman created at 2012-06-01 18:06:09

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2012-06-02 12:35:44

Resolution: invalid
