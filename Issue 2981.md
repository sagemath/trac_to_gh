# Issue 2981: Itanium (RHEL 5) -- error parsing gap output because of unaligned access kernel warning

archive/issues_002981.json:
```json
{
    "body": "Assignee: mabshoff\n\nWe can fix the following by better pexpect parsing.  Much much better though is\nto get #2209 in, which would very likely resolve the problem below. \n\n\n```\nFile \"/home/wstein/sage-3.0.rc0/tmp/const.py\", line 2076:\n    : C = G.cayley_graph(); C\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wstein/sage-3.0.rc0/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_67[2]>\", line 1, in <module>\n        C = G.cayley_graph(); C###line 2076:\n    : C = G.cayley_graph(); C\n      File \"group.pyx\", line 163, in sage.groups.group.FiniteGroup.cayley_graph (sage/groups/group.c:1376)\n      File \"/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/graphs/graph.py\", line 7819, in __init__\n        import networkx\n      File \"/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py\", line 498, in __iter__\n        for g in self.list():\n      File \"/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/groups/perm_gps/permgroup.py\", line 419, in list\n        for i in range(1,n+1)]\n      File \"permgroup_element.pyx\", line 267, in sage.groups.perm_gps.permgroup_element.PermutationGroupElement.__init__ (sage/groups/perm_gps/permgroup_\nelement.c:1861)\n      File \"<string>\", line 1\n         gap(18857): unaligned access to 0x60000fffff606cff, ip=0x400000000034a110\n                   ^\n     SyntaxError: invalid syntax\n**********************************************************************\n1 items had failures:\n                                                                      \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2981\n\n",
    "created_at": "2008-04-21T03:22:37Z",
    "labels": [
        "porting",
        "major",
        "bug"
    ],
    "title": "Itanium (RHEL 5) -- error parsing gap output because of unaligned access kernel warning",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2981",
    "user": "was"
}
```
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


Issue created by migration from https://trac.sagemath.org/ticket/2981





---

archive/issue_comments_020529.json:
```json
{
    "body": "This will be fixed by #2984.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-21T04:34:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2981#issuecomment-20529",
    "user": "mabshoff"
}
```

This will be fixed by #2984.

Cheers,

Michael



---

archive/issue_comments_020530.json:
```json
{
    "body": "Fixed by merging #2984.",
    "created_at": "2008-04-21T06:54:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2981#issuecomment-20530",
    "user": "mabshoff"
}
```

Fixed by merging #2984.



---

archive/issue_comments_020531.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-21T06:54:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2981",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2981#issuecomment-20531",
    "user": "mabshoff"
}
```

Resolution: fixed
