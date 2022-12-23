# Issue 4640: Do not dot out the number of pickles in the pickle jar doctest in sage/structure/sage_object.pyx

archive/issues_004640.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\n[7:17pm] mabshoff: ws-4083: In the pickle jar doctest the number of pickles is dotted out. Shouldn't we hard code that number and update it every time we do the latest pickle jar?\n[7:17pm] ws-4083 is now known as ws-3621.\n[7:17pm] ws-3621: mabshoff -- sure, we could.\n[7:18pm] ws-3621: I don't see why not.\n[7:18pm] ws-3621: good idea.\n[7:18pm] mabshoff: mk, ticket coming up.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4640\n\n",
    "created_at": "2008-11-28T03:21:17Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "Do not dot out the number of pickles in the pickle jar doctest in sage/structure/sage_object.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4640",
    "user": "mabshoff"
}
```
Assignee: mabshoff


```
[7:17pm] mabshoff: ws-4083: In the pickle jar doctest the number of pickles is dotted out. Shouldn't we hard code that number and update it every time we do the latest pickle jar?
[7:17pm] ws-4083 is now known as ws-3621.
[7:17pm] ws-3621: mabshoff -- sure, we could.
[7:18pm] ws-3621: I don't see why not.
[7:18pm] ws-3621: good idea.
[7:18pm] mabshoff: mk, ticket coming up.
```


Issue created by migration from https://trac.sagemath.org/ticket/4640





---

archive/issue_comments_034927.json:
```json
{
    "body": "If we are going to update the pickle jar for 3.2.2 we might as well fix this.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-15T19:13:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4640#issuecomment-34927",
    "user": "mabshoff"
}
```

If we are going to update the pickle jar for 3.2.2 we might as well fix this.

Cheers,

Michael



---

archive/issue_comments_034928.json:
```json
{
    "body": "I am seeing two doctest failures, one which could have been caused by my dumb rebase attempt:\n\n```\nsage -t -long devel/sage/sage/structure/sage_object.pyx # 1 doctests \nsage -t -long devel/sage/sage/combinat/words/word_generators.py # 1 doctests failed\n```\n\nIn detail: This might be caused by missing pickles in the pickle jar:\n\n```\nsage -t -long \"devel/sage/sage/structure/sage_object.pyx\"   \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.2.rc0/devel/sage/sage/structure/sage_object.pyx\", line 371, in __main__.example_16\nFailed example:\n    sage.structure.sage_object.unpickle_all(std)###line 682:_sage_    >>> sage.structure.sage_object.unpickle_all(std)\nExpected:\n    doctest:...: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.\n    Successfully unpickled ... objects.\n    Failed to unpickle 0 objects.\nGot:\n    doctest:1172: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.\n    ** failed:  _class__sage_combinat_word_Words_alphabet__.sobj\n    ** failed:  _class__sage_combinat_word_Words_n__.sobj\n    ** failed:  _class__sage_combinat_word_ShuffleProduct_overlapping__.sobj\n    ** failed:  _class__sage_combinat_word_ShuffleProduct_shifted__.sobj\n    ** failed:  _class__sage_combinat_word_ShuffleProduct_overlapping_r__.sobj\n    ** failed:  _class__sage_combinat_word_ShuffleProduct_w1w2__.sobj\n    Failed:\n    _class__sage_combinat_word_Words_alphabet__.sobj\n    _class__sage_combinat_word_Words_n__.sobj\n    _class__sage_combinat_word_ShuffleProduct_overlapping__.sobj\n    _class__sage_combinat_word_ShuffleProduct_shifted__.sobj\n    _class__sage_combinat_word_ShuffleProduct_overlapping_r__.sobj\n    _class__sage_combinat_word_ShuffleProduct_w1w2__.sobj\n    Successfully unpickled 448 objects.\n    Failed to unpickle 6 objects.\n**********************************************************************\n```\n\nand\n\n```\nsage -t -long \"devel/sage/sage/combinat/words/word_generators.py\"\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.2.2.rc0/devel/sage/sage/combinat/words/word_generators.py\", line 282, in __main__.example_6\nFailed example:\n    f[:Integer(10000)] == u[:Integer(10000)] #long time###line 286:_sage_    >>> f[:10000] == u[:10000] #long time\nExpected:\n    True\nGot:\n    False\n**********************************************************************\n```\n\n\nCheers,\n\nMichael",
    "created_at": "2008-12-15T19:18:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4640#issuecomment-34928",
    "user": "mabshoff"
}
```

I am seeing two doctest failures, one which could have been caused by my dumb rebase attempt:

```
sage -t -long devel/sage/sage/structure/sage_object.pyx # 1 doctests 
sage -t -long devel/sage/sage/combinat/words/word_generators.py # 1 doctests failed
```

In detail: This might be caused by missing pickles in the pickle jar:

```
sage -t -long "devel/sage/sage/structure/sage_object.pyx"   
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc0/devel/sage/sage/structure/sage_object.pyx", line 371, in __main__.example_16
Failed example:
    sage.structure.sage_object.unpickle_all(std)###line 682:_sage_    >>> sage.structure.sage_object.unpickle_all(std)
