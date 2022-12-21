# Issue 844: dsage -- priority queues

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-10-10 02:11:49

Assignee: yqiang

Yi,

Suppose I launch 1000 jobs like you saw me do.  Now I want to do
something else, e.g., compute a bunch of things "at another level",
while leaving those 1000 jobs (or what remains) in the queue.
Is there any way to make a d = DSage() that submits jobs ahead
of the 1000 jobs I submitted before.  E.g.,

```
    d.eval('foo', priority=-1)
```

???



---

Comment by mvngu created at 2010-02-01 03:07:26

Resolution: wontfix


---

Comment by mvngu created at 2010-02-01 03:07:26

Close as wontfix. The dsage module has been removed by #7975.
