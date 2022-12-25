# Issue 9065: Add support for facade parents

archive/issues_009065.json:
```json
{
    "body": "Assignee: @nthiery\n\nCC:  sage-combinat\n\nKeywords: facade, parent, TestSuite\n\nThe goal of this tickets is to add support for facade parents; see:\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/a5ea008c24c17956/00ab8c6d2a16f57a\n\nThe main issue currently is that facade parents (Primes, NonNegativeIntegers, SymmetricFunctions, ...) are not aware that they are, which breaks some of the generic TestSuite tests.\n\nThis involves:\n- Creating a category or abstract class for facade parents\n  Such parents should declare a list of parents they are facade\n  for.\n- Adding a method P.check_element(x) (find a better name!) in Sets.ParentMethods which checks that the parent of x is P. Override this method for facade parents to check that the parent of x is one of the declared parents of P.\n- Fix P._test_one(), P._test_zero(), P._test_an_element() (and maybe others) to use P.check_element(x) instead of x in P.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9065\n\n",
    "created_at": "2010-05-27T13:02:37Z",
    "labels": [
        "component: categories"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7.1",
    "title": "Add support for facade parents",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9065",
    "user": "https://trac.sagemath.org/admin/accounts/users/nborie"
}
```
Assignee: @nthiery

CC:  sage-combinat

Keywords: facade, parent, TestSuite

The goal of this tickets is to add support for facade parents; see:
http://groups.google.com/group/sage-devel/browse_thread/thread/a5ea008c24c17956/00ab8c6d2a16f57a

The main issue currently is that facade parents (Primes, NonNegativeIntegers, SymmetricFunctions, ...) are not aware that they are, which breaks some of the generic TestSuite tests.

This involves:
- Creating a category or abstract class for facade parents
  Such parents should declare a list of parents they are facade
  for.
- Adding a method P.check_element(x) (find a better name!) in Sets.ParentMethods which checks that the parent of x is P. Override this method for facade parents to check that the parent of x is one of the declared parents of P.
- Fix P._test_one(), P._test_zero(), P._test_an_element() (and maybe others) to use P.check_element(x) instead of x in P.

Issue created by migration from https://trac.sagemath.org/ticket/9065





---

archive/issue_comments_083984.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-03-28T14:49:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9065#issuecomment-83984",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_083985.json:
```json
{
    "body": "Hi Nicolas, \n\nI started to review this. I currently have only the following interface\nremark: id there a reason why you need to pass a tuple for parameter\n`facade` whereas for `category` you can pass either a category or a\ntuple ? For example, why do you force the user to write \n\n```\nParent.__init__(self, facade = (IntegerRing(), ), category = Sets()) \n```\n\ninstead of\n\n```\nParent.__init__(self, facade = IntegerRing(), category = Sets()) \n```\n",
    "created_at": "2011-04-04T20:43:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9065#issuecomment-83985",
    "user": "https://github.com/hivert"
}
```

Hi Nicolas, 

I started to review this. I currently have only the following interface
remark: id there a reason why you need to pass a tuple for parameter
`facade` whereas for `category` you can pass either a category or a
tuple ? For example, why do you force the user to write 

```
Parent.__init__(self, facade = (IntegerRing(), ), category = Sets()) 
```

instead of

```
Parent.__init__(self, facade = IntegerRing(), category = Sets()) 
```




---

archive/issue_comments_083986.json:
```json
{
    "body": "Sorry for replying to myself...\n\n> I started to review this. I currently have only the following interface\n> remark: id there a reason why you need to pass a tuple for parameter\n> `facade` whereas for `category` you can pass either a category or a\n> tuple ?\n\nActually, it seems that the code in `Parent` allows for it. So I guess\nthat the example where the one parameter tuple occur could be simplified. I'm\nwriting a review patch on the sage-combinat queue.",
    "created_at": "2011-04-04T20:49:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9065#issuecomment-83986",
    "user": "https://github.com/hivert"
}
```

Sorry for replying to myself...

> I started to review this. I currently have only the following interface
> remark: id there a reason why you need to pass a tuple for parameter
> `facade` whereas for `category` you can pass either a category or a
> tuple ?

