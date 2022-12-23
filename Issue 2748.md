# Issue 2748: Permutation constructor does not accept lists of tuples

Issue created by migration from https://trac.sagemath.org/ticket/2748

Original creator: ddrake

Original creation time: 2008-04-01 01:42:23

Assignee: ddrake

CC:  sage-combinat

Keywords: combinat, permutations

The following works:


```
sage: p = ((1, 2, 4, 5, 3, 6))
sage: q = Permutation(p)
sage: q.to_cycles()
[(1, 2, 4, 5, 3, 6)]
sage: q.cycle_type()
[6]
```


...but if `p` is a list of tuples, it doesn't, and Permutation doesn't tell you that it's not happy with the input:


```
sage: p = [(1, 2, 4, 5, 3, 6)]
sage: q = Permutation(p)
sage: q.to_cycles()
---------------------------------------------------------------------------
<type 'exceptions.ValueError'>            Traceback (most recent call last)

/home/drake/code/sage/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/combinat/permutation.py in to_cycles(self, singletons)
    415             else:
    416                 cycle.append( next )    
--> 417                 l.remove( next )
    418                 toConsider = next
    419 

<type 'exceptions.ValueError'>: list.remove(x): x not in list
```



---

Attachment


---

Comment by mhansen created at 2008-04-07 08:19:06

Looks good to me.


---

Comment by mabshoff created at 2008-04-07 14:44:35

Resolution: fixed


---

Comment by mabshoff created at 2008-04-07 14:44:35

Merged in Sage 3.0.alpha3
