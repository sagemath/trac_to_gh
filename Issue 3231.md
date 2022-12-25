# Issue 3231: Use the randgen framework to set the seeds for controlled Magma, Singular, etc. sessions

archive/issues_003231.json:
```json
{
    "body": "Assignee: @williamstein\n\nIf e.g. Magma is started from Sage then the seed parameter (`-S seed`) should be set using the randgen framework maybe.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3231\n\n",
    "created_at": "2008-05-16T23:14:33Z",
    "labels": [
        "component: interfaces",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Use the randgen framework to set the seeds for controlled Magma, Singular, etc. sessions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3231",
    "user": "https://github.com/malb"
}
```
Assignee: @williamstein

If e.g. Magma is started from Sage then the seed parameter (`-S seed`) should be set using the randgen framework maybe.

Issue created by migration from https://trac.sagemath.org/ticket/3231





---

archive/issue_comments_022298.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-24T02:15:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22298",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Changing status from new to assigned.



---

archive/issue_comments_022299.json:
```json
{
    "body": "Changing assignee from @williamstein to cwitty.",
    "created_at": "2009-02-24T02:15:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22299",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Changing assignee from @williamstein to cwitty.



---

archive/issue_comments_022300.json:
```json
{
    "body": "New commits:",
    "created_at": "2015-05-25T22:53:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22300",
    "user": "https://github.com/tscholl2"
}
```

New commits:



---

archive/issue_comments_022301.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-05-26T13:46:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22301",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_022302.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-05-26T15:48:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22302",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_022303.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-05-26T15:51:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22303",
    "user": "https://github.com/tscholl2"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_022304.json:
```json
{
    "body": "I added a `set_seed` function on a lot of the interfaces such as gap, gp, magma, maxima, R, and singular. This allows setting the seed for the corresponding random number generator.\n\nThis made solving the ticket very easy by just calling \"set_seed\" when the interface is started with `_start`.\n\nI think someone should rewrite the `randstate` class to use these methods if possible. However that would require someone with more cython knowledge.\n\nAlso `set_seed` still needs to be implemented on a few more interfaces, but those are not free so they are not as easy to test with.",
    "created_at": "2015-05-26T15:55:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22304",
    "user": "https://github.com/tscholl2"
}
```

I added a `set_seed` function on a lot of the interfaces such as gap, gp, magma, maxima, R, and singular. This allows setting the seed for the corresponding random number generator.

This made solving the ticket very easy by just calling "set_seed" when the interface is started with `_start`.

I think someone should rewrite the `randstate` class to use these methods if possible. However that would require someone with more cython knowledge.

Also `set_seed` still needs to be implemented on a few more interfaces, but those are not free so they are not as easy to test with.



---

archive/issue_comments_022305.json:
```json
{
    "body": "Maybe this ticket should be repurposed then and another ticket created to realise the integration into the randgen() framework? It'd be a shame if this bitrots.",
    "created_at": "2015-05-27T09:23:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22305",
    "user": "https://github.com/malb"
}
```

Maybe this ticket should be repurposed then and another ticket created to realise the integration into the randgen() framework? It'd be a shame if this bitrots.



---

archive/issue_comments_022306.json:
```json
{
    "body": "I think this ticket is fine because it's still a step in the right direction. In my mind the best framework would be for every interface to have a `set_seed` function like these. Then `randstate` would have methods that take in an instance of an interface and set it's seed using that method. Right now there is no control over multiple instances of interfaces, which it seems like there could/should be, and it might even simplify some of the `randstate` code.\n\nAlso `randstate` would still set seeds for non-interfaces such as libraries like `libc` and `python.random` (or wrap the random calls as it does). All of the `set_seed` methods I wrote default to `interface.rand_seed` on startup which uses `randstate`, so I think this fit the description of this ticket.\n\nI think the next ticket should be specifically about `randstate` and be dependent on this one. I am worried repurposing this ticket to do both might be a bit much. Or did you have something else in mind?",
    "created_at": "2015-05-27T14:31:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22306",
    "user": "https://github.com/tscholl2"
}
```

I think this ticket is fine because it's still a step in the right direction. In my mind the best framework would be for every interface to have a `set_seed` function like these. Then `randstate` would have methods that take in an instance of an interface and set it's seed using that method. Right now there is no control over multiple instances of interfaces, which it seems like there could/should be, and it might even simplify some of the `randstate` code.

Also `randstate` would still set seeds for non-interfaces such as libraries like `libc` and `python.random` (or wrap the random calls as it does). All of the `set_seed` methods I wrote default to `interface.rand_seed` on startup which uses `randstate`, so I think this fit the description of this ticket.

I think the next ticket should be specifically about `randstate` and be dependent on this one. I am worried repurposing this ticket to do both might be a bit much. Or did you have something else in mind?



---

archive/issue_comments_022307.json:
```json
{
    "body": "I agree: let's deal with what you've done in this ticket (and change the description accordingly) and then open another follow up ticket which deals with the `randstate` business.",
    "created_at": "2015-05-28T10:23:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22307",
    "user": "https://github.com/malb"
}
```

I agree: let's deal with what you've done in this ticket (and change the description accordingly) and then open another follow up ticket which deals with the `randstate` business.



---

archive/issue_comments_022308.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-05-29T02:36:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22308",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_022309.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-05-29T02:41:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22309",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_022310.json:
```json
{
    "body": "I repurposed this ticket to match the new directions for the `randstate` class. This ticket is now focused on setting the seeds for the interfaces as the code I uploaded does for many of the interfaces.\n\nThere will be a new ticket to rewrite the `randstate` class to use these methods as well as allow for setting the seed on particular instances of interfaces. This may force a small change in the `randstate` api, but that is for the next ticket.",
    "created_at": "2015-05-29T02:54:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22310",
    "user": "https://github.com/tscholl2"
}
```

I repurposed this ticket to match the new directions for the `randstate` class. This ticket is now focused on setting the seeds for the interfaces as the code I uploaded does for many of the interfaces.

There will be a new ticket to rewrite the `randstate` class to use these methods as well as allow for setting the seed on particular instances of interfaces. This may force a small change in the `randstate` api, but that is for the next ticket.



---

archive/issue_comments_022311.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-06-12T17:28:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22311",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_022312.json:
```json
{
    "body": "In /src/sage/interfaces/interface.py the new function\n\n\n```\n+    def get_seed(self):\n+        return self._seed\n```\n\n\nlacks documentation and a doctest. The next two functions lack doctests (I know it's silly)\n\nOther than that, it looks good to me.",
    "created_at": "2015-06-12T17:28:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22312",
    "user": "https://github.com/malb"
}
```

In /src/sage/interfaces/interface.py the new function


```
+    def get_seed(self):
+        return self._seed
```


lacks documentation and a doctest. The next two functions lack doctests (I know it's silly)

Other than that, it looks good to me.



---

archive/issue_comments_022313.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-06-12T20:12:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22313",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_022314.json:
```json
{
    "body": "Woops, examples are always helpful!\n\nI added documentation and doctests to the functions in interfaces. I copied them out of octave's file, hopefully that works.",
    "created_at": "2015-06-12T20:17:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22314",
    "user": "https://github.com/tscholl2"
}
```

Woops, examples are always helpful!

I added documentation and doctests to the functions in interfaces. I copied them out of octave's file, hopefully that works.



---

archive/issue_comments_022315.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-06-12T20:17:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22315",
    "user": "https://github.com/tscholl2"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_022316.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2015-06-13T09:55:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22316",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_022317.json:
```json
{
    "body": "Why does your patch drop `set_seed` for Gap? \n\nI'd also say, if possible, then it shouldn't be tested with the Octave example: Octave is optional, e.g. Singular is not. Secondly, the closer to the actual code, the better. So if we can instantiate an `Interface` object directly that'd be best.",
    "created_at": "2015-06-13T09:55:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22317",
    "user": "https://github.com/malb"
}
```

Why does your patch drop `set_seed` for Gap? 

I'd also say, if possible, then it shouldn't be tested with the Octave example: Octave is optional, e.g. Singular is not. Secondly, the closer to the actual code, the better. So if we can instantiate an `Interface` object directly that'd be best.



---

archive/issue_comments_022318.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-06-13T14:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22318",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_022319.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-06-13T14:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22319",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_022320.json:
```json
{
    "body": "There was actually two `set_seed` for Gap. The file was long and I accidentally copied another to a slightly different place. You can still see the actual `set_seed` function under the total diff.\n\nThese new pushes change the doc tests in `interface.py` to use Singular (so less optional packages) and also use an instance of `Interface` directly. This is ok for `rand_seed` and `get_seed` but not for `set_seed` as that has to be implemented by the specific interface. Do you think we need a doc test which raises the `NotImplementedError`?",
    "created_at": "2015-06-13T14:32:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22320",
    "user": "https://github.com/tscholl2"
}
```

There was actually two `set_seed` for Gap. The file was long and I accidentally copied another to a slightly different place. You can still see the actual `set_seed` function under the total diff.

These new pushes change the doc tests in `interface.py` to use Singular (so less optional packages) and also use an instance of `Interface` directly. This is ok for `rand_seed` and `get_seed` but not for `set_seed` as that has to be implemented by the specific interface. Do you think we need a doc test which raises the `NotImplementedError`?



---

archive/issue_comments_022321.json:
```json
{
    "body": "Changing status from needs_info to positive_review.",
    "created_at": "2015-06-15T07:31:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22321",
    "user": "https://github.com/malb"
}
```

Changing status from needs_info to positive_review.



---

archive/issue_comments_022322.json:
```json
{
    "body": "Looks good to me. \n\nI guess technically we should actually doctest a `NotImplementedError` but I'll leave it up to you.",
    "created_at": "2015-06-15T07:31:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22322",
    "user": "https://github.com/malb"
}
```

Looks good to me. 

I guess technically we should actually doctest a `NotImplementedError` but I'll leave it up to you.



---

archive/issue_comments_022323.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:",
    "created_at": "2015-06-15T15:07:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22323",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. New commits:



---

archive/issue_comments_022324.json:
```json
{
    "body": "Changing status from positive_review to needs_review.",
    "created_at": "2015-06-15T15:07:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22324",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Changing status from positive_review to needs_review.



---

archive/issue_comments_022325.json:
```json
{
    "body": "I added a doc test for the `set_seed` method for the general interface. It was easy to add.",
    "created_at": "2015-06-15T15:08:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22325",
    "user": "https://github.com/tscholl2"
}
```

I added a doc test for the `set_seed` method for the general interface. It was easy to add.



---

archive/issue_comments_022326.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-06-15T16:36:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22326",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_022327.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2015-06-15T16:36:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22327",
    "user": "https://github.com/malb"
}
```

Looks good to me.



---

archive/issue_comments_022328.json:
```json
{
    "body": "\n```\nsage -t --long src/sage/interfaces/magma.py  # 2 doctests failed\nsage -t --long src/sage/interfaces/octave.py  # 2 doctests failed\nsage -t --long src/sage/interfaces/scilab.py  # 2 doctests failed\nsage -t --long src/sage/repl/interpreter.py  # 1 doctest failed\n```\n",
    "created_at": "2015-06-15T20:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22328",
    "user": "https://github.com/vbraun"
}
```


```
sage -t --long src/sage/interfaces/magma.py  # 2 doctests failed
sage -t --long src/sage/interfaces/octave.py  # 2 doctests failed
sage -t --long src/sage/interfaces/scilab.py  # 2 doctests failed
sage -t --long src/sage/repl/interpreter.py  # 1 doctest failed
```




---

archive/issue_comments_022329.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2015-06-15T20:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22329",
    "user": "https://github.com/vbraun"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_022330.json:
```json
{
    "body": "I get the first 3 errors if I run `sage -t --long src/sage/interfaces/magma.py` but not if I run `./sage -t --long src/sage/interfaces/magma.py`. Shouldn't I only be checking if it runs with the version of Sage on the branch and not the user's systems' version?\n\nThe last error seems to be something I didn't notice. Apparently some of the interfaces keep a counter of the commands used and label things with it. The `set_seed` function for some interfaces raises this counter because it needs to call a command in the interface. So running the test in `src/sage/repl/interpreter.py` the counter is off from what it used to be.\n\nThis error doesn't occur if I comment out line 626 in `src/sage/interfaces/maxima.py`:\n\n```\n625 # set random seed\n626 self.set_seed(self._seed)\n```\n\n\nI'm not sure what to do about this. It seems like there is a few options:\n\n* We could reset the counter after the `set_seed` function is called (I actually don't know if this is possible yet).\n* We could change all the doc tests in functions which use this counter and increment it manually.\n* We could not run `set_seed` on start and leave it up to the user to run it.\n\nMartin, do you have any suggestions on which way to proceed?",
    "created_at": "2015-06-17T02:54:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22330",
    "user": "https://github.com/tscholl2"
}
```

I get the first 3 errors if I run `sage -t --long src/sage/interfaces/magma.py` but not if I run `./sage -t --long src/sage/interfaces/magma.py`. Shouldn't I only be checking if it runs with the version of Sage on the branch and not the user's systems' version?

The last error seems to be something I didn't notice. Apparently some of the interfaces keep a counter of the commands used and label things with it. The `set_seed` function for some interfaces raises this counter because it needs to call a command in the interface. So running the test in `src/sage/repl/interpreter.py` the counter is off from what it used to be.

This error doesn't occur if I comment out line 626 in `src/sage/interfaces/maxima.py`:

```
625 # set random seed
626 self.set_seed(self._seed)
```


I'm not sure what to do about this. It seems like there is a few options:

* We could reset the counter after the `set_seed` function is called (I actually don't know if this is possible yet).
* We could change all the doc tests in functions which use this counter and increment it manually.
* We could not run `set_seed` on start and leave it up to the user to run it.

Martin, do you have any suggestions on which way to proceed?



---

archive/issue_comments_022331.json:
```json
{
    "body": "Ah, crap my comments from yesterday seem not to have arrived:\n\n- You are not seeing these errors because you have octave et al. installed in your local development environment. In other words: some doctests are not marked optional but you should be marked optional. \n\n- I'd just update the doctest, `set_seed()` is a proper call, so no point in resetting the counter.",
    "created_at": "2015-06-18T14:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22331",
    "user": "https://github.com/malb"
}
```

Ah, crap my comments from yesterday seem not to have arrived:

- You are not seeing these errors because you have octave et al. installed in your local development environment. In other words: some doctests are not marked optional but you should be marked optional. 

- I'd just update the doctest, `set_seed()` is a proper call, so no point in resetting the counter.



---

archive/issue_comments_022332.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-06-18T16:10:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22332",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_022333.json:
```json
{
    "body": "I added `# optional -` tags to the corresponding doc tests. I think I got all of them, but someone should check. Strangely enough, this also fixed the other test `sage -t --long src/sage/repl/interpreter.py`. Which may mean that either it wasn't actually counting the calls to the interpreter, or something else happened with the optional flags which affected it.",
    "created_at": "2015-06-18T18:32:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22333",
    "user": "https://github.com/tscholl2"
}
```

I added `# optional -` tags to the corresponding doc tests. I think I got all of them, but someone should check. Strangely enough, this also fixed the other test `sage -t --long src/sage/repl/interpreter.py`. Which may mean that either it wasn't actually counting the calls to the interpreter, or something else happened with the optional flags which affected it.



