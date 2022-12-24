# Issue 4625: improve pth power map for finite fields of characteristic p

archive/issues_004625.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  @JohnCremona\n\nKeywords: field element, frobenius\n\nThe implementation of the pth_power method for FiniteFieldElement is naive; maybe it can be sped up.  cremona had the following suggestion in the discussion about ticket #4553:\n\n```\nLastly, I think it would be more efficient to compute (and cache) the matrix of frobenius \nas a linear map, viewing F_q as an F_p-vector space of dimension d where q=p^d. I know \nan efficient way to do this (similar to tricks used in Berlekamp factorization). Then taking \nq'th roots would be easy (invert the matrix).\n```\n\n\n```\nThe linear algebra approach will have to wait until we have a common interface for all \nfinite fields -- currently the functions available depend on q since they differ according \nto whether we use givaro or NTL or pari. (e.g. an element a in GF(q) sometimes has \na._coordinates() but not always. So it's fine to go ahead with this one for now, perhaps \nwith a note that a better implementation might be possible in future.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4625\n\n",
    "created_at": "2008-11-26T15:58:21Z",
    "labels": [
        "algebra",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "improve pth power map for finite fields of characteristic p",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4625",
    "user": "@jhpalmieri"
}
```
Assignee: somebody

CC:  @JohnCremona

Keywords: field element, frobenius

The implementation of the pth_power method for FiniteFieldElement is naive; maybe it can be sped up.  cremona had the following suggestion in the discussion about ticket #4553:

```
Lastly, I think it would be more efficient to compute (and cache) the matrix of frobenius 
as a linear map, viewing F_q as an F_p-vector space of dimension d where q=p^d. I know 
an efficient way to do this (similar to tricks used in Berlekamp factorization). Then taking 
q'th roots would be easy (invert the matrix).
```


```
The linear algebra approach will have to wait until we have a common interface for all 
finite fields -- currently the functions available depend on q since they differ according 
to whether we use givaro or NTL or pari. (e.g. an element a in GF(q) sometimes has 
a._coordinates() but not always. So it's fine to go ahead with this one for now, perhaps 
with a note that a better implementation might be possible in future.
```


Issue created by migration from https://trac.sagemath.org/ticket/4625





---

archive/issue_comments_034782.json:
```json
{
    "body": "Changing priority from minor to major.",
    "created_at": "2010-01-01T23:15:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4625",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4625#issuecomment-34782",
    "user": "@aghitza"
}
```

Changing priority from minor to major.
