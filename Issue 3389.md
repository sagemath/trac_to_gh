# Issue 3389: CartesianProduct infinite sequences

archive/issues_003389.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\nHi!\n\nThe Cartesian Product iterator of infinite sequences doesn't enumerate the\nevery element in the product.\n\nI tried:\n\nfor t in CartesianProduct(QQ,ZZ):\n\n....:     print t\n\n....:     \n\n[0, 0]\n\n[0, 1]\n\n[0, -1]\n\n[0, 2]\n\n\nThis is equivalent to nest for loops, which won't work.\nYou have to enumerate the set in a different way.\n\nSee \nhttp://en.wikipedia.org/wiki/Recursively_enumerable\nhttp://en.wikipedia.org/wiki/Cantor_pairing_function\n\nBest regards,\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3389\n\n",
    "created_at": "2008-06-10T10:15:49Z",
    "labels": [
        "combinatorics",
        "minor",
        "enhancement"
    ],
    "title": "CartesianProduct infinite sequences",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3389",
    "user": "PolyBoRi"
}
```
Assignee: mhansen

CC:  sage-combinat

Hi!

The Cartesian Product iterator of infinite sequences doesn't enumerate the
every element in the product.

I tried:

for t in CartesianProduct(QQ,ZZ):

....:     print t

....:     

[0, 0]

[0, 1]

[0, -1]

[0, 2]


This is equivalent to nest for loops, which won't work.
You have to enumerate the set in a different way.

See 
http://en.wikipedia.org/wiki/Recursively_enumerable
http://en.wikipedia.org/wiki/Cantor_pairing_function

Best regards,
Michael

Issue created by migration from https://trac.sagemath.org/ticket/3389





---

archive/issue_comments_023726.json:
```json
{
    "body": "How often does one want to iterate through a CartesianProduct of infinite things?  Is the speed tradeoff for implementing the general solution worth it?",
    "created_at": "2008-06-10T10:24:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3389#issuecomment-23726",
    "user": "mhansen"
}
```

How often does one want to iterate through a CartesianProduct of infinite things?  Is the speed tradeoff for implementing the general solution worth it?



---

archive/issue_comments_023727.json:
```json
{
    "body": "I would try checking via\nlen\nif the sequence might be finite (of course, there are finite sequence, where len doesn't work).\nIf you know, that the sequences are finite, you can return an naive iterator.",
    "created_at": "2008-06-10T10:32:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3389#issuecomment-23727",
    "user": "PolyBoRi"
}
```

I would try checking via
len
if the sequence might be finite (of course, there are finite sequence, where len doesn't work).
If you know, that the sequences are finite, you can return an naive iterator.



---

archive/issue_comments_023728.json:
```json
{
    "body": "Sure, but I still feel a bit like I'd be writing a bunch of useless code in the end.  I'd be more apt to rename CartesianProduct to CartesianProductOfFiniteSets or something like that.",
    "created_at": "2008-06-10T10:44:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3389#issuecomment-23728",
    "user": "mhansen"
}
```

Sure, but I still feel a bit like I'd be writing a bunch of useless code in the end.  I'd be more apt to rename CartesianProduct to CartesianProductOfFiniteSets or something like that.



---

archive/issue_comments_023729.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-06-10T18:01:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3389#issuecomment-23729",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_023730.json:
```json
{
    "body": "So... it looks like I already have some code that does something similar in http://trac.sagemath.org/sage_trac/attachment/ticket/1448/1448-2.patch .  The question then becomes whether to cache the elements as you iterate over them or reiterate to them each time you need them.  Also, there are many things finite things whose cartesian product I want to iterate over for which len() takes a nontrivial amount of time.",
    "created_at": "2008-06-10T18:01:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3389#issuecomment-23730",
    "user": "mhansen"
}
```

So... it looks like I already have some code that does something similar in http://trac.sagemath.org/sage_trac/attachment/ticket/1448/1448-2.patch .  The question then becomes whether to cache the elements as you iterate over them or reiterate to them each time you need them.  Also, there are many things finite things whose cartesian product I want to iterate over for which len() takes a nontrivial amount of time.



---

archive/issue_comments_023731.json:
```json
{
    "body": "I don't think, this could give acceptable performance without caching in a similar way as in the code for the matrix spaces.",
    "created_at": "2008-06-12T09:08:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3389",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3389#issuecomment-23731",
    "user": "PolyBoRi"
}
```

I don't think, this could give acceptable performance without caching in a similar way as in the code for the matrix spaces.
