# Issue 949: "sage -f" fails to install packages when given an absolute path

Issue created by migration from https://trac.sagemath.org/ticket/949

Original creator: cwitty

Original creation time: 2007-10-20 19:52:36

Assignee: was

When you run this command:

```
cwitty@magnetar:~/my-sage$ ~/sage/sage -f ~/spkg/mercurial-0.9.5.spkg 
```


the output includes this line:

```
/home/cwitty/sage/local/bin/sage-spkg: file /home/cwitty/my-sage//home/cwitty/spkg/mercurial-0.9.5.spkg does not exist
```


showing that "sage -f" does some sort of "convert relative filename to absolute", but does the operation even if the path is already absolute.


---

Attachment


---

Comment by cwitty created at 2007-10-20 21:45:21

Simple patch: just don't prefix the filename with the current directory if it already starts with a slash.


---

Comment by was created at 2007-10-20 22:30:46

Resolution: fixed
