# Issue 6468: FiniteField_prime_modn.__call__ should raise an error, rather than return an error

archive/issues_006468.json:
```json
{
    "body": "Assignee: somebody\n\nKeywords: Finite field, call\n\nThe `__call__` method of `FiniteField_prime_modn` reads like this:\n\n```\n    def __call__(self, x):\n        try:\n            return integer_mod.IntegerMod(self, x)\n        except (NotImplementedError, PariError):\n            return TypeError, \"error coercing to finite field\"\n        except TypeError:\n            if sage.interfaces.all.is_GapElement(x):\n                from sage.interfaces.gap import gfq_gap_to_sage\n                try:\n                    return gfq_gap_to_sage(x, self)\n                except (ValueError, IndexError, TypeError), msg:\n                    raise TypeError, \"%s\\nerror coercing to finite field\"%msg\n            else:\n                raise\n```\n\n\nSo, in the fourth line of the function body, an error is not raised but returned.\n\nActually I met this when calling `GF(2)` with one of my extension types. Unfortunately I did not find anything in Sage that would trigger it as well.\n\nAnyway, I think it should be obvious that \n\n```\n            return TypeError, \"error coercing to finite field\"\n```\n\nshould be changed into\n\n```\n            raise TypeError, \"error coercing to finite field\"\n```\n\n\nThis is what my patch does.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6468\n\n",
    "created_at": "2009-07-06T13:10:08Z",
    "labels": [
        "basic arithmetic",
        "major",
        "bug"
    ],
    "title": "FiniteField_prime_modn.__call__ should raise an error, rather than return an error",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6468",
    "user": "SimonKing"
}
```
Assignee: somebody

Keywords: Finite field, call

The `__call__` method of `FiniteField_prime_modn` reads like this:

```
    def __call__(self, x):
        try:
            return integer_mod.IntegerMod(self, x)
        except (NotImplementedError, PariError):
            return TypeError, "error coercing to finite field"
        except TypeError:
            if sage.interfaces.all.is_GapElement(x):
                from sage.interfaces.gap import gfq_gap_to_sage
                try:
                    return gfq_gap_to_sage(x, self)
                except (ValueError, IndexError, TypeError), msg:
                    raise TypeError, "%s\nerror coercing to finite field"%msg
            else:
                raise
```


So, in the fourth line of the function body, an error is not raised but returned.

Actually I met this when calling `GF(2)` with one of my extension types. Unfortunately I did not find anything in Sage that would trigger it as well.

Anyway, I think it should be obvious that 

```
            return TypeError, "error coercing to finite field"
```

should be changed into

```
            raise TypeError, "error coercing to finite field"
```


This is what my patch does.

Issue created by migration from https://trac.sagemath.org/ticket/6468





---

archive/issue_comments_052289.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-07-06T13:12:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6468#issuecomment-52289",
    "user": "SimonKing"
}
```

Changing status from new to assigned.



---

archive/issue_comments_052290.json:
```json
{
    "body": "Changing assignee from somebody to SimonKing.",
    "created_at": "2009-07-06T13:12:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6468#issuecomment-52290",
    "user": "SimonKing"
}
```

Changing assignee from somebody to SimonKing.



---

archive/issue_comments_052291.json:
```json
{
    "body": "REFEREE REPORT:\n\n* Put in an example in the patch that clearly illustrates that you've fixed the bug.  I.e., write some code that raises that exception, and illustrate that it is raised.  Put this in the TESTS: section of the tests.",
    "created_at": "2009-07-07T04:07:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6468#issuecomment-52291",
    "user": "was"
}
```

REFEREE REPORT:

* Put in an example in the patch that clearly illustrates that you've fixed the bug.  I.e., write some code that raises that exception, and illustrate that it is raised.  Put this in the TESTS: section of the tests.



---

