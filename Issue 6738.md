# Issue 6738: typo in spkg-install for atlas spkg

Issue created by migration from https://trac.sagemath.org/ticket/6738

Original creator: was

Original creation time: 2009-08-11 22:45:21

Assignee: mabshoff

I just noticed this in an error message:


```
Building shared ATLAS libraris failed
```


See the typo in the word "libraris".


---

Comment by mvngu created at 2009-08-11 23:34:11

The typo lies in the file `spkg-install-script` of the ATLAS spkg. An updated spkg that fixes the reported typo is up at:

http://sage.math.washington.edu/home/mvngu/patch/atlas-3.8.3.p7.spkg


---

Comment by mvngu created at 2009-08-12 00:59:35

Merged in the standard spkg repository.


---

Comment by mvngu created at 2009-08-12 00:59:35

Resolution: fixed
