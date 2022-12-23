# Issue 1948: K.factor_integer needs a name change, since now it does much more

archive/issues_001948.json:
```json
{
    "body": "Assignee: was\n\nFor K a number field, K.factor_integer slices, dices, and also factors rationals, elements of the number field, etc.:\n\n\n```\nsage: K.<a> = NumberField(x^2 + 1)\nsage: K.factor_integer(1/3)\nFractional ideal (3)^-1\nsage: K.factor_integer(1+a)\nFractional ideal (a + 1)\nsage: K.factor_integer(1+a/5)\n(Fractional ideal (-3*a - 2)) * (Fractional ideal (a + 1)) * (Fractional ideal (-a - 2))^-1 * (Fractional ideal (2*a + 1))^-1\nsage: \n```\n\n\nSo it needs to be named something else.  Suggestions welcome.  \n\nIssue created by migration from https://trac.sagemath.org/ticket/1948\n\n",
    "created_at": "2008-01-27T15:33:16Z",
    "labels": [
        "number theory",
        "major",
        "bug"
    ],
    "title": "K.factor_integer needs a name change, since now it does much more",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1948",
    "user": "was"
}
```
Assignee: was

For K a number field, K.factor_integer slices, dices, and also factors rationals, elements of the number field, etc.:


```
sage: K.<a> = NumberField(x^2 + 1)
sage: K.factor_integer(1/3)
Fractional ideal (3)^-1
sage: K.factor_integer(1+a)
Fractional ideal (a + 1)
sage: K.factor_integer(1+a/5)
(Fractional ideal (-3*a - 2)) * (Fractional ideal (a + 1)) * (Fractional ideal (-a - 2))^-1 * (Fractional ideal (2*a + 1))^-1
sage: 
```


So it needs to be named something else.  Suggestions welcome.  

Issue created by migration from https://trac.sagemath.org/ticket/1948





---

archive/issue_comments_012388.json:
```json
{
    "body": "How about just calling it K.factor()?",
    "created_at": "2008-02-17T02:18:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1948#issuecomment-12388",
    "user": "AlexGhitza"
}
```

How about just calling it K.factor()?



---

archive/issue_comments_012389.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-05T14:26:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1948#issuecomment-12389",
    "user": "cremona"
}
```

Attachment



---

archive/issue_comments_012390.json:
```json
{
    "body": "The patch (based on 3.0.alpha0) follows Alex's suggestion.  It is a simple text replacement of all factor_integer -> factor in the source code.\n\nI wondered about keeping factor_integer as an alias but decided against.",
    "created_at": "2008-04-05T14:28:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1948#issuecomment-12390",
    "user": "cremona"
}
```

The patch (based on 3.0.alpha0) follows Alex's suggestion.  It is a simple text replacement of all factor_integer -> factor in the source code.

I wondered about keeping factor_integer as an alias but decided against.



---

archive/issue_comments_012391.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-04-13T00:51:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1948#issuecomment-12391",
    "user": "AlexGhitza"
}
```

Looks good to me.



---

archive/issue_comments_012392.json:
```json
{
    "body": "Attachment\n\napply after trac1948.patch",
    "created_at": "2008-04-13T00:59:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1948#issuecomment-12392",
    "user": "AlexGhitza"
}
```

Attachment

apply after trac1948.patch



---

archive/issue_comments_012393.json:
```json
{
    "body": "I just realized that it is a good idea to document the fact that factor() does more than factor integral elements, so I added a small patch that puts in William's examples as doctests.",
    "created_at": "2008-04-13T01:00:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1948#issuecomment-12393",
    "user": "AlexGhitza"
}
```

I just realized that it is a good idea to document the fact that factor() does more than factor integral elements, so I added a small patch that puts in William's examples as doctests.



---

archive/issue_comments_012394.json:
```json
{
    "body": "Merged both patches in Sage 3.0.alpha4",
    "created_at": "2008-04-13T02:20:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1948#issuecomment-12394",
    "user": "mabshoff"
}
```

