# Issue 8149: files with space in their names do not load properly

archive/issues_008149.json:
```json
{
    "body": "Assignee: tbd\n\nThanks to the load/attach rewrite most of the weirdness is gone. My only issue left is that files with space in their names somehow only work with the depreciated style of calling load. This behavior is the same in prompt and notebook.\n\n\n```\nsage: t=tmp_filename()+' space.py'; open(t,'w').write(\"print 'hello world'\")\nsage: load t\nhello world\nsage: load(t)\n---------------------------------------------------------------------------\nValueError  \n```\n\n\nI should be able to fix this soon, as probably it is a minor tweak, but if anyone wants to go ahead...\n\nIssue created by migration from https://trac.sagemath.org/ticket/8149\n\n",
    "created_at": "2010-02-02T07:30:10Z",
    "labels": [
        "component: misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "files with space in their names do not load properly",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8149",
    "user": "https://trac.sagemath.org/admin/accounts/users/rkirov"
}
```
Assignee: tbd

Thanks to the load/attach rewrite most of the weirdness is gone. My only issue left is that files with space in their names somehow only work with the depreciated style of calling load. This behavior is the same in prompt and notebook.


```
sage: t=tmp_filename()+' space.py'; open(t,'w').write("print 'hello world'")
sage: load t
hello world
sage: load(t)
---------------------------------------------------------------------------
ValueError  
```


I should be able to fix this soon, as probably it is a minor tweak, but if anyone wants to go ahead...

Issue created by migration from https://trac.sagemath.org/ticket/8149





---

archive/issue_comments_071514.json:
```json
{
    "body": "ok, the culprit is in sage.misc.preparser.load \n\n\n```\n    try:\n        filename = eval(filename, globals)\n    except Exception:\n        # handle multiple input files separated by spaces, which was\n        # maybe a bad idea, but which we have to handle for backwards\n        # compatibility.\n        v = filename.split()\n        if len(v) > 1:\n            for file in v:\n                load(file, globals, attach=attach)\n            return\n```\n\n\nso I guess any fix for files with spacebars will break the backwards compatibility :/ Maybe for Sage 4 we can go away with backwards compatibility on this issue (also maybe remove 'eval'). The new load() already has capabilities of loading multiple files. Consider \n\n1) load('file1.py file2.py')\n2) load('file1.py','file2.py')\n\n2) looks more pythonic to me.",
    "created_at": "2010-02-26T07:16:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8149#issuecomment-71514",
    "user": "https://trac.sagemath.org/admin/accounts/users/rkirov"
}
```

ok, the culprit is in sage.misc.preparser.load 


```
    try:
        filename = eval(filename, globals)
    except Exception:
        # handle multiple input files separated by spaces, which was
        # maybe a bad idea, but which we have to handle for backwards
        # compatibility.
        v = filename.split()
        if len(v) > 1:
            for file in v:
                load(file, globals, attach=attach)
            return
```


so I guess any fix for files with spacebars will break the backwards compatibility :/ Maybe for Sage 4 we can go away with backwards compatibility on this issue (also maybe remove 'eval'). The new load() already has capabilities of loading multiple files. Consider 

1) load('file1.py file2.py')
2) load('file1.py','file2.py')

2) looks more pythonic to me.



---

archive/issue_comments_071515.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-03-25T16:28:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8149#issuecomment-71515",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071516.json:
```json
{
    "body": "This works correctly now (with a doctest in `src/sage/repl/load.py`)",
    "created_at": "2015-03-25T16:28:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8149#issuecomment-71516",
    "user": "https://github.com/jdemeyer"
}
```

This works correctly now (with a doctest in `src/sage/repl/load.py`)



---

archive/issue_comments_071517.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-03-25T16:28:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8149#issuecomment-71517",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071518.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-03-25T19:21:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8149",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8149#issuecomment-71518",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_008354.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2015-03-25T19:21:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8149",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8149#event-8354"
}
```
