# Issue 1085: include John Voight's code for enumerating totally real fields

archive/issues_001085.json:
```json
{
    "body": "Assignee: craigcitro\n\nJohn Voight has written some code for enumerating totally real fields; this needs to be added into SAGE. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1085\n\n",
    "created_at": "2007-11-03T20:16:55Z",
    "labels": [
        "number theory",
        "major",
        "enhancement"
    ],
    "title": "include John Voight's code for enumerating totally real fields",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1085",
    "user": "craigcitro"
}
```
Assignee: craigcitro

John Voight has written some code for enumerating totally real fields; this needs to be added into SAGE. 

Issue created by migration from https://trac.sagemath.org/ticket/1085





---

archive/issue_comments_006559.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-11-28T00:49:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1085#issuecomment-6559",
    "user": "craigcitro"
}
```

Changing status from new to assigned.



---

archive/issue_comments_006560.json:
```json
{
    "body": "Finally! \n\nSo this is the bundle with John's code in it. It's larger than it should be, because there are a few merges, but it shouldn't be any trouble to include. \n\nI was the referee for this patch, but I also ended up writing a bit of code for it, so I think someone should review the patch for me? I'm not sure. In any event, it has my strong endorsement, and I'd like to see it included in 2.10.2.",
    "created_at": "2008-02-13T10:58:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1085#issuecomment-6560",
    "user": "craigcitro"
}
```

Finally! 

So this is the bundle with John's code in it. It's larger than it should be, because there are a few merges, but it shouldn't be any trouble to include. 

I was the referee for this patch, but I also ended up writing a bit of code for it, so I think someone should review the patch for me? I'm not sure. In any event, it has my strong endorsement, and I'd like to see it included in 2.10.2.



---

archive/issue_comments_006561.json:
```json
{
    "body": "Attachment\n\nMerged in Sage 2.10.2.alpha0 - if you find additional issues please open another ticket and post patches there.",
    "created_at": "2008-02-13T13:07:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1085#issuecomment-6561",
    "user": "mabshoff"
}
```

Attachment

Merged in Sage 2.10.2.alpha0 - if you find additional issues please open another ticket and post patches there.



---

archive/issue_comments_006562.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-02-13T13:07:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1085#issuecomment-6562",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_006563.json:
```json
{
    "body": "Attachment\n\nMerged the updated trac-1085-jv-mods.hg in Sage 2.10.2.alpha0",
    "created_at": "2008-02-14T10:55:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1085#issuecomment-6563",
    "user": "mabshoff"
}
```

Attachment

Merged the updated trac-1085-jv-mods.hg in Sage 2.10.2.alpha0



---

archive/issue_comments_006564.json:
```json
{
    "body": "With the second bundle applied I get the following doctest failure on sage.math:\n\n```\nsage -t  devel/sage-main/sage/rings/number_field/totallyreal_rel.py\n**********************************************************************\nFile \"totallyreal_rel.py\", line 92:\n    sage: sage.rings.number_field.totallyreal_rel.integral_elements_in_box(K, [[0,5],[0,10]])\nExpected:\n    [0, 5, -alpha + 2, -alpha + 3, 1, 2, 3, 4, alpha + 2, alpha + 3, alpha + 4, alpha + 5, alpha + 6, 2*alpha + 3, 2*alpha + 4, 2*alpha + 5, 2*alpha + 6, 2*alpha + 7, 3*alpha + 5]\nGot:\n    [0, -alpha + 3, -alpha + 2, 5, 4, 3, 2, 1, alpha + 6, alpha + 5, alpha + 4, alpha + 3, alpha + 2, 2*alpha + 7, 2*alpha + 6, 2*alpha + 5, 2*alpha + 4, 2*alpha + 3, 3*alpha + 5]\n**********************************************************************\nFile \"totallyreal_rel.py\", line 625:\n    sage: enumerate_totallyreal_fields_rel(F, 2, 10^4)\nExpected:\n    [[725, x^4 - x^3 - 3*x^2 + x + 1, xF^2 + (-1/2*t + 1/2)*xF - t - 2],\n     [1125, x^4 - x^3 - 4*x^2 + 4*x + 1, xF^2 + (-1/2*t + 1/2)*xF - 1/2*t - 3/2],\n     [1600, x^4 - 6*x^2 + 4, xF^2 - t - 3],\n     [2000, x^4 - 5*x^2 + 5, xF^2 - 1/2*t - 5/2],\n     [2225, x^4 - x^3 - 5*x^2 + 2*x + 4, xF^2 + (-1/2*t + 1/2)*xF - 3/2*t - 7/2],\n     [2525, x^4 - 2*x^3 - 4*x^2 + 5*x + 5, xF^2 + (-1/2*t - 1/2)*xF - 1/2*t - 5/2],\n     [3600, x^4 - 2*x^3 - 7*x^2 + 8*x + 1, xF^2 - 3/2*t - 9/2],\n     [4225, x^4 - 9*x^2 + 4, xF^2 + (-1/2*t - 1/2)*xF - 3/2*t - 9/2],\n     [4400, x^4 - 7*x^2 + 11, xF^2 - 1/2*t - 7/2],\n     [4525, x^4 - x^3 - 7*x^2 + 3*x + 9, xF^2 + (-1/2*t - 1/2)*xF - 3],\n     [5125, x^4 - 2*x^3 - 6*x^2 + 7*x + 11, xF^2 + (-1/2*t - 1/2)*xF - t - 4],\n     [5225, x^4 - x^3 - 8*x^2 + x + 11, xF^2 + (-1/2*t - 1/2)*xF - 1/2*t - 7/2],\n     [5725, x^4 - x^3 - 8*x^2 + 6*x + 11, xF^2 + (-1/2*t + 1/2)*xF - 1/2*t - 7/2],\n     [6125, x^4 - x^3 - 9*x^2 + 9*x + 11, xF^2 + (-1/2*t + 1/2)*xF - t - 4],\n     [7600, x^4 - 9*x^2 + 19, xF^2 - 1/2*t - 9/2],\n     [7625, x^4 - x^3 - 9*x^2 + 4*x + 16, xF^2 + (-1/2*t - 1/2)*xF - 4],\n     [8000, x^4 - 10*x^2 + 20, xF^2 - t - 5],\n     [8525, x^4 - 2*x^3 - 8*x^2 + 9*x + 19, xF^2 + xF - 1/2*t - 9/2],\n     [8725, x^4 - x^3 - 10*x^2 + 2*x + 19, xF^2 + (-1/2*t - 1/2)*xF - 1/2*t - 9/2],\n     [9225, x^4 - x^3 - 10*x^2 + 7*x + 19, xF^2 + (-1/2*t + 1/2)*xF - 1/2*t - 9/2]]\nGot:\n    [[725, x^4 - x^3 - 3*x^2 + x + 1, xF^2 + (-1/2*t + 1/2)*xF - t - 2], [1125, x^4 - x^3 - 4*x^2 + 4*x + 1, xF^2 + (-1/2*t + 1/2)*xF - 1/2*t - 3/2], [1600, x^4 - 6*x^2 + 4, xF^2 - t - 3], [2000, x^4 - 5*x^2 + 5, xF^2 - 1/2*t - 5/2], [2225, x^4 - x^3 - 5*x^2 + 2*x + 4, xF^2 + (-1/2*t + 1/2)*xF - 3/2*t - 7/2], [2525, x^4 - 2*x^3 - 4*x^2 + 5*x + 5, xF^2 + (-1/2*t - 1/2)*xF - 1/2*t - 5/2], [3600, x^4 - 2*x^3 - 7*x^2 + 8*x + 1, xF^2 - 3/2*t - 9/2], [4225, x^4 - 9*x^2 + 4, xF^2 + (-1/2*t - 1/2)*xF - 3/2*t - 9/2], [4400, x^4 - 7*x^2 + 11, xF^2 - 1/2*t - 7/2], [4525, x^4 - x^3 - 7*x^2 + 3*x + 9, xF^2 + (-1/2*t - 1/2)*xF - 3], [5125, x^4 - 2*x^3 - 6*x^2 + 7*x + 11, xF^2 + (-1/2*t - 1/2)*xF - t - 4], [5225, x^4 - x^3 - 8*x^2 + x + 11, xF^2 + (-1/2*t - 1/2)*xF - 1/2*t - 7/2], [5725, x^4 - x^3 - 8*x^2 + 6*x + 11, xF^2 + (-1/2*t + 1/2)*xF - 1/2*t - 7/2], [6125, x^4 - x^3 - 9*x^2 + 9*x + 11, xF^2 + (-1/2*t + 1/2)*xF - t - 4], [7600, x^4 - 9*x^2 + 19, xF^2 - 1/2*t - 9/2], [7625, x^4 - x^3 - 9*x^2 + 4*x + 16, xF^2 + (-1/2*t - 1/2)*xF - 4], [8000, x^4 - 10*x^2 + 20, xF^2 - t - 5], [8525, x^4 - 2*x^3 - 8*x^2 + 9*x + 19, xF^2 + (-1)*xF - 1/2*t - 9/2], [8725, x^4 - x^3 - 10*x^2 + 2*x + 19, xF^2 + (-1/2*t - 1/2)*xF - 1/2*t - 9/2], [9225, x^4 - x^3 - 10*x^2 + 7*x + 19, xF^2 + (-1/2*t + 1/2)*xF - 1/2*t - 9/2]]\n**********************************************************************\nFile \"totallyreal_rel.py\", line 661:\n    sage: enumerate_totallyreal_fields_rel(F, 3, 17*10^9)\nExpected:\n    [[16240385609L, x^9 - x^8 - 9*x^7 + 4*x^6 + 26*x^5 - 2*x^4 - 25*x^3 - x^2 + 7*x + 1, xF^3 + (-t^2 - 4*t + 1)*xF^2 + (t^2 + 3*t - 5)*xF + 3*t^2 + 11*t - 5]]\nGot:\n    [[16240385609, x^9 - x^8 - 9*x^7 + 4*x^6 + 26*x^5 - 2*x^4 - 25*x^3 - x^2 + 7*x + 1, xF^3 + (-t^2 - 4*t + 1)*xF^2 + (t^2 + 3*t - 5)*xF + 3*t^2 + 11*t - 5]]\n**********************************************************************\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-02-14T10:56:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1085#issuecomment-6564",
    "user": "mabshoff"
}
```

With the second bundle applied I get the following doctest failure on sage.math:

```
sage -t  devel/sage-main/sage/rings/number_field/totallyreal_rel.py
**********************************************************************
File "totallyreal_rel.py", line 92:
    sage: sage.rings.number_field.totallyreal_rel.integral_elements_in_box(K, [[0,5],[0,10]])
