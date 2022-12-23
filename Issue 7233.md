# Issue 7233: [with patch, positive review] adapted SymmetricGroupAlgebra to the category framework

archive/issues_007233.json:
```json
{
    "body": "Assignee: nthiery\n\nCC:  combinat\n\nKeywords: Symmetric Group Algebra, Categories\n\nThe goal of the patch is to adapt SymmetricGroupAlgebra to categories and to add some improvements. The patch improve SymmetricGroupAlgebra in two ways:\n \n- SymmetricGroupAlgebra is now in the category FiniteDimensionalAlgebraWithBasis. Note: A forthcomming patch from Valentin Feray will put it in the correct GroupAlgebras category;\n\n- When creating SGA(n) a coercion from SGA(n-1) is declared.\n\nI'm submitting the patch on behalf on Nicolas after reviewing it.\n\nDepends on the categories framework #5891.\n\nCheers,\n\nFlorent\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7233\n\n",
    "created_at": "2009-10-16T11:03:04Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "title": "[with patch, positive review] adapted SymmetricGroupAlgebra to the category framework",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7233",
    "user": "hivert"
}
```
Assignee: nthiery

CC:  combinat

Keywords: Symmetric Group Algebra, Categories

The goal of the patch is to adapt SymmetricGroupAlgebra to categories and to add some improvements. The patch improve SymmetricGroupAlgebra in two ways:
 
- SymmetricGroupAlgebra is now in the category FiniteDimensionalAlgebraWithBasis. Note: A forthcomming patch from Valentin Feray will put it in the correct GroupAlgebras category;

- When creating SGA(n) a coercion from SGA(n-1) is declared.

I'm submitting the patch on behalf on Nicolas after reviewing it.

Depends on the categories framework #5891.

Cheers,

Florent


Issue created by migration from https://trac.sagemath.org/ticket/7233





---

archive/issue_comments_060001.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-10-16T11:04:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7233#issuecomment-60001",
    "user": "hivert"
}
```

Attachment



---

archive/issue_comments_060002.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2009-10-16T11:12:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7233#issuecomment-60002",
    "user": "hivert"
}
```

Resolution: duplicate



---

archive/issue_comments_060003.json:
```json
{
    "body": "Oops !!! This is a duplicate of 6138... I should have gessed it from the name of the patch. Sorry for the mess,\n\nFlorent",
    "created_at": "2009-10-16T11:12:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7233",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7233#issuecomment-60003",
    "user": "hivert"
}
```

Oops !!! This is a duplicate of 6138... I should have gessed it from the name of the patch. Sorry for the mess,

Florent
