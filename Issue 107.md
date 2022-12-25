# Issue 107: can't multiply matrix by vector over an arbitrary ring?

archive/issues_000107.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nsage: R = Integers(125)\nsage: M = Matrix(R, 2, 2, [0, 1, 2, 3])\nsage: V = Vector(R, [2, 3])\nsage: M * V\n---------------------------------------------------------------------------\nexceptions.AttributeError                            Traceback (most recent call last)\n\n/home/dmharvey/sage-1.3.7.3.3/<ipython console> \n\n/home/dmharvey/sage-1.3.7.3.3/matrix_pyx.pyx in matrix_pyx.Matrix.__mul__()\n\n/home/dmharvey/sage-1.3.7.3.3/matrix_pyx.pyx in matrix_pyx.Matrix.vector_matrix_multiply()\n\n/home/dmharvey/sage/local/lib/python2.4/site-packages/sage/modules/free_module_element.py in __add__(self, right)\n     65         if self.parent() is right.parent():\n     66             V = self.parent()\n---> 67         elif self.parent().ambient_vector_space() == right.parent().ambient_vector_space():\n     68             V = self.parent().ambient_vector_space()\n     69         else:\n\nAttributeError: 'FreeModule_ambient' object has no attribute 'ambient_vector_space'\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/107\n\n",
    "created_at": "2006-10-03T17:50:08Z",
    "labels": [
        "component: linear algebra",
        "bug"
    ],
    "title": "can't multiply matrix by vector over an arbitrary ring?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/107",
    "user": "https://trac.sagemath.org/admin/accounts/users/dmharvey"
}
```
Assignee: @williamstein


```
sage: R = Integers(125)
sage: M = Matrix(R, 2, 2, [0, 1, 2, 3])
sage: V = Vector(R, [2, 3])
sage: M * V
---------------------------------------------------------------------------
exceptions.AttributeError                            Traceback (most recent call last)

/home/dmharvey/sage-1.3.7.3.3/<ipython console> 

/home/dmharvey/sage-1.3.7.3.3/matrix_pyx.pyx in matrix_pyx.Matrix.__mul__()

/home/dmharvey/sage-1.3.7.3.3/matrix_pyx.pyx in matrix_pyx.Matrix.vector_matrix_multiply()

/home/dmharvey/sage/local/lib/python2.4/site-packages/sage/modules/free_module_element.py in __add__(self, right)
     65         if self.parent() is right.parent():
     66             V = self.parent()
---> 67         elif self.parent().ambient_vector_space() == right.parent().ambient_vector_space():
     68             V = self.parent().ambient_vector_space()
     69         else:

AttributeError: 'FreeModule_ambient' object has no attribute 'ambient_vector_space'
```



Issue created by migration from https://trac.sagemath.org/ticket/107





---

archive/issue_comments_000505.json:
```json
{
    "body": "We shouldn't bother fixing this until when we are doing the serious pyrexing of linear algebra...",
    "created_at": "2006-10-05T08:16:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/107#issuecomment-505",
    "user": "https://github.com/williamstein"
}
```

We shouldn't bother fixing this until when we are doing the serious pyrexing of linear algebra...



---

archive/issue_comments_000506.json:
```json
{
    "body": "This works fine now in sage-1.5:\n\n```\nsage: R = Integers(125)\nsage: M = Matrix(R, 2, 2, [0, 1, 2, 3])\nsage: V = vector(R, [2, 3])\nsage: M * V\n(3, 13)\n```\n",
    "created_at": "2007-01-07T19:42:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/107#issuecomment-506",
    "user": "https://github.com/williamstein"
}
```

This works fine now in sage-1.5:

```
sage: R = Integers(125)
sage: M = Matrix(R, 2, 2, [0, 1, 2, 3])
sage: V = vector(R, [2, 3])
sage: M * V
(3, 13)
```




---

archive/issue_events_000217.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2007-01-07T19:42:39Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/107",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/107#event-217"
}
```



---

archive/issue_comments_000507.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-07T19:42:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/107",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/107#issuecomment-507",
    "user": "https://github.com/williamstein"
}
```

Resolution: fixed