Expected:
    [0, 5, -alpha + 2, -alpha + 3, 1, 2, 3, 4, alpha + 2, alpha + 3, alpha + 4, alpha + 5, alpha + 6, 2*alpha + 3, 2*alpha + 4, 2*alpha + 5, 2*alpha + 6, 2*alpha + 7, 3*alpha + 5]
Got:
    [0, -alpha + 3, -alpha + 2, 5, 4, 3, 2, 1, alpha + 6, alpha + 5, alpha + 4, alpha + 3, alpha + 2, 2*alpha + 7, 2*alpha + 6, 2*alpha + 5, 2*alpha + 4, 2*alpha + 3, 3*alpha + 5]
**********************************************************************
File "totallyreal_rel.py", line 625:
    sage: enumerate_totallyreal_fields_rel(F, 2, 10^4)
Expected:
    [[725, x^4 - x^3 - 3*x^2 + x + 1, xF^2 + (-1/2*t + 1/2)*xF - t - 2],
     [1125, x^4 - x^3 - 4*x^2 + 4*x + 1, xF^2 + (-1/2*t + 1/2)*xF - 1/2*t - 3/2],
     [1600, x^4 - 6*x^2 + 4, xF^2 - t - 3],
     [2000, x^4 - 5*x^2 + 5, xF^2 - 1/2*t - 5/2],
     [2225, x^4 - x^3 - 5*x^2 + 2*x + 4, xF^2 + (-1/2*t + 1/2)*xF - 3/2*t - 7/2],
     [2525, x^4 - 2*x^3 - 4*x^2 + 5*x + 5, xF^2 + (-1/2*t - 1/2)*xF - 1/2*t - 5/2],
     [3600, x^4 - 2*x^3 - 7*x^2 + 8*x + 1, xF^2 - 3/2*t - 9/2],
     [4225, x^4 - 9*x^2 + 4, xF^2 + (-1/2*t - 1/2)*xF - 3/2*t - 9/2],
     [4400, x^4 - 7*x^2 + 11, xF^2 - 1/2*t - 7/2],
     [4525, x^4 - x^3 - 7*x^2 + 3*x + 9, xF^2 + (-1/2*t - 1/2)*xF - 3],
     [5125, x^4 - 2*x^3 - 6*x^2 + 7*x + 11, xF^2 + (-1/2*t - 1/2)*xF - t - 4],
     [5225, x^4 - x^3 - 8*x^2 + x + 11, xF^2 + (-1/2*t - 1/2)*xF - 1/2*t - 7/2],
     [5725, x^4 - x^3 - 8*x^2 + 6*x + 11, xF^2 + (-1/2*t + 1/2)*xF - 1/2*t - 7/2],
     [6125, x^4 - x^3 - 9*x^2 + 9*x + 11, xF^2 + (-1/2*t + 1/2)*xF - t - 4],
     [7600, x^4 - 9*x^2 + 19, xF^2 - 1/2*t - 9/2],
     [7625, x^4 - x^3 - 9*x^2 + 4*x + 16, xF^2 + (-1/2*t - 1/2)*xF - 4],
     [8000, x^4 - 10*x^2 + 20, xF^2 - t - 5],
     [8525, x^4 - 2*x^3 - 8*x^2 + 9*x + 19, xF^2 + xF - 1/2*t - 9/2],
     [8725, x^4 - x^3 - 10*x^2 + 2*x + 19, xF^2 + (-1/2*t - 1/2)*xF - 1/2*t - 9/2],
     [9225, x^4 - x^3 - 10*x^2 + 7*x + 19, xF^2 + (-1/2*t + 1/2)*xF - 1/2*t - 9/2]]
