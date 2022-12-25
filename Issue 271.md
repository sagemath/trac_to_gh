# Issue 271: defining classes in the notebook with examples

archive/issues_000271.json:
```json
{
    "body": "Assignee: @williamstein\n\nExecutable examples in comments seem to interfere with the creation of class definitions in the notebook:\n\nWe define a class in a notebook cell without executable example:\n\n```\nclass test1():\n  \"\"\"\n  doc here\n  \"\"\"\n\n  def __init__(self):\n    \"\"\"\n    EXAMPLES:\n      asage: print \"there you are!\"\n      there you are!\n    \"\"\"\n    print \"here I am!\"\n```\n\n\nWe test it and successfully create the class:\n\n```\nA=test1()\n///\nhere I am!\n```\n\n\nSame example, but now the example is executable. Note that we get the result from the example.\n\n```\nclass test2():\n  \"\"\"\n  doc here\n  \"\"\"\n\n  def __init__(self):\n    \"\"\"\n    EXAMPLES:\n      sage: print \"there you are!\"\n      there you are!\n    \"\"\"\n    print \"here I am!\"\n///\nthere you are!\n```\n\n\nBut creating an instance of this class now fails:\n\n```\nB=test2()\n///\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"/usr/local/sage/nobody/sage_notebook/worksheets/test/code/20.py\", line 4, in <module>\n    exec compile(ur'B=test2()' + '\\n', '', 'single')\n  File \"/usr/local/sage/nobody/\", line 1, in <module>\n    \nNameError: name 'test2' is not defined\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/271\n\n",
    "created_at": "2007-02-20T22:09:04Z",
    "labels": [
        "component: packages",
        "bug"
    ],
    "title": "defining classes in the notebook with examples",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/271",
    "user": "https://github.com/nbruin"
}
```
Assignee: @williamstein

Executable examples in comments seem to interfere with the creation of class definitions in the notebook:

We define a class in a notebook cell without executable example:

```
class test1():
  """
  doc here
  """

  def __init__(self):
    """
    EXAMPLES:
      asage: print "there you are!"
      there you are!
    """
    print "here I am!"
```


We test it and successfully create the class:

```
A=test1()
///
here I am!
```


Same example, but now the example is executable. Note that we get the result from the example.

```
class test2():
  """
  doc here
  """

  def __init__(self):
    """
    EXAMPLES:
      sage: print "there you are!"
      there you are!
    """
    print "here I am!"
///
there you are!
```


But creating an instance of this class now fails:

```
B=test2()
///
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/usr/local/sage/nobody/sage_notebook/worksheets/test/code/20.py", line 4, in <module>
    exec compile(ur'B=test2()' + '\n', '', 'single')
  File "/usr/local/sage/nobody/", line 1, in <module>
    
NameError: name 'test2' is not defined
```



Issue created by migration from https://trac.sagemath.org/ticket/271





---

archive/issue_comments_001284.json:
```json
{
    "body": "Same as ticket #228",
    "created_at": "2007-03-01T01:59:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/271#issuecomment-1284",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Same as ticket #228



---

archive/issue_events_000286.json:
```json
{
    "actor": "TimothyClemans",
    "created_at": "2007-03-26T03:35:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/271",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/271#event-286"
}
```



---

archive/issue_comments_001285.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2007-03-26T03:35:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/271#issuecomment-1285",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Resolution: duplicate



---

archive/issue_comments_001286.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2007-03-26T05:48:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/271#issuecomment-1286",
    "user": "https://trac.sagemath.org/admin/accounts/users/kohel"
}
```

Changing status from closed to reopened.



---

archive/issue_events_000287.json:
```json
{
    "actor": "kohel",
    "created_at": "2007-03-26T05:48:06Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/271",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/271#event-287"
}
```



---

archive/issue_comments_001287.json:
```json
{
    "body": "Resolution changed from duplicate to ",
    "created_at": "2007-03-26T05:48:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/271#issuecomment-1287",
    "user": "https://trac.sagemath.org/admin/accounts/users/kohel"
}
```

Resolution changed from duplicate to 



---

archive/issue_comments_001288.json:
```json
{
    "body": "Changing component from packages to user interface.",
    "created_at": "2007-03-26T05:48:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/271#issuecomment-1288",
    "user": "https://trac.sagemath.org/admin/accounts/users/kohel"
}
```

Changing component from packages to user interface.



---

archive/issue_comments_001289.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-04-03T06:18:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/271",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/271#issuecomment-1289",
    "user": "https://trac.sagemath.org/admin/accounts/users/TimothyClemans"
}
```

Resolution: fixed



---

archive/issue_events_000288.json:
```json
{
    "actor": "TimothyClemans",
    "created_at": "2007-04-03T06:18:14Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/271",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/271#event-288"
}
```