Merged both patches in Sage 3.0.alpha4



---

archive/issue_comments_012395.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-13T02:20:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1948#issuecomment-12395",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012396.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-13T14:45:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1948#issuecomment-12396",
    "user": "AlexGhitza"
}
```

Attachment



---

archive/issue_comments_012397.json:
```json
{
    "body": "While working on something else, I realized that there are a few instances of factor_integer in ell_finite_field.py, which is now broken.  See the attached (trivial) patch.\n\nBTW, I checked and there are no other instances of factor_integer anywhere else in the Sage code (yes, I should have done that before...)",
    "created_at": "2008-04-13T14:47:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1948#issuecomment-12397",
    "user": "AlexGhitza"
}
```

While working on something else, I realized that there are a few instances of factor_integer in ell_finite_field.py, which is now broken.  See the attached (trivial) patch.

BTW, I checked and there are no other instances of factor_integer anywhere else in the Sage code (yes, I should have done that before...)



---

archive/issue_comments_012398.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-04-13T14:47:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1948#issuecomment-12398",
    "user": "AlexGhitza"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_012399.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-04-13T14:47:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1948#issuecomment-12399",
    "user": "AlexGhitza"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_012400.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-13T15:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1948#issuecomment-12400",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_012401.json:
```json
{
    "body": "Replying to [comment:7 AlexGhitza]:\n> While working on something else, I realized that there are a few instances of factor_integer in ell_finite_field.py, which is now broken.  See the attached (trivial) patch.\n> \n> BTW, I checked and there are no other instances of factor_integer anywhere else in the Sage code (yes, I should have done that before...)\n> \n\nHi Alex,\n\nthose factor_integer instances do no longer exist in alpha4 [I assume John has rewritten that code in some other patch]:\n\n```\nsage-3.0.alpha4/devel/sage$ grep -r factor_integer *\nsage-3.0.alpha4/devel/sage$     \n```\n\nI did run `-t -long` on the tree after applying the inital two patches. So I am closing this again.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-13T15:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1948#issuecomment-12401",
    "user": "mabshoff"
}
```

Replying to [comment:7 AlexGhitza]:
> While working on something else, I realized that there are a few instances of factor_integer in ell_finite_field.py, which is now broken.  See the attached (trivial) patch.
> 
> BTW, I checked and there are no other instances of factor_integer anywhere else in the Sage code (yes, I should have done that before...)
> 

Hi Alex,

those factor_integer instances do no longer exist in alpha4 [I assume John has rewritten that code in some other patch]:

```
sage-3.0.alpha4/devel/sage$ grep -r factor_integer *
sage-3.0.alpha4/devel/sage$     
```

I did run `-t -long` on the tree after applying the inital two patches. So I am closing this again.

Cheers,

Michael



---

archive/issue_comments_012402.json:
```json
{
    "body": "Ahh, the irony: The problem is introduced by the two patches at #2880. I get doctest failures related to factor_interger and after applying the latest patch they get fixed.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-13T15:56:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1948#issuecomment-12402",
    "user": "mabshoff"
}
```

Ahh, the irony: The problem is introduced by the two patches at #2880. I get doctest failures related to factor_interger and after applying the latest patch they get fixed.

Cheers,

Michael



---

archive/issue_comments_012403.json:
```json
{
    "body": "That makes sense, because I ran into this while reviewing #2880.\n\nAll is well that ends well.",
    "created_at": "2008-04-13T15:57:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1948#issuecomment-12403",
    "user": "AlexGhitza"
}
```

That makes sense, because I ran into this while reviewing #2880.

All is well that ends well.



---

archive/issue_comments_012404.json:
```json
{
    "body": "Merged trac1948-ell_finite_field.patch in Sage 3.0.alpha5 after merging #2880.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-13T16:03:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1948",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1948#issuecomment-12404",
    "user": "mabshoff"
}
```

Merged trac1948-ell_finite_field.patch in Sage 3.0.alpha5 after merging #2880.

Cheers,

Michael
