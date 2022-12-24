# Issue 133: Galois action

archive/issues_000133.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: Galois group, algebric number theory\n\nIt would be great if something like the following worked:\n\n\n```\nsage: F = CyclotomicField(7)\n\nsage: z = F.gen()\n\nsage: G = F.galois_group()\n\nsage: phi = G.random()\n\nsage: z.galois_action(phi)\n```\n\n\nAlso needed, I think, are embedding into CC.\nAFAIK, neither of these has been entered onto the SAGE\n\"wish list\".\n\nIssue created by migration from https://trac.sagemath.org/ticket/133\n\n",
    "created_at": "2006-10-15T16:47:17Z",
    "labels": [
        "number theory",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "Galois action",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/133",
    "user": "@wdjoyner"
}
```
Assignee: @williamstein

Keywords: Galois group, algebric number theory

It would be great if something like the following worked:


```
sage: F = CyclotomicField(7)

sage: z = F.gen()

sage: G = F.galois_group()

sage: phi = G.random()

sage: z.galois_action(phi)
```


Also needed, I think, are embedding into CC.
AFAIK, neither of these has been entered onto the SAGE
"wish list".

Issue created by migration from https://trac.sagemath.org/ticket/133





---

archive/issue_comments_000627.json:
```json
{
    "body": "Complex embeddings were written long ago.  In your example above, try:\n\n```\n    F.complex_embeddings()\n```\n",
    "created_at": "2006-10-15T17:42:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/133#issuecomment-627",
    "user": "@williamstein"
}
```

Complex embeddings were written long ago.  In your example above, try:

```
    F.complex_embeddings()
```




---

archive/issue_comments_000628.json:
```json
{
    "body": "This is quite usable:\n\n```\nsage: F = CyclotomicField(7)\nsage: z = F.gen()           \nsage: G = F.embeddings(F)   \nsage: G                     \n\n[\nRing endomorphism of Cyclotomic Field of order 7 and degree 6\n  Defn: zeta7 |--> zeta7,\nRing endomorphism of Cyclotomic Field of order 7 and degree 6\n  Defn: zeta7 |--> zeta7^2,\nRing endomorphism of Cyclotomic Field of order 7 and degree 6\n  Defn: zeta7 |--> zeta7^3,\nRing endomorphism of Cyclotomic Field of order 7 and degree 6\n  Defn: zeta7 |--> zeta7^4,\nRing endomorphism of Cyclotomic Field of order 7 and degree 6\n  Defn: zeta7 |--> zeta7^5,\nRing endomorphism of Cyclotomic Field of order 7 and degree 6\n  Defn: zeta7 |--> -zeta7^5 - zeta7^4 - zeta7^3 - zeta7^2 - zeta7 - 1\n]\nsage: [g(z) for g in G]     \n\n[zeta7,\n zeta7^2,\n zeta7^3,\n zeta7^4,\n zeta7^5,\n -zeta7^5 - zeta7^4 - zeta7^3 - zeta7^2 - zeta7 - 1]\n```\n\n\nOne could easily implement F.autumorphisms() to return F.embeddings(F), but in fact there is already End(F) -- whose existence I discovered by doing F.galois_group?\n\nSo what should be done is to change the structure returned by F.galois_group() which is <class 'sage.rings.number_field.galois_group.GaloisGroup'> to be derived from that of End(F) which is <class 'sage.rings.number_field.morphism.NumberFieldHomset'>,  which does not look very difficult to me...",
    "created_at": "2008-09-04T16:13:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/133#issuecomment-628",
    "user": "@JohnCremona"
}
```

This is quite usable:

```
sage: F = CyclotomicField(7)
sage: z = F.gen()           
sage: G = F.embeddings(F)   
sage: G                     

[
Ring endomorphism of Cyclotomic Field of order 7 and degree 6
  Defn: zeta7 |--> zeta7,
Ring endomorphism of Cyclotomic Field of order 7 and degree 6
  Defn: zeta7 |--> zeta7^2,
Ring endomorphism of Cyclotomic Field of order 7 and degree 6
  Defn: zeta7 |--> zeta7^3,
Ring endomorphism of Cyclotomic Field of order 7 and degree 6
  Defn: zeta7 |--> zeta7^4,
Ring endomorphism of Cyclotomic Field of order 7 and degree 6
  Defn: zeta7 |--> zeta7^5,
Ring endomorphism of Cyclotomic Field of order 7 and degree 6
  Defn: zeta7 |--> -zeta7^5 - zeta7^4 - zeta7^3 - zeta7^2 - zeta7 - 1
]
sage: [g(z) for g in G]     

