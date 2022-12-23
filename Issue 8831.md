# Issue 8831: fail to build PDF version of reference manual in Sage 4.4.1.alpha2

Issue created by migration from https://trac.sagemath.org/ticket/8831

Original creator: mvngu

Original creation time: 2010-04-30 19:28:09

Assignee: mvngu

As the subject says. Even after fixing warnings in building the HTML version of the reference manual as per #8819, building the PDF version hangs while processing a reference to graphviz:

```
Underfull \hbox (badness 6380) in paragraph at lines 410101--410105
[]\T1/ptm/m/n/10 Aric Hag-berg, Dan Schult and Pieter Swart. Net-workX doc-u-me
n-ta-tion. [On-line] Avail-able:
! Missing $ inserted.
<inserted text> 
                $
l.410122 \bibitem[dot_spec]{dot_spec}
                                     {\hypertarget{dot_spec}{}
```

This is traced to the function `graphviz_string()` in `sage/graphs/generic_graph.py`


---

Attachment

based on Sage 4.4.1.alpha2


---

Comment by mvngu created at 2010-04-30 19:48:53

Changing status from new to needs_review.


---

Comment by was created at 2010-05-02 16:44:03

Resolution: fixed
