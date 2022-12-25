# Issue 1159: Bug in python range

archive/issues_001159.json:
```json
{
    "body": "Assignee: @williamstein\n\n%python\nclass MyInt:\n    def __init__(self, n):\n        self.n = int(n)\n    def __int__(self):\n        return self.n\n\nprint range(MyInt(2**3), MyInt(2**3+10))\nprint \"here\"\nprint range(MyInt(2**34), MyInt(2**34+10))\n\nIssue created by migration from https://trac.sagemath.org/ticket/1159\n\n",
    "created_at": "2007-11-12T22:12:49Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Bug in python range",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1159",
    "user": "https://github.com/robertwb"
}
```
Assignee: @williamstein

%python
class MyInt:
    def __init__(self, n):
        self.n = int(n)
    def __int__(self):
        return self.n

print range(MyInt(2**3), MyInt(2**3+10))
print "here"
print range(MyInt(2**34), MyInt(2**34+10))

Issue created by migration from https://trac.sagemath.org/ticket/1159





---

archive/issue_comments_007061.json:
```json
{
    "body": "\n```\n%python\nclass MyInt:\n    def __init__(self, n):\n        self.n = int(n)\n    def __int__(self):\n        return self.n\n\nprint range(MyInt(2**3), MyInt(2**3+10))\nprint \"here\"\nprint range(MyInt(2**34), MyInt(2**34+10))\n```\n",
    "created_at": "2007-11-12T22:13:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1159#issuecomment-7061",
    "user": "https://github.com/robertwb"
}
```


```
%python
class MyInt:
    def __init__(self, n):
        self.n = int(n)
    def __int__(self):
        return self.n

print range(MyInt(2**3), MyInt(2**3+10))
print "here"
print range(MyInt(2**34), MyInt(2**34+10))
```




---

archive/issue_comments_007062.json:
```json
{
    "body": "I can't find any issue with this.  It works correctly for me in both the Python and Sage environments.",
    "created_at": "2007-11-20T00:16:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1159#issuecomment-7062",
    "user": "https://github.com/mwhansen"
}
```

I can't find any issue with this.  It works correctly for me in both the Python and Sage environments.



---

archive/issue_comments_007063.json:
```json
{
    "body": "I get \n\n\n```\nTraceback (most recent call last):    print range(MyInt(2**34), MyInt(2**34+10))\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/server/support.py\", line 260, in syseval\n    return system.eval(cmd)\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/misc/python.py\", line 21, in eval\n    eval(z, globals, locals)\n  File \"/Users/robert/sage/sage-2.8.11/data/extcode/sage/\", line 1, in <module>\n    \nTypeError: range() integer start argument expected, got instance.\n```\n\n\nOn a 64-bit machine, try \n\n```\nprint range(2**64, 2**64+10)\nprint range(MyInt(2**64), MyInt(2**64+10))\n```\n\n\nI believe this is a bug in Python, and have reported it here: http://bugs.python.org/issue1533",
    "created_at": "2007-12-01T00:30:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1159#issuecomment-7063",
    "user": "https://github.com/robertwb"
}
```

I get 


```
Traceback (most recent call last):    print range(MyInt(2**34), MyInt(2**34+10))
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/server/support.py", line 260, in syseval
    return system.eval(cmd)
  File "/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/misc/python.py", line 21, in eval
    eval(z, globals, locals)
  File "/Users/robert/sage/sage-2.8.11/data/extcode/sage/", line 1, in <module>
    
TypeError: range() integer start argument expected, got instance.
```


On a 64-bit machine, try 

```
print range(2**64, 2**64+10)
print range(MyInt(2**64), MyInt(2**64+10))
```


I believe this is a bug in Python, and have reported it here: http://bugs.python.org/issue1533



---

archive/issue_comments_007064.json:
```json
{
    "body": "Changing status from new to needs_info_new.",
    "created_at": "2009-10-06T19:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1159#issuecomment-7064",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_info_new.



---

archive/issue_comments_007065.json:
```json
{
    "body": "Fixed in upstream Python 2.6.6 / Python 2.7 (see issue 1533 linked to above) and fix will also be in Python 3 releases. This needs an upgrade of the Sage Python from 2.6.4 to 2.6.6.",
    "created_at": "2010-12-10T14:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1159#issuecomment-7065",
    "user": "https://trac.sagemath.org/admin/accounts/users/Koen"
}
```

Fixed in upstream Python 2.6.6 / Python 2.7 (see issue 1533 linked to above) and fix will also be in Python 3 releases. This needs an upgrade of the Sage Python from 2.6.4 to 2.6.6.



---

archive/issue_comments_007066.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2010-12-10T14:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1159#issuecomment-7066",
    "user": "https://trac.sagemath.org/admin/accounts/users/Koen"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_007067.json:
```json
{
    "body": "Alternative fix to upgrade to Python 2.6.6 would be the upgrade to Python 2.7 from ticket http://trac.sagemath.org/sage_trac/ticket/9958",
    "created_at": "2010-12-10T14:34:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1159#issuecomment-7067",
    "user": "https://trac.sagemath.org/admin/accounts/users/Koen"
}
```

Alternative fix to upgrade to Python 2.6.6 would be the upgrade to Python 2.7 from ticket http://trac.sagemath.org/sage_trac/ticket/9958



---

archive/issue_comments_007068.json:
```json
{
    "body": "Fixed by #9958, when it gets merged (upgrade to python 2.7)",
    "created_at": "2011-12-14T03:26:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1159#issuecomment-7068",
    "user": "https://github.com/jasongrout"
}
```

Fixed by #9958, when it gets merged (upgrade to python 2.7)



---

archive/issue_comments_007069.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-01-06T08:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1159#issuecomment-7069",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_events_001289.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2012-01-13T08:58:35Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/1159",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/1159#event-1289"
}
```



---

archive/issue_comments_007070.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-01-13T08:58:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1159#issuecomment-7070",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: duplicate
