# Issue 9225: Indicate progress and elapsed time when running multiple doctests

archive/issues_009225.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @wjp @nexttime @rbeezer\n\nWhen we doctest several files in parallel or in sequence, it might be helpful to print stats relating to the test suite's progress, e.g.,\n\n```sh\n$ sage -t monoids/\nsage -t  \"monoids/monoid.py\"\n 1/10    1.9 s / 1.9 s\nsage -t  \"monoids/free_monoid.py\"\n 2/10    2.0 s / 3.9 s\n[...]\n```\n\nWhat other columns would be useful?  Coverage?\n\nIssue created by migration from https://trac.sagemath.org/ticket/9225\n\n",
    "created_at": "2010-06-12T10:18:49Z",
    "labels": [
        "component: doctest coverage",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Indicate progress and elapsed time when running multiple doctests",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9225",
    "user": "https://github.com/qed777"
}
```
Assignee: mvngu

CC:  @wjp @nexttime @rbeezer

When we doctest several files in parallel or in sequence, it might be helpful to print stats relating to the test suite's progress, e.g.,

```sh
$ sage -t monoids/
sage -t  "monoids/monoid.py"
 1/10    1.9 s / 1.9 s
sage -t  "monoids/free_monoid.py"
 2/10    2.0 s / 3.9 s
