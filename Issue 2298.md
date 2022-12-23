# Issue 2298: [with patch, needs review] implement a way to compute a number field containing given algebraic numbers

archive/issues_002298.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  jason ncalexan\n\nThe attached patch implements a way to compute a number field containing given algebraic numbers:\n\n```\nsage: nf_elements_from_algebraics([AA(sqrt(2)), AA(sqrt(3))])\n\n(Number Field in a with defining polynomial y^4 - 4*y^2 + 1,\n [-a^3 + 3*a, -a^2 + 2],\n Ring morphism:\n  From: Number Field in a with defining polynomial y^4 - 4*y^2 + 1\n  To:   Algebraic Real Field\n  Defn: a |--> [0.51763809020504147 .. 0.51763809020504159])\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2298\n\n",
    "created_at": "2008-02-25T03:07:21Z",
    "labels": [
        "misc",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] implement a way to compute a number field containing given algebraic numbers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2298",
    "user": "cwitty"
}
```
Assignee: cwitty

CC:  jason ncalexan

The attached patch implements a way to compute a number field containing given algebraic numbers:

```
sage: nf_elements_from_algebraics([AA(sqrt(2)), AA(sqrt(3))])

(Number Field in a with defining polynomial y^4 - 4*y^2 + 1,
 [-a^3 + 3*a, -a^2 + 2],
 Ring morphism:
  From: Number Field in a with defining polynomial y^4 - 4*y^2 + 1
  To:   Algebraic Real Field
  Defn: a |--> [0.51763809020504147 .. 0.51763809020504159])
```


Issue created by migration from https://trac.sagemath.org/ticket/2298





---

archive/issue_comments_015237.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-25T16:18:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2298#issuecomment-15237",
    "user": "jason"
}
```

Attachment



---

archive/issue_comments_015238.json:
```json
{
    "body": "I get the following doctest failure:\n\n```\nExpected:\n    (Number Field in a with defining polynomial y^4 + 2*y^2 + 4, [1/2*a^3], Ring morphism:\n      From: Number Field in a with defining polynomial y^4 + 2*y^2 + 4\n      To:   Algebraic Field\n      Defn: a |--> [-0.70710678118654758 .. -0.70710678118654746] + [1.2247448713915889 .. 1.2247448713915892]*I)\nGot:\n    (Number Field in a with defining polynomial y^4 + 2*y^2 + 4, [1/2*a^3], Ring morphism:\n      From: Number Field in a with defining polynomial y^4 + 2*y^2 + 4\n      To:   Algebraic Field\n      Defn: a |--> [-0.70710678118654758 .. -0.70710678118654746] - [1.2247448713915889 .. 1.2247448713915892]*I)\n```\n",
    "created_at": "2008-02-27T19:38:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2298#issuecomment-15238",
    "user": "mhansen"
}
```

I get the following doctest failure:

```
Expected:
    (Number Field in a with defining polynomial y^4 + 2*y^2 + 4, [1/2*a^3], Ring morphism:
      From: Number Field in a with defining polynomial y^4 + 2*y^2 + 4
      To:   Algebraic Field
      Defn: a |--> [-0.70710678118654758 .. -0.70710678118654746] + [1.2247448713915889 .. 1.2247448713915892]*I)
Got:
    (Number Field in a with defining polynomial y^4 + 2*y^2 + 4, [1/2*a^3], Ring morphism:
      From: Number Field in a with defining polynomial y^4 + 2*y^2 + 4
      To:   Algebraic Field
      Defn: a |--> [-0.70710678118654758 .. -0.70710678118654746] - [1.2247448713915889 .. 1.2247448713915892]*I)
```




---

archive/issue_comments_015239.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-27T23:28:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2298#issuecomment-15239",
    "user": "cwitty"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015240.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-02-28T03:51:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2298#issuecomment-15240",
    "user": "cwitty"
}
```

Attachment



---

archive/issue_comments_015241.json:
```json
{
    "body": "Evidently one of the Pari functions I call gives different results on 32-bit vs. 64-bit, so I've added \"# 32-bit\" and \"# 64-bit\" on the relevant doctest (and tested the result on 32-bit x86 and 64-bit x86).",
    "created_at": "2008-02-28T03:54:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2298#issuecomment-15241",
    "user": "cwitty"
}
```

