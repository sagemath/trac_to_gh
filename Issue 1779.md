# Issue 1779: setup.py computes the cache of some irrelevent files

Issue created by migration from Trac.

Original creator: moretti

Original creation time: 2008-01-14 23:12:39

Assignee: cwitty

I discovered this:

Installing c_lib
scons: `install' is up to date.
Traceback (most recent call last):
  File "setup.py", line 1079, in <module>
    H = str(hash_of_cython_file_timestamps())
  File "setup.py", line 1076, in hash_of_cython_file_timestamps
    return hash_of_dir('sage')
  File "setup.py", line 1072, in hash_of_dir
    h += hash_of_dir(z)
  File "setup.py", line 1072, in hash_of_dir
    h += hash_of_dir(z)
  File "setup.py", line 1074, in hash_of_dir
    h += hash(os.path.getmtime(z))
  File "/home/bob/sage/local/lib/python2.5/posixpath.py", line 143, in getmtime
    return os.stat(filename).st_mtime
OSError: [Errno 2] No such file or directory: 'sage/rings/polynomial/.#polynomial_element.pyx'
sage: There was an error installing modified sage library code.

Emacs must have made a temp file .#polynomial_element.pyx. Python screws up on hashing this; the string should be sanitized in some way, I suppose; however, we do not need to be hashing the timestamp on hidden .pyx files.


---

Comment by moretti created at 2008-01-14 23:23:49

The attached patch should fix the build issues


---

Attachment


---

Comment by mabshoff created at 2008-01-15 02:45:07

Patch looks good to me. It seems unlikely that anybody would add legitimate Cython files that start with a dot.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-15 02:47:39

Resolution: fixed


---

Comment by mabshoff created at 2008-01-15 02:47:39

Merged in Sage 2.10.alpha3