archive/issue_comments_052292.json:
```json
{
    "body": "Replying to [comment:2 was]:\n> REFEREE REPORT:\n> \n> * Put in an example in the patch that clearly illustrates that you've fixed the bug.  I.e., write some code that raises that exception, and illustrate that it is raised.  Put this in the TESTS: section of the tests. \n\nI'd be happy to do so. But it turns out that it is not easy to make `integer_mod.IntegerMod(self, x)` raising a `NotImplementedError` or a `PariError`. By accident, I found that this is the case when using my extension class for describing elements of modular polynomial rings of finite p-groups. But certainly items from a to-be-created-and-at-most-optional package can't be part of a doc test...\n\nI try to cook something else up that triggers the error. But perhaps you now better how to produce a PariError?\n\nAnyway, since currently the call method has no doc test at all, it is certainly wise to create one.\n\nBest regards\n   Simon",
    "created_at": "2009-07-07T06:38:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6468#issuecomment-52292",
    "user": "SimonKing"
}
```

Replying to [comment:2 was]:
> REFEREE REPORT:
> 
> * Put in an example in the patch that clearly illustrates that you've fixed the bug.  I.e., write some code that raises that exception, and illustrate that it is raised.  Put this in the TESTS: section of the tests. 

I'd be happy to do so. But it turns out that it is not easy to make `integer_mod.IntegerMod(self, x)` raising a `NotImplementedError` or a `PariError`. By accident, I found that this is the case when using my extension class for describing elements of modular polynomial rings of finite p-groups. But certainly items from a to-be-created-and-at-most-optional package can't be part of a doc test...

I try to cook something else up that triggers the error. But perhaps you now better how to produce a PariError?

Anyway, since currently the call method has no doc test at all, it is certainly wise to create one.

Best regards
   Simon



---

archive/issue_comments_052293.json:
```json
{
    "body": "Gotcha!\n\nThe following nasty example triggers the error:\n\n```\nsage: class foo_parent(Parent):\n....:     pass\n....:\nsage: class foo(RingElement):\n....:     def lift(self):\n....:         raise PariError\n....:\nsage: P = foo_parent()\nsage: F = foo(P)\nsage: GF(2)(F)\n(<type 'exceptions.TypeError'>, 'error coercing to finite field')\n```\n\n\nI will produce a patch, adding doc tests to the call method (it is currently lacking any doc tests!), and also adding the nasty example with reference to this ticket.",
    "created_at": "2009-07-07T12:54:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6468#issuecomment-52293",
    "user": "SimonKing"
}
```

Gotcha!

The following nasty example triggers the error:

```
sage: class foo_parent(Parent):
....:     pass
....:
sage: class foo(RingElement):
....:     def lift(self):
....:         raise PariError
....:
sage: P = foo_parent()
sage: F = foo(P)
sage: GF(2)(F)
(<type 'exceptions.TypeError'>, 'error coercing to finite field')
```


I will produce a patch, adding doc tests to the call method (it is currently lacking any doc tests!), and also adding the nasty example with reference to this ticket.



---

archive/issue_comments_052294.json:
```json
{
    "body": "OK, done, there is a new patch including doc tests.",
    "created_at": "2009-07-07T13:14:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6468#issuecomment-52294",
    "user": "SimonKing"
}
```

OK, done, there is a new patch including doc tests.



---

archive/issue_comments_052295.json:
```json
{
    "body": "FiniteField.__call__ should raise an error rather than return an error",
    "created_at": "2009-07-07T13:16:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6468#issuecomment-52295",
    "user": "SimonKing"
}
```

FiniteField.__call__ should raise an error rather than return an error



---

archive/issue_comments_052296.json:
```json
{
    "body": "Attachment\n\nReplying to [comment:5 SimonKing]:\n> OK, done, there is a new patch including doc tests.\n\nPS: I did the doc tests for the patched version of sage/rings/integer_mod_ring.py, and they passed. However, as I have only sage-4.0.2, it'd be better if someone else runs the tests as well.\n\nCheers,\n  Simon",
    "created_at": "2009-07-07T13:19:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6468#issuecomment-52296",
    "user": "SimonKing"
}
```

Attachment

Replying to [comment:5 SimonKing]:
> OK, done, there is a new patch including doc tests.

PS: I did the doc tests for the patched version of sage/rings/integer_mod_ring.py, and they passed. However, as I have only sage-4.0.2, it'd be better if someone else runs the tests as well.

Cheers,
  Simon



---

archive/issue_comments_052297.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-07-11T09:13:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6468#issuecomment-52297",
    "user": "AlexGhitza"
}
```

Looks good to me.



---

archive/issue_comments_052298.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-17T08:09:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6468",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6468#issuecomment-52298",
    "user": "mvngu"
}
```

Resolution: fixed
