# Issue 4789: numerically stable computation of nullspace of RDF/CDF matrices

archive/issues_004789.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @ClementPernet @slel\n\nI think this message might be useful:\n\nhttp://projects.scipy.org/pipermail/scipy-user/2008-December/019064.html\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4789\n\n",
    "created_at": "2008-12-14T01:57:58Z",
    "labels": [
        "algebra",
        "major",
        "enhancement"
    ],
    "title": "numerically stable computation of nullspace of RDF/CDF matrices",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4789",
    "user": "@jasongrout"
}
```
Assignee: tbd

CC:  @ClementPernet @slel

I think this message might be useful:

http://projects.scipy.org/pipermail/scipy-user/2008-December/019064.html



Issue created by migration from https://trac.sagemath.org/ticket/4789





---

archive/issue_comments_036305.json:
```json
{
    "body": "Changing component from algebra to linear algebra.",
    "created_at": "2008-12-14T01:58:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4789#issuecomment-36305",
    "user": "@jasongrout"
}
```

Changing component from algebra to linear algebra.



---

archive/issue_comments_036306.json:
```json
{
    "body": "Changing assignee from tbd to @jasongrout.",
    "created_at": "2008-12-14T01:58:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4789#issuecomment-36306",
    "user": "@jasongrout"
}
```

Changing assignee from tbd to @jasongrout.



---

archive/issue_comments_036307.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-12-14T01:58:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4789#issuecomment-36307",
    "user": "@jasongrout"
}
```

Changing status from new to assigned.



---

archive/issue_comments_036308.json:
```json
{
    "body": "Example:\n\n```\nsage: a = matrix(RDF,4,[1..16])*1.293949599304953485; a\n[ 1.2939495993 2.58789919861 3.88184879791 5.17579839722]\n[6.46974799652 7.76369759583 9.05764719513 10.3515967944]\n[11.6455463937  12.939495993 14.2334455924 15.5273951917]\n[ 16.821344791 18.1152943903 19.4092439896 20.7031935889]\nsage: a.kernel()\nVector space of degree 4 and dimension 0 over Real Double Field\nBasis matrix:\n[]\n```\n\nDefine this from the email linked to above:\n\n```\nimport scipy\nimport scipy.linalg\n\ndef null(A, eps=1e-15):\n    \"\"\"\n    computes the null space of the real matrix A\n    \"\"\"\n    n, m = scipy.shape(A)\n    if n > m :\n        return scipy.transpose(null(scipy.transpose(A), eps))\n        return null(scipy.transpose(A), eps)\n    u, s, vh = scipy.linalg.svd(A)\n    s=scipy.append(s,scipy.zeros(m))[0:m]\n    null_mask = (s <= eps)\n    null_space = scipy.compress(null_mask, vh, axis=0)\n    return scipy.transpose(null_space)\n```\n\n\nThen:\n\n\n```\nsage: null(a.numpy(),eps=1e-13)\narray([[-0.29797676,  0.45957573],\n       [ 0.73984987, -0.39066887],\n       [-0.58576946, -0.59738944],\n       [ 0.14389635,  0.52848258]])\n```\n",
    "created_at": "2009-12-11T23:36:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4789#issuecomment-36308",
    "user": "@williamstein"
}
```

Example:

```
sage: a = matrix(RDF,4,[1..16])*1.293949599304953485; a
[ 1.2939495993 2.58789919861 3.88184879791 5.17579839722]
[6.46974799652 7.76369759583 9.05764719513 10.3515967944]
[11.6455463937  12.939495993 14.2334455924 15.5273951917]
[ 16.821344791 18.1152943903 19.4092439896 20.7031935889]
sage: a.kernel()
Vector space of degree 4 and dimension 0 over Real Double Field
Basis matrix:
[]
```

Define this from the email linked to above:

```
import scipy
import scipy.linalg

def null(A, eps=1e-15):
    """
    computes the null space of the real matrix A
    """
    n, m = scipy.shape(A)
    if n > m :
        return scipy.transpose(null(scipy.transpose(A), eps))
        return null(scipy.transpose(A), eps)
    u, s, vh = scipy.linalg.svd(A)
    s=scipy.append(s,scipy.zeros(m))[0:m]
    null_mask = (s <= eps)
    null_space = scipy.compress(null_mask, vh, axis=0)
    return scipy.transpose(null_space)
```


Then:


```
sage: null(a.numpy(),eps=1e-13)
array([[-0.29797676,  0.45957573],
       [ 0.73984987, -0.39066887],
       [-0.58576946, -0.59738944],
       [ 0.14389635,  0.52848258]])
```




---

archive/issue_comments_036309.json:
```json
{
    "body": "As the Sage-8.8 release milestone is pending, we should delete the sage-8.8 milestone for tickets that are not actively being worked on or that still require significant work to move forward.  If you feel that this ticket should be included in the next Sage release at the soonest please set its milestone to the next release milestone (sage-8.9).",
    "created_at": "2019-06-14T14:54:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4789",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4789#issuecomment-36309",
    "user": "@embray"
}
```

As the Sage-8.8 release milestone is pending, we should delete the sage-8.8 milestone for tickets that are not actively being worked on or that still require significant work to move forward.  If you feel that this ticket should be included in the next Sage release at the soonest please set its milestone to the next release milestone (sage-8.9).
