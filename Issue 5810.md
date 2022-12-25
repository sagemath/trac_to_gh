# Issue 5810: Sage 3.4.1.rc3: Fedora 10/64 - unable to start Maxima issue in shapes.pyx

archive/issues_005810.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe following pops up regularly on some FC10 systems:\n\n```\nsage -t -long \"devel/sage/sage/plot/plot3d/shapes.pyx\"      Exception exceptions.TypeError: TypeError(RuntimeError('Unable to start maxima',),) in 'sage.structure.parent_old._unregister_pair' ignored\n**********************************************************************\nFile \"/space/wstein/farm/sage-3.4.1.rc3/devel/sage/sage/plot/plot3d/shapes.pyx\", line 267:\n    sage: G += sum(Cylinder(.2, 1).translate(cos(2*pi*n/9), sin(2*pi*n/9), 0) for n in [1..9])Exception raised:\n    Traceback (most recent call last):\n      File \"/space/wstein/farm/sage-3.4.1.rc3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/space/wstein/farm/sage-3.4.1.rc3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/space/wstein/farm/sage-3.4.1.rc3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_10[7]>\", line 1, in <module>\n        G += sum(Cylinder(RealNumber('.2'), Integer(1)).translate(cos(Integer(2)*pi*n/Integer(9)), sin(Integer(2)*pi*n/Integer(9)), Integer(0)) for n in (ellipsis_range(I\nnteger(1),Ellipsis,Integer(9))))###line 267:\n    sage: G += sum(Cylinder(.2, 1).translate(cos(2*pi*n/9), sin(2*pi*n/9), 0) for n in [1..9])\n      File \"<doctest __main__.example_10[7]>\", line 1, in <genexpr>\n        G += sum(Cylinder(RealNumber('.2'), Integer(1)).translate(cos(Integer(2)*pi*n/Integer(9)), sin(Integer(2)*pi*n/Integer(9)), Integer(0)) for n in (ellipsis_range(I\nnteger(1),Ellipsis,Integer(9))))###line 267:\n    sage: G += sum(Cylinder(.2, 1).translate(cos(2*pi*n/9), sin(2*pi*n/9), 0) for n in [1..9])\n      File \"element.pyx\", line 1154, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:10558)\n      File \"coerce.pyx\", line 706, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6543)\n      File \"coerce.pyx\", line 1152, in sage.structure.coerce.CoercionModel_cache_maps.get_action (sage/structure/coerce.c:11646)\n      File \"coerce.pyx\", line 1275, in sage.structure.coerce.CoercionModel_cache_maps.discover_action (sage/structure/coerce.c:12920)\n      File \"parent.pyx\", line 1142, in sage.structure.parent.Parent.get_action (sage/structure/parent.c:11816)\n      File \"parent_old.pyx\", line 586, in sage.structure.parent_old.Parent._get_action_ (sage/structure/parent_old.c:8141)\n      File \"parent_old.pyx\", line 197, in sage.structure.parent_old.Parent.get_action_c (sage/structure/parent_old.c:2998)\n      File \"parent_old.pyx\", line 209, in sage.structure.parent_old.Parent.get_action_impl (sage/structure/parent_old.c:3333)\n      File \"parent_old.pyx\", line 268, in sage.structure.parent_old.Parent.get_action_c_impl (sage/structure/parent_old.c:4193)\n      File \"parent_old.pyx\", line 635, in sage.structure.parent_old._register_pair (sage/structure/parent_old.c:9303)\n    NotImplementedError: Infinite loop in multiplication of \n                                           0 (parent Symbolic Ring) and 1 (parent Integer Ring)!\n**********************************************************************\n```\n\n\nOne would guess that disabling mmap in Maxima might fix this.\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/5810\n\n",
    "created_at": "2009-04-17T11:27:10Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "Sage 3.4.1.rc3: Fedora 10/64 - unable to start Maxima issue in shapes.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5810",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

The following pops up regularly on some FC10 systems:

