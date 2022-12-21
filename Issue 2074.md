# Issue 2074: PermutationGroupElement constructor bug.

Issue created by migration from Trac.

Original creator: boothby

Original creation time: 2008-02-06 09:41:23

Assignee: boothby

Getting a permutation with empty, or singleton tuples blows up.


```
sage: G = SymmetricGroup(10)
sage: G(((1,2,3),(4,),(5,)))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/boothby/.sage/sage_notebook/worksheets/admin/15/code/148.py", line 5, in <module>
    G(((Integer(1),Integer(2),Integer(3)),(Integer(4),),(Integer(4),)))
  File "/home/boothby/sage/local/lib/python2.5/site-packages/sympy/plotting/", line 1, in <module>
    
  File "/home/boothby/sagebuilds/sage-2.9.3/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py", line 298, in __call__
    return PermutationGroupElement([x], self, check = check)
  File "permgroup_element.pyx", line 239, in sage.groups.perm_gps.permgroup_element.PermutationGroupElement.__init__
  File "/home/boothby/sagebuilds/sage-2.9.3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 738, in __call__
    return cls(self, x)
  File "/home/boothby/sagebuilds/sage-2.9.3/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 989, in __init__
    raise TypeError, x
TypeError: Gap produced error output
Syntax error: expression expected
$sage156:=((1,2,3)(4,)(4,));;
                     ^

   executing $sage156:=((1,2,3)(4,)(4,));;
```


Similarly, a tuple consisting of a single cycle blows up:


```
sage: G(((1,2,3),))
Exception (click to the left for traceback):
...
   executing $sage163:=((1,2,3),);;
```



---

Attachment


---

Attachment

Apply the second patch -- positive review.


---

Comment by mabshoff created at 2008-02-07 09:59:52

Resolution: fixed


---

Comment by mabshoff created at 2008-02-07 09:59:52

Merged in Sage 2.10.2.alpha0
