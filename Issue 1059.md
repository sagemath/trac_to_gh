# Issue 1059: fix lcalc installation on OSX 10.5

Issue created by migration from https://trac.sagemath.org/ticket/1059

Original creator: mabshoff

Original creation time: 2007-11-02 00:24:10

Assignee: mabshoff

The fix for lcalc is to change the line

```
cp lcalc* "$SAGE_LOCAL"/bin
```

in spkg-install to

```
cp lcalc "$SAGE_LOCAL"/bin
```

The former was needed when we supported windows (e.g., lcalc.exe), and was sort of hack-ish. The latter works around that there is some small problem with strip on os x, which isn't an issue.

    -- William



---

Comment by mabshoff created at 2007-11-02 00:24:18

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-11-02 00:41:45

Resolution: fixed


---

Comment by mabshoff created at 2007-11-02 00:41:45

applied to 2.8.11.rc1 - via with new lcalc-20070107.p0.spkg
