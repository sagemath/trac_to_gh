# Issue 6066: constructing Sage graphs is slow compared to NetworkX graphs

archive/issues_006066.json:
```json
{
    "body": "Assignee: rlm\n\nSee https://groups.google.com/group/sage-devel/browse_thread/thread/802227fa22233d5/310379356a804e7f\n\n```\nI was playing with some big(10^6) graphs and noticed SAGE cannot\nhandle constructing them in good time. However, networkx does just\nfine. Before I dive into the code, is this a feature (i.e. sage graph\nobject has richer data and methods available) or this is a bug?\n\nsage: D={}\nsage: for i in xrange(10^3):\n    D[i]=[i+1,i-1]\n....:\nsage: timeit('g=Graph(D)')\n5 loops, best of 3: 2.05 s per loop\nsage: import networkx\nsage: timeit('g=networkx.XGraph(D)')\n25 loops, best of 3: 21.9 ms per loop\n\nRado \n```\n\nThen\n\n```\nThe bug is almost trivial. The code\n\nverts = data.keys()\n....\nfor u in data:\n   verts.union([v for v in data[u] if v not in verts])\n\nis slowing down because in python searching in lists is slow. If we\nuse \"verts = set(data.keys())\" the code speeds up tremendously.\n\nsage: D={}\nsage: for i in xrange(10^3):\n....:     D[i]=[i+1,i-1]\n....:\nsage: timeit('g=Graph(D)')\n5 loops, best of 3: 79.6 ms per loop\n\nBefore I submit a patch how do I run the the graph theory doctests to\nmake sure nothing else is broken by changing verts from list to set?\n\nRado \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6066\n\n",
    "created_at": "2009-05-18T07:45:45Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "constructing Sage graphs is slow compared to NetworkX graphs",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6066",
    "user": "mabshoff"
}
```
Assignee: rlm

See https://groups.google.com/group/sage-devel/browse_thread/thread/802227fa22233d5/310379356a804e7f

```
I was playing with some big(10^6) graphs and noticed SAGE cannot
handle constructing them in good time. However, networkx does just
fine. Before I dive into the code, is this a feature (i.e. sage graph
object has richer data and methods available) or this is a bug?

sage: D={}
sage: for i in xrange(10^3):
    D[i]=[i+1,i-1]
....:
sage: timeit('g=Graph(D)')
5 loops, best of 3: 2.05 s per loop
sage: import networkx
sage: timeit('g=networkx.XGraph(D)')
25 loops, best of 3: 21.9 ms per loop

Rado 
```

Then

```
The bug is almost trivial. The code

verts = data.keys()
....
for u in data:
   verts.union([v for v in data[u] if v not in verts])

is slowing down because in python searching in lists is slow. If we
use "verts = set(data.keys())" the code speeds up tremendously.

sage: D={}
sage: for i in xrange(10^3):
....:     D[i]=[i+1,i-1]
....:
sage: timeit('g=Graph(D)')
5 loops, best of 3: 79.6 ms per loop

Before I submit a patch how do I run the the graph theory doctests to
make sure nothing else is broken by changing verts from list to set?

Rado 
```


Issue created by migration from https://trac.sagemath.org/ticket/6066





---

archive/issue_comments_048277.json:
```json
{
    "body": "Attachment [11804.2.patch](tarball://root/attachments/some-uuid/ticket6066/11804.2.patch) by mabshoff created at 2009-05-18 07:47:19",
    "created_at": "2009-05-18T07:47:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6066#issuecomment-48277",
    "user": "mabshoff"
}
```

Attachment [11804.2.patch](tarball://root/attachments/some-uuid/ticket6066/11804.2.patch) by mabshoff created at 2009-05-18 07:47:19



---

archive/issue_comments_048278.json:
```json
{
    "body": "Doctests pass in `graphs` and `combinat`, and long tests also pass in `graphs`. This needs to be tested on all of Sage before it gets merged, but pending that, I say merge the code!",
    "created_at": "2009-05-18T18:16:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6066#issuecomment-48278",
    "user": "rlm"
}
```

Doctests pass in `graphs` and `combinat`, and long tests also pass in `graphs`. This needs to be tested on all of Sage before it gets merged, but pending that, I say merge the code!



---

archive/issue_comments_048279.json:
```json
{
    "body": "Doctests pass long globally, too.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-18T18:18:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6066#issuecomment-48279",
    "user": "mabshoff"
}
```

Doctests pass long globally, too.

Cheers,

Michael



---

archive/issue_comments_048280.json:
```json
{
    "body": "Merged in Sage 4.0.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-18T18:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6066#issuecomment-48280",
    "user": "mabshoff"
}
```

Merged in Sage 4.0.rc0.

Cheers,

Michael



---

archive/issue_comments_048281.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-18T18:29:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6066",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6066#issuecomment-48281",
    "user": "mabshoff"
}
```

Resolution: fixed
