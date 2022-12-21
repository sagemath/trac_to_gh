# Issue 3161: sdist: #3046 seems to have broken sage-banner

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2008-05-11 23:41:28

Assignee: mabshoff

Running sdist on 3.0.2.alpha1 results in:

```
running install_egg_info
Writing /scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage-3.0.2.alpha1-py2.5.egg-info
ls: devel/sage: No such file or directory
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/misc/banner.py", line 56, in banner
    print banner_text()
  File "/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/misc/banner.py", line 48, in banner_text
    s += "\n| %-66s |\n"%version()
  File "/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/misc/banner.py", line 38, in version
    branch = os.popen("ls -l devel/sage").read().split()[-1][5:]
IndexError: list index out of range
cp: cannot stat `ipythonrc': No such file or directory
cp: cannot stat `spkg/update': No such file or directory
```


Cheers,

Michael


---

Comment by mabshoff created at 2008-05-11 23:42:06

The problem boils down to the following:

```
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0$ echo "import sage.misc.banner; sage.misc.banner.banner()" | ./local/bin/python
----------------------------------------------------------------------
----------------------------------------------------------------------
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0$ cd local/bin/
mabshoff`@`sage:/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/bin$ echo "import sage.misc.banner; sage.misc.banner.banner()" | ./python
ls: devel/sage: No such file or directory
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/misc/banner.py", line 56, in banner
    print banner_text()
  File "/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/misc/banner.py", line 48, in banner_text
    s += "\n| %-66s |\n"%version()
  File "/scratch/mabshoff/release-cycle/sage-3.0.2.alpha0/local/lib/python2.5/site-packages/sage/misc/banner.py", line 38, in version
    branch = os.popen("ls -l devel/sage").read().split()[-1][5:]
IndexError: list index out of range
```

| SAGE Version 3.0.2.alpha1, Release Date: 2008-05-11                |
| Type notebook() for the GUI, and license() for information.        |
Cheers,

Michael


---

Comment by mabshoff created at 2008-05-11 23:42:06

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-05-19 06:40:36

Ok. Figured it out: #3046 determines the branch by using "ls -la devel/sage" and that assume that the current working directory is in $SAGE_ROOT. Patch coming up.

Cheers,

Michael


---

Attachment


---

Comment by mabshoff created at 2008-05-19 06:53:20

To test this run 

```
echo "import sage.misc.banner; sage.misc.banner.banner()" | ./python
```

i.e. with #3041 *and* #3161 we get:

```
sage-3.0.2.alpha1/local/bin$ echo "import sage.misc.banner; sage.misc.banner.banner()" | ./python
----------------------------------------------------------------------
----------------------------------------------------------------------
```

| SAGE Version 3.0.2.alpha0, Release Date: 2008-05-11                |
| Type notebook() for the GUI, and license() for information.        |
Cheers,

Michael


---

Comment by ddrake created at 2008-05-19 07:13:05

mabshoff's patch works for me against a 3.0 tree.


---

Comment by mabshoff created at 2008-05-19 07:16:13

Resolution: fixed


---

Comment by mabshoff created at 2008-05-19 07:16:13

Merged in Sage 3.0.2.alpha1