[zeta7,
 zeta7^2,
 zeta7^3,
 zeta7^4,
 zeta7^5,
 -zeta7^5 - zeta7^4 - zeta7^3 - zeta7^2 - zeta7 - 1]
```


One could easily implement F.autumorphisms() to return F.embeddings(F), but in fact there is already End(F) -- whose existence I discovered by doing F.galois_group?

So what should be done is to change the structure returned by F.galois_group() which is <class 'sage.rings.number_field.galois_group.GaloisGroup'> to be derived from that of End(F) which is <class 'sage.rings.number_field.morphism.NumberFieldHomset'>,  which does not look very difficult to me...



---

archive/issue_comments_000629.json:
```json
{
    "body": "This one was almost fixed by #5159; but unfortunately the above snippet didn't quite work, because my new GaloisGroup class derived from PermutationGroup_generic, and the random_element method of that class always returned a PermutationGroupElement (rather than a GaloisGroupElement, which has more functionality).\n\nThe above patch makes the necessary tiny changes to the permutation groups code so this now works, although the interface is slightly different from the above:\n\n```\nsage: F.<z> = CyclotomicField(7)\nsage: G = F.galois_group()\nsage: phi = G.random_element()\nsage: phi(z)\nz^4\n```\n",
    "created_at": "2009-05-25T13:39:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/133#issuecomment-629",
    "user": "@loefflerd"
}
```

This one was almost fixed by #5159; but unfortunately the above snippet didn't quite work, because my new GaloisGroup class derived from PermutationGroup_generic, and the random_element method of that class always returned a PermutationGroupElement (rather than a GaloisGroupElement, which has more functionality).

The above patch makes the necessary tiny changes to the permutation groups code so this now works, although the interface is slightly different from the above:

```
sage: F.<z> = CyclotomicField(7)
sage: G = F.galois_group()
sage: phi = G.random_element()
sage: phi(z)
z^4
```




---

archive/issue_comments_000630.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-25T13:39:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/133#issuecomment-630",
    "user": "@loefflerd"
}
```

Changing status from new to assigned.



---

archive/issue_comments_000631.json:
```json
{
    "body": "Changing assignee from @williamstein to @loefflerd.",
    "created_at": "2009-05-25T13:39:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/133#issuecomment-631",
    "user": "@loefflerd"
}
```

Changing assignee from @williamstein to @loefflerd.



---

archive/issue_comments_000632.json:
```json
{
    "body": "patch against 4.0.rc1",
    "created_at": "2009-05-28T15:42:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/133#issuecomment-632",
    "user": "@loefflerd"
}
```

patch against 4.0.rc1



---

archive/issue_comments_000633.json:
```json
{
    "body": "Attachment [trac_133.patch](tarball://root/attachments/some-uuid/ticket133/trac_133.patch) by @loefflerd created at 2009-05-28 15:42:41\n\nThe previous patch broke a doctest due to silly sorting issues; here's a better patch.",
    "created_at": "2009-05-28T15:42:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/133#issuecomment-633",
    "user": "@loefflerd"
}
```

Attachment [trac_133.patch](tarball://root/attachments/some-uuid/ticket133/trac_133.patch) by @loefflerd created at 2009-05-28 15:42:41

The previous patch broke a doctest due to silly sorting issues; here's a better patch.



---

archive/issue_comments_000634.json:
```json
{
    "body": "Changing keywords from \"Galois group, algebric number theory\" to \"Galois group, algebraic number theory\".",
    "created_at": "2009-05-30T09:07:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/133#issuecomment-634",
    "user": "@aghitza"
}
```

Changing keywords from "Galois group, algebric number theory" to "Galois group, algebraic number theory".



---

archive/issue_comments_000635.json:
```json
{
    "body": "Very good!",
    "created_at": "2009-05-30T09:15:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/133#issuecomment-635",
    "user": "@aghitza"
}
```

Very good!



---

archive/issue_comments_000636.json:
```json
{
    "body": "Merged in 4.0.1.alpha0.",
    "created_at": "2009-06-01T04:43:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/133#issuecomment-636",
    "user": "@mwhansen"
}
```

Merged in 4.0.1.alpha0.



---

archive/issue_comments_000637.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-01T04:43:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/133#issuecomment-637",
    "user": "@mwhansen"
}
```

Resolution: fixed



---

archive/issue_comments_000638.json:
```json
{
    "body": "Lowest ticket award!",
    "created_at": "2009-06-01T04:53:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/133",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/133#issuecomment-638",
    "user": "@williamstein"
}
```

Lowest ticket award!
