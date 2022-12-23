# Issue 5327: multiple edge plots use symbolic computations

Issue created by migration from https://trac.sagemath.org/ticket/5327

Original creator: rlm

Original creation time: 2009-02-21 02:35:37

Assignee: rlm


```
sage: S = SupersingularModule(389)
sage: H = S.hecke_matrix(2)
sage: D = DiGraph(H)
sage: P = D.plot()
^CControl-C pressed.  Interrupting Maxima. Please wait a few seconds...
```


Maxima is absolutely not the thing to use here: I see in `graph_plot.py` the use of

```
x = SymbolicVariable('x')
d = SymbolicVariable('d')
```

etc.

Probably my bad for letting that past review.


---

Attachment


---

Comment by was created at 2009-02-21 03:57:39

Excellent.  I'm glad you were so fast with this and that you (rlm) got to look like Bill Gates doing the demo today instead of me looking like that again at Microsoft!


---

Comment by mabshoff created at 2009-02-21 09:42:43

Resolution: fixed


---

Comment by mabshoff created at 2009-02-21 09:42:43

Merged in Sage 3.3.final.

Cheers,

Michael
