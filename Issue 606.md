# Issue 606: add notebook support for loading of spyx and pyx files

Issue created by migration from https://trac.sagemath.org/ticket/606

Original creator: mhansen

Original creation time: 2007-09-07 00:02:17

Assignee: boothby

From the notebook,


```
%sh
cat > hello.pyx << EOF
def hello(name):
    """
    Print hello with the given name.
    """
    print("Hello %s"%name)
EOF
```


```
load "hello.pyx"
Loading of file
"/opt/sage-2.8.3.rc3/sage_notebook/worksheets/admin/0/cells/0/hello.pyx"
has type not implemented.
```


There is a function that currently just checks to see if the filename extension is .py or .sage before it tries to load the file.


---

Attachment


---

Comment by mhansen created at 2007-09-07 00:33:09

Changing assignee from boothby to mhansen.


---

Comment by mhansen created at 2007-09-07 00:33:09

Patch added and tested.


---

Comment by was created at 2007-09-07 01:14:41

This patch is completely bogus.


---

Comment by was created at 2007-09-07 01:14:48

Changing priority from minor to major.


---

Comment by was created at 2007-09-07 01:15:29

This is a good spyx file to test:


```
was@ubuntu:~$ more a.spyx
def foo(int n):
    return n*n
```



---

Attachment

changed version that i like


---

Comment by was created at 2007-09-07 02:38:16

Resolution: fixed


---

Attachment
