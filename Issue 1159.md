# Issue 1159: Bug in python range

archive/issues_001159.json:
```json
{
    "body": "Assignee: @williamstein\n\n%python\nclass MyInt:\n    def __init__(self, n):\n        self.n = int(n)\n    def __int__(self):\n        return self.n\n\nprint range(MyInt(2**3), MyInt(2**3+10))\nprint \"here\"\nprint range(MyInt(2**34), MyInt(2**34+10))\n\nIssue created by migration from https://trac.sagemath.org/ticket/1159\n\n",
    "created_at": "2007-11-12T22:12:49Z",
    "labels": [
        "packages: standard",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Bug in python range",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1159",
    "user": "@robertwb"
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

archive/issue_comments_007083.json:
```json
{
    "body": "\n```\n%python\nclass MyInt:\n    def __init__(self, n):\n        self.n = int(n)\n    def __int__(self):\n        return self.n\n\nprint range(MyInt(2**3), MyInt(2**3+10))\nprint \"here\"\nprint range(MyInt(2**34), MyInt(2**34+10))\n```\n",
    "created_at": "2007-11-12T22:13:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1159#issuecomment-7083",
    "user": "@robertwb"
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

archive/issue_comments_007084.json:
```json
{
    "body": "I can't find any issue with this.  It works correctly for me in both the Python and Sage environments.",
    "created_at": "2007-11-20T00:16:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1159#issuecomment-7084",
    "user": "@mwhansen"
}
```

I can't find any issue with this.  It works correctly for me in both the Python and Sage environments.



---

archive/issue_comments_007085.json:
```json
{
    "body": "I get \n\n\n```\nTraceback (most recent call last):    print range(MyInt(2**34), MyInt(2**34+10))\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/server/support.py\", line 260, in syseval\n    return system.eval(cmd)\n  File \"/Users/robert/sage/current/local/lib/python2.5/site-packages/sage/misc/python.py\", line 21, in eval\n    eval(z, globals, locals)\n  File \"/Users/robert/sage/sage-2.8.11/data/extcode/sage/\", line 1, in <module>\n    \nTypeError: range() integer start argument expected, got instance.\n```\n\n\nOn a 64-bit machine, try \n\n```\nprint range(2**64, 2**64+10)\nprint range(MyInt(2**64), MyInt(2**64+10))\n```\n\n\nI believe this is a bug in Python, and have reported it here: http://bugs.python.org/issue1533",
    "created_at": "2007-12-01T00:30:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1159#issuecomment-7085",
    "user": "@robertwb"
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

archive/issue_comments_007086.json:
```json
{
    "body": "Changing status from new to needs_info_new.",
    "created_at": "2009-10-06T19:25:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1159#issuecomment-7086",
    "user": "@jasongrout"
}
```

Changing status from new to needs_info_new.



---

archive/issue_comments_007087.json:
```json
{
    "body": "Fixed in upstream Python 2.6.6 / Python 2.7 (see issue 1533 linked to above) and fix will also be in Python 3 releases. This needs an upgrade of the Sage Python from 2.6.4 to 2.6.6.",
    "created_at": "2010-12-10T14:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1159#issuecomment-7087",
    "user": "Koen"
}
```

Fixed in upstream Python 2.6.6 / Python 2.7 (see issue 1533 linked to above) and fix will also be in Python 3 releases. This needs an upgrade of the Sage Python from 2.6.4 to 2.6.6.



---

archive/issue_comments_007088.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2010-12-10T14:30:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1159#issuecomment-7088",
    "user": "Koen"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_007089.json:
```json
{
    "body": "Alternative fix to upgrade to Python 2.6.6 would be the upgrade to Python 2.7 from ticket http://trac.sagemath.org/sage_trac/ticket/9958",
    "created_at": "2010-12-10T14:34:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1159#issuecomment-7089",
    "user": "Koen"
}
```

Alternative fix to upgrade to Python 2.6.6 would be the upgrade to Python 2.7 from ticket http://trac.sagemath.org/sage_trac/ticket/9958



---

archive/issue_comments_007090.json:
```json
{
    "body": "Fixed by #9958, when it gets merged (upgrade to python 2.7)",
    "created_at": "2011-12-14T03:26:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1159#issuecomment-7090",
    "user": "@jasongrout"
}
```

Fixed by #9958, when it gets merged (upgrade to python 2.7)



---

archive/issue_comments_007091.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2012-01-06T08:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1159#issuecomment-7091",
    "user": "@jdemeyer"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_007092.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-01-13T08:58:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1159",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1159#issuecomment-7092",
    "user": "@jdemeyer"
}
```

Resolution: duplicate
