# Issue 4597: setup.py dependency checker does not invalidate cache correctly

Issue created by migration from https://trac.sagemath.org/ticket/4597

Original creator: cwitty

Original creation time: 2008-11-23 16:30:54

Assignee: craigcitro

After applying the following patches: #846, #4564, #4579, and #4592, applying #4580 gives the following error:

```
Updating Cython code....
Traceback (most recent call last):
  File "setup.py", line 463, in <module>
    queue = compile_command_list(ext_modules, deps)
  File "setup.py", line 424, in compile_command_list
    dep_file, dep_time = deps.newest_dep(f)
  File "setup.py", line 355, in newest_dep
    for f in self.all_deps(filename):
  File "setup.py", line 338, in all_deps
    deps.update(self.all_deps(f, path))
  File "setup.py", line 336, in all_deps
    for f in self.immediate_deps(filename):
  File "setup.py", line 318, in immediate_deps
    self._deps[filename] = self.parse_deps(filename)
  File "setup.py", line 274, in parse_deps
    f = open(filename)
IOError: [Errno 2] No such file or directory: 'sage/rings/mpfr.pxi'
sage: There was an error installing modified sage library code.
```


I have an unconfirmed theory as to the cause of the problem.  My theory is that there's a chain like this: A.pyx depends on B.pxd; B.pxd depends on C.pxi.  So setup.py records a transitive dependency of A.pyx on C.pxi.  Then a patch removes C.pxi and modifies B.pxd to not depend on C.pxi any more, but does not touch A.pyx.  Then setup.py checks all the dependencies of A.pyx to see whether to recompile it, but fails when it tries to check the no-longer-existing C.pxi.

Removing .cython_deps allows compilation to proceed.


---

Attachment


---

Comment by craigcitro created at 2008-11-23 23:00:37

I *think* the attached patch will fix the problem. The issue is this: when a file doesn't exist, we want to have different behaviors at different parts of the compilation process. So, I made the `timestamp` function take an extra argument, which is what to return if the file doesn't exist, and set it accordingly. The default behavior is that if the file doesn't exist, it returns the current time -- so that a nonexistent file is considered new (i.e. things depending on it need updated).

Let me know if this doesn't fix the problem.


---

Comment by craigcitro created at 2008-11-23 23:00:37

Changing status from new to assigned.


---

Comment by cwitty created at 2008-11-25 01:40:20

Looks reasonable, and does fix my problem.

Positive review.


---

Comment by mabshoff created at 2008-11-25 02:12:25

Resolution: fixed


---

Comment by mabshoff created at 2008-11-25 02:12:25

Merged in Sage 3.2.1.alpha1
