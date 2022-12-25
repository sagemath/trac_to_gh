# Issue 7398: Added is_iterator method and fixes sage to use it.

archive/issues_007398.json:
```json
{
    "body": "Assignee: @hivert\n\nCC:  sage-combinat @williamstein\n\nKeywords: iterators, itertools\n\nThe following mantra occurs at three places in Sage's code to test whether v is an iterator:\n\n```\n     if hasattr(v, 'next'):\n```\nThis is not quite correct since some sage objects have a next method without being iterable, or with a different semantic. \n\nLet me quote python's doc:\n\n> The iterator objects themselves are required to support the following two methods, which together form the iterator protocol:\n\n \n>  iterator.__iter__()::\n\n> \n     Return the iterator object itself. This is required to allow both containers and iterators to be used with the for and in statements. This method corresponds to the tp_iter slot of the type structure for Python objects in the Python/C API.\n\n> iterator.next()::\n> \n\n    Return the next item from the container. If there are no further items, raise the StopIteration exception. This method corresponds to the tp_iternext slot of the type structure for Python objects in the Python/C API.\n\n\nTherefore here is the good way to test if an element is an iterator:\n\n```\n    try:\n        return it is iter(it)\n    except:\n        return False\n```\nNote: it is not sufficient to check for the existence of the methods since some sage object implement `__iter__` to raise a `NotImplemented` exception !\n\nFlorent\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7398\n\n",
    "closed_at": "2009-11-12T06:21:27Z",
    "created_at": "2009-11-05T18:15:27Z",
    "labels": [
        "component: misc"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "Added is_iterator method and fixes sage to use it.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7398",
    "user": "https://github.com/nthiery"
}
```
Assignee: @hivert

CC:  sage-combinat @williamstein

Keywords: iterators, itertools

The following mantra occurs at three places in Sage's code to test whether v is an iterator:

```
     if hasattr(v, 'next'):
```
This is not quite correct since some sage objects have a next method without being iterable, or with a different semantic. 

Let me quote python's doc:

> The iterator objects themselves are required to support the following two methods, which together form the iterator protocol:

 
>  iterator.__iter__()::

> 
     Return the iterator object itself. This is required to allow both containers and iterators to be used with the for and in statements. This method corresponds to the tp_iter slot of the type structure for Python objects in the Python/C API.

> iterator.next()::
> 

    Return the next item from the container. If there are no further items, raise the StopIteration exception. This method corresponds to the tp_iternext slot of the type structure for Python objects in the Python/C API.


Therefore here is the good way to test if an element is an iterator:

```
    try:
        return it is iter(it)
    except:
        return False
```
Note: it is not sufficient to check for the existence of the methods since some sage object implement `__iter__` to raise a `NotImplemented` exception !

Florent


Issue created by migration from https://trac.sagemath.org/ticket/7398





---

