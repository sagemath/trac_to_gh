# Issue 184: negation of RealDouble broken

archive/issues_000184.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nsage: -RDF(1)\n///\nTraceback (most recent call last):\n  File \"\", line 1, in \n  File \"/home/server2/sage_notebook/worksheets/bugs_/code/12.py\", line 4, in \n    -RDF(Integer(1))\n  File \"/sage/local/lib/python2.5/\", line 1, in \n    \n  File \"element.pyx\", line 511, in element.ModuleElement.__neg__\n  File \"element.pyx\", line 525, in element.ModuleElement._neg_c\n  File \"element.pyx\", line 535, in element.ModuleElement._neg_c_impl\nTypeError: 'NoneType' object is not callable\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/184\n\n",
    "created_at": "2006-12-17T19:36:55Z",
    "labels": [
        "basic arithmetic",
        "blocker",
        "bug"
    ],
    "title": "negation of RealDouble broken",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/184",
    "user": "boothby"
}
```
Assignee: somebody


```
sage: -RDF(1)
///
Traceback (most recent call last):
  File "", line 1, in 
  File "/home/server2/sage_notebook/worksheets/bugs_/code/12.py", line 4, in 
    -RDF(Integer(1))
  File "/sage/local/lib/python2.5/", line 1, in 
    
  File "element.pyx", line 511, in element.ModuleElement.__neg__
  File "element.pyx", line 525, in element.ModuleElement._neg_c
  File "element.pyx", line 535, in element.ModuleElement._neg_c_impl
TypeError: 'NoneType' object is not callable
```


Issue created by migration from https://trac.sagemath.org/ticket/184





---

archive/issue_comments_000838.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2006-12-17T22:28:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/184#issuecomment-838",
    "user": "dmharvey"
}
```

Resolution: fixed



---

archive/issue_comments_000839.json:
```json
{
    "body": "Fixed, patch =\n\nhttp://sage.math.washington.edu/home/dmharvey/patches/rdf-negative.hg",
    "created_at": "2006-12-17T22:28:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/184",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/184#issuecomment-839",
    "user": "dmharvey"
}
```

Fixed, patch =

http://sage.math.washington.edu/home/dmharvey/patches/rdf-negative.hg