Evidently one of the Pari functions I call gives different results on 32-bit vs. 64-bit, so I've added "# 32-bit" and "# 64-bit" on the relevant doctest (and tested the result on 32-bit x86 and 64-bit x86).



---

archive/issue_comments_015242.json:
```json
{
    "body": "This patch is excellent.  Great doctests, valuable functionality -- I needed this in my research today :)  Apply, post haste!\n\nThe only issue I raise is the name -- I'd really like number_field to appear, not just nf.  And the fact that it's toplevel means it will be easy to miss -- could there be another patch defining an alias, and making it so that QQbar(sqrt(2)).number_field_containing() calls this automagically?  I'm more likely to find this valuable functionality that way.",
    "created_at": "2008-03-01T23:27:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2298#issuecomment-15242",
    "user": "ncalexan"
}
```

This patch is excellent.  Great doctests, valuable functionality -- I needed this in my research today :)  Apply, post haste!

The only issue I raise is the name -- I'd really like number_field to appear, not just nf.  And the fact that it's toplevel means it will be easy to miss -- could there be another patch defining an alias, and making it so that QQbar(sqrt(2)).number_field_containing() calls this automagically?  I'm more likely to find this valuable functionality that way.



---

archive/issue_comments_015243.json:
```json
{
    "body": "It would be nice if\n\n```\nnf_elements_from_algebraics([sqrt(2), sqrt(3 + sqrt(2))*I, sqrt(3 - sqrt(2))*I])\n```\n\njust worked, too -- coerced to QQbar for you.",
    "created_at": "2008-03-02T00:57:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2298#issuecomment-15243",
    "user": "ncalexan"
}
```

It would be nice if

```
nf_elements_from_algebraics([sqrt(2), sqrt(3 + sqrt(2))*I, sqrt(3 - sqrt(2))*I])
```

just worked, too -- coerced to QQbar for you.



---

archive/issue_comments_015244.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-03-02T19:18:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2298#issuecomment-15244",
    "user": "cwitty"
}
```

Attachment



---

archive/issue_comments_015245.json:
```json
{
    "body": "I've created a new patch in response to Nick's comments above: nf-from-algebraic-response.patch (to be applied after nf-from-algebraic-v2.patch).  Note that nf-from-algebraic-v2.patch has already been positively reviewed by Nick; only the -response.patch needs to be reviewed.\n\nI mostly did what Nick asked, with two exceptions: 1) I don't like aliases; since there are no backward-compatibility issues, I just renamed the function to the more-descriptive name, instead of having an alias. 2) I named the method version \"as_number_field_element\", instead of \"number_field_containing\".\n\nI did test that doctests pass in qqbar.py on both 32-bit and 64-bit x86 linux after this patch.",
    "created_at": "2008-03-02T19:23:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2298#issuecomment-15245",
    "user": "cwitty"
}
```

I've created a new patch in response to Nick's comments above: nf-from-algebraic-response.patch (to be applied after nf-from-algebraic-v2.patch).  Note that nf-from-algebraic-v2.patch has already been positively reviewed by Nick; only the -response.patch needs to be reviewed.

I mostly did what Nick asked, with two exceptions: 1) I don't like aliases; since there are no backward-compatibility issues, I just renamed the function to the more-descriptive name, instead of having an alias. 2) I named the method version "as_number_field_element", instead of "number_field_containing".

I did test that doctests pass in qqbar.py on both 32-bit and 64-bit x86 linux after this patch.



---

archive/issue_comments_015246.json:
```json
{
    "body": "Response patch is fantastic.  This is so useful for my research, please apply!",
    "created_at": "2008-03-02T19:54:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2298#issuecomment-15246",
    "user": "ncalexan"
}
```

Response patch is fantastic.  This is so useful for my research, please apply!



---

archive/issue_comments_015247.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-02T20:47:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2298#issuecomment-15247",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015248.json:
```json
{
    "body": "Merged nf-from-algebraic-v2.patch and nf-from-algebraic-response.patch  in Sage 2.10.3.rc1",
    "created_at": "2008-03-02T20:47:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2298#issuecomment-15248",
    "user": "mabshoff"
}
```

Merged nf-from-algebraic-v2.patch and nf-from-algebraic-response.patch  in Sage 2.10.3.rc1