Expected:
    doctest:...: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.
    Successfully unpickled ... objects.
    Failed to unpickle 0 objects.
Got:
    doctest:1172: DeprecationWarning: Your data is stored in an old format. Please use the save() function to store your data in a more recent format.
    ** failed:  _class__sage_combinat_word_Words_alphabet__.sobj
    ** failed:  _class__sage_combinat_word_Words_n__.sobj
    ** failed:  _class__sage_combinat_word_ShuffleProduct_overlapping__.sobj
    ** failed:  _class__sage_combinat_word_ShuffleProduct_shifted__.sobj
    ** failed:  _class__sage_combinat_word_ShuffleProduct_overlapping_r__.sobj
    ** failed:  _class__sage_combinat_word_ShuffleProduct_w1w2__.sobj
    Failed:
    _class__sage_combinat_word_Words_alphabet__.sobj
    _class__sage_combinat_word_Words_n__.sobj
    _class__sage_combinat_word_ShuffleProduct_overlapping__.sobj
    _class__sage_combinat_word_ShuffleProduct_shifted__.sobj
    _class__sage_combinat_word_ShuffleProduct_overlapping_r__.sobj
    _class__sage_combinat_word_ShuffleProduct_w1w2__.sobj
    Successfully unpickled 448 objects.
    Failed to unpickle 6 objects.
**********************************************************************
```

and

```
sage -t -long "devel/sage/sage/combinat/words/word_generators.py"
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.2.rc0/devel/sage/sage/combinat/words/word_generators.py", line 282, in __main__.example_6
Failed example:
    f[:Integer(10000)] == u[:Integer(10000)] #long time###line 286:_sage_    >>> f[:10000] == u[:10000] #long time
Expected:
    True
Got:
    False
**********************************************************************
```


Cheers,

Michael



---

archive/issue_comments_034929.json:
```json
{
    "body": "oops, wrong ticket.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-15T19:19:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4640#issuecomment-34929",
    "user": "mabshoff"
}
```

oops, wrong ticket.

Cheers,

Michael



---

archive/issue_comments_034930.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-03-10T20:17:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4640#issuecomment-34930",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_034931.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-10T20:17:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4640#issuecomment-34931",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_034932.json:
```json
{
    "body": "yes!",
    "created_at": "2009-03-10T20:35:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4640#issuecomment-34932",
    "user": "was"
}
```

yes!



---

archive/issue_comments_034933.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-10T20:43:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4640#issuecomment-34933",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_034934.json:
```json
{
    "body": "Merged in Sage 3.4.final.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-10T20:43:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4640",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4640#issuecomment-34934",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.final.

Cheers,

Michael
