# Issue 9830: Strange behaviour of Permutation(list) when list contains 0

Issue created by migration from https://trac.sagemath.org/ticket/9831

Original creator: mmezzarobba

Original creation time: 2010-08-28 08:13:00

Assignee: sage-combinat

CC:  brunellus


```
~$ ulimit -v 1048576 
~$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: Permutation([1]).signature()
1
sage: Permutation([0]).signature()
-1
sage: Permutation([1,0]).signature()
-1
sage: Permutation([0,1]).signature()
---------------------------------------------------------------------------
MemoryError                               Traceback (most recent call last)
| Sage Version 4.5.1, Release Date: 2010-07-19                       |
| Type notebook() for the GUI, and license() for information.        |
/home/marc/<ipython console> in <module>()

/data/sage-4.5.1/local/lib/python2.6/site-packages/sage/combinat/permutation.pyc in signature(p)
    739             -1
    740         """
--> 741         return (-1)**(len(p)-len(p.to_cycles()))
    742     
    743 

/data/sage-4.5.1/local/lib/python2.6/site-packages/sage/combinat/permutation.pyc in to_cycles(self, singletons)
    556             l[i], next = False, l[i]
    557             while next != cycleFirst:
--> 558                 cycle.append( next )
    559                 l[next - 1], next  = False, l[next - 1]
    560             #Add the cycle to the list of cycles

MemoryError:
```



---

Comment by lftabera created at 2010-09-08 13:00:33

Yes, Permutation should check the input. Moreover, it should be better documented.


In cycle notation:


```
sage: Permutation([(1,2),(3,4),(1,3)])
[3, 1, 1, 3]
```


which is not a permutation.


---

Attachment


---

Comment by nharris created at 2010-11-07 04:03:35

Changing status from new to needs_work.


---

Comment by nharris created at 2010-11-07 04:03:35

I've uploaded a patch which takes care of this issue.  (It also allows Permutation to take a list of non-disjoint tuples.)  There's still some work to be done, as the patch breaks several doctests:


```
----------------------------------------------------------------------

The following tests failed:

	sage -t -long devel/sage-test/doc/en/bordeaux_2008/generators_for_rings.rst # 4 doctests failed
	sage -t -long devel/sage-test/sage/combinat/integer_vector_weighted.py # 7 doctests failed
	sage -t -long devel/sage-test/sage/combinat/posets/hasse_diagram.py # 1 doctests failed
	sage -t -long devel/sage-test/sage/combinat/posets/poset_examples.py # 6 doctests failed
	sage -t -long devel/sage-test/sage/misc/sagedoc.py # 3 doctests failed
	sage -t -long devel/sage-test/sage/modular/modform/find_generators.py # 18 doctests failed
	sage -t -long devel/sage-test/sage/plot/plot3d/base.pyx # 4 doctests failed
	sage -t -long devel/sage-test/sage/modular/ssmod/ssmod.py # Time out
----------------------------------------------------------------------
```



---

Comment by brunellus created at 2011-12-02 15:10:21

Please note that this ticket duplicates #8392, which also contains some patch. Moreover, it links to [a discussion](http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/c6a39caca9df29dc) on combinat-devel, where an additional computational load of the check is considered.

Would you mind if I resolve failing doctests? I am new to the Sage development, so I am not sure whether someone is working on this issue right now.


---

Comment by brunellus created at 2011-12-31 01:44:18

Large portion of the errors was caused by integer_vector_weighted that used permutation multiplication instead of permutation acting on list.


---

Attachment

Now, I would like to send this to review, because I see no more error (maybe I overlooked some?). But the original patch refuses to apply -- I guess it's because codebase shifted somehow in last year. Is this a problem I should correct?


---

Comment by mhansen created at 2013-07-22 15:28:55

This is indeed a duplicate of #8392 which has been merged.


---

Comment by mhansen created at 2013-07-22 15:28:55

Resolution: duplicate