[...]
```

What other columns would be useful?  Coverage?

Issue created by migration from https://trac.sagemath.org/ticket/9225





---

archive/issue_comments_086413.json:
```json
{
    "body": "If we widen the scope here a bit:  We should use [optparse](http://docs.python.org/library/optparse.html), at least, to handle command-line arguments.",
    "created_at": "2010-07-07T06:47:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9225#issuecomment-86413",
    "user": "https://github.com/qed777"
}
```

If we widen the scope here a bit:  We should use [optparse](http://docs.python.org/library/optparse.html), at least, to handle command-line arguments.



---

archive/issue_comments_086414.json:
```json
{
    "body": "Other possibilities, probably mentioned before and probably for other tickets:\n\n* \"Librarify:\" Make it possible to doctest files and objects from the Sage command-line or notebook, e.g.,\n\n```python\nsage: doctest('file.sage', long=True, optional=['axiom', 'magma'])\nsage: doctest(os.path.join(SAGE_ROOT, 'devel', 'sage', 'sage', 'monoids'), processes=4)\nsage: stats = {}     # Collect errors, counts, timings, etc.\nsage: doctest(['foo.py', 'bar.pyx'], stats=stats)\nsage: def f():\n....:     \"\"\"\n....:     sage: f()\n....:     1\n....:     \"\"\"\n....:     return 1\n....: \nsage: doctest(f)\n```\n\n\n* Doctest the doctesting framework!  I think we could include [comment:ticket:9449:13 this example], at least.\n\n* An option to run an individual `file.py`'s \"examples\" (i.e., the files `example_*` functions) in parallel.",
    "created_at": "2010-07-09T00:33:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9225#issuecomment-86414",
    "user": "https://github.com/qed777"
}
```

Other possibilities, probably mentioned before and probably for other tickets:

* "Librarify:" Make it possible to doctest files and objects from the Sage command-line or notebook, e.g.,

```python
sage: doctest('file.sage', long=True, optional=['axiom', 'magma'])
sage: doctest(os.path.join(SAGE_ROOT, 'devel', 'sage', 'sage', 'monoids'), processes=4)
sage: stats = {}     # Collect errors, counts, timings, etc.
sage: doctest(['foo.py', 'bar.pyx'], stats=stats)
sage: def f():
....:     """
....:     sage: f()
....:     1
....:     """
....:     return 1
....: 
sage: doctest(f)
```


* Doctest the doctesting framework!  I think we could include [comment:ticket:9449:13 this example], at least.

* An option to run an individual `file.py`'s "examples" (i.e., the files `example_*` functions) in parallel.



---

archive/issue_comments_086415.json:
```json
{
    "body": "A way to upload anonymized test stats and system information to a remote server?",
    "created_at": "2010-07-15T07:23:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9225#issuecomment-86415",
    "user": "https://github.com/qed777"
}
```

A way to upload anonymized test stats and system information to a remote server?



---

archive/issue_comments_086416.json:
```json
{
    "body": "Also potentially useful: doctesting the same file multiple times in parallel.  I think this is just a matter of generating in `sage-doctest` a unique name, e.g., `.doctest_foo-R3X87S.py` for each run on `foo.py`.",
    "created_at": "2010-08-08T08:44:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9225#issuecomment-86416",
    "user": "https://github.com/qed777"
}
```

Also potentially useful: doctesting the same file multiple times in parallel.  I think this is just a matter of generating in `sage-doctest` a unique name, e.g., `.doctest_foo-R3X87S.py` for each run on `foo.py`.



---

archive/issue_comments_086417.json:
```json
{
    "body": "I have a suspicion that some doctests fail when the system is under heavy load. It would be good if the one-minute and perhaps 5 minute load average could be recorded with any failures, along with the dates and time as I mentioned before.",
    "created_at": "2010-08-27T11:46:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9225#issuecomment-86417",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I have a suspicion that some doctests fail when the system is under heavy load. It would be good if the one-minute and perhaps 5 minute load average could be recorded with any failures, along with the dates and time as I mentioned before.



---

archive/issue_comments_086418.json:
```json
{
    "body": "Replying to [comment:5 mpatel]:\n> A way to upload anonymized test stats and system information to a remote server?\nYes, but with the option of giving a name if one wishes to. It will make problems easier to manage if people did give a name + email, but certainly make it optional.",
    "created_at": "2010-08-27T11:48:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9225#issuecomment-86418",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:5 mpatel]:
> A way to upload anonymized test stats and system information to a remote server?
Yes, but with the option of giving a name if one wishes to. It will make problems easier to manage if people did give a name + email, but certainly make it optional.



---

archive/issue_comments_086419.json:
```json
{
    "body": "Replying to [comment:6 mpatel]:\n> Also potentially useful: doctesting the same file multiple times in parallel.  I think this is just a matter of generating in `sage-doctest` a unique name, e.g., `.doctest_foo-R3X87S.py` for each run on `foo.py`.\n\nThis is #9739.",
    "created_at": "2010-08-27T22:25:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9225#issuecomment-86419",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:6 mpatel]:
> Also potentially useful: doctesting the same file multiple times in parallel.  I think this is just a matter of generating in `sage-doctest` a unique name, e.g., `.doctest_foo-R3X87S.py` for each run on `foo.py`.

This is #9739.



---

archive/issue_comments_086420.json:
```json
{
    "body": "Replying to [comment:2 mpatel]:\n> If we widen the scope here a bit:  We should use [optparse](http://docs.python.org/library/optparse.html), at least, to handle command-line arguments.\nThough if you look at that link, it says its been depreciated in favor of `argparse`. \n\nDave",
    "created_at": "2010-08-27T22:32:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9225#issuecomment-86420",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:2 mpatel]:
> If we widen the scope here a bit:  We should use [optparse](http://docs.python.org/library/optparse.html), at least, to handle command-line arguments.
Though if you look at that link, it says its been depreciated in favor of `argparse`. 

Dave



---

archive/issue_comments_086421.json:
```json
{
    "body": "Replying to [comment:11 drkirkby]:\n> Replying to [comment:2 mpatel]:\n> > If we widen the scope here a bit:  We should use [optparse](http://docs.python.org/library/optparse.html), at least, to handle command-line arguments.\n> Though if you look at that link, it says its been depreciated in favor of `argparse`. \n\nThat's why I inserted \"at least,\" but I should have more specific.  We'll need to upgrade to Python 2.7 to use [argparse](http://docs.python.org/library/argparse.html#module-argparse) readily.  [argparse](http://code.google.com/p/argparse/) used to be an independent project.",
    "created_at": "2010-08-28T00:44:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9225#issuecomment-86421",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:11 drkirkby]:
> Replying to [comment:2 mpatel]:
> > If we widen the scope here a bit:  We should use [optparse](http://docs.python.org/library/optparse.html), at least, to handle command-line arguments.
> Though if you look at that link, it says its been depreciated in favor of `argparse`. 

That's why I inserted "at least," but I should have more specific.  We'll need to upgrade to Python 2.7 to use [argparse](http://docs.python.org/library/argparse.html#module-argparse) readily.  [argparse](http://code.google.com/p/argparse/) used to be an independent project.



---

archive/issue_comments_086422.json:
```json
{
    "body": "Rob, perhaps you could state your personal wishes here, too.\n\n(E.g. `./sage -testall ...` with an option to specify the number of threads IIRC rather than always doing that serially.)",
    "created_at": "2010-12-16T02:40:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9225#issuecomment-86422",
    "user": "https://github.com/nexttime"
}
```

Rob, perhaps you could state your personal wishes here, too.

(E.g. `./sage -testall ...` with an option to specify the number of threads IIRC rather than always doing that serially.)



---

archive/issue_comments_086423.json:
```json
{
    "body": "#10458 improves cut & paste of doctest code & output from an actual Sage session, in that it allows also \"`....: `\" for line continuations. (Previously, for some reason only \"`...`\" was supported in docstrings; also the confusion with an ellipsis intended to mean arbitrary **output** should be reduced by this ticket.)\n\nAnother problem still has to be addressed: The original (non-preparsed) source code of continuation lines gets \"lost\", i.e. doesn't end up in the end-of-line comments of the generated test files (`.doctest_*`) as it does for ordinary lines, hence also won't be shown on doctest errors or when one doctests in verbose mode.",
    "created_at": "2010-12-16T03:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9225#issuecomment-86423",
    "user": "https://github.com/nexttime"
}
```

#10458 improves cut & paste of doctest code & output from an actual Sage session, in that it allows also "`....: `" for line continuations. (Previously, for some reason only "`...`" was supported in docstrings; also the confusion with an ellipsis intended to mean arbitrary **output** should be reduced by this ticket.)

Another problem still has to be addressed: The original (non-preparsed) source code of continuation lines gets "lost", i.e. doesn't end up in the end-of-line comments of the generated test files (`.doctest_*`) as it does for ordinary lines, hence also won't be shown on doctest errors or when one doctests in verbose mode.



---

archive/issue_comments_086424.json:
```json
{
    "body": "#12415 will add many of these features.",
    "created_at": "2012-02-06T05:22:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9225#issuecomment-86424",
    "user": "https://github.com/roed314"
}
```

#12415 will add many of these features.



---

archive/issue_comments_086425.json:
```json
{
    "body": "As David mentioned, there is a lot of work at #12415. And apart from that, this ticket is extremely vague.",
    "created_at": "2013-02-28T16:09:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9225#issuecomment-86425",
    "user": "https://github.com/jdemeyer"
}
```

As David mentioned, there is a lot of work at #12415. And apart from that, this ticket is extremely vague.



---

archive/issue_comments_086426.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-02-28T16:09:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9225#issuecomment-86426",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_086427.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2013-02-28T16:10:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9225#issuecomment-86427",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_009383.json:
```json
{
    "actor": "@jdemeyer",
    "created_at": "2013-03-07T08:18:34Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9225",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9225#event-9383"
}
```



---

archive/issue_comments_086428.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2013-03-07T08:18:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9225",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9225#issuecomment-86428",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: invalid
