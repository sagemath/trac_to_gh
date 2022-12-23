# Issue 5104: setup.py dependency checking issues

Issue created by migration from https://trac.sagemath.org/ticket/5104

Original creator: craigcitro

Original creation time: 2009-01-26 16:47:03

Assignee: mabshoff

CC:  sbarthelemy robertwb

In addition to the problems fixed on trac #5060, we also have the following, reported by `sbarthelemy`:

Hello,

reading the code, I see another problem if ones has the following line in its `.pyx`:

`cimport mod#mycomment`

In such a case, we'll look for a dependency `mod#mycomment.pxd` instead of `mod.pxd`.




---

Comment by mhansen created at 2009-01-26 16:50:23

Resolution: duplicate


---

Comment by mhansen created at 2009-01-26 16:50:23

I beat you to it Craig :-)

This is a duplicate of #5103.


---

Comment by craigcitro created at 2009-01-26 16:54:27

Resolution changed from duplicate to 


---

Comment by craigcitro created at 2009-01-26 16:54:27

Changing status from closed to reopened.


---

Comment by craigcitro created at 2009-01-26 16:55:03

Oops -- Mike and I made tickets at the same time; apparently we closed each other's tickets at the same time, too. 

We'll keep this one open.


---

Comment by mabshoff created at 2009-02-08 08:48:30

This also seems like a worthwhile fix to be in 3.3

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-14 09:23:54

Positive review & good catch.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-14 09:27:43

Arrg, this code actually does introduce a problem since `\w` does not include the directory separator `/`. Hence:

```
Installing c_lib
scons: `install' is up to date.
Updating Cython code....
Traceback (most recent call last):
  File "setup.py", line 510, in <module>
    queue = compile_command_list(ext_modules, deps)
  File "setup.py", line 470, in compile_command_list
    dep_file, dep_time = deps.newest_dep(f)
  File "setup.py", line 385, in newest_dep
    for f in self.all_deps(filename):
  File "setup.py", line 366, in all_deps
    for f in self.immediate_deps(filename):
  File "setup.py", line 348, in immediate_deps
    self._deps[filename] = self.parse_deps(filename)
  File "setup.py", line 338, in parse_deps
    raise IOError, "could not find dependency %s included in %s."%(path, filename)
IOError: could not find dependency sage/finance/sage.pxd included in sage/finance/time_series.pyx.
sage: There was an error installing modified sage library code.
```


Sorry for the hasty review :(

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-16 05:00:31

I am cleaning up the 3.3 milestone. If a patch with positive review is put up to this ticket on time it might make it into 3.3.

Cheers,

Michael


---

Attachment


---

Comment by robertwb created at 2009-02-17 10:38:38

Updated the patch.


---

Comment by mabshoff created at 2009-02-20 13:06:57

Looks good to me. The complete Sage library dependency tree is parse successfully and also builds from scratch.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 13:07:15

Merged in Sage 3.3.rc3.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-20 13:07:15

Resolution: fixed
