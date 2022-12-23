# Issue 2679: sage docs -- get rid of aux, etc., files when packaging up for distribution

Issue created by migration from https://trac.sagemath.org/ticket/2679

Original creator: was

Original creation time: 2008-03-26 18:36:16

Assignee: tba


```
> 3. removing the .aux and .toc cache files from the documentation area
> solved the pdf/html problems.

ok, we ought to make sure that we remove all those temp files before
packaging the documentation.
```



---

Comment by was created at 2008-03-26 18:39:19

The file to change is 

```
   doc/scripts/spkg-dist
```


See also #2675, which is the same problem.


---

Comment by jhpalmieri created at 2009-02-26 17:09:11

This can be closed now, right?


---

Comment by mabshoff created at 2009-02-26 17:27:05

Resolution: fixed


---

Comment by mabshoff created at 2009-02-26 17:27:05

Close in Sage 3.4.alpha0 due to the switch to ReST.

Thanks for catching this.

Cheers,

Michael
