# Issue 4182: plot3d fails with 'IndexError: list index out of range'

archive/issues_004182.json:
```json
{
    "body": "Assignee: was\n\n\n```\nsage: def g(x,y): \n...            if y <= 0 or y >= x**2: \n...                return 0 \n...           else: \n...               return 1 \nsage: plot3d(g, (-3, 3), (-3, 3), adaptive=True) \n```\n\nfails, returning\n\n```\nTraceback (most recent call last): \n  File \"<stdin>\", line 1, in <module> \n  File \"/home/palmieri/.sage/sage_notebook/worksheets/admin/37/code/ \n7.py\", line 6, in <module> \n    plot3d(g, (-Integer(3), Integer(3)), (-Integer(3), Integer(3)), \nadaptive=True) \n  File \"/usr/local/share/sage/local/lib/python2.5/site-packages/ \nSQLAlchemy-0.4.6-py2.5.egg/\", line 1, in <module> \n  File \"/home/palmieri/Documents/sage-3.1.2/local/lib/python2.5/site- \npackages/sage/plot/plot3d/plot3d.py\", line 157, in plot3d \n    P = plot3d_adaptive(f, urange, vrange, **kwds) \n  File \"/home/palmieri/Documents/sage-3.1.2/local/lib/python2.5/site- \npackages/sage/plot/plot3d/plot3d.py\", line 255, in plot3d_adaptive \n    G.set_texture(texture[k], opacity=opacity) \nIndexError: list index out of range\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4182\n\n",
    "created_at": "2008-09-23T22:52:24Z",
    "labels": [
        "graphics",
        "minor",
        "bug"
    ],
    "title": "plot3d fails with 'IndexError: list index out of range'",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4182",
    "user": "jhpalmieri"
}
```
Assignee: was


```
sage: def g(x,y): 
...            if y <= 0 or y >= x**2: 
...                return 0 
...           else: 
...               return 1 
sage: plot3d(g, (-3, 3), (-3, 3), adaptive=True) 
```

fails, returning

```
Traceback (most recent call last): 
  File "<stdin>", line 1, in <module> 
  File "/home/palmieri/.sage/sage_notebook/worksheets/admin/37/code/ 
7.py", line 6, in <module> 
    plot3d(g, (-Integer(3), Integer(3)), (-Integer(3), Integer(3)), 
adaptive=True) 
  File "/usr/local/share/sage/local/lib/python2.5/site-packages/ 
SQLAlchemy-0.4.6-py2.5.egg/", line 1, in <module> 
  File "/home/palmieri/Documents/sage-3.1.2/local/lib/python2.5/site- 
packages/sage/plot/plot3d/plot3d.py", line 157, in plot3d 
    P = plot3d_adaptive(f, urange, vrange, **kwds) 
  File "/home/palmieri/Documents/sage-3.1.2/local/lib/python2.5/site- 
packages/sage/plot/plot3d/plot3d.py", line 255, in plot3d_adaptive 
    G.set_texture(texture[k], opacity=opacity) 
IndexError: list index out of range
```


Issue created by migration from https://trac.sagemath.org/ticket/4182





---

archive/issue_comments_030353.json:
```json
{
    "body": "Attachment [4182.patch](tarball://root/attachments/some-uuid/ticket4182/4182.patch) by jhpalmieri created at 2008-10-20 21:19:01",
    "created_at": "2008-10-20T21:19:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4182#issuecomment-30353",
    "user": "jhpalmieri"
}
```

Attachment [4182.patch](tarball://root/attachments/some-uuid/ticket4182/4182.patch) by jhpalmieri created at 2008-10-20 21:19:01



---

archive/issue_comments_030354.json:
```json
{
    "body": "Here's a patch.  I was getting an index error in the last line in this code snippet:\n\n```\n                span = len(texture) / (max_z - min_z)    # max to avoid dividing by 0\n            parts = P.partition(lambda x,y,z: int((z-min_z)*span))\n        all = []\n        for k, G in parts.iteritems():\n            G.set_texture(texture[k], opacity=opacity)\n```\n\nThe function g(x,y) described above is discontinuous at various places, and I think this was making the `k` in the last line of this snippet equal to 128 while `len(texture)` was also 128. Changing the definition of `span` in the first line, as this patch does, I hope should make `k` always strictly less than `len(texture)`.",
    "created_at": "2008-10-20T21:25:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4182#issuecomment-30354",
    "user": "jhpalmieri"
}
```

Here's a patch.  I was getting an index error in the last line in this code snippet:

```
                span = len(texture) / (max_z - min_z)    # max to avoid dividing by 0
            parts = P.partition(lambda x,y,z: int((z-min_z)*span))
        all = []
        for k, G in parts.iteritems():
            G.set_texture(texture[k], opacity=opacity)
```

The function g(x,y) described above is discontinuous at various places, and I think this was making the `k` in the last line of this snippet equal to 128 while `len(texture)` was also 128. Changing the definition of `span` in the first line, as this patch does, I hope should make `k` always strictly less than `len(texture)`.



---

archive/issue_comments_030355.json:
```json
{
    "body": "This does fix the problem and looks ok.",
    "created_at": "2008-10-23T19:50:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4182#issuecomment-30355",
    "user": "anakha"
}
```

This does fix the problem and looks ok.



---

archive/issue_comments_030356.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-26T03:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4182#issuecomment-30356",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030357.json:
```json
{
    "body": "Merged in Sage 3.2.alpha1",
    "created_at": "2008-10-26T03:18:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4182",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4182#issuecomment-30357",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.alpha1
