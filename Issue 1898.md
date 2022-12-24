# Issue 1898: Sage 2.10: numerical doctest failure for polynomial_element.pyx on Linux/Itanium

archive/issues_001898.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nsage -t  devel/sage-main/sage/rings/polynomial/\npolynomial_element.pyx**********************************************************************\nFile \"polynomial_element.pyx\", line 2669:\n    sage: p.roots(ring=CIF)\nExpected:\n    [([-1.4142135623730952 .. -1.4142135623730949], 1),\n([1.4142135623730949 ..\n1.4142135623730952], 1), ([-1.2146389322441827 .. -1.2146389322441821]\n- [0.1414250525823937... .. 0.1414250525823939...]*I, 2),\n([-0.141425052582393... .. -0.1414250525823937...] +\n[1.2146389322441821 .. 1.2146389322441827]*I, 2),\n([0.141425052582393... .. 0.141425052582393...] -\n[1.2146389322441821 .. 1.2146389322441827]*I, 2),\n([1.2146389322441821 .. 1.2146389322441827] + [0.14142505258239376 ..\n0.14142505258239399]*I, 2)]\nGot:\n    [([-1.4142135623730952 .. -1.4142135623730949], 1),\n([1.4142135623730949 ..\n1.4142135623730952], 1), ([-1.2146389322441827 .. -1.2146389322441821]\n- [0.14142505258239371 .. 0.14142505258239397]*I, 2),\n([-0.14142505258239397 .. -0.14142505258239376] +\n[1.2146389322441821 .. 1.2146389322441829]*I, 2),\n([0.14142505258239373 .. 0.14142505258239394] - [1.2146389322441821 ..\n1.2146389322441829]*I, 2), ([1.2146389322441821 .. 1.2146389322441827]\n+ [0.14142505258239376 .. 0.14142505258239399]*I, 2)]\n**********************************************************************\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1898\n\n",
    "created_at": "2008-01-23T21:15:57Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "Sage 2.10: numerical doctest failure for polynomial_element.pyx on Linux/Itanium",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1898",
    "user": "mabshoff"
}
```
Assignee: mabshoff


```
sage -t  devel/sage-main/sage/rings/polynomial/
polynomial_element.pyx**********************************************************************
File "polynomial_element.pyx", line 2669:
    sage: p.roots(ring=CIF)
Expected:
    [([-1.4142135623730952 .. -1.4142135623730949], 1),
([1.4142135623730949 ..
1.4142135623730952], 1), ([-1.2146389322441827 .. -1.2146389322441821]
- [0.1414250525823937... .. 0.1414250525823939...]*I, 2),
([-0.141425052582393... .. -0.1414250525823937...] +
[1.2146389322441821 .. 1.2146389322441827]*I, 2),
([0.141425052582393... .. 0.141425052582393...] -
[1.2146389322441821 .. 1.2146389322441827]*I, 2),
([1.2146389322441821 .. 1.2146389322441827] + [0.14142505258239376 ..
0.14142505258239399]*I, 2)]
Got:
    [([-1.4142135623730952 .. -1.4142135623730949], 1),
([1.4142135623730949 ..
1.4142135623730952], 1), ([-1.2146389322441827 .. -1.2146389322441821]
- [0.14142505258239371 .. 0.14142505258239397]*I, 2),
([-0.14142505258239397 .. -0.14142505258239376] +
[1.2146389322441821 .. 1.2146389322441829]*I, 2),
([0.14142505258239373 .. 0.14142505258239394] - [1.2146389322441821 ..
1.2146389322441829]*I, 2), ([1.2146389322441821 .. 1.2146389322441827]
+ [0.14142505258239376 .. 0.14142505258239399]*I, 2)]
**********************************************************************
```


Issue created by migration from https://trac.sagemath.org/ticket/1898





---

archive/issue_comments_012012.json:
```json
{
    "body": "Attachment [Sage-2.10.1.alpha2-fix-numerical-doctests-failure-trac_1898.patch](tarball://root/attachments/some-uuid/ticket1898/Sage-2.10.1.alpha2-fix-numerical-doctests-failure-trac_1898.patch) by mabshoff created at 2008-01-24 00:29:37",
    "created_at": "2008-01-24T00:29:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1898#issuecomment-12012",
    "user": "mabshoff"
}
```

Attachment [Sage-2.10.1.alpha2-fix-numerical-doctests-failure-trac_1898.patch](tarball://root/attachments/some-uuid/ticket1898/Sage-2.10.1.alpha2-fix-numerical-doctests-failure-trac_1898.patch) by mabshoff created at 2008-01-24 00:29:37



---

archive/issue_comments_012013.json:
```json
{
    "body": "Attachment [trac-1898-part2-fix_for_lower_order_doctest_bits.patch](tarball://root/attachments/some-uuid/ticket1898/trac-1898-part2-fix_for_lower_order_doctest_bits.patch) by was created at 2008-01-24 19:48:53\n\napply the other patch then this one.",
    "created_at": "2008-01-24T19:48:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1898#issuecomment-12013",
    "user": "was"
}
```

Attachment [trac-1898-part2-fix_for_lower_order_doctest_bits.patch](tarball://root/attachments/some-uuid/ticket1898/trac-1898-part2-fix_for_lower_order_doctest_bits.patch) by was created at 2008-01-24 19:48:53

apply the other patch then this one.



---

archive/issue_comments_012014.json:
```json
{
    "body": "Kate confirmed in https://groups.google.com/group/sage-support/t/d489d89ec68b6706 that William's patch now fixes it.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-24T20:48:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1898#issuecomment-12014",
    "user": "mabshoff"
}
```

Kate confirmed in https://groups.google.com/group/sage-support/t/d489d89ec68b6706 that William's patch now fixes it.

Cheers,

Michael



---

archive/issue_comments_012015.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-24T20:48:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1898#issuecomment-12015",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012016.json:
```json
{
    "body": "Merged in Sage 2.10.1.alpha2",
    "created_at": "2008-01-24T20:48:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1898",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1898#issuecomment-12016",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.1.alpha2
