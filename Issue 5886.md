# Issue 5886: Bug in free module homomorphism creation

archive/issues_005886.json:
```json
{
    "body": "Assignee: was\n\nConsider the following\n\n```\nsage: V = (QQ^3).span_of_basis([[1,1,0],[1,0,2]]); V\nVector space of degree 3 and dimension 2 over Rational Field\nUser basis matrix:\n[1 1 0]\n[1 0 2]\nsage: V.hom([V.0, V.1])\nTraceback (most recent call last):\n...\nTypeError: entries has the wrong length\n```\n\n\nThe hom command above *should* create the identity morphism, since according to the docs hom takes as input a list of the images of the generators.    Instead, what is happening is that the list is being turned into a matrix directly.  Conclusion, the above just goes boom, since the matrix would have to be 2x2, as V has rank 2.   E.g., this works:\n\n```\nsage: V.hom([[1,2],[3,4]], V)\nFree module morphism defined by the matrix\n[1 2]\n[3 4]\nDomain: Vector space of degree 3 and dimension 2 over Rational Field\nUser ...\nCodomain: Vector space of degree 3 and dimension 2 over Rational Field\nUser ...\n```\n\n\nThe really *scary* thing is that this broken code will accidentally and *silently* give totally wrong answers in some cases, e.g.,\n\n```\nsage: V = (QQ^2).span_of_basis([[1,2],[3,4]])\nsage: I = V.hom([V.0,V.1]); I\nFree module morphism defined by the matrix\n[1 2]\n[3 4]\nDomain: Vector space of degree 2 and dimension 2 over Rational Field\nUser ...\nCodomain: Vector space of degree 2 and dimension 2 over Rational Field\nUser ...\nsage: I(V.0)\n(7, 10)\nsage: V.0\n(1, 2)\n```\n\n\nNotice above that I *should* be the identity map, but it's most certainly not -- it's the map defined by the matrix [[1,2],[3,4]].  \n\nIssue created by migration from https://trac.sagemath.org/ticket/5886\n\n",
    "created_at": "2009-04-24T03:40:43Z",
    "labels": [
        "linear algebra",
        "critical",
        "bug"
    ],
    "title": "Bug in free module homomorphism creation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5886",
    "user": "was"
}
```
Assignee: was

Consider the following

```
sage: V = (QQ^3).span_of_basis([[1,1,0],[1,0,2]]); V
Vector space of degree 3 and dimension 2 over Rational Field
User basis matrix:
[1 1 0]
[1 0 2]
sage: V.hom([V.0, V.1])
Traceback (most recent call last):
...
TypeError: entries has the wrong length
```


The hom command above *should* create the identity morphism, since according to the docs hom takes as input a list of the images of the generators.    Instead, what is happening is that the list is being turned into a matrix directly.  Conclusion, the above just goes boom, since the matrix would have to be 2x2, as V has rank 2.   E.g., this works:

```
sage: V.hom([[1,2],[3,4]], V)
Free module morphism defined by the matrix
[1 2]
[3 4]
Domain: Vector space of degree 3 and dimension 2 over Rational Field
User ...
Codomain: Vector space of degree 3 and dimension 2 over Rational Field
User ...
```


The really *scary* thing is that this broken code will accidentally and *silently* give totally wrong answers in some cases, e.g.,

```
sage: V = (QQ^2).span_of_basis([[1,2],[3,4]])
sage: I = V.hom([V.0,V.1]); I
Free module morphism defined by the matrix
[1 2]
[3 4]
Domain: Vector space of degree 2 and dimension 2 over Rational Field
User ...
Codomain: Vector space of degree 2 and dimension 2 over Rational Field
User ...
sage: I(V.0)
(7, 10)
sage: V.0
(1, 2)
```


Notice above that I *should* be the identity map, but it's most certainly not -- it's the map defined by the matrix [[1,2],[3,4]].  

Issue created by migration from https://trac.sagemath.org/ticket/5886





---

archive/issue_comments_046539.json:
```json
{
    "body": "Attachment\n\nIt looks good. I'm having trouble running any doctests (applied to a pre-3.4.1 branch after upgrading) but the examples I tried manually work.",
    "created_at": "2009-04-24T04:42:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5886#issuecomment-46539",
    "user": "robertwb"
}
```

Attachment

It looks good. I'm having trouble running any doctests (applied to a pre-3.4.1 branch after upgrading) but the examples I tried manually work.



---

archive/issue_comments_046540.json:
```json
{
    "body": "No doctests break :-)\n\nSeriously, I did apply this patch to a clean 3.4.1 build on sage.math, run --long doctests, and got no failures.",
    "created_at": "2009-04-24T04:53:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5886#issuecomment-46540",
    "user": "was"
}
```

No doctests break :-)

Seriously, I did apply this patch to a clean 3.4.1 build on sage.math, run --long doctests, and got no failures.



---

archive/issue_comments_046541.json:
```json
{
    "body": "Good.",
    "created_at": "2009-04-24T04:59:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5886#issuecomment-46541",
    "user": "robertwb"
}
```

Good.



---

archive/issue_comments_046542.json:
```json
{
    "body": "I can confirm William's observation: no doctest breakage with -long in my 3.4.2.alpha0 merge tree.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T05:03:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5886#issuecomment-46542",
    "user": "mabshoff"
}
```

I can confirm William's observation: no doctest breakage with -long in my 3.4.2.alpha0 merge tree.

Cheers,

Michael



---

archive/issue_comments_046543.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-24T05:03:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5886#issuecomment-46543",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_046544.json:
```json
{
    "body": "Merged in Sage 3.4.2.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T05:03:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5886",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5886#issuecomment-46544",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.2.alpha0.

Cheers,

Michael