Got:
    [[725, x^4 - x^3 - 3*x^2 + x + 1, xF^2 + (-1/2*t + 1/2)*xF - t - 2], [1125, x^4 - x^3 - 4*x^2 + 4*x + 1, xF^2 + (-1/2*t + 1/2)*xF - 1/2*t - 3/2], [1600, x^4 - 6*x^2 + 4, xF^2 - t - 3], [2000, x^4 - 5*x^2 + 5, xF^2 - 1/2*t - 5/2], [2225, x^4 - x^3 - 5*x^2 + 2*x + 4, xF^2 + (-1/2*t + 1/2)*xF - 3/2*t - 7/2], [2525, x^4 - 2*x^3 - 4*x^2 + 5*x + 5, xF^2 + (-1/2*t - 1/2)*xF - 1/2*t - 5/2], [3600, x^4 - 2*x^3 - 7*x^2 + 8*x + 1, xF^2 - 3/2*t - 9/2], [4225, x^4 - 9*x^2 + 4, xF^2 + (-1/2*t - 1/2)*xF - 3/2*t - 9/2], [4400, x^4 - 7*x^2 + 11, xF^2 - 1/2*t - 7/2], [4525, x^4 - x^3 - 7*x^2 + 3*x + 9, xF^2 + (-1/2*t - 1/2)*xF - 3], [5125, x^4 - 2*x^3 - 6*x^2 + 7*x + 11, xF^2 + (-1/2*t - 1/2)*xF - t - 4], [5225, x^4 - x^3 - 8*x^2 + x + 11, xF^2 + (-1/2*t - 1/2)*xF - 1/2*t - 7/2], [5725, x^4 - x^3 - 8*x^2 + 6*x + 11, xF^2 + (-1/2*t + 1/2)*xF - 1/2*t - 7/2], [6125, x^4 - x^3 - 9*x^2 + 9*x + 11, xF^2 + (-1/2*t + 1/2)*xF - t - 4], [7600, x^4 - 9*x^2 + 19, xF^2 - 1/2*t - 9/2], [7625, x^4 - x^3 - 9*x^2 + 4*x + 16, xF^2 + (-1/2*t - 1/2)*xF - 4], [8000, x^4 - 10*x^2 + 20, xF^2 - t - 5], [8525, x^4 - 2*x^3 - 8*x^2 + 9*x + 19, xF^2 + (-1)*xF - 1/2*t - 9/2], [8725, x^4 - x^3 - 10*x^2 + 2*x + 19, xF^2 + (-1/2*t - 1/2)*xF - 1/2*t - 9/2], [9225, x^4 - x^3 - 10*x^2 + 7*x + 19, xF^2 + (-1/2*t + 1/2)*xF - 1/2*t - 9/2]]