```
sage -t -long "devel/sage/sage/plot/plot3d/shapes.pyx"      Exception exceptions.TypeError: TypeError(RuntimeError('Unable to start maxima',),) in 'sage.structure.parent_old._unregister_pair' ignored
**********************************************************************
File "/space/wstein/farm/sage-3.4.1.rc3/devel/sage/sage/plot/plot3d/shapes.pyx", line 267:
    sage: G += sum(Cylinder(.2, 1).translate(cos(2*pi*n/9), sin(2*pi*n/9), 0) for n in [1..9])Exception raised:
    Traceback (most recent call last):
      File "/space/wstein/farm/sage-3.4.1.rc3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/space/wstein/farm/sage-3.4.1.rc3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/space/wstein/farm/sage-3.4.1.rc3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[7]>", line 1, in <module>
        G += sum(Cylinder(RealNumber('.2'), Integer(1)).translate(cos(Integer(2)*pi*n/Integer(9)), sin(Integer(2)*pi*n/Integer(9)), Integer(0)) for n in (ellipsis_range(I
nteger(1),Ellipsis,Integer(9))))###line 267:
    sage: G += sum(Cylinder(.2, 1).translate(cos(2*pi*n/9), sin(2*pi*n/9), 0) for n in [1..9])
      File "<doctest __main__.example_10[7]>", line 1, in <genexpr>
        G += sum(Cylinder(RealNumber('.2'), Integer(1)).translate(cos(Integer(2)*pi*n/Integer(9)), sin(Integer(2)*pi*n/Integer(9)), Integer(0)) for n in (ellipsis_range(I
nteger(1),Ellipsis,Integer(9))))###line 267:
    sage: G += sum(Cylinder(.2, 1).translate(cos(2*pi*n/9), sin(2*pi*n/9), 0) for n in [1..9])
      File "element.pyx", line 1154, in sage.structure.element.RingElement.__mul__ (sage/structure/element.c:10558)
      File "coerce.pyx", line 706, in sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/structure/coerce.c:6543)
      File "coerce.pyx", line 1152, in sage.structure.coerce.CoercionModel_cache_maps.get_action (sage/structure/coerce.c:11646)
      File "coerce.pyx", line 1275, in sage.structure.coerce.CoercionModel_cache_maps.discover_action (sage/structure/coerce.c:12920)
      File "parent.pyx", line 1142, in sage.structure.parent.Parent.get_action (sage/structure/parent.c:11816)
      File "parent_old.pyx", line 586, in sage.structure.parent_old.Parent._get_action_ (sage/structure/parent_old.c:8141)
      File "parent_old.pyx", line 197, in sage.structure.parent_old.Parent.get_action_c (sage/structure/parent_old.c:2998)
      File "parent_old.pyx", line 209, in sage.structure.parent_old.Parent.get_action_impl (sage/structure/parent_old.c:3333)
      File "parent_old.pyx", line 268, in sage.structure.parent_old.Parent.get_action_c_impl (sage/structure/parent_old.c:4193)
      File "parent_old.pyx", line 635, in sage.structure.parent_old._register_pair (sage/structure/parent_old.c:9303)
    NotImplementedError: Infinite loop in multiplication of 
                                           0 (parent Symbolic Ring) and 1 (parent Integer Ring)!
**********************************************************************
```


One would guess that disabling mmap in Maxima might fix this.

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/5810





---

archive/issue_comments_045547.json:
```json
{
    "body": "The disabling of mmap should happen in #5662, so hopefully that ticket will fix it.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-19T00:17:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5810#issuecomment-45547",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The disabling of mmap should happen in #5662, so hopefully that ticket will fix it.

Cheers,

Michael



---

archive/issue_comments_045548.json:
```json
{
    "body": "The updated clisp-2.47.spkg seems to fix this. I am rerunning doctests on the box to see if any other problems are popping up.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-19T06:32:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5810#issuecomment-45548",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The updated clisp-2.47.spkg seems to fix this. I am rerunning doctests on the box to see if any other problems are popping up.

Cheers,

Michael



---

archive/issue_comments_045549.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-20T03:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5810#issuecomment-45549",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_045550.json:
```json
{
    "body": "This has been fixed by #5662 and #5823.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-20T03:11:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5810",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5810#issuecomment-45550",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This has been fixed by #5662 and #5823.

Cheers,

Michael



---

archive/issue_events_013638.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-20T03:11:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5810",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5810#event-13638"
}
```
