# Issue 8823: Fix Cayley table doctest failure in group theory tutorial

archive/issues_008823.json:
```json
{
    "body": "Assignee: mvngu\n\nOn 32-bit Suse I build 4.4.1.alpha2 fine and get just one error in a\nnew tutorial:\n\n\n```\nsage -t  devel/sage/doc/en/thematic_tutorials/group_theory.rst\n**********************************************************************\nFile \"/local/jec/sage-4.4.1.alpha2/devel/sage-main/doc/en/thematic_tutorials/group_theory.rst\",\nline 432:\n    sage: H.cayley_table()\nExpected:\n    [ x0  x1  x2  x3  x4  x5  x6  x7  x8  x9 x10 x11]\n    [ x1  x0  x3  x2  x5  x4  x7  x6  x9  x8 x11 x10]\n    [ x2 x10  x0  x4  x3  x6  x5  x8  x7 x11  x1  x9]\n    [ x3 x11  x1  x5  x2  x7  x4  x9  x6 x10  x0  x8]\n    [ x4  x9 x10  x6  x0  x8  x3 x11  x5  x1  x2  x7]\n    [ x5  x8 x11  x7  x1  x9  x2 x10  x4  x0  x3  x6]\n    [ x6  x7  x9  x8 x10 x11  x0  x1  x3  x2  x4  x5]\n    [ x7  x6  x8  x9 x11 x10  x1  x0  x2  x3  x5  x4]\n    [ x8  x5  x7 x11  x9  x1 x10  x2  x0  x4  x6  x3]\n    [ x9  x4  x6 x10  x8  x0 x11  x3  x1  x5  x7  x2]\n    [x10  x2  x4  x0  x6  x3  x8  x5 x11  x7  x9  x1]\n    [x11  x3  x5  x1  x7  x2  x9  x4 x10  x6  x8  x0]\nGot:\n    *  a b c d e f g h i j k l\n     +------------------------\n    a| a b c d e f g h i j k l\n    b| b a d c f e h g j i l k\n    c| c k a e d g f i h l b j\n    d| d l b f c h e j g k a i\n    e| e j k g a i d l f b c h\n    f| f i l h b j c k e a d g\n    g| g h j i k l a b d c e f\n    h| h g i j l k b a c d f e\n    i| i f h l j b k c a e g d\n    j| j e g k i a l d b f h c\n    k| k c e a g d i f l h j b\n    l| l d f b h c j e k g i a\n    <BLANKLINE>\n**********************************************************************\n\nwhich looks trivial.\n\nJohn \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8823\n\n",
    "created_at": "2010-04-29T14:56:21Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "title": "Fix Cayley table doctest failure in group theory tutorial",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8823",
    "user": "rbeezer"
}
```
Assignee: mvngu

On 32-bit Suse I build 4.4.1.alpha2 fine and get just one error in a
new tutorial:


```
sage -t  devel/sage/doc/en/thematic_tutorials/group_theory.rst
**********************************************************************
File "/local/jec/sage-4.4.1.alpha2/devel/sage-main/doc/en/thematic_tutorials/group_theory.rst",
line 432:
    sage: H.cayley_table()
Expected:
    [ x0  x1  x2  x3  x4  x5  x6  x7  x8  x9 x10 x11]
    [ x1  x0  x3  x2  x5  x4  x7  x6  x9  x8 x11 x10]
    [ x2 x10  x0  x4  x3  x6  x5  x8  x7 x11  x1  x9]
    [ x3 x11  x1  x5  x2  x7  x4  x9  x6 x10  x0  x8]
    [ x4  x9 x10  x6  x0  x8  x3 x11  x5  x1  x2  x7]
    [ x5  x8 x11  x7  x1  x9  x2 x10  x4  x0  x3  x6]
    [ x6  x7  x9  x8 x10 x11  x0  x1  x3  x2  x4  x5]
    [ x7  x6  x8  x9 x11 x10  x1  x0  x2  x3  x5  x4]
    [ x8  x5  x7 x11  x9  x1 x10  x2  x0  x4  x6  x3]
    [ x9  x4  x6 x10  x8  x0 x11  x3  x1  x5  x7  x2]
    [x10  x2  x4  x0  x6  x3  x8  x5 x11  x7  x9  x1]
    [x11  x3  x5  x1  x7  x2  x9  x4 x10  x6  x8  x0]
Got:
    *  a b c d e f g h i j k l
     +------------------------
    a| a b c d e f g h i j k l
    b| b a d c f e h g j i l k
    c| c k a e d g f i h l b j
    d| d l b f c h e j g k a i
    e| e j k g a i d l f b c h
    f| f i l h b j c k e a d g
    g| g h j i k l a b d c e f
    h| h g i j l k b a c d f e
    i| i f h l j b k c a e g d
    j| j e g k i a l d b f h c
    k| k c e a g d i f l h j b
    l| l d f b h c j e k g i a
    <BLANKLINE>
**********************************************************************

which looks trivial.

John 
```


Issue created by migration from https://trac.sagemath.org/ticket/8823





---

archive/issue_comments_081027.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-05-01T05:36:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8823#issuecomment-81027",
    "user": "rbeezer"
}
```

Attachment



---

archive/issue_comments_081028.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-01T05:48:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8823#issuecomment-81028",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_081029.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-05-01T05:48:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8823#issuecomment-81029",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_081030.json:
```json
{
    "body": "This ticket really depends on merging the patch at #8468, which has its own prerequisites. But since this ticket is merged in Sage 4.4.1.alpha3, it has messed up the dependencies in #8468. What we can do now is close #8468. The other tickets relating to the thematic tutorials can be dealt with later.",
    "created_at": "2010-05-02T07:33:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8823",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8823#issuecomment-81030",
    "user": "mvngu"
}
```

This ticket really depends on merging the patch at #8468, which has its own prerequisites. But since this ticket is merged in Sage 4.4.1.alpha3, it has messed up the dependencies in #8468. What we can do now is close #8468. The other tickets relating to the thematic tutorials can be dealt with later.
