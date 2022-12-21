# Issue 1073: right after "sage -pkg" creates a package, print out some useful information

Issue created by migration from Trac.

Original creator: was

Original creation time: 2007-11-02 23:49:55

Assignee: was

This would save people a lot of confusion.


```
$ sage -pkg foo-bar-2.3
...

Created package foo-bar-2.3.spkg, 

NAME: foo
VERSION: bar-2.3      (not version number looks suspicious)
SIZE: 2.3MB
HG REPO: Unchecked in changes (!)
SPKG.txt: File is missing.

Please test this package using
    sage -f foo-bar-2.3.spkg
immediately.   Also, note that you can use 
    sage -pkg_nc foo-bar-2.3
to make an uncompressed version of the package (useful if the
package is full of compressed data).



```



---

Comment by was created at 2007-11-02 23:50:03

Changing type from defect to enhancement.


---

Attachment

I am not a bash expert but the attached patch does the job for me.


---

Comment by mabshoff created at 2008-01-10 05:46:03

Patch looks good to me. We should add the detect binary crap script, but I will open another ticket for that once William does send it to me.

Cheers,

Michael


---

Comment by mabshoff created at 2008-01-10 06:31:08

Resolution: fixed
