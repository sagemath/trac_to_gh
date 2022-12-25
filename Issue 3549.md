# Issue 3549: change pari (and sage) so that one can add to the list of precomputed primes that are used for trial division

archive/issues_003549.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  @jdemeyer\n\nThis is a very very useful unique feature that magma has.  We need to change pari so it can do it to and add an interface so sage can use that function.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3549\n\n",
    "created_at": "2008-07-04T04:22:14Z",
    "labels": [
        "component: number theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "change pari (and sage) so that one can add to the list of precomputed primes that are used for trial division",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3549",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

CC:  @jdemeyer

This is a very very useful unique feature that magma has.  We need to change pari so it can do it to and add an interface so sage can use that function.

Issue created by migration from https://trac.sagemath.org/ticket/3549





---

archive/issue_comments_025052.json:
```json
{
    "body": "Pari can already do this; it's the \"addprimes\" function.",
    "created_at": "2008-07-10T01:20:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3549#issuecomment-25052",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Pari can already do this; it's the "addprimes" function.



---

archive/issue_comments_025053.json:
```json
{
    "body": "Changing component from number theory to interfaces.",
    "created_at": "2010-08-01T15:32:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3549#issuecomment-25053",
    "user": "https://github.com/jdemeyer"
}
```

Changing component from number theory to interfaces.



---

archive/issue_comments_025054.json:
```json
{
    "body": "The `addprimes` function is currently available via automatic import:\n\n```\nsage: pari([3, 7]).addprimes()\n[3 ,7]\n```\n\nIf this is sufficient, then I would propose to close this ticket as invalid.\n\nA more proactive alternative would be to add a wrapper function somewhere, maybe `sage.rings.fast_arith` where things like `prime_range` live.",
    "created_at": "2016-04-09T23:22:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3549",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3549#issuecomment-25054",
    "user": "https://github.com/kedlaya"
}
```

The `addprimes` function is currently available via automatic import:

```
sage: pari([3, 7]).addprimes()
[3 ,7]
```

If this is sufficient, then I would propose to close this ticket as invalid.

A more proactive alternative would be to add a wrapper function somewhere, maybe `sage.rings.fast_arith` where things like `prime_range` live.
