# Issue 4675: Get Josh Kantor's "Numerical Computing with SAGE" into the Sage documentation

Issue created by migration from https://trac.sagemath.org/ticket/4675

Original creator: mabshoff

Original creation time: 2008-12-02 15:52:14

Assignee: jkantor

See http://www.math.washington.edu/~jkantor/Numerical_Sage/Numerical_Sage.html

Cheers,

Michael


---

Comment by was created at 2008-12-02 17:25:09

Just for the record, this document is already technically "in the Sage Documentation", since it has shipped with Sage for months here:


```
SAGE_ROOT/devel/doc/overviews/numerical_sage
```


not that anybody would notice... and of course it needs to be sphinxed.


---

Comment by mabshoff created at 2008-12-05 01:30:19

Ok, changes the summary to reflect William's comment.

Cheers,

Michael


---

Comment by jhpalmieri created at 2009-02-26 17:41:43

"Numerical computing with Sage" is in the new docs, and you can build it with 'sage -docbuild numerical_sage html' or something like that.  The same goes for a few other pieces of documentation: "bordeaux_2008" and "a_tour_of_sage".

So can this be closed, or was there something else to be done on this ticket?


---

Comment by mabshoff created at 2009-02-26 17:44:45

Resolution: fixed


---

Comment by mabshoff created at 2009-02-26 17:44:45

This can be closed for Sage 3.4.alpha0 due to Mike's work on the conversation of the doc repo.

Should anything be left or improvements need to be made this should be addressed via a more specific ticket since this one is rather general.

Cheers,

Michael
