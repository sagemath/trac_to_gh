# Issue 8430: three doctest failures with Sage 4.3.4.alpha0

archive/issues_008430.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  sage-combinat\n\nFrom [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/99b72f5f27858b53):\n\n```\n* The following tests failed on sage.math:\n\nsage -t  -long local/lib/python2.6/site-packages/sagenb-0.7.5.1-py2.6.egg/sagenb/notebook/interact.py # 1 doctests failed\nsage -t  -long local/lib/python2.6/site-packages/sagenb-0.7.5.1-py2.6.egg/sagenb/misc/sageinspect.py # 1 doctests failed\nsage -t  -long devel/sage/sage/categories/finite_semigroups.py # 2 doctests failed\nsage -t  -long devel/sage/sage/categories/examples/finite_semigroups.py # 1 doctests failed \n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8430\n\n",
    "created_at": "2010-03-03T18:42:04Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "three doctest failures with Sage 4.3.4.alpha0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8430",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: tbd

CC:  sage-combinat

From [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/99b72f5f27858b53):

```
* The following tests failed on sage.math:

sage -t  -long local/lib/python2.6/site-packages/sagenb-0.7.5.1-py2.6.egg/sagenb/notebook/interact.py # 1 doctests failed
sage -t  -long local/lib/python2.6/site-packages/sagenb-0.7.5.1-py2.6.egg/sagenb/misc/sageinspect.py # 1 doctests failed
sage -t  -long devel/sage/sage/categories/finite_semigroups.py # 2 doctests failed
sage -t  -long devel/sage/sage/categories/examples/finite_semigroups.py # 1 doctests failed 
```


Issue created by migration from https://trac.sagemath.org/ticket/8430





---

archive/issue_comments_075454.json:
```json
{
    "body": "I've tried to address the problem with sageinspect.py in ticket #8324.",
    "created_at": "2010-03-03T22:08:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8430#issuecomment-75454",
    "user": "https://github.com/jhpalmieri"
}
```

I've tried to address the problem with sageinspect.py in ticket #8324.



---

archive/issue_comments_075455.json:
```json
{
    "body": "Note that the problem with `sagenb/notebook/interact.py` should be fixed by the sagenb patch at ticket #5601.",
    "created_at": "2010-03-03T22:29:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8430#issuecomment-75455",
    "user": "https://github.com/jhpalmieri"
}
```

Note that the problem with `sagenb/notebook/interact.py` should be fixed by the sagenb patch at ticket #5601.



---

archive/issue_comments_075456.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-04T10:14:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8430#issuecomment-75456",
    "user": "https://github.com/hivert"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075457.json:
```json
{
    "body": "> * The following tests failed on sage.math:\n\n```\nsage -t  -long devel/sage/sage/categories/finite_semigroups.py # 2 doctests failed\nsage -t  -long devel/sage/sage/categories/examples/finite_semigroups.py # 1 doctests failed \n```\n\nThose last two should be fixed by the submitted patch. A better fix together with improvements is being written on sage-combinat but I don't know how long finishing those improvements will take. So please review the patch. \n\nBy the way, should'nt I create a ticket for this patch ? It is certainly orthogonal to the two other one doctest failure.\n\nCheers,\n\nFlorent",
    "created_at": "2010-03-04T10:14:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8430#issuecomment-75457",
    "user": "https://github.com/hivert"
}
```

> * The following tests failed on sage.math:

```
sage -t  -long devel/sage/sage/categories/finite_semigroups.py # 2 doctests failed
sage -t  -long devel/sage/sage/categories/examples/finite_semigroups.py # 1 doctests failed 
```

Those last two should be fixed by the submitted patch. A better fix together with improvements is being written on sage-combinat but I don't know how long finishing those improvements will take. So please review the patch. 

By the way, should'nt I create a ticket for this patch ? It is certainly orthogonal to the two other one doctest failure.

Cheers,

Florent



---

archive/issue_comments_075458.json:
```json
{
    "body": "Since the other issues have there own tickets I don't think another one is necessary.\n\nThere is one doctest failure still:\n\n```\nFile \"/Volumes/E/sage-4.3.4.alpha0/devel/sage-t1/sage/categories/finite_semigroups.py\", line 229:\n    sage: sorted(S.j_transversal_of_idempotents())\nExpected:\n    ['a', 'ab', 'ac', 'acb', 'b', 'bc', 'c']\nGot:\n    ['a', 'ab', 'ac', 'acb', 'b', 'c', 'cb']\n*********************************************\n```\n\n\nwhich is not covered by the patch.  Seems like maybe the expected string is wrong, unless the sorted function has varying behavior.",
    "created_at": "2010-03-04T21:08:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8430#issuecomment-75458",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Since the other issues have there own tickets I don't think another one is necessary.

There is one doctest failure still:

```
File "/Volumes/E/sage-4.3.4.alpha0/devel/sage-t1/sage/categories/finite_semigroups.py", line 229:
    sage: sorted(S.j_transversal_of_idempotents())
Expected:
    ['a', 'ab', 'ac', 'acb', 'b', 'bc', 'c']
Got:
    ['a', 'ab', 'ac', 'acb', 'b', 'c', 'cb']
*********************************************
```


which is not covered by the patch.  Seems like maybe the expected string is wrong, unless the sorted function has varying behavior.



---

archive/issue_comments_075459.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-04T21:08:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8430#issuecomment-75459",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075460.json:
```json
{
    "body": "Attachment [trac_8430-semigroup_doctest_fix-fh.patch](tarball://root/attachments/some-uuid/ticket8430/trac_8430-semigroup_doctest_fix-fh.patch) by @hivert created at 2010-03-04 21:41:49\n\nReplying to [comment:5 mhampton]:\n\n> There is one doctest failure still:\n\n```\nFile \"/Volumes/E/sage-4.3.4.alpha0/devel/sage-t1/sage/categories/finite_semigroups.py\", line 229:\n    sage: sorted(S.j_transversal_of_idempotents())\nExpected:\n    ['a', 'ab', 'ac', 'acb', 'b', 'bc', 'c']\nGot:\n    ['a', 'ab', 'ac', 'acb', 'b', 'c', 'cb']\n*********************************************\n```\n \n> which is not covered by the patch.  Seems like maybe the expected string is wrong, unless the sorted function has varying behavior.\n\nI'm not sure to understand:\n- why I missed this one;\n- why the result of sorted changed between 4.3.3 and 4.3.4;\n- why despite of this change it seems to be stable on both version...\nAnyway the newly uploaded patch passed the tests 10 times in a raw on the machine sage. Maybe it could be worth checking of it is also stable on other architectures.\n\nSorry for the mess and please review.",
    "created_at": "2010-03-04T21:41:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8430#issuecomment-75460",
    "user": "https://github.com/hivert"
}
```

Attachment [trac_8430-semigroup_doctest_fix-fh.patch](tarball://root/attachments/some-uuid/ticket8430/trac_8430-semigroup_doctest_fix-fh.patch) by @hivert created at 2010-03-04 21:41:49

Replying to [comment:5 mhampton]:

> There is one doctest failure still:

```
File "/Volumes/E/sage-4.3.4.alpha0/devel/sage-t1/sage/categories/finite_semigroups.py", line 229:
    sage: sorted(S.j_transversal_of_idempotents())
