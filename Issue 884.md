# Issue 884: 2.8.7-alpha0: doctest failure in rings/residue_field.pyx

archive/issues_000884.json:
```json
{
    "body": "Assignee: failure\n\nOn sage.math, the rings/residue_field.pyx doctest fails as follows in 2.8.7:\n\n```\nsage -t  devel/sage-rtest/sage/rings/residue_field.pyx      **********************************************************************\nFile \"residue_field.pyx\", line 364:\n    sage: b*c^2\nException raised:\n    Traceback (most recent call last):\n      File \"/home/cwitty/pre-sage/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_15[8]>\", line 1, in <module>\n        b*c**Integer(2)###line 364:\n    sage: b*c^2\n      File \"element.pyx\", line 1463, in element.RingElement.__pow__\n      File \"element.pyx\", line 2777, in element.generic_power_c\n      File \"element.pyx\", line 1376, in element.RingElement.__mul__\n      File \"coerce.pxi\", line 126, in element._mul_c\n    RuntimeError\n**********************************************************************\nFile \"residue_field.pyx\", line 221:\n    sage: k.coerce_map_from(OK)(OK(a)^7)\nException raised:\n    Traceback (most recent call last):\n      File \"/home/cwitty/pre-sage/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_9[4]>\", line 1, in <module>\n        k.coerce_map_from(OK)(OK(a)**Integer(7))###line 221:\n    sage: k.coerce_map_from(OK)(OK(a)^7)\n      File \"element.pyx\", line 1463, in element.RingElement.__pow__\n      File \"element.pyx\", line 2782, in element.generic_power_c\n      File \"element.pyx\", line 1376, in element.RingElement.__mul__\n      File \"coerce.pxi\", line 126, in element._mul_c\n    RuntimeError\n**********************************************************************\n2 items had failures:\n   1 of  10 in __main__.example_15\n   1 of   5 in __main__.example_9\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file .doctest_residue_field.pyxException exceptions.AttributeError: \"'AbsoluteOrder' object has no attribute 'polynomial_ntl'\" in 'number_field_element.NumberFieldElement_absolute._parent_poly_c_' ignored\nZZX: division by zero\nException exceptions.AttributeError: \"'AbsoluteOrder' object has no attribute 'polynomial_ntl'\" in 'number_field_element.NumberFieldElement_absolute._parent_poly_c_' ignored\nZZX: division by zero\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/884\n\n",
    "created_at": "2007-10-13T20:19:37Z",
    "labels": [
        "component: doctest coverage",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.7",
    "title": "2.8.7-alpha0: doctest failure in rings/residue_field.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/884",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: failure

On sage.math, the rings/residue_field.pyx doctest fails as follows in 2.8.7:

```
sage -t  devel/sage-rtest/sage/rings/residue_field.pyx      **********************************************************************
File "residue_field.pyx", line 364:
    sage: b*c^2
Exception raised:
    Traceback (most recent call last):
      File "/home/cwitty/pre-sage/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_15[8]>", line 1, in <module>
        b*c**Integer(2)###line 364:
    sage: b*c^2
      File "element.pyx", line 1463, in element.RingElement.__pow__
      File "element.pyx", line 2777, in element.generic_power_c
      File "element.pyx", line 1376, in element.RingElement.__mul__
      File "coerce.pxi", line 126, in element._mul_c
    RuntimeError
**********************************************************************
File "residue_field.pyx", line 221:
    sage: k.coerce_map_from(OK)(OK(a)^7)
Exception raised:
    Traceback (most recent call last):
      File "/home/cwitty/pre-sage/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_9[4]>", line 1, in <module>
        k.coerce_map_from(OK)(OK(a)**Integer(7))###line 221:
    sage: k.coerce_map_from(OK)(OK(a)^7)
      File "element.pyx", line 1463, in element.RingElement.__pow__
      File "element.pyx", line 2782, in element.generic_power_c
      File "element.pyx", line 1376, in element.RingElement.__mul__
      File "coerce.pxi", line 126, in element._mul_c
    RuntimeError
**********************************************************************
2 items had failures:
   1 of  10 in __main__.example_15
   1 of   5 in __main__.example_9
***Test Failed*** 2 failures.
For whitespace errors, see the file .doctest_residue_field.pyxException exceptions.AttributeError: "'AbsoluteOrder' object has no attribute 'polynomial_ntl'" in 'number_field_element.NumberFieldElement_absolute._parent_poly_c_' ignored
ZZX: division by zero
Exception exceptions.AttributeError: "'AbsoluteOrder' object has no attribute 'polynomial_ntl'" in 'number_field_element.NumberFieldElement_absolute._parent_poly_c_' ignored
ZZX: division by zero
```

Issue created by migration from https://trac.sagemath.org/ticket/884





---

archive/issue_comments_005441.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-14T03:13:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/884#issuecomment-5441",
    "user": "https://github.com/roed314"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005442.json:
```json
{
    "body": "Changing assignee from failure to @roed314.",
    "created_at": "2007-10-14T03:13:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/884#issuecomment-5442",
    "user": "https://github.com/roed314"
}
```

Changing assignee from failure to @roed314.



---

archive/issue_comments_005443.json:
```json
{
    "body": "Uncommented region that shouldn't have been commented out.",
    "created_at": "2007-10-14T03:24:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/884#issuecomment-5443",
    "user": "https://github.com/roed314"
}
```

Uncommented region that shouldn't have been commented out.



---

archive/issue_comments_005444.json:
```json
{
    "body": "Attachment [trac884.patch](tarball://root/attachments/some-uuid/ticket884/trac884.patch) by @roed314 created at 2007-10-14 03:24:34",
    "created_at": "2007-10-14T03:24:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/884#issuecomment-5444",
    "user": "https://github.com/roed314"
}
```

Attachment [trac884.patch](tarball://root/attachments/some-uuid/ticket884/trac884.patch) by @roed314 created at 2007-10-14 03:24:34



---

archive/issue_comments_005445.json:
```json
{
    "body": "I reject this patch.  That code was commented out for a reason.  It is conceptually completely wrong to have such methods on an order -- the order can't be defined by a single poly in general, etc.",
    "created_at": "2007-10-14T17:40:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/884#issuecomment-5445",
    "user": "https://github.com/williamstein"
}
```

I reject this patch.  That code was commented out for a reason.  It is conceptually completely wrong to have such methods on an order -- the order can't be defined by a single poly in general, etc.



---

archive/issue_comments_005446.json:
```json
{
    "body": "Actually David Roes' code is right and his example just exposes a bug in my code.",
    "created_at": "2007-10-14T17:57:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/884#issuecomment-5446",
    "user": "https://github.com/williamstein"
}
```

Actually David Roes' code is right and his example just exposes a bug in my code.



---

archive/issue_comments_005447.json:
```json
{
    "body": "I'm working on this...",
    "created_at": "2007-10-14T19:14:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/884#issuecomment-5447",
    "user": "https://github.com/williamstein"
}
```

I'm working on this...



---

archive/issue_comments_005448.json:
```json
{
    "body": "Changing status from assigned to new.",
    "created_at": "2007-10-14T19:14:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/884#issuecomment-5448",
    "user": "https://github.com/williamstein"
}
```

Changing status from assigned to new.



---

archive/issue_comments_005449.json:
```json
{
    "body": "Changing assignee from @roed314 to was*.",
    "created_at": "2007-10-14T19:14:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/884#issuecomment-5449",
    "user": "https://github.com/williamstein"
}
```

Changing assignee from @roed314 to was*.



---

archive/issue_comments_005450.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-10-14T19:14:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/884#issuecomment-5450",
    "user": "https://github.com/williamstein"
}
```

Changing status from new to assigned.



---

archive/issue_comments_005451.json:
```json
{
    "body": "Changing assignee from was* to @williamstein.",
    "created_at": "2007-10-14T19:14:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/884#issuecomment-5451",
    "user": "https://github.com/williamstein"
}
```

Changing assignee from was* to @williamstein.



---

archive/issue_comments_005452.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-10-15T18:14:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/884",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/884#issuecomment-5452",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed



---

archive/issue_events_002460.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-10-15T18:14:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/884",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/884#event-2460"
}
```
