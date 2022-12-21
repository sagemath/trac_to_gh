# Issue 6242: *long* birds_other.rst doctest fails with mysterious error repeatedly on OS X

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-06-07 13:36:47

Assignee: was


```
wstein`@`bsd:~/build/sage-4.0.1$ ./sage -t -long "devel/sage/doc/en/bordeaux_2008/birds_other.rst"
sage -t -long "devel/sage/doc/en/bordeaux_2008/birds_other.rst"
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
         [44.5 s]
exit code: 768

----------------------------------------------------------------------
The following tests failed:


        sage -t -long "devel/sage/doc/en/bordeaux_2008/birds_other.rst"

wstein`@`bsd:~/build/sage-4.0.1$ ./sage -t  "devel/sage/doc/en/bordeaux_2008/birds_other.rst"
sage -t  "devel/sage/doc/en/bordeaux_2008/birds_other.rst"  
         [39.5 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 39.5 seconds
wstein`@`bsd:~/build/sage-4.0.1$ 

```



---

Comment by was created at 2009-06-07 13:37:54

The failure does not happen in --verbose mode. :-(


---

Comment by was created at 2009-06-15 23:37:12

This happens very sporadically, and is triggered by the parallel bernoulli number code by David Harvey.


---

Comment by was created at 2009-06-15 23:37:12

Changing priority from blocker to critical.


---

Comment by craigcitro created at 2009-06-19 04:47:11

This is a duplicate of #6304, where David Harvey has made some more specific comments about what's causing this.


---

Comment by craigcitro created at 2009-06-19 04:47:11

Resolution: duplicate