Expected:
    ['a', 'ab', 'ac', 'acb', 'b', 'bc', 'c']
Got:
    ['a', 'ab', 'ac', 'acb', 'b', 'c', 'cb']
*********************************************
```
 
> which is not covered by the patch.  Seems like maybe the expected string is wrong, unless the sorted function has varying behavior.

I'm not sure to understand:
- why I missed this one;
- why the result of sorted changed between 4.3.3 and 4.3.4;
- why despite of this change it seems to be stable on both version...
Anyway the newly uploaded patch passed the tests 10 times in a raw on the machine sage. Maybe it could be worth checking of it is also stable on other architectures.

Sorry for the mess and please review.



---

archive/issue_comments_075461.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-04T21:41:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8430#issuecomment-75461",
    "user": "https://github.com/hivert"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075462.json:
```json
{
    "body": "Changing assignee from tbd to @hivert.",
    "created_at": "2010-03-04T21:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8430#issuecomment-75462",
    "user": "https://github.com/hivert"
}
```

Changing assignee from tbd to @hivert.



---

archive/issue_comments_075463.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-04T22:27:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8430#issuecomment-75463",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075464.json:
```json
{
    "body": "All tests in categories passed on a 10.6 mac and on 64-bit Ubuntu 9.10, so I think I can give this a positive review.",
    "created_at": "2010-03-04T22:27:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8430#issuecomment-75464",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

All tests in categories passed on a 10.6 mac and on 64-bit Ubuntu 9.10, so I think I can give this a positive review.



---

archive/issue_comments_075465.json:
```json
{
    "body": "SageNB 0.7.5.2 includes fixes for the first two failures in the description (see #8435).\n\nAn important note:  It's best to test SageNB files with `-force_lib`, e.g.,\n\n\n```sh\nsage -t -long -force_lib local/lib/python2.6/site-packages/sagenb-0.7.5.1-py2.6.egg/sagenb/notebook/interact.py\n```\n\n\nRunning `sage -t -sagenb` or `make test` and its friends will set it implicitly.  If the option is set, `SAGE_LOCAL/bin/sage-doctest` will treat the file(s) as Sage library code, even if it does not live under `SAGE_ROOT/devel`.  In particular, `sage-doctest` will not attempt the equivalent of `from filebase import *`, which can raise false errors or cause segfaults.\n\nI suppose I should have called it `-library_code`, instead.\n\nPlease remember to fillin",
    "created_at": "2010-03-04T23:28:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8430#issuecomment-75465",
    "user": "https://github.com/qed777"
}
```

SageNB 0.7.5.2 includes fixes for the first two failures in the description (see #8435).

An important note:  It's best to test SageNB files with `-force_lib`, e.g.,


```sh
sage -t -long -force_lib local/lib/python2.6/site-packages/sagenb-0.7.5.1-py2.6.egg/sagenb/notebook/interact.py
```


Running `sage -t -sagenb` or `make test` and its friends will set it implicitly.  If the option is set, `SAGE_LOCAL/bin/sage-doctest` will treat the file(s) as Sage library code, even if it does not live under `SAGE_ROOT/devel`.  In particular, `sage-doctest` will not attempt the equivalent of `from filebase import *`, which can raise false errors or cause segfaults.

I suppose I should have called it `-library_code`, instead.

Please remember to fillin



---

archive/issue_comments_075466.json:
```json
{
    "body": "I'm not at home, and can't very easily start applying patches, but I can confirm I get the same results, based on Sage 4.3.4.alpha0 but with a few Solaris-specific patches on Solaris 10 (SPARC)\n\n\n```\n**********************************************************************\nFile \"/export/home/drkirkby/32/sage-4.3.4.alpha0/devel/sage/sage/categories/fini\nte_semigroups.py\", line 232:\n    sage: sorted(S.j_transversal_of_idempotents())\nExpected:\n    ['a', 'ab', 'ac', 'acb', 'b', 'bc', 'c']\nGot:\n    ['a', 'ab', 'ac', 'acb', 'b', 'c', 'cb']\n**********************************************************************\nFile \"/export/home/drkirkby/32/sage-4.3.4.alpha0/devel/sage/sage/categories/fini\nte_semigroups.py\", line 198:\n    sage: S.j_classes()\nExpected:\n    [['acb', 'cab', 'bca', 'abc', 'bac', 'cba'], ['ac', 'ca'],\n    ['ab', 'ba'], ['bc', 'cb'], ['a'], ['c'], ['b']]\nGot:\n    [['a'], ['acb', 'cba', 'bca', 'abc', 'bac', 'cab'], ['ac', 'ca'], ['ab', 'ba\n'], ['cb', 'bc'], ['c'], ['b']]\n**********************************************************************\n2 items had failures:\n```\n\n\n\nSo the problem is occuring on more that one architecuture. I hope to try the patch within the next 12 hours.",
    "created_at": "2010-03-05T14:00:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8430#issuecomment-75466",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'm not at home, and can't very easily start applying patches, but I can confirm I get the same results, based on Sage 4.3.4.alpha0 but with a few Solaris-specific patches on Solaris 10 (SPARC)


```
**********************************************************************
File "/export/home/drkirkby/32/sage-4.3.4.alpha0/devel/sage/sage/categories/fini
te_semigroups.py", line 232:
    sage: sorted(S.j_transversal_of_idempotents())
Expected:
    ['a', 'ab', 'ac', 'acb', 'b', 'bc', 'c']
Got:
    ['a', 'ab', 'ac', 'acb', 'b', 'c', 'cb']
**********************************************************************
File "/export/home/drkirkby/32/sage-4.3.4.alpha0/devel/sage/sage/categories/fini
te_semigroups.py", line 198:
    sage: S.j_classes()
Expected:
    [['acb', 'cab', 'bca', 'abc', 'bac', 'cba'], ['ac', 'ca'],
    ['ab', 'ba'], ['bc', 'cb'], ['a'], ['c'], ['b']]
Got:
    [['a'], ['acb', 'cba', 'bca', 'abc', 'bac', 'cab'], ['ac', 'ca'], ['ab', 'ba
'], ['cb', 'bc'], ['c'], ['b']]
**********************************************************************
2 items had failures:
```



So the problem is occuring on more that one architecuture. I hope to try the patch within the next 12 hours.



---

archive/issue_comments_075467.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-09T07:44:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8430",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8430#issuecomment-75467",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_008615.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2010-03-09T07:44:51Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8430",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8430#event-8615"
}
```
