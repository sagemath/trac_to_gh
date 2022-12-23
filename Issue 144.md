# Issue 144: Numpy build breaks on sage-1.4.1.2

Issue created by migration from https://trac.sagemath.org/ticket/144

Original creator: justin

Original creation time: 2006-10-21 20:44:08

Assignee: was

Gets a key error here:

numpy-2006-08-16: blew chunks here;
    File "/SandBox/Justin/sb/sage-1.4/spkg/build/numpy-2006-08-16/numpy/distutils/\
            ..../fcompiler/__init__.py", line 199, in get_flags_linker_exe
      if self.executables['linker_exe']:
    KeyError: 'linker_exe'



---

Attachment

Numpy build log


---

Comment by justin created at 2006-10-21 20:47:57

Changing component from algebraic geometry to packages.


---

Comment by justin created at 2006-10-21 20:47:57

Changed component to 'packages'


---

Comment by was created at 2007-01-08 19:28:05

Numpy is now a standard sage component.


---

Comment by was created at 2007-01-08 19:28:05

Resolution: fixed
