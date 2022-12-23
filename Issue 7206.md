# Issue 7206: doctest failure in groups/perm_gps/permgroup.py

Issue created by migration from https://trac.sagemath.org/ticket/7206

Original creator: ddrake

Original creation time: 2009-10-14 03:02:20

Assignee: joyner

With 4.1.2.rc2, I have one doctest failure on Ubuntu 9.04 amd64:

```
drake@sagenb:~/s/sage-4.1.2.rc2$ ./sage -t  devel/sage/sage/groups/perm_gps/permgroup.py
  sage -t  "devel/sage/sage/groups/perm_gps/permgroup.py"    
  **********************************************************************
  File "/home/drake/s/sage-4.1.2.rc2/devel/sage/sage/groups/perm_gps/permgroup.py", line 1114:
      sage: G.random_element()
  Expected:
      (1,2)(4,5)
  Got:
      (2,3)(4,5)
  **********************************************************************
  1 items had failures:
     1 of   4 in __main__.example_34
  ***Test Failed*** 1 failures.
  For whitespace errors, see the file /home/drake/.sage//tmp/.doctest_permgroup.py
           [6.7 s]
  exit code: 1024

  ----------------------------------------------------------------------
  The following tests failed:

          sage -t  "devel/sage/sage/groups/perm_gps/permgroup.py" 
```


This seems like #5584 again. I ran a bisect and it blames #6647.


---

Comment by nborie created at 2009-10-14 12:38:01

Hy Dan,

With 4.1.1 and sage-combinat queue applied (the patch come from here : #6647), I have

```
nicolas@nicolas-laptop:/opt/sage/devel/sage-combinat$ sage -t sage/groups/perm_gps/permgroup.py 
sage -t  "devel/sage-combinat/sage/groups/perm_gps/permgroup.py"
	 [5.4 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 5.4 seconds
```


But, if I play with the method .random_element()

```
sage: G = PermutationGroup([[(1,2,3),(4,5)],[(1,2)]])
sage: G.random_element()
()
sage: G.random_element()
(4,5)
sage: G.random_element()
(1,3,2)(4,5)
sage: G.random_element()
(1,3,2)
sage: G.random_element()
(2,3)(4,5)
sage: G = PermutationGroup([[(1,2,3),(4,5)],[(1,2)]])
sage: G.random_element()                             
(4,5)
sage: G.random_element()
(1,3,2)
sage: G.random_element()
(1,3,2)
sage: G = PermutationGroup([[(1,2,3),(4,5)],[(1,2)]])
sage: G.random_element()                             
(2,3)(4,5)
sage: G = PermutationGroup([[(1,2,3),(4,5)],[(1,2)]])
sage: G.random_element()                             
(1,3,2)
sage: G = PermutationGroup([[(1,2,3),(4,5)],[(1,2)]])
sage: G.random_element()                             
(1,3)
```


I saw your pointer from my patch about strong generating system. I didn't touch random_element(). I would be very happy to help and investigate this but my guess is that touch interface and Gap behavior... I don't know even if it is possible to put a doctest on such random method where the random part is inside Gap and not inside Sage...

I don't really know that is very important in this doctest, a possible trick is

```
sage: G = PermutationGroup([[(1,2,3),(4,5)],[(1,2)]])
sage: G.random_element() in G                        
True
```

Here, one's can be sure there no timestamps random dependencies of Gap or other things I should not say because I really don't know anything about random and Gap.

If anyone know something about that ?


---

Comment by ddrake created at 2009-10-15 02:13:35

Hi Nicolas...

First, don't worry, nobody is blaming you! I did go look at #6647, and I don't see why it should cause the doctest failure. Above, you get many different results for `random_element()`, but when running the doctests, the random seed is reset every time, so the random element is actually not random at all. :)  Perhaps your "`G.random_element() in G`" doctest would be just as good.


---

Comment by chapoton created at 2013-10-27 15:37:29

no such doctest failure in 5.13.beta1

ticket can be closed as invalid


---

Comment by chapoton created at 2013-10-27 15:37:29

Changing status from new to needs_review.


---

Comment by chapoton created at 2013-10-27 15:37:43

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-10-31 08:30:25

Resolution: worksforme
