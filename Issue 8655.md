# Issue 8655: Fix graph genus (broken on multigraphs?)

archive/issues_008655.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\n\n```\nsage: G = Graph(multiedges=True)\nsage: G.add_edge(0,1)\nsage: G.add_edge(0,1)\nsage: G.genus()\n1\nsage: G.to_simple().genus()\n0\n```\n\n\nAdding parallel edges to a graph never changes the minimal genus.  I'm concerned that genus() might be entirely broken... but maybe it's just on multigraphs?  At the very least, removing parallel edges will speed things up and fix this bug.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8655\n\n",
    "created_at": "2010-04-06T19:42:13Z",
    "labels": [
        "graph theory",
        "major",
        "bug"
    ],
    "title": "Fix graph genus (broken on multigraphs?)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8655",
    "user": "boothby"
}
```
Assignee: jason, ncohen, rlm


```
sage: G = Graph(multiedges=True)
sage: G.add_edge(0,1)
sage: G.add_edge(0,1)
sage: G.genus()
1
sage: G.to_simple().genus()
0
```


Adding parallel edges to a graph never changes the minimal genus.  I'm concerned that genus() might be entirely broken... but maybe it's just on multigraphs?  At the very least, removing parallel edges will speed things up and fix this bug.

Issue created by migration from https://trac.sagemath.org/ticket/8655





---

archive/issue_comments_078536.json:
```json
{
    "body": "Attachment\n\nDepends on #8691",
    "created_at": "2010-05-21T21:32:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8655#issuecomment-78536",
    "user": "boothby"
}
```

Attachment

Depends on #8691



---

archive/issue_comments_078537.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-21T21:35:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8655#issuecomment-78537",
    "user": "boothby"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_078538.json:
```json
{
    "body": "Everything applies cleanly and tests pass. I'll be willing to give this the thumbs up if the author wants to walk me through the code a little at Sage Days.",
    "created_at": "2010-05-25T23:55:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8655#issuecomment-78538",
    "user": "rlm"
}
```

Everything applies cleanly and tests pass. I'll be willing to give this the thumbs up if the author wants to walk me through the code a little at Sage Days.



---

archive/issue_comments_078539.json:
```json
{
    "body": "Changing assignee from jason, ncohen, rlm to rlm.",
    "created_at": "2010-05-27T21:48:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8655#issuecomment-78539",
    "user": "rlm"
}
```

Changing assignee from jason, ncohen, rlm to rlm.



---

archive/issue_comments_078540.json:
```json
{
    "body": "line 220 (raise MemoryError, \"Error allocating memory for graph genus a\")\nalso 228 (...)\n\n --> insert comment regarding free-ing automatically via dealloc\n\n\nline 231 -> probably a bitset way to do this faster\n\n\nline 296 -> memcpy = better good doing thing\n\ncdef list darts_to_verts (orbit_v?) in line 327",
    "created_at": "2010-05-27T21:48:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8655#issuecomment-78540",
    "user": "rlm"
}
```

line 220 (raise MemoryError, "Error allocating memory for graph genus a")
also 228 (...)

 --> insert comment regarding free-ing automatically via dealloc


line 231 -> probably a bitset way to do this faster


line 296 -> memcpy = better good doing thing

cdef list darts_to_verts (orbit_v?) in line 327



---

archive/issue_comments_078541.json:
```json
{
    "body": "ammendments to satisfy reviewer",
    "created_at": "2010-05-27T22:48:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8655#issuecomment-78541",
    "user": "boothby"
}
```

ammendments to satisfy reviewer



---

archive/issue_comments_078542.json:
```json
{
    "body": "Attachment\n\nRegarding \"line 231 -> probably a bitset way to do this faster\", I agree, there probably is, but I'd rather not peek any further into the cgraph structure than necessary.",
    "created_at": "2010-05-27T22:49:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8655#issuecomment-78542",
    "user": "boothby"
}
```

Attachment

Regarding "line 231 -> probably a bitset way to do this faster", I agree, there probably is, but I'd rather not peek any further into the cgraph structure than necessary.



---

archive/issue_comments_078543.json:
```json
{
    "body": "Maths speeds up!",
    "created_at": "2010-05-27T23:03:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8655#issuecomment-78543",
    "user": "rlm"
}
```

Maths speeds up!



---

archive/issue_comments_078544.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-27T23:03:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8655#issuecomment-78544",
    "user": "rlm"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_078545.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-05T22:07:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8655#issuecomment-78545",
    "user": "mhansen"
}
```

Resolution: fixed
