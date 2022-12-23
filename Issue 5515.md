# Issue 5515: "make" attempts to build documentation even if the build fails

Issue created by migration from https://trac.sagemath.org/ticket/5515

Original creator: cwitty

Original creation time: 2009-03-14 15:09:49

Assignee: mabshoff

In $SAGE_ROOT/spkg/install:

```
time make -f standard/deps $1
"$SAGE_ROOT"/sage -docbuild --jsmath all html
```


This hides the true cause of a build error if something goes wrong -- you see a totally irrelevant error about failing to build the documentation, instead of a useful error about whatever went wrong with the build.


---

Comment by tornaria created at 2009-03-14 16:09:23

I was hit by this issue in three different ways, with different errors reported:
 1. error building `gmp-mpir-0.9` (#5516), when I didn't have system wide python installed, the error reported in the last line in the compilation was:

```
/opt/sage/sage-3.4/local/bin/sage-sage: line 852: python: command not found
```

 2. same error in `gmp-mpir-0.9` (#5516), after installing system wide python, the error reported was:

```
python: can't open file '/opt/sage/sage-3.4/devel/sage/doc/common/builder.py': [Errno 2] No such file or directory
```

 3. error building `cvxopt-0.9.p7` (#5517), the error reported was:

```
ImportError: No module named jinja
```

I think all of these misreporting are due to the issue reported in this ticket. The actual issues in `gmp-mpir-0.9` and `cvxopt-0.9.p7` are reported in #5516 and #5517 resp.


---

Comment by timdumol created at 2009-08-30 18:21:29

Duplicate of #6295.


---

Comment by mvngu created at 2009-09-26 07:55:43

Resolution: duplicate


---

Comment by mvngu created at 2009-09-26 07:55:43

Close this ticket as a duplicate of #6295.
