# Issue 2110: Cython annotation should be available more easily

Issue created by migration from https://trac.sagemath.org/ticket/2110

Original creator: roed

Original creation time: 2008-02-08 11:37:09

Assignee: was

cython -a creates an annotated html file that helps with profiling code.  It would be nice if this functionality were available on:
1. .spyx files
2. .pyx files in the sage library, more easily.

I propose that there should be a new flag to sage (eg sage -n) that fulfills these goals.

sage -n file.spyx would proprocess file.spyx and then call cython -a then start a web-browser to view the file.
sage -bn would build sage and call cython -a on the cython files that are being built.
sage -ban would run sage -ba with cython -a.



---

Comment by robertwb created at 2011-09-19 19:14:20

Resolution: fixed


---

Comment by robertwb created at 2011-09-19 19:14:20

As of http://hg.sagemath.org/scripts-main/annotate/b1badfb26e13/sage-cython#1

You can do 


```
sage -cython -a /path/to/file.spyx
```


or 


```
sage -cython -a /sage/library/file.pyx
```


or even 


```
sage -cython -a -sage /path/to/non/library/file.pyx
```


To do this.  

Also, as of Cython 0.15 , existing .html files will automatically get updated even if the -a flag is not used to ensure they stay in sync.