archive/issue_comments_062085.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-05T22:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7398#issuecomment-62085",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_062086.json:
```json
{
    "body": "Attachment [trac_7398_iter_detect-fh.patch](tarball://root/attachments/some-uuid/ticket7398/trac_7398_iter_detect-fh.patch) by @hivert created at 2009-11-05 22:47:31",
    "created_at": "2009-11-05T22:47:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7398#issuecomment-62086",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_7398_iter_detect-fh.patch](tarball://root/attachments/some-uuid/ticket7398/trac_7398_iter_detect-fh.patch) by @hivert created at 2009-11-05 22:47:31



---

archive/issue_events_017493.json:
```json
{
    "actor": "https://github.com/hivert",
    "created_at": "2009-11-06T07:38:51Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "milestone": "sage-4.2.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7398#event-17493"
}
```



---

archive/issue_comments_062087.json:
```json
{
    "body": "Attachment [trac_7398_iter_detect-fh.2.patch](tarball://root/attachments/some-uuid/ticket7398/trac_7398_iter_detect-fh.2.patch) by @nthiery created at 2009-11-06 13:58:11\n\nUpdated patch after review by Nicolas (uses itertools to simplify further  sage.server.interact.list_of_first_n)",
    "created_at": "2009-11-06T13:58:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7398#issuecomment-62087",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_7398_iter_detect-fh.2.patch](tarball://root/attachments/some-uuid/ticket7398/trac_7398_iter_detect-fh.2.patch) by @nthiery created at 2009-11-06 13:58:11

Updated patch after review by Nicolas (uses itertools to simplify further  sage.server.interact.list_of_first_n)



---

archive/issue_comments_062088.json:
```json
{
    "body": "William: this makes a small edit to sage.server.notebook.interact.list_of_first_n\n\nYou may want to check/backport to the notebook code",
    "created_at": "2009-11-06T14:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7398#issuecomment-62088",
    "user": "https://github.com/nthiery"
}
```

William: this makes a small edit to sage.server.notebook.interact.list_of_first_n

You may want to check/backport to the notebook code



---

archive/issue_comments_062089.json:
```json
{
    "body": "Changing keywords from \"iterators\" to \"iterators, itertools\".",
    "created_at": "2009-11-06T14:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7398#issuecomment-62089",
    "user": "https://github.com/nthiery"
}
```

Changing keywords from "iterators" to "iterators, itertools".



---

archive/issue_comments_062090.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-06T14:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7398#issuecomment-62090",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062091.json:
```json
{
    "body": "The given patch actually breaks somme code... I'm uploading a new one.",
    "created_at": "2009-11-06T21:10:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7398#issuecomment-62091",
    "user": "https://github.com/hivert"
}
```

The given patch actually breaks somme code... I'm uploading a new one.



---

archive/issue_comments_062092.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2009-11-06T21:10:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7398#issuecomment-62092",
    "user": "https://github.com/hivert"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_062093.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-06T21:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7398#issuecomment-62093",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_062094.json:
```json
{
    "body": "Attachment [trac_7398_iter_detect-fh.3.patch](tarball://root/attachments/some-uuid/ticket7398/trac_7398_iter_detect-fh.3.patch) by @hivert created at 2009-11-06 21:15:51\n\nNicolas : can you re-review this patch...\nI commented out some line saying that it was never user and actually is was quite a lot... I don't understand why we didn't caught it by the tests. Anyway, Massena did.\n\nSorry for the mess,\n\nFlorent",
    "created_at": "2009-11-06T21:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7398#issuecomment-62094",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_7398_iter_detect-fh.3.patch](tarball://root/attachments/some-uuid/ticket7398/trac_7398_iter_detect-fh.3.patch) by @hivert created at 2009-11-06 21:15:51

Nicolas : can you re-review this patch...
I commented out some line saying that it was never user and actually is was quite a lot... I don't understand why we didn't caught it by the tests. Anyway, Massena did.

Sorry for the mess,

Florent



---

archive/issue_comments_062095.json:
```json
{
    "body": "Attachment [trac_7398_combclass_set_compat-fh.patch](tarball://root/attachments/some-uuid/ticket7398/trac_7398_combclass_set_compat-fh.patch) by @hivert created at 2009-11-09 16:30:11",
    "created_at": "2009-11-09T16:30:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7398#issuecomment-62095",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_7398_combclass_set_compat-fh.patch](tarball://root/attachments/some-uuid/ticket7398/trac_7398_combclass_set_compat-fh.patch) by @hivert created at 2009-11-09 16:30:11



---

archive/issue_comments_062096.json:
```json
{
    "body": "The patch trac_7398_iter_detect-fh.3.patch broke something in graph_generators. \nthe patch trac_7398_combclass_set_compat-fh.patch should fix it. \n\nApply those two patches in that order.\n\nCheers,\n\nFlorent",
    "created_at": "2009-11-09T16:35:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7398#issuecomment-62096",
    "user": "https://github.com/hivert"
}
```

The patch trac_7398_iter_detect-fh.3.patch broke something in graph_generators. 
the patch trac_7398_combclass_set_compat-fh.patch should fix it. 

Apply those two patches in that order.

Cheers,

Florent



---

archive/issue_comments_062097.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-09T17:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7398#issuecomment-62097",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_062098.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-12T06:21:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7398#issuecomment-62098",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_017494.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-12T06:21:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7398#event-17494"
}
```



---

archive/issue_events_017495.json:
```json
{
    "actor": "https://github.com/nthiery",
    "created_at": "2009-11-12T09:40:23Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "milestone": "sage-4.2.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7398#event-17495"
}
```



---

archive/issue_events_017496.json:
```json
{
    "actor": "https://github.com/nthiery",
    "created_at": "2009-11-12T09:40:23Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7398",
    "milestone": "sage-4.2.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7398#event-17496"
}
```
