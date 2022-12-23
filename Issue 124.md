# Issue 124: Fix string comma errors with DihedralGroup(n) where n = 1,2 or 3

Issue created by migration from https://trac.sagemath.org/ticket/124

Original creator: moretti

Original creation time: 2006-10-10 06:07:35

Assignee: moretti

I get the following, indicating a bug with the way we send data to GAP.


```

sage: DihedralGroup(3)

Traceback (most recent call last):
    DihedralGroup(3)
  File "/home/moretti/sage/sage-1.4/local/lib/python2.5/", line 1, in <module>
    
  File
"/home/moretti/sage/sage-1.4/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py",
line 954, in __init__
    PermutationGroup_generic.__init__(self, [gen0, gen1], from_group = True)
  File
"/home/moretti/sage/sage-1.4/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py",
line 195, in __init__
    self.gens()
  File
"/home/moretti/sage/sage-1.4/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py",
line 342, in gens
    raise RuntimeError, "(It might be necessary to install the database_gap optional SAGE package,
if you haven't already.)\n%s"%s
RuntimeError: (It might be necessary to install the database_gap optional SAGE package, if you
haven't already.)
Gap produced error output
Syntax error: expression expected
$sage8:=Group([(1,2,3), ((1,3),)]);;
                               ^

   executing $sage8:=Group([(1,2,3), ((1,3),)]);;
```



---

Comment by moretti created at 2006-10-10 23:29:43

Resolution: fixed


---

Comment by moretti created at 2006-10-10 23:29:43

Replying to [ticket:124 moretti]:
> I get the following, indicating a bug with the way we send data to GAP.
> 
> {{{
> 
> sage: DihedralGroup(3)
> 
> Traceback (most recent call last):
>     DihedralGroup(3)
>   File "/home/moretti/sage/sage-1.4/local/lib/python2.5/", line 1, in <module>
>     
>   File
> "/home/moretti/sage/sage-1.4/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py",
> line 954, in __init__
>     PermutationGroup_generic.__init__(self, [gen0, gen1], from_group = True)
>   File
> "/home/moretti/sage/sage-1.4/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py",
> line 195, in __init__
>     self.gens()
>   File
> "/home/moretti/sage/sage-1.4/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py",
> line 342, in gens
>     raise RuntimeError, "(It might be necessary to install the database_gap optional SAGE package,
> if you haven't already.)\n%s"%s
> RuntimeError: (It might be necessary to install the database_gap optional SAGE package, if you
> haven't already.)
> Gap produced error output
> Syntax error: expression expected
> $sage8:=Group([(1,2,3), ((1,3),)]);;
>                                ^
> 
>    executing $sage8:=Group([(1,2,3), ((1,3),)]);;
> }}}

Fixed in patch #1410:d981cce6baa2
