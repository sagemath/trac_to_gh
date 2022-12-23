# Issue 1565: RealDoubleField documentation missing

archive/issues_001565.json:
```json
{
    "body": "Assignee: tba\n\nSomewhere I read that missing documentation should be considered as a bug:\nsage version 2.9\n\n```\nRealDoubleField?\n```\n\n\n```\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"/home/server4/sage_notebook/worksheets/phatsphere/0/code/11.py\", line 4, in <module>\n    print _support_.docstring(\"RealDoubleField\", globals())\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/server/support.py\", line 142, in docstring\n    s += 'Definition:  %s\\n'%sageinspect.sage_getdef(obj, obj_name)\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/misc/sageinspect.py\", line 276, in sage_getdef\n    spec = sage_getargspec(obj)\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/misc/sageinspect.py\", line 249, in sage_getargspec\n    return _sage_getargspec_cython(source)\n  File \"/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/misc/sageinspect.py\", line 201, in _sage_getargspec_cython\n    raise ValueError, \"Could not parse cython argspec\"\nValueError: Could not parse cython argspec\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1565\n\n",
    "created_at": "2007-12-19T10:50:37Z",
    "labels": [
        "documentation",
        "trivial",
        "bug"
    ],
    "title": "RealDoubleField documentation missing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1565",
    "user": "phatsphere"
}
```
Assignee: tba

Somewhere I read that missing documentation should be considered as a bug:
sage version 2.9

```
RealDoubleField?
```


```
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/server4/sage_notebook/worksheets/phatsphere/0/code/11.py", line 4, in <module>
    print _support_.docstring("RealDoubleField", globals())
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/server/support.py", line 142, in docstring
    s += 'Definition:  %s\n'%sageinspect.sage_getdef(obj, obj_name)
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/misc/sageinspect.py", line 276, in sage_getdef
    spec = sage_getargspec(obj)
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/misc/sageinspect.py", line 249, in sage_getargspec
    return _sage_getargspec_cython(source)
  File "/usr/local/sage-2.6/local/lib/python2.5/site-packages/sage/misc/sageinspect.py", line 201, in _sage_getargspec_cython
    raise ValueError, "Could not parse cython argspec"
ValueError: Could not parse cython argspec
```


Issue created by migration from https://trac.sagemath.org/ticket/1565





---

archive/issue_comments_009959.json:
```json
{
    "body": "I cannot reproduce this with either Sage 2.9.1.alpha1 compiled from source as well as 2.9 on sage.math:\n\n```\nmabshoff@sage:/tmp/Work-mabshoff/sage-2.9.1.alpha1$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.9.1.alpha1, Release Date: 2007-12-18                |\n| Type notebook() for the GUI, and license() for information.        |\nsage: RealDoubleField?\nType:           builtin_function_or_method\nBase Class:     <type 'builtin_function_or_method'>\nString Form:    <built-in function RealDoubleField>\nNamespace:      Interactive\n\nsage: RealDoubleField??\nType:           builtin_function_or_method\nBase Class:     <type 'builtin_function_or_method'>\nString Form:    <built-in function RealDoubleField>\nNamespace:      Interactive\nSource:\ndef RealDoubleField():\n    global _RDF\n    return _RDF\nsage:\nExiting SAGE (CPU time 0m0.02s, Wall time 0m38.13s).\nmabshoff@sage:/tmp/Work-mabshoff/sage-2.9.1.alpha1$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| SAGE Version 2.9, Release Date: 2007-12-16                         |\n| Type notebook() for the GUI, and license() for information.        |\nsage: RealDoubleField?\nType:           builtin_function_or_method\nBase Class:     <type 'builtin_function_or_method'>\nString Form:    <built-in function RealDoubleField>\nNamespace:      Interactive\n\nsage: RealDoubleField??\nType:           builtin_function_or_method\nBase Class:     <type 'builtin_function_or_method'>\nString Form:    <built-in function RealDoubleField>\nNamespace:      Interactive\nSource:\ndef RealDoubleField():\n    global _RDF\n    return _RDF\nsage:\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2007-12-19T11:04:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1565#issuecomment-9959",
    "user": "mabshoff"
}
```

I cannot reproduce this with either Sage 2.9.1.alpha1 compiled from source as well as 2.9 on sage.math:

```
mabshoff@sage:/tmp/Work-mabshoff/sage-2.9.1.alpha1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.9.1.alpha1, Release Date: 2007-12-18                |
| Type notebook() for the GUI, and license() for information.        |
sage: RealDoubleField?
Type:           builtin_function_or_method
Base Class:     <type 'builtin_function_or_method'>
String Form:    <built-in function RealDoubleField>
Namespace:      Interactive

