# Issue 2981: Itanium (RHEL 5) -- error parsing gap output because of unaligned access kernel warning

Issue created by migration from https://trac.sagemath.org/ticket/2981

Original creator: was

Original creation time: 2008-04-21 03:22:37

Assignee: mabshoff

We can fix the following by better pexpect parsing.  Much much better though is
to get #2209 in, which would very likely resolve the problem below. 


```
File "/home/wstein/sage-3.0.rc0/tmp/const.py", line 2076:
    : C = G.cayley_graph(); C
Exception raised:
    Traceback (most recent call last):
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_67[2]>", line 1, in <module>
        C = G.cayley_graph(); C###line 2076:
    : C = G.cayley_graph(); C
      File "group.pyx", line 163, in sage.groups.group.FiniteGroup.cayley_graph (sage/groups/group.c:1376)
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/graphs/graph.py", line 7819, in __init__
        import networkx
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py", line 498, in __iter__
        for g in self.list():
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py", line 419, in list
        for i in range(1,n+1)]
      File "permgroup_element.pyx", line 267, in sage.groups.perm_gps.permgroup_element.PermutationGroupElement.__init__ (sage/groups/perm_gps/permgroup_
element.c:1861)
      File "<string>", line 1
         gap(18857): unaligned access to 0x60000fffff606cff, ip=0x400000000034a110
                   ^
     SyntaxError: invalid syntax
**********************************************************************
1 items had failures:
                                                                      
```



---

Comment by mabshoff created at 2008-04-21 04:34:10

This will be fixed by #2984.

Cheers,

Michael


---

Comment by mabshoff created at 2008-04-21 06:54:35

Fixed by merging #2984.


---

Comment by mabshoff created at 2008-04-21 06:54:35

Resolution: fixed
