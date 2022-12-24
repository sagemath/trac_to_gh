# Issue 214: bug in small finite field error checking and modulus type

archive/issues_000214.json:
```json
{
    "body": "Assignee: somebody\n\n\n```\nIt worries me that the outputs live in different rings for different\nclasses, and the latter is not even a field \n \nsage: x = ZZ['x'].0\n \nsage: K.<a> = GF(11**11, name='a', modulus=x^11 - x + 1)\nsage: type(K)\n <class 'sage.rings.finite_field.FiniteField_ext_pari'>\nsage: K.modulus()\n x^11 - x + 1\n \nsage: K.<a> = GF(5**5, name='a', modulus=x^5 - x + 1)\nsage: type(K)\n <type 'sage.rings.finite_field_givaro.FiniteField_givaro'>\nsage: K.modulus()\n a^5\n \nNick\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/214\n\n",
    "created_at": "2007-01-24T20:01:23Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "bug in small finite field error checking and modulus type",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/214",
    "user": "@williamstein"
}
```
Assignee: somebody


```
It worries me that the outputs live in different rings for different
classes, and the latter is not even a field 
 
sage: x = ZZ['x'].0
 
sage: K.<a> = GF(11**11, name='a', modulus=x^11 - x + 1)
sage: type(K)
 <class 'sage.rings.finite_field.FiniteField_ext_pari'>
sage: K.modulus()
 x^11 - x + 1
 
sage: K.<a> = GF(5**5, name='a', modulus=x^5 - x + 1)
sage: type(K)
 <type 'sage.rings.finite_field_givaro.FiniteField_givaro'>
sage: K.modulus()
 a^5
 
Nick
```


Issue created by migration from https://trac.sagemath.org/ticket/214





---

archive/issue_comments_000958.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-01-25T14:35:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/214#issuecomment-958",
    "user": "@williamstein"
}
```

Resolution: fixed



---

archive/issue_comments_000959.json:
```json
{
    "body": "Fixed. for sage-1.9.",
    "created_at": "2007-01-25T14:35:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/214",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/214#issuecomment-959",
    "user": "@williamstein"
}
```

Fixed. for sage-1.9.