---

archive/issue_comments_022334.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-06-18T18:32:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22334",
    "user": "https://github.com/tscholl2"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_022335.json:
```json
{
    "body": "I still get \n\n\n```\nsage -t --warn-long 33.6 src/sage/repl/interpreter.py  # 1 doctest failed\n**********************************************************************\nFile \"src/sage/repl/interpreter.py\", line 561, in sage.repl.interpreter.InterfaceShellTransformer.preparse_imports_from_sage\nFailed example:\n    ift.preparse_imports_from_sage('2 + maxima(a)')\nExpected:\n    '2 +  sage1 '\nGot:\n    '2 +  sage4 '\n```\n\n\nbut the other three are gone.",
    "created_at": "2015-06-19T08:10:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22335",
    "user": "https://github.com/malb"
}
```

I still get 


```
sage -t --warn-long 33.6 src/sage/repl/interpreter.py  # 1 doctest failed
**********************************************************************
File "src/sage/repl/interpreter.py", line 561, in sage.repl.interpreter.InterfaceShellTransformer.preparse_imports_from_sage
Failed example:
    ift.preparse_imports_from_sage('2 + maxima(a)')
Expected:
    '2 +  sage1 '
Got:
    '2 +  sage4 '
```


but the other three are gone.



---

archive/issue_comments_022336.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-06-19T08:10:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22336",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_022337.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-06-21T17:47:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22337",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_022338.json:
```json
{
    "body": "I removed some white space and changed a doctest in `src/sage/repl/interpreter.py`.\n\nThe doc test was failing because `maxima` now calls `set_seed` on startup which uses several calls to the maxima interpreter. Therefore instead of getting back `2 +  sage1`, it should get back `2 + sage4`.",
    "created_at": "2015-06-21T17:54:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22338",
    "user": "https://github.com/tscholl2"
}
```

I removed some white space and changed a doctest in `src/sage/repl/interpreter.py`.

The doc test was failing because `maxima` now calls `set_seed` on startup which uses several calls to the maxima interpreter. Therefore instead of getting back `2 +  sage1`, it should get back `2 + sage4`.



---

archive/issue_comments_022339.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-06-21T17:54:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22339",
    "user": "https://github.com/tscholl2"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_022340.json:
```json
{
    "body": "tests pass here & looks good.",
    "created_at": "2015-06-22T13:09:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22340",
    "user": "https://github.com/malb"
}
```

tests pass here & looks good.



---

archive/issue_comments_022341.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-06-22T13:09:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22341",
    "user": "https://github.com/malb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_003450.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-06-22T22:25:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3231#event-3450"
}
```



---

archive/issue_comments_022342.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-06-22T22:25:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3231",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3231#issuecomment-22342",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
