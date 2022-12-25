# Issue 5318: [with patch, positive review] ideas for improving random testers (like #4779)

archive/issues_005318.json:
```json
{
    "body": "Assignee: mabshoff\n\nRandom testers (like the ones in #4779) should have a structure something like this (untested):\n\n```\ndef test_foo(n_trials, seed=None, verbose=False):\n  with random_seed(seed):\n    used_seed = initial_seed()\n    try:\n        for i in range(n_trials): # or whatever\n            ... do test\n            ... if verbose, then print out the details of the\n                test you're running\n    except:\n        print \"We've detected a failure in random testing.\"\n        print \"Please report this bug; you may be the only person\"\n        print \"in the world to see this particular problem!\"\n        print \"initial seed: \" + used_seed\n        print \"trial: \" + i\n        raise\n```\n\nThen the doctests should start with:\n\n```\nsage: test_foo(2, seed=0, verbose=True)\n... verbose output from two tests; should always be the same across machines, etc.\n```\nto verify that the test is correctly using the randstate framework, so that failures can be reproduced.\n\nThen you can continue to:\n\n```\nsage: test_foo(10)\nsage: test_foo(100) # long time\n```\nwhich will use truly random seeds (with /dev/urandom).\n\nThe above should be adjusted if you want to run the testing function for a very long time; you would want to re-initialize the random seed at least every few seconds, so that if you detect a problem after running for several hours, you don't have to run for the same several hours to reproduce it.\n\nThe simplest way is not to loop for long inside the function; instead, do:\n\n```\nwhile True:\n    test_foo(100)\n```\n\n(That's a lot of boilerplate; maybe this whole setup can be encapsulated in a decorator?)\n\nIssue created by migration from https://trac.sagemath.org/ticket/5318\n\n",
    "closed_at": "2009-04-01T01:54:30Z",
    "created_at": "2009-02-20T07:51:47Z",
    "labels": [
        "component: doctest coverage"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "[with patch, positive review] ideas for improving random testers (like #4779)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5318",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: mabshoff

Random testers (like the ones in #4779) should have a structure something like this (untested):

```
def test_foo(n_trials, seed=None, verbose=False):
  with random_seed(seed):
    used_seed = initial_seed()
    try:
        for i in range(n_trials): # or whatever
            ... do test
            ... if verbose, then print out the details of the
                test you're running
    except:
        print "We've detected a failure in random testing."
        print "Please report this bug; you may be the only person"
        print "in the world to see this particular problem!"
        print "initial seed: " + used_seed
        print "trial: " + i
        raise
```

Then the doctests should start with:

```
sage: test_foo(2, seed=0, verbose=True)
... verbose output from two tests; should always be the same across machines, etc.
```
to verify that the test is correctly using the randstate framework, so that failures can be reproduced.

Then you can continue to:

```
sage: test_foo(10)
sage: test_foo(100) # long time
```
which will use truly random seeds (with /dev/urandom).

The above should be adjusted if you want to run the testing function for a very long time; you would want to re-initialize the random seed at least every few seconds, so that if you detect a problem after running for several hours, you don't have to run for the same several hours to reproduce it.

The simplest way is not to loop for long inside the function; instead, do:

```
while True:
    test_foo(100)
```

(That's a lot of boilerplate; maybe this whole setup can be encapsulated in a decorator?)

Issue created by migration from https://trac.sagemath.org/ticket/5318





---

archive/issue_comments_040872.json:
```json
{
    "body": "I've attached a patch implementing the above ideas as a decorator, and adapted the random testers from #4779 to use this decorator.\n\nI'm changing the milestone to Sage 3.3.  I don't actually expect to get this patch into 3.3, and I'm happy to rebase it if it doesn't make it; but I didn't want to rule out the possibility :)",
    "created_at": "2009-02-21T03:05:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5318",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5318#issuecomment-40872",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

I've attached a patch implementing the above ideas as a decorator, and adapted the random testers from #4779 to use this decorator.

I'm changing the milestone to Sage 3.3.  I don't actually expect to get this patch into 3.3, and I'm happy to rebase it if it doesn't make it; but I didn't want to rule out the possibility :)



---

archive/issue_events_012390.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/cwitty",
    "created_at": "2009-02-21T03:05:45Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5318",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5318#event-12390"
}
```



---

archive/issue_events_012391.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-21T05:05:43Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5318",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5318#event-12391"
}
```



---

archive/issue_events_012392.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-21T05:05:43Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5318",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5318#event-12392"
}
```



---

archive/issue_comments_040873.json:
```json
{
    "body": "Hi!\n\nCool stuff. I am about to give it a thumb up!\n\nThree comments:\n- When the category stuff will be in there, we should merge this into the category-held tests.\n  But let's not wait for that.\n\n- The code is not trivially small, so I would put it in a separate file with the same name as the decorator\n\n-  while we are at saving on boiler plate: would it be possible for the wrapper\n   to also handle the iteration loop?\n\n  One nice side benefit is that the wrapper would be aware of the value of the seed at the begining of each iteration, and therefore could report it in case of trouble (I have not yet played with random generators in python, but I assume that we can access the current value of the seed after a couple random generation). Reproducing  the error would then involve a single iteration.",
    "created_at": "2009-03-18T08:41:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5318",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5318#issuecomment-40873",
    "user": "https://github.com/nthiery"
}
```

Hi!

Cool stuff. I am about to give it a thumb up!

Three comments:
- When the category stuff will be in there, we should merge this into the category-held tests.
  But let's not wait for that.

- The code is not trivially small, so I would put it in a separate file with the same name as the decorator

-  while we are at saving on boiler plate: would it be possible for the wrapper
   to also handle the iteration loop?

  One nice side benefit is that the wrapper would be aware of the value of the seed at the begining of each iteration, and therefore could report it in case of trouble (I have not yet played with random generators in python, but I assume that we can access the current value of the seed after a couple random generation). Reproducing  the error would then involve a single iteration.



---

archive/issue_comments_040874.json:
```json
{
    "body": "*the code is not trivially small*\n\nActually, it is; random_testing is 26 lines of code by my count, ignoring docstrings and comments :)\n\nBut yes, once you include the tests, the documentation, and the comments, it does look pretty big.  I'll move it into its own file.\n\nI'm not sure what to do about the iteration loop idea.  I wouldn't want iteration to be always handled in the wrapper; for example, that could vastly slow down testing if the tester were written in Cython, or if the testing function needed to do some non-trivial setup before starting the loop.  And there's no good way to tell the wrapper whether the wrapper or the wrappee should handle iteration (it could key off the argument name, but that doesn't sound like a good way).\n\nAlso, unfortunately, the primary source of random numbers in Sage (GMP's Mersenne Twister implementation) doesn't let you read back the current state.",
    "created_at": "2009-03-18T15:27:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5318",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5318#issuecomment-40874",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

*the code is not trivially small*

Actually, it is; random_testing is 26 lines of code by my count, ignoring docstrings and comments :)

But yes, once you include the tests, the documentation, and the comments, it does look pretty big.  I'll move it into its own file.

I'm not sure what to do about the iteration loop idea.  I wouldn't want iteration to be always handled in the wrapper; for example, that could vastly slow down testing if the tester were written in Cython, or if the testing function needed to do some non-trivial setup before starting the loop.  And there's no good way to tell the wrapper whether the wrapper or the wrappee should handle iteration (it could key off the argument name, but that doesn't sound like a good way).

Also, unfortunately, the primary source of random numbers in Sage (GMP's Mersenne Twister implementation) doesn't let you read back the current state.



---

archive/issue_comments_040875.json:
```json
{
    "body": "Attachment [trac5318-random-testing.patch](tarball://root/attachments/some-uuid/ticket5318/trac5318-random-testing.patch) by cwitty created at 2009-03-21 04:25:18\n\nI posted a new patch (and deleted the old version) that moves `@`random_testing into its own file (and adds it to the reference manual).  I didn't implement the other requested feature, of providing an iteration loop, for the reasons mentioned in my previous comment.",
    "created_at": "2009-03-21T04:25:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5318",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5318#issuecomment-40875",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [trac5318-random-testing.patch](tarball://root/attachments/some-uuid/ticket5318/trac5318-random-testing.patch) by cwitty created at 2009-03-21 04:25:18

I posted a new patch (and deleted the old version) that moves `@`random_testing into its own file (and adds it to the reference manual).  I didn't implement the other requested feature, of providing an iteration loop, for the reasons mentioned in my previous comment.



---

archive/issue_comments_040876.json:
```json
{
    "body": "See #5647 for a follow up.",
    "created_at": "2009-03-31T03:27:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5318",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5318#issuecomment-40876",
    "user": "https://github.com/nthiery"
}
```

See #5647 for a follow up.



---

archive/issue_comments_040877.json:
```json
{
    "body": "Merged in Sage 3.4.1.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-01T01:54:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5318",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5318#issuecomment-40877",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.1.rc0.

Cheers,

Michael



---

archive/issue_comments_040878.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-01T01:54:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5318",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5318#issuecomment-40878",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_012393.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-01T01:54:30Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5318",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5318#event-12393"
}
```



---

archive/issue_events_012394.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-01T01:54:30Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5318",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5318#event-12394"
}
```



---

archive/issue_events_012395.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-04-01T01:54:30Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5318",
    "milestone": "sage-3.4.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5318#event-12395"
}
```
