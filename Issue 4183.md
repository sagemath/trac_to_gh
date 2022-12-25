# Issue 4183: ?? can't always find the source for new style classes

archive/issues_004183.json:
```json
{
    "body": "Assignee: @williamstein\n\nI think one needs to check bit 9 (Py_TPFLAGS_HEAPTYPE) of the __class__.__flags__ attribute to see if one should do the same trick as in #2777 or something like that.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4183\n\n",
    "created_at": "2008-09-24T01:25:02Z",
    "labels": [
        "component: user interface",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "?? can't always find the source for new style classes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4183",
    "user": "https://github.com/robertwb"
}
```
Assignee: @williamstein

I think one needs to check bit 9 (Py_TPFLAGS_HEAPTYPE) of the __class__.__flags__ attribute to see if one should do the same trick as in #2777 or something like that.

Issue created by migration from https://trac.sagemath.org/ticket/4183





---

archive/issue_comments_030296.json:
```json
{
    "body": "I didn't though about if for #2777, but based on [http://psyco.sourceforge.net/psycoguide/metaclass.html](http://psyco.sourceforge.net/psycoguide/metaclass.html), i.e. part \"... if `x` contains an instance of ... a new-style class, then `type(x)` will be `x.__class__` instead of `types.InstanceType`.\" - I think that test like:\n\n`hasattr(arg, __class__) and type(arg) == arg.__class__`\n\ncould do the thing, maybe not best way but it works for example with instances of `sage.rings.rational_field.RationalField`... no code to attach yet (just in-place tests in console, it's 4:30 am here) - will try to do some small patch soon",
    "created_at": "2008-09-24T02:40:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4183#issuecomment-30296",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

I didn't though about if for #2777, but based on [http://psyco.sourceforge.net/psycoguide/metaclass.html](http://psyco.sourceforge.net/psycoguide/metaclass.html), i.e. part "... if `x` contains an instance of ... a new-style class, then `type(x)` will be `x.__class__` instead of `types.InstanceType`." - I think that test like:

`hasattr(arg, __class__) and type(arg) == arg.__class__`

could do the thing, maybe not best way but it works for example with instances of `sage.rings.rational_field.RationalField`... no code to attach yet (just in-place tests in console, it's 4:30 am here) - will try to do some small patch soon



---

archive/issue_comments_030297.json:
```json
{
    "body": "Ah, that sounds like a much nicer way to detect it.",
    "created_at": "2008-09-24T05:10:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4183#issuecomment-30297",
    "user": "https://github.com/robertwb"
}
```

Ah, that sounds like a much nicer way to detect it.



---

archive/issue_comments_030298.json:
```json
{
    "body": "Used other approach, above with type equal class is true for too much, for example:\n\n\n```\nsage: type(arg)\n<type 'function'>\nsage: arg.__class__\n<type 'function'>\n```\n\n\nCheck like:\n\n`obj.__class__.__module__ not in ('__builtin__', 'exceptions')`\n\nseems to work both old and new style classes, the problem seems to be that everything is object, so best we can do is check if something is object of non built-in class",
    "created_at": "2008-09-24T22:16:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4183#issuecomment-30298",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

Used other approach, above with type equal class is true for too much, for example:


```
sage: type(arg)
<type 'function'>
sage: arg.__class__
<type 'function'>
```


Check like:

`obj.__class__.__module__ not in ('__builtin__', 'exceptions')`

seems to work both old and new style classes, the problem seems to be that everything is object, so best we can do is check if something is object of non built-in class



---

archive/issue_comments_030299.json:
```json
{
    "body": "second try",
    "created_at": "2008-09-25T00:43:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4183#issuecomment-30299",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

second try



---

archive/issue_comments_030300.json:
```json
{
    "body": "Attachment [4183-2.patch](tarball://root/attachments/some-uuid/ticket4183/4183-2.patch) by aginiewicz created at 2008-09-25 00:47:39\n\nin previous patch I trusted the \"everything is object\" too much... so not everything have `__class__`, that's why I added back the check for `__class__` and also `__module__`, though every class should have one... better safe than sorry",
    "created_at": "2008-09-25T00:47:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4183#issuecomment-30300",
    "user": "https://trac.sagemath.org/admin/accounts/users/aginiewicz"
}
```

Attachment [4183-2.patch](tarball://root/attachments/some-uuid/ticket4183/4183-2.patch) by aginiewicz created at 2008-09-25 00:47:39

in previous patch I trusted the "everything is object" too much... so not everything have `__class__`, that's why I added back the check for `__class__` and also `__module__`, though every class should have one... better safe than sorry



---

archive/issue_comments_030301.json:
```json
{
    "body": "Applies cleanly and works well. This is very nice.",
    "created_at": "2008-10-14T19:44:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4183#issuecomment-30301",
    "user": "https://github.com/robertwb"
}
```

Applies cleanly and works well. This is very nice.



---

archive/issue_comments_030302.json:
```json
{
    "body": "Note: apply only the second patch.",
    "created_at": "2008-10-14T19:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4183#issuecomment-30302",
    "user": "https://github.com/robertwb"
}
```

Note: apply only the second patch.



---

archive/issue_comments_030303.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-18T12:03:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4183#issuecomment-30303",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030304.json:
```json
{
    "body": "Merged 4183-2.patch in Sage 3.2.alpha0",
    "created_at": "2008-10-18T12:03:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4183",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4183#issuecomment-30304",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 4183-2.patch in Sage 3.2.alpha0
