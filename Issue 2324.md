# Issue 2324: RealNumber->QQ coercion fails for NaN, infinity

Issue created by migration from https://trac.sagemath.org/ticket/2324

Original creator: cwitty

Original creation time: 2008-02-26 20:27:06

Assignee: somebody

Both of these should raise an exception immediately.  Instead, the former crashes, and the latter takes a long time to do something (I haven't tracked down what yet).


```
sage: QQ(RR(0.0/0.0))
/home/cwitty/sage/local/bin/sage-sage: line 212:  5344 Segmentation fault      sage-ipython -wthread -c "$SAGE_STARTUP_COMMAND;" "$@"
```



```
sage: QQ(RR(1.0/0.0))
... infinite loop?
```




---

Comment by cwitty created at 2008-02-26 20:47:11

Changing assignee from somebody to cwitty.


---

Comment by cwitty created at 2008-02-26 20:47:11

Changing status from new to assigned.


---

Attachment


---

Comment by mhansen created at 2008-02-27 19:26:52

After a long build, this works for me against 2.10.3.alpha0


---

Comment by mabshoff created at 2008-02-27 23:59:16

Resolution: fixed


---

Comment by mabshoff created at 2008-02-27 23:59:16

Merged in Sage 2.10.3.rc0