sage: RealDoubleField??
Type:           builtin_function_or_method
Base Class:     <type 'builtin_function_or_method'>
String Form:    <built-in function RealDoubleField>
Namespace:      Interactive
Source:
def RealDoubleField():
    global _RDF
    return _RDF
sage:
Exiting SAGE (CPU time 0m0.02s, Wall time 0m38.13s).
mabshoff@sage:/tmp/Work-mabshoff/sage-2.9.1.alpha1$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.9, Release Date: 2007-12-16                         |
| Type notebook() for the GUI, and license() for information.        |
sage: RealDoubleField?
Type:           builtin_function_or_method
Base Class:     <type 'builtin_function_or_method'>
String Form:    <built-in function RealDoubleField>
Namespace:      Interactive

sage: RealDoubleField??
Type:           builtin_function_or_method
Base Class:     <type 'builtin_function_or_method'>
String Form:    <built-in function RealDoubleField>
Namespace:      Interactive
Source:
def RealDoubleField():
    global _RDF
    return _RDF
sage:
```


Cheers,

Michael



---

archive/issue_comments_009960.json:
```json
{
    "body": "Replying to [comment:1 mabshoff]:\n> I cannot reproduce this with either Sage 2.9.1.alpha1 compiled from source as well as 2.9 on sage.math:\n\n```\nsage: RealDoubleField?\nType:           builtin_function_or_method\nBase Class:     <type 'builtin_function_or_method'>\nString Form:    <built-in function RealDoubleField>\nNamespace:      Interactive\n```\n\n\nActually, you just reproduced it: There is no documentation.",
    "created_at": "2007-12-19T12:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1565#issuecomment-9960",
    "user": "malb"
}
```

Replying to [comment:1 mabshoff]:
> I cannot reproduce this with either Sage 2.9.1.alpha1 compiled from source as well as 2.9 on sage.math:

```
sage: RealDoubleField?
Type:           builtin_function_or_method
Base Class:     <type 'builtin_function_or_method'>
String Form:    <built-in function RealDoubleField>
Namespace:      Interactive
```


Actually, you just reproduced it: There is no documentation.



---

archive/issue_comments_009961.json:
```json
{
    "body": "The patch for #1459 might also fix this issue.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-22T15:18:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1565#issuecomment-9961",
    "user": "mabshoff"
}
```

The patch for #1459 might also fix this issue.

Cheers,

Michael



---

archive/issue_comments_009962.json:
```json
{
    "body": "This wasn't fixed in 2.9.1.\n\nCheers,\n\nMichael",
    "created_at": "2007-12-26T03:30:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1565#issuecomment-9962",
    "user": "mabshoff"
}
```

This wasn't fixed in 2.9.1.

Cheers,

Michael



---

archive/issue_comments_009963.json:
```json
{
    "body": "This is fixed as of 3.0.3.alpha2.  Please close",
    "created_at": "2008-06-15T23:29:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1565#issuecomment-9963",
    "user": "gfurnish"
}
```

This is fixed as of 3.0.3.alpha2.  Please close



---

archive/issue_comments_009964.json:
```json
{
    "body": "Closed since it is fixed :)\n\nCheers,\n\nMichael",
    "created_at": "2008-06-16T19:05:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1565#issuecomment-9964",
    "user": "mabshoff"
}
```

Closed since it is fixed :)

Cheers,

Michael



---

archive/issue_comments_009965.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-16T19:05:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1565",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1565#issuecomment-9965",
    "user": "mabshoff"
}
```

Resolution: fixed
