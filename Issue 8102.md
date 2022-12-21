# Issue 8102: Simplify Sphinxify

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-01-28 02:23:43

Assignee: was

CC:  timdumol

Simplifying `sagenb.misc.sphinxify` and importing `sphinx.application.Sphinx` on demand should make docstrings render faster and reduce Sage startup time.


---

Attachment

Simplify `sphinxify.py`.  Some pep8 tweaks.  sagenb repo.


---

Comment by mpatel created at 2010-01-28 02:36:10

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-01-28 02:36:10

The patch also includes some [pep8](http://pypi.python.org/pypi/pep8/) tweaks.


---

Comment by mpatel created at 2010-02-03 05:10:03

Specifically,

```sh
/usr/bin/pep8 --repeat --show-source --ignore=E251,E301,E302,E501 sphinxify.py
```


And to test the startup imports / time:  `sage -startuptime`


---

Comment by jhpalmieri created at 2010-02-03 05:42:07

In line 89

```
confdir = os.path.join(SAGE_DOC, 'en', 'introspect') 
```

won't there be problems if SAGE_DOC is None?  I guess earlier in the file, you could change the last line in the following:

```
try:
    from sage.misc.misc import SAGE_DOC
except ImportError:
    SAGE_DOC = ""  # used to be None
```

Otherwise it looks good.


---

Attachment

Replace `SAGE_DOC = None` with `SAGE_DOC = ''`.  Replaces previous.


---

Comment by mpatel created at 2010-02-03 05:58:47

Thanks for catching that exception.  V2 includes the change.


---

Comment by jhpalmieri created at 2010-02-03 16:08:05

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-02-05 00:36:37

Resolution: fixed
