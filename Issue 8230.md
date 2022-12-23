# Issue 8230: strange behaviour

archive/issues_008230.json:
```json
{
    "body": "Assignee: robertwb\n\nHi, I found the following strange behaviour of the addition\n<int> + 1/2. I have a file `MurphyE.sage` which contains:\n\n```\nload E.sage\n\nfoo(2)\n```\n\nwhere `E.sage` contains:\n\n```\ndef foo(K):\n    for i in range(K):\n       print i, i+1/2, type(i), type(i+1/2)\n```\n\nThen I get:\n\n```\nsage: load MurphyE.sage\n0 0 <type 'int'> <type 'int'>\n1 1 <type 'int'> <type 'int'>\n```\n\nNow if instead I replace `load E.sage` in my file by the\ncontent of the procedure `foo`, i.e.:\n\n```\ndef foo(K):\n    for i in range(K):\n       print i, i+1/2, type(i), type(i+1/2)\n\nfoo(2)\n```\n\nthen I get:\n\n```\nsage: load MurphyE.sage\n0 1/2 <type 'int'> <type 'sage.rings.rational.Rational'>\n1 3/2 <type 'int'> <type 'sage.rings.rational.Rational'>\n```\n\nwhich is the expected behaviour. Please can someone explain to me\nthe first result? I forgot to say it is with Sage 4.3.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8230\n\n",
    "created_at": "2010-02-10T15:17:22Z",
    "labels": [
        "coercion",
        "major",
        "bug"
    ],
    "title": "strange behaviour",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8230",
    "user": "zimmerma"
}
```
Assignee: robertwb

Hi, I found the following strange behaviour of the addition
<int> + 1/2. I have a file `MurphyE.sage` which contains:

```
load E.sage

foo(2)
```

where `E.sage` contains:

```
def foo(K):
    for i in range(K):
       print i, i+1/2, type(i), type(i+1/2)
```

Then I get:

```
sage: load MurphyE.sage
0 0 <type 'int'> <type 'int'>
1 1 <type 'int'> <type 'int'>
```

Now if instead I replace `load E.sage` in my file by the
content of the procedure `foo`, i.e.:

```
def foo(K):
    for i in range(K):
       print i, i+1/2, type(i), type(i+1/2)

foo(2)
```

then I get:

```
sage: load MurphyE.sage
0 1/2 <type 'int'> <type 'sage.rings.rational.Rational'>
1 3/2 <type 'int'> <type 'sage.rings.rational.Rational'>
```

which is the expected behaviour. Please can someone explain to me
the first result? I forgot to say it is with Sage 4.3.

Issue created by migration from https://trac.sagemath.org/ticket/8230





---

archive/issue_comments_072703.json:
```json
{
    "body": "Dupe of #6345",
    "created_at": "2010-02-10T19:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8230#issuecomment-72703",
    "user": "robertwb"
}
```

Dupe of #6345



---

archive/issue_comments_072704.json:
```json
{
    "body": "it seems to be fixed now.",
    "created_at": "2010-08-15T18:01:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8230#issuecomment-72704",
    "user": "ylchapuy"
}
```

it seems to be fixed now.



---

archive/issue_comments_072705.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-08-15T18:01:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8230#issuecomment-72705",
    "user": "ylchapuy"
}
```

Resolution: fixed



---

archive/issue_comments_072706.json:
```json
{
    "body": "I'm closing this as a \"duplicate\" of #6345.",
    "created_at": "2010-08-15T21:32:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8230#issuecomment-72706",
    "user": "mpatel"
}
```

I'm closing this as a "duplicate" of #6345.



---

archive/issue_comments_072707.json:
```json
{
    "body": "Resolution changed from fixed to duplicate",
    "created_at": "2010-08-15T21:32:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8230",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8230#issuecomment-72707",
    "user": "mpatel"
}
```

Resolution changed from fixed to duplicate
