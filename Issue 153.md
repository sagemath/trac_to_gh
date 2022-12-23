# Issue 153: automated testing of the whole SAGE install

Issue created by migration from https://trac.sagemath.org/ticket/153

Original creator: was

Original creation time: 2006-10-25 21:53:14

Assignee: was

Add the following:


```
  sage -i -t packagename.spkg
```


will build and install the package and run whatever the standard tests are
for that package.  The tests will be run by running 

```
  spkg-test
```

if that script is in the package.  Otherwise, it always reports failure.
Then I go through and figure out what the test suite is for each package,
and get it to work. 

Have a "make safe" which does build of all of SAGE but at each point
running the tests.

William



---

Comment by mabshoff created at 2007-08-23 11:28:45

This is a duplicate of #299.

Cheers,

Michael


---

Comment by mabshoff created at 2007-08-23 11:28:45

Resolution: duplicate