Actually, it seems that the code in `Parent` allows for it. So I guess
that the example where the one parameter tuple occur could be simplified. I'm
writing a review patch on the sage-combinat queue.



---

archive/issue_comments_083987.json:
```json
{
    "body": "Replying to [comment:6 hivert]:\n> \n> Actually, it seems that the code in `Parent` allows for it. So I guess\n> that the example where the one parameter tuple occur could be simplified. I'm\n> writing a review patch on the sage-combinat queue.\n\nGood point :-) +1 on that change.",
    "created_at": "2011-04-05T11:38:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9065#issuecomment-83987",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:6 hivert]:
> 
> Actually, it seems that the code in `Parent` allows for it. So I guess
> that the example where the one parameter tuple occur could be simplified. I'm
> writing a review patch on the sage-combinat queue.

Good point :-) +1 on that change.



---

archive/issue_comments_083988.json:
```json
{
    "body": "Hi!\n\nI folded in Florent's reviewer patch for the above issue, added facade option in SearchForest, updated an example there as well as NN and Primes to be facades, and fixed some trivially failing tests reported by the patchbot. The patch should be good to go. Florent: can you confirm?",
    "created_at": "2011-04-21T10:51:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9065#issuecomment-83988",
    "user": "https://github.com/nthiery"
}
```

Hi!

I folded in Florent's reviewer patch for the above issue, added facade option in SearchForest, updated an example there as well as NN and Primes to be facades, and fixed some trivially failing tests reported by the patchbot. The patch should be good to go. Florent: can you confirm?



---

archive/issue_comments_083989.json:
```json
{
    "body": "Replying to [comment:8 nthiery]:\n> I folded in Florent's reviewer patch for the above issue, added facade option in SearchForest, updated an example there as well as NN and Primes to be facades, and fixed some trivially failing tests reported by the patchbot. The patch should be good to go. Florent: can you confirm?\n\nUnfortunately not ! I spotted a few more wrong sphinx markup. Please have a look at my review patch on trac. Otherwise, it is ready to go.",
    "created_at": "2011-04-22T22:17:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9065#issuecomment-83989",
    "user": "https://github.com/hivert"
}
```

Replying to [comment:8 nthiery]:
> I folded in Florent's reviewer patch for the above issue, added facade option in SearchForest, updated an example there as well as NN and Primes to be facades, and fixed some trivially failing tests reported by the patchbot. The patch should be good to go. Florent: can you confirm?

Unfortunately not ! I spotted a few more wrong sphinx markup. Please have a look at my review patch on trac. Otherwise, it is ready to go.



---

archive/issue_comments_083990.json:
```json
{
    "body": "I checked your patch, folded it in, and reuploaded. Thanks!",
    "created_at": "2011-04-23T01:44:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9065#issuecomment-83990",
    "user": "https://github.com/nthiery"
}
```

I checked your patch, folded it in, and reuploaded. Thanks!



---

archive/issue_comments_083991.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-04-23T01:44:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9065#issuecomment-83991",
    "user": "https://github.com/nthiery"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_022217.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-04-25T10:52:25Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9065",
    "milestone": "sage-4.7.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9065#event-22217"
}
```



---

archive/issue_comments_083992.json:
```json
{
    "body": "Attachment [trac_9065-facade_parents-nt.patch](tarball://root/attachments/some-uuid/ticket9065/trac_9065-facade_parents-nt.patch) by @nthiery created at 2011-04-26 04:34:27\n\nFixed another trivial failing test in a separate file. Hopefuly the last one!\n\nFlorent just checked it, and is ok to leave the positive review.",
    "created_at": "2011-04-26T04:34:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9065#issuecomment-83992",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_9065-facade_parents-nt.patch](tarball://root/attachments/some-uuid/ticket9065/trac_9065-facade_parents-nt.patch) by @nthiery created at 2011-04-26 04:34:27

Fixed another trivial failing test in a separate file. Hopefuly the last one!

Florent just checked it, and is ok to leave the positive review.



---

archive/issue_events_022218.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-05-03T12:28:29Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9065",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9065#event-22218"
}
```



---

archive/issue_comments_083993.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-05-03T12:28:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9065",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9065#issuecomment-83993",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
