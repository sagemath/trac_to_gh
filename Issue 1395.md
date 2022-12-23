# Issue 1395: notebook(directory="foo/") misbehaves

Issue created by migration from https://trac.sagemath.org/ticket/1395

Original creator: malb

Original creation time: 2007-12-04 15:37:30

Assignee: boothby

If the directory name is provied with a trailing "/" then

```
SAGE/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py in __init__(self, dir, system, show_debug, log_server, address, port, secure, server_pool)
     59         self.__worksheet_dir = '%s/worksheets'%dir
     60         self.__object_dir    = '%s/objects'%dir
---> 61         self.__makedirs()
     62         self.__history = []
     63         self.__history_count = 0

SAGE/local/lib/python2.5/site-packages/sage/server/notebook/notebook.py in __makedirs(self)
    666     def __makedirs(self):
    667         if not os.path.exists(self.__dir):
--> 668             os.makedirs(self.__dir)
    669         if not os.path.exists(self.__worksheet_dir):
    670             os.makedirs(self.__worksheet_dir)


SAGE/local/lib/python2.5/os.py in makedirs(name, mode)
    170         if tail == curdir:           # xxx/newdir/. exists if xxx/newdir exists
    171             return
--> 172     mkdir(name, mode)
    173
    174 def removedirs(name):

<type 'exceptions.OSError'>: [Errno 2] No such file or directory: ''
```


This is particularly annoying because tab completion returns directory names with trailing "/".


---

Comment by mhansen created at 2007-12-06 00:38:38

Changing assignee from boothby to mhansen.


---

Comment by mhansen created at 2007-12-06 00:38:38

Changing status from new to assigned.


---

Attachment


---

Comment by cwitty created at 2007-12-15 02:15:57

Looks good: code seems reasonable, and it does fix the problem.


---

Comment by mabshoff created at 2007-12-15 04:47:35

Merged in 2.9.rc0.


---

Comment by mabshoff created at 2007-12-15 04:47:35

Resolution: fixed
