# Issue 2574: problem with Abelian groups and trivial elements

archive/issues_002574.json:
```json
{
    "body": "Assignee: joyner\n\nCC:  ncalexan\n\nKeywords: trivial abelian group class group\n\nThis is a problem:\n\n\n```\nsage: AbelianGroup(1, [1], names='e')\nTrivial Abelian Group\nsage: AbelianGroup(1, [1], names='e').list()\n[]\n```\n\n\nThe handling of 1's in the list of element orders is a problem:\n\n\n```\nsage: AbelianGroup(3, [2, 1, 2], names=list('abc')).list()\n---------------------------------------------------------------------------\n<type 'exceptions.IndexError'>            Traceback (most recent call last)\n\n/Users/ncalexan/Documents/School/MATH235/genus2cm/<ipython console> in <module>()\n\n/Users/ncalexan/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/groups/abelian_gps/abelian_group.py in AbelianGroup(n, invfac, names)\n    304     elif len(invfac) > n:\n    305         raise ValueError, \"invfac (=%s) must have length n (=%s)\"%(invfac, n)\n--> 306     M = AbelianGroup_class(n, invfac, names)\n    307     return M\n    308 \n\n/Users/ncalexan/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/groups/abelian_gps/abelian_group.py in __init__(self, n, invfac, names)\n    371         # *now* define ngens\n    372         self.__ngens = len(self.__invariants)\n--> 373         self._assign_names(names)\n    374 \n    375 \n\n/Users/ncalexan/Documents/School/MATH235/genus2cm/parent_gens.pyx in sage.structure.parent_gens.ParentWithGens._assign_names()\n\n/Users/ncalexan/Documents/School/MATH235/genus2cm/parent_gens.pyx in sage.structure.parent_gens.normalize_names()\n\n<type 'exceptions.IndexError'>: the number of names must equal the number of generators\n```\n\n\nThis is the cause of strange things like:\n\n\n```\nsage: x = ZZ['x'].gen()\nsage: K\nNumber Field in a with defining polynomial x^4 + 4*x^2 + 2\nsage: K = NumberField(x^4 + 4*x^2 + 2, 'a')\nsage: K.class_group()\nClass group of order 1 with structure  of Number Field in a with defining polynomial x^4 + 4*x^2 + 2\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2574\n\n",
    "created_at": "2008-03-17T18:12:45Z",
    "labels": [
        "group theory",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "problem with Abelian groups and trivial elements",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2574",
    "user": "ncalexan"
}
```
Assignee: joyner

CC:  ncalexan

Keywords: trivial abelian group class group

This is a problem:


```
sage: AbelianGroup(1, [1], names='e')
Trivial Abelian Group
sage: AbelianGroup(1, [1], names='e').list()
[]
```


The handling of 1's in the list of element orders is a problem:


```
sage: AbelianGroup(3, [2, 1, 2], names=list('abc')).list()
---------------------------------------------------------------------------
<type 'exceptions.IndexError'>            Traceback (most recent call last)

/Users/ncalexan/Documents/School/MATH235/genus2cm/<ipython console> in <module>()

/Users/ncalexan/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/groups/abelian_gps/abelian_group.py in AbelianGroup(n, invfac, names)
    304     elif len(invfac) > n:
    305         raise ValueError, "invfac (=%s) must have length n (=%s)"%(invfac, n)
--> 306     M = AbelianGroup_class(n, invfac, names)
    307     return M
    308 

/Users/ncalexan/sage-2.10.3.rc3/local/lib/python2.5/site-packages/sage/groups/abelian_gps/abelian_group.py in __init__(self, n, invfac, names)
    371         # *now* define ngens
    372         self.__ngens = len(self.__invariants)
--> 373         self._assign_names(names)
    374 
    375 

/Users/ncalexan/Documents/School/MATH235/genus2cm/parent_gens.pyx in sage.structure.parent_gens.ParentWithGens._assign_names()

/Users/ncalexan/Documents/School/MATH235/genus2cm/parent_gens.pyx in sage.structure.parent_gens.normalize_names()

<type 'exceptions.IndexError'>: the number of names must equal the number of generators
```


This is the cause of strange things like:


```
sage: x = ZZ['x'].gen()
sage: K
Number Field in a with defining polynomial x^4 + 4*x^2 + 2
sage: K = NumberField(x^4 + 4*x^2 + 2, 'a')
sage: K.class_group()
Class group of order 1 with structure  of Number Field in a with defining polynomial x^4 + 4*x^2 + 2
```


Issue created by migration from https://trac.sagemath.org/ticket/2574





---

archive/issue_comments_017583.json:
```json
{
    "body": "And also of \n\n\n```\nsage: x = ZZ['x'].gen()\nsage: K\nNumber Field in a with defining polynomial x^4 + 4*x^2 + 2\nsage: K = NumberField(x^4 + 4*x^2 + 2, 'a')\nsage: K.class_group()\nClass group of order 1 with structure  of Number Field in a with defining polynomial x^4 + 4*x^2 + 2\nsage: K.class_group().gens()\n[]\n```\n",
    "created_at": "2008-03-17T18:19:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2574#issuecomment-17583",
    "user": "ncalexan"
}
```

And also of 


```
sage: x = ZZ['x'].gen()
sage: K
Number Field in a with defining polynomial x^4 + 4*x^2 + 2
sage: K = NumberField(x^4 + 4*x^2 + 2, 'a')
sage: K.class_group()
Class group of order 1 with structure  of Number Field in a with defining polynomial x^4 + 4*x^2 + 2
sage: K.class_group().gens()
[]
```




---

archive/issue_comments_017584.json:
```json
{
    "body": "I don't know about the class_group code, but this patch fixes the other error mentioned:\n\n\n```\nsage: AbelianGroup(1, [1], names='e')\nMultiplicative Abelian Group isomorphic to C1\nsage: AbelianGroup(1, [1], names='e').gens()\n(e,)\nsage: AbelianGroup(1, [1], names='e').list()\n[1]\n```\n",
    "created_at": "2008-03-18T03:19:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2574#issuecomment-17584",
    "user": "wdj"
}
```

I don't know about the class_group code, but this patch fixes the other error mentioned:


```
sage: AbelianGroup(1, [1], names='e')
Multiplicative Abelian Group isomorphic to C1
sage: AbelianGroup(1, [1], names='e').gens()
(e,)
sage: AbelianGroup(1, [1], names='e').list()
[1]
```




---

archive/issue_comments_017585.json:
```json
{
    "body": "abelian group patch",
    "created_at": "2008-03-18T03:19:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2574#issuecomment-17585",
    "user": "wdj"
}
```

abelian group patch



---

archive/issue_comments_017586.json:
```json
{
    "body": "Attachment [8962.patch](tarball://root/attachments/some-uuid/ticket2574/8962.patch) by wdj created at 2008-03-18 10:46:11",
    "created_at": "2008-03-18T10:46:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2574#issuecomment-17586",
    "user": "wdj"
}
```

Attachment [8962.patch](tarball://root/attachments/some-uuid/ticket2574/8962.patch) by wdj created at 2008-03-18 10:46:11



---

archive/issue_comments_017587.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-03-19T21:17:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2574#issuecomment-17587",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_017588.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-20T00:46:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2574#issuecomment-17588",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_017589.json:
```json
{
    "body": "Merged in Sage 2.11.alpha0",
    "created_at": "2008-03-20T00:46:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2574",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2574#issuecomment-17589",
    "user": "mabshoff"
}
```

Merged in Sage 2.11.alpha0
