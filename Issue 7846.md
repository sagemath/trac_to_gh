# Issue 7846: Missing triple-secret ___code___.py files when copying a worksheet

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-01-05 03:27:06

Assignee: was

CC:  was

Copying a worksheet in Sage 4.3.1.alpha0 sometimes gives

```python
          File "/home/sage/notebook/sagenb-0.4.9/sagenb/notebook/twist.py", line 795, in render
            W = notebook.copy_worksheet(self.worksheet, self.username)
          File "/home/sage/notebook/sagenb-0.4.9/sagenb/notebook/notebook.py", line 719, in copy_worksheet
            self._initialize_worksheet(ws, W)
          File "/home/sage/notebook/sagenb-0.4.9/sagenb/notebook/notebook.py", line 631, in _initialize_worksheet
            shutil.copytree(cells, target)
          File "/home/apps/sage/local/lib/python/shutil.py", line 177, in copytree
            raise Error, errors
        shutil.Error: [('/home/.sage/sage_notebook.sagenb/home/aaaa/21/cells/2/___code___.py', '/home/.sage/sage_notebook.sagenb/home/aaaa/28/cells/2/___code___.py', "[Errno 2] No such file or directory: '/home/.sage/sage_notebook.sagenb/home/aaaa/21/cells/2/___code___.py'")]

```


This is a follow-up to #7514.


---

Comment by was created at 2010-01-05 03:45:58

Changing priority from major to critical.


---

Comment by was created at 2010-01-05 03:45:58

Can you systematically trigger this?  It looks serious?  What was the worksheet that caused this.  The problem is probably symlinks to ___code___.py files being created when they shouldn't be, or something.   Those files should be completely ignored when copying the worksheet.


---

Comment by mpatel created at 2010-01-05 04:07:00

I'll try to find a reproducible case.


---

Comment by mpatel created at 2010-01-05 06:24:35

Suppress `CODE_PY` symlinks.  sagenb repo.


---

Attachment

The attached patch should work for copying and re-publishing worksheets --- both use `Notebook._initialize_worksheet`.  But we should cover

```python
fname = 'foo.txt'
fd = open(fname, 'w')
fd.write('bar')
fd.close()
print os.listdir('.')
import time; time.sleep(3)
os.unlink(fname)
print os.listdir('.')
```

too...


---

Comment by mpatel created at 2010-01-05 07:21:32

Which is better

```python
import os, shutil

def ignore_nonexistent_files(curdir, dirlist):
    ignore = []
    for x in dirlist:
        if not os.path.exists(os.path.join(curdir, x)):
            ignore.append(x)
    return ignore

# This:
shutil.copytree('foo', 'bar', ignore=ignore_nonexistent_files)
# Or this:
shutil.copytree('foo', 'bar', symlinks=True)
```

?  We use [shutil.copytree](http://docs.python.org/library/shutil.html#shutil.copytree) in 5 places under `sagenb`.  If it's necessary, I can add `sagenb.misc.misc.ignore_nonexistent_files`.


---

Attachment

Also ignore non-existent files.  Replaces previous.


---

Comment by mpatel created at 2010-01-05 08:21:59

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-01-05 08:21:59

It seems safer to skip non-existent files.  I haven't changed the lines in `Notebook.migrate_old_worksheet`, since the they're wrapped in Try-N-Save blocks.

Should we delete all files that are temporarily symlinked but not actually in the final output?  Do people like to keep track of intermediaries?

Different problem: Should deleting a cell in the notebook delete its contents on disk?


---

Comment by was created at 2010-01-08 20:00:37

Positive review.  

Merged into sagenb-0.5


---

Comment by was created at 2010-01-08 20:00:37

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-01-08 20:00:41

Resolution: fixed
