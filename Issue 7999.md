# Issue 7999: SyntaxError when loading Sage 4.3.1.rc1 due to non-ASCII character

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-01-19 15:29:25

Assignee: tbd

I built Sage 4.3.1.rc1 from source and then produced a sage.math binary. Loading the binary resulted in the following SyntaxError:

```
SyntaxError: Non-ASCII character '\xc3' in file /dev/shm/mvngu/sage-4.3.1.rc1-dev/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py on line 5448, but no encoding declared; see http://www.python.org/peps/pep-0263.html for details (ell_rational_field.py, line 5447)
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.
```

The guilty line is line 5447:

```
           modular forms. Astérisque, (295):ix, 117-290, 2004.                  
```

of `sage/schemes/elliptic_curves/ell_rational_field.py`, which doesn't have the following preamble to indicate that the file has non-ASCII characters:

```
# -*- coding: utf-8 -*-
```



---

Comment by mvngu created at 2010-01-19 15:35:09

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-01-19 16:35:14

based on Sage 4.3.1.rc1


---

Comment by mpatel created at 2010-01-19 19:42:03

Changing status from needs_review to positive_review.


---

Attachment


---

Comment by rlm created at 2010-01-19 20:06:46

Resolution: fixed
