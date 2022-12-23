# Issue 1063: [with patch] "sage -sh" should run $SHELL with Sage environment variables set

Issue created by migration from https://trac.sagemath.org/ticket/1063

Original creator: cwitty

Original creation time: 2007-11-02 01:56:46

Assignee: was

After the patch, this works:

```
cwitty@magnetar:~/sage$ ./sage -sh
Starting subshell with Sage environment variables set:
cwitty@magnetar:~/sage$ echo $SAGE_LOCAL
/home/cwitty/sage/local
cwitty@magnetar:~/sage$ exit
exit
Exited Sage subshell.
```


I also patch sage-spkg, to change the error message it prints on failed package installs:

```
If you want to try to fix the problem, yourself *don't* just cd to
/home/cwitty/sage/spkg/build/genus2reduction-0.3 and type 'make'.
Instead type "/home/cwitty/sage/sage -sh"
in order to set all environment variables correctly, then cd to
/home/cwitty/sage/spkg/build/genus2reduction-0.3
(When you are done debugging, you can type "exit" to leave the
subshell.)
```



---

Attachment


---

Comment by mabshoff created at 2007-11-02 02:26:17

applied to 2.8.11.rc1


---

Comment by mabshoff created at 2007-11-02 02:26:17

Resolution: fixed