**********************************************************************
File "totallyreal_rel.py", line 661:
    sage: enumerate_totallyreal_fields_rel(F, 3, 17*10^9)
Expected:
    [[16240385609L, x^9 - x^8 - 9*x^7 + 4*x^6 + 26*x^5 - 2*x^4 - 25*x^3 - x^2 + 7*x + 1, xF^3 + (-t^2 - 4*t + 1)*xF^2 + (t^2 + 3*t - 5)*xF + 3*t^2 + 11*t - 5]]
Got:
    [[16240385609, x^9 - x^8 - 9*x^7 + 4*x^6 + 26*x^5 - 2*x^4 - 25*x^3 - x^2 + 7*x + 1, xF^3 + (-t^2 - 4*t + 1)*xF^2 + (t^2 + 3*t - 5)*xF + 3*t^2 + 11*t - 5]]
**********************************************************************
```


Cheers,

Michael



---

archive/issue_comments_006565.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-14T12:06:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1085#issuecomment-6565",
    "user": "craigcitro"
}
```

Attachment



---

archive/issue_comments_006566.json:
```json
{
    "body": "Merged trac-1085-touch-ups.patch in Sage 2.10.2.alpha0",
    "created_at": "2008-02-14T12:53:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1085#issuecomment-6566",
    "user": "mabshoff"
}
```

Merged trac-1085-touch-ups.patch in Sage 2.10.2.alpha0



---

archive/issue_comments_006567.json:
```json
{
    "body": "trac-1085-touch-ups.patch fixes the doctest failure issues on sage.math.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-14T14:58:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1085",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1085#issuecomment-6567",
    "user": "mabshoff"
}
```

trac-1085-touch-ups.patch fixes the doctest failure issues on sage.math.

Cheers,

Michael
