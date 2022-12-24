# Issue 2546: vectors over SR should be callable? over function rings?

archive/issues_002546.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: function rings vectors\n\nElements of SR are \"callable\", perhaps vectors over SR should be too, which wouldallows symbolic vectors to act as vector-valued mappings from R<sup>m</sup> -> R<sup>n</sup>.\n\nNow that I think about it, I don't know if it really makes sense for SR elts to be callable, since how does one define order of arguments (or arguments period for that matter)? The problem gets worse if you are talking about a vector with SR coefficients.\n\nI actually like the symbolic function ring syntax/construction much better since it makes the mapping explicit (if a mapping is what you want to represent), but these seem to be less well-supported (for example, ` _f(x,y)=x<sup>2+y</sup>2; g(x,y)=1;vector((f,g)) ` yields a NotImplementedError ) and are definitely less common in doctest examples. I think a vector over a particular symbolic function ring  (say the one from (x,y,z)) would be a particularly useful mathematical object. vector((x1, x2, ..., xn)) could give an error (NotImplemented or just NotAGoodIdea). Then the resulting vector would be a clear mapping from R<sup>m</sup> to R<sup>n</sup>, with a well-defined argument order. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2546\n\n",
    "created_at": "2008-03-16T16:42:12Z",
    "labels": [
        "linear algebra",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "vectors over SR should be callable? over function rings?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2546",
    "user": "edrex"
}
```
Assignee: @williamstein

Keywords: function rings vectors

Elements of SR are "callable", perhaps vectors over SR should be too, which wouldallows symbolic vectors to act as vector-valued mappings from R<sup>m</sup> -> R<sup>n</sup>.

Now that I think about it, I don't know if it really makes sense for SR elts to be callable, since how does one define order of arguments (or arguments period for that matter)? The problem gets worse if you are talking about a vector with SR coefficients.

I actually like the symbolic function ring syntax/construction much better since it makes the mapping explicit (if a mapping is what you want to represent), but these seem to be less well-supported (for example, ` _f(x,y)=x<sup>2+y</sup>2; g(x,y)=1;vector((f,g)) ` yields a NotImplementedError ) and are definitely less common in doctest examples. I think a vector over a particular symbolic function ring  (say the one from (x,y,z)) would be a particularly useful mathematical object. vector((x1, x2, ..., xn)) could give an error (NotImplemented or just NotAGoodIdea). Then the resulting vector would be a clear mapping from R<sup>m</sup> to R<sup>n</sup>, with a well-defined argument order. 

Issue created by migration from https://trac.sagemath.org/ticket/2546





---

archive/issue_comments_017378.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-03-16T20:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2546#issuecomment-17378",
    "user": "@garyfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_017379.json:
```json
{
    "body": "Changing assignee from @williamstein to @garyfurnish.",
    "created_at": "2008-03-16T20:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2546#issuecomment-17379",
    "user": "@garyfurnish"
}
```

Changing assignee from @williamstein to @garyfurnish.



---

archive/issue_comments_017380.json:
```json
{
    "body": "Invalid.  This is the sort of thing that needs to be discussed on sage-support or sage-devel.  If a VERY CLEAR task emerges, then that goes into trac.",
    "created_at": "2008-03-16T20:48:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2546#issuecomment-17380",
    "user": "@williamstein"
}
```

Invalid.  This is the sort of thing that needs to be discussed on sage-support or sage-devel.  If a VERY CLEAR task emerges, then that goes into trac.



---

archive/issue_comments_017381.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-03-16T20:48:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2546#issuecomment-17381",
    "user": "@williamstein"
}
```

Resolution: invalid



---

archive/issue_comments_017382.json:
```json
{
    "body": "See also #2549 for a related ticket.",
    "created_at": "2009-02-13T17:44:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2546",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2546#issuecomment-17382",
    "user": "@jasongrout"
}
```

See also #2549 for a related ticket.
