# Issue 2980: itanium (RHEL 5) -- weyl_group.py is broken on itanium

archive/issues_002980.json:
```json
{
    "body": "Assignee: @mwhansen\n\n```\nsage -t  devel/sage/sage/combinat/root_system/weyl_group.py **********************************************************************\nFile \"/home/wstein/sage-3.0.rc0/tmp/weyl_group.py\", line 235:\n    sage: [WeylGroup(t).long_element().length() for t in ['A',5],['B',3],['C',3],['D',4],['G',2],['F',4],['E',6]]\nException raised:\n    Traceback (most recent call last):\n      File \"/home/wstein/sage-3.0.rc0/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_13[1]>\", line 1, in <module>\n        [WeylGroup(t).long_element().length() for t in ['A',Integer(5)],['B',Integer(3)],['C',Integer(3)],['D',Integer(4)],['G',Integer(2)],['F',Integer(\n4)],['E',Integer(6)]]###line 235:\n    sage: [WeylGroup(t).long_element().length() for t in ['A',5],['B',3],['C',3],['D',4],['G',2],['F',4],['E',6]]\n      File \"/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/combinat/root_system/weyl_group.py\", line 271, in long_element\n        return self.__call__(m)\n      File \"/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/combinat/root_system/weyl_group.py\", line 146, in __call__\n        raise TypeError, \"no way to coerce element into self.\"\n    TypeError: no way to coerce element into self.\n**********************************************************************\n1 items had failures:\n   1 of   2 in __main__.example_13\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /home/wstein/sage-3.0.rc0/tmp/.doctest_weyl_group.py\n         [61.1 s]\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/2980\n\n",
    "created_at": "2008-04-21T03:21:13Z",
    "labels": [
        "component: porting",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "itanium (RHEL 5) -- weyl_group.py is broken on itanium",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2980",
    "user": "https://github.com/williamstein"
}
```
Assignee: @mwhansen

```
sage -t  devel/sage/sage/combinat/root_system/weyl_group.py **********************************************************************
File "/home/wstein/sage-3.0.rc0/tmp/weyl_group.py", line 235:
    sage: [WeylGroup(t).long_element().length() for t in ['A',5],['B',3],['C',3],['D',4],['G',2],['F',4],['E',6]]
Exception raised:
    Traceback (most recent call last):
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_13[1]>", line 1, in <module>
        [WeylGroup(t).long_element().length() for t in ['A',Integer(5)],['B',Integer(3)],['C',Integer(3)],['D',Integer(4)],['G',Integer(2)],['F',Integer(
4)],['E',Integer(6)]]###line 235:
    sage: [WeylGroup(t).long_element().length() for t in ['A',5],['B',3],['C',3],['D',4],['G',2],['F',4],['E',6]]
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/combinat/root_system/weyl_group.py", line 271, in long_element
        return self.__call__(m)
      File "/home/wstein/sage-3.0.rc0/local/lib/python2.5/site-packages/sage/combinat/root_system/weyl_group.py", line 146, in __call__
        raise TypeError, "no way to coerce element into self."
    TypeError: no way to coerce element into self.
**********************************************************************
1 items had failures:
   1 of   2 in __main__.example_13
***Test Failed*** 1 failures.
For whitespace errors, see the file /home/wstein/sage-3.0.rc0/tmp/.doctest_weyl_group.py
         [61.1 s]
```

Issue created by migration from https://trac.sagemath.org/ticket/2980





---

archive/issue_comments_020482.json:
```json
{
    "body": "```\n20:18 < mhansen> That Weyl group issue on Itanium is weird.  The code that raises that error is from a call \n                 in GAP.\n20:19 < wstein> Gap is potentially broken on itanium.\n20:19 < wstein> We have to build it -O0 to get it to build at all.\n20:19 < wstein> So possibly all problems originate from that.\n20:20 < wstein> See #2209.\n20:20 < mhansen> I'm pretty sure that's the issue since the code causing that error is very simple and works \n                 on lots of other things.\n\n```",
    "created_at": "2008-04-21T03:26:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2980#issuecomment-20482",
    "user": "https://github.com/williamstein"
}
```

```
20:18 < mhansen> That Weyl group issue on Itanium is weird.  The code that raises that error is from a call 
                 in GAP.
20:19 < wstein> Gap is potentially broken on itanium.
20:19 < wstein> We have to build it -O0 to get it to build at all.
20:19 < wstein> So possibly all problems originate from that.
20:20 < wstein> See #2209.
20:20 < mhansen> I'm pretty sure that's the issue since the code causing that error is very simple and works 
                 on lots of other things.

```



---

archive/issue_events_006802.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-21T04:34:37Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/2980",
    "milestone": "sage-3.0",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2980#event-6802"
}
```



---

archive/issue_comments_020483.json:
```json
{
    "body": "This will be fixed by #2984.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-21T04:34:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2980#issuecomment-20483",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This will be fixed by #2984.

Cheers,

Michael



---

archive/issue_comments_020484.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-21T06:54:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2980#issuecomment-20484",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_020485.json:
```json
{
    "body": "Fixed by merging #2984.",
    "created_at": "2008-04-21T06:54:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2980",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2980#issuecomment-20485",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Fixed by merging #2984.



---

archive/issue_events_006803.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-21T06:54:26Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2980",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2980#event-6803"
}
```
