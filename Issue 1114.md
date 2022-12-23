# Issue 1114: Delete a file to fix an example involving the sage latex mode

Issue created by migration from https://trac.sagemath.org/ticket/1114

Original creator: was

Original creation time: 2007-11-06 16:25:11

Assignee: tba


```

This is for a 2.8.10 installation so apologies if it has been fixed.

The file examples/latex_embed/E2.sobj contains bad cached data so that
when you run "sage example.sage" you get a run-time error, even though
example.tex is correct!   The clue came from looking at the backup
file #example.tex#.   Since the script cleverly only does a long
computation when the result has not been stored, it keeps on using the
bad data (just an array subscript out of range).  The solution is to
delete file E2.sobj .

I didn't think this was worth a trac ticket...
```


Yes it is, or it will be lost...


---

Comment by was created at 2007-11-07 05:22:13

Resolution: fixed
