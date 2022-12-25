# Issue 124: Fix string comma errors with DihedralGroup(n) where n = 1,2 or 3

archive/issues_000124.json:
```json
{
    "body": "Assignee: @bobmoretti\n\nI get the following, indicating a bug with the way we send data to GAP.\n\n\n```\n\nsage: DihedralGroup(3)\n\nTraceback (most recent call last):\n    DihedralGroup(3)\n  File \"/home/moretti/sage/sage-1.4/local/lib/python2.5/\", line 1, in <module>\n    \n  File\n\"/home/moretti/sage/sage-1.4/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py\",\nline 954, in __init__\n    PermutationGroup_generic.__init__(self, [gen0, gen1], from_group = True)\n  File\n\"/home/moretti/sage/sage-1.4/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py\",\nline 195, in __init__\n    self.gens()\n  File\n\"/home/moretti/sage/sage-1.4/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py\",\nline 342, in gens\n    raise RuntimeError, \"(It might be necessary to install the database_gap optional SAGE package,\nif you haven't already.)\\n%s\"%s\nRuntimeError: (It might be necessary to install the database_gap optional SAGE package, if you\nhaven't already.)\nGap produced error output\nSyntax error: expression expected\n$sage8:=Group([(1,2,3), ((1,3),)]);;\n                               ^\n\n   executing $sage8:=Group([(1,2,3), ((1,3),)]);;\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/124\n\n",
    "created_at": "2006-10-10T06:07:35Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "title": "Fix string comma errors with DihedralGroup(n) where n = 1,2 or 3",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/124",
    "user": "https://github.com/bobmoretti"
}
```
Assignee: @bobmoretti

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


Issue created by migration from https://trac.sagemath.org/ticket/124





---

archive/issue_comments_000564.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2006-10-10T23:29:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/124#issuecomment-564",
    "user": "https://github.com/bobmoretti"
}
```

Resolution: fixed



---

archive/issue_comments_000565.json:
```json
{
    "body": "Replying to [ticket:124 moretti]:\n> I get the following, indicating a bug with the way we send data to GAP.\n> \n> {{{\n> \n> sage: DihedralGroup(3)\n> \n> Traceback (most recent call last):\n>     DihedralGroup(3)\n>   File \"/home/moretti/sage/sage-1.4/local/lib/python2.5/\", line 1, in <module>\n>     \n>   File\n> \"/home/moretti/sage/sage-1.4/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py\",\n> line 954, in __init__\n>     PermutationGroup_generic.__init__(self, [gen0, gen1], from_group = True)\n>   File\n> \"/home/moretti/sage/sage-1.4/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py\",\n> line 195, in __init__\n>     self.gens()\n>   File\n> \"/home/moretti/sage/sage-1.4/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py\",\n> line 342, in gens\n>     raise RuntimeError, \"(It might be necessary to install the database_gap optional SAGE package,\n> if you haven't already.)\\n%s\"%s\n> RuntimeError: (It might be necessary to install the database_gap optional SAGE package, if you\n> haven't already.)\n> Gap produced error output\n> Syntax error: expression expected\n> $sage8:=Group([(1,2,3), ((1,3),)]);;\n>                                ^\n> \n>    executing $sage8:=Group([(1,2,3), ((1,3),)]);;\n> }}}\n\nFixed in patch #1410:d981cce6baa2",
    "created_at": "2006-10-10T23:29:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/124",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/124#issuecomment-565",
    "user": "https://github.com/bobmoretti"
}
```

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



---

archive/issue_events_000130.json:
```json
{
    "actor": "@bobmoretti",
    "created_at": "2006-10-10T23:29:43Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/124",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/124#event-130"
}
```
