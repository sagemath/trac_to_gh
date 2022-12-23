# Issue 7662: Chordal Graphs

Issue created by migration from https://trac.sagemath.org/ticket/7662

Original creator: ncohen

Original creation time: 2009-12-11 14:27:34

Assignee: rlm

Create a module for chordal graphs :

   * Perfect elimination order ( use 7541 )
   * Move is-chordal in this module
   * Polynomial-time algorithms for
        * Vertex coloring
        * Max clique/stable
   * MaxBFS
   * BFS*


---

Comment by ncohen created at 2010-06-06 11:00:42

Changing status from new to needs_work.


---

Comment by ncohen created at 2010-08-02 12:02:23

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-11-10 12:01:20

You should define what a "perfect elimination order" and a "hole" are in the documentation.


```
sage -t -long ./sage/graphs/generic_graph.py
**********************************************************************
File "/home/rlmill/sage-4.6/devel/sage-main/sage/graphs/generic_graph.py", line 8758:
    sage: (_, peo) = g.is_chordal(certificate = True)
Exception raised:
    Traceback (most recent call last):
      File "/home/rlmill/sage-4.6/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/rlmill/sage-4.6/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/rlmill/sage-4.6/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_135[7]>", line 1, in <module>
        (_, peo) = g.is_chordal(certificate = True)###line 8758:
    sage: (_, peo) = g.is_chordal(certificate = True)
      File "/home/rlmill/sage-4.6/local/lib/python/site-packages/sage/graphs/generic_graph.py", line 8854, in is_chordal
        return True, peo_copy
    NameError: global name 'peo_copy' is not defined
**********************************************************************
File "/home/rlmill/sage-4.6/devel/sage-main/sage/graphs/generic_graph.py", line 8759:
    sage: for v in peo:
          if not g.subgraph(g.neighbors(v)).is_clique():
               print "This should never happen !"
          g.delete_vertex(v)
Exception raised:
    Traceback (most recent call last):
      File "/home/rlmill/sage-4.6/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/rlmill/sage-4.6/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/rlmill/sage-4.6/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_135[8]>", line 1, in <module>
        for v in peo:###line 8759:
    sage: for v in peo:
    NameError: name 'peo' is not defined
**********************************************************************
```



---

Comment by rlm created at 2010-11-10 12:01:20

Changing status from needs_review to needs_work.


---

Comment by ncohen created at 2010-11-15 14:55:33

Hello ! I added a short definition of what a hole is (a cycle of length at least 4), and replaced peo_copy by peo (sorry for that `O_o`).

What about my `Such an ordering is called a Perfect Elimination Order` ? Would you like something more formal instead ?

Nathann


---

Comment by ncohen created at 2010-11-15 14:55:33

Changing status from needs_work to needs_info.


---

Comment by rlm created at 2010-11-26 10:37:46

Replying to [comment:5 ncohen]:
> What about my `Such an ordering is called a Perfect Elimination Order` ? Would you like something more formal instead ?

I'm not sure whether this is enough. Imagine a user who knows what the definition of chordal is, but not much else. You still want the documentation for this function to make sense to that user. Granted, it is not Sage's job to educate people about all of mathematics, but it certainly should be able to make clear what the input and output of each function is. Perhaps in this case it could do a better job of informing the user of what it is returning.

As long as you say what an elimination order is, then I think that's enough, but right now it is an undefined term.


---

Comment by rlm created at 2010-11-26 10:37:46

Changing status from needs_info to needs_work.


---

Attachment

What about this one, then ?

It was a good idea to explain it... I quite liked writing it `:-)`

Nathann


---

Comment by ncohen created at 2010-11-26 11:19:46

Changing status from needs_work to needs_review.


---

Comment by rlm created at 2010-11-26 16:34:00

Changing status from needs_review to positive_review.


---

Comment by rlm created at 2010-11-26 16:34:00

Much better! :)


---

Comment by jdemeyer created at 2011-01-12 06:31:19

Resolution: fixed
