# Issue 7776: Implements sage.misc.misc.inject_variable(name, value)

archive/issues_007776.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  sage-combinat\n\nFrom the doc:\n\n    inject a variable into the main global namespace\n\n    INPUT:\n- name  - a string\n- value - anything\n\n    EXAMPLES::\n\n        sage: from sage.misc.misc import inject_variable\n        sage: inject_variable(\"a\", 314)\n        sage: a\n        314\n\nThis will be used in the upcoming \"inject_shorthands\" patch for symmetric functions, and could be used in the various inject_variable code instead of manipulating directly globals() (which could be incorrect if not called directly from the interpreter/notebook.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7776\n\n",
    "created_at": "2009-12-27T22:27:38Z",
    "labels": [
        "component: user interface"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "Implements sage.misc.misc.inject_variable(name, value)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7776",
    "user": "https://github.com/nthiery"
}
```
Assignee: @williamstein

CC:  sage-combinat

From the doc:

    inject a variable into the main global namespace

    INPUT:
- name  - a string
- value - anything

    EXAMPLES::

        sage: from sage.misc.misc import inject_variable
        sage: inject_variable("a", 314)
        sage: a
        314

This will be used in the upcoming "inject_shorthands" patch for symmetric functions, and could be used in the various inject_variable code instead of manipulating directly globals() (which could be incorrect if not called directly from the interpreter/notebook.

Issue created by migration from https://trac.sagemath.org/ticket/7776





---

archive/issue_comments_066925.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-27T22:34:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7776#issuecomment-66925",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066926.json:
```json
{
    "body": "(note: patch prepared and tested on 4.2 not 4.3)",
    "created_at": "2009-12-27T22:35:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7776#issuecomment-66926",
    "user": "https://github.com/nthiery"
}
```

(note: patch prepared and tested on 4.2 not 4.3)



---

archive/issue_comments_066927.json:
```json
{
    "body": "I'd rather it looked for `__name__ == '__main__'` than `wiki_create_instance`.",
    "created_at": "2009-12-30T09:13:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7776#issuecomment-66927",
    "user": "https://github.com/robertwb"
}
```

I'd rather it looked for `__name__ == '__main__'` than `wiki_create_instance`.



---

archive/issue_comments_066928.json:
```json
{
    "body": "Attachment [trac_7776-inject_variable-nt.patch](tarball://root/attachments/some-uuid/ticket7776/trac_7776-inject_variable-nt.patch) by @nthiery created at 2010-01-03 16:15:15",
    "created_at": "2010-01-03T16:15:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7776#issuecomment-66928",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_7776-inject_variable-nt.patch](tarball://root/attachments/some-uuid/ticket7776/trac_7776-inject_variable-nt.patch) by @nthiery created at 2010-01-03 16:15:15



---

archive/issue_comments_066929.json:
```json
{
    "body": "Replying to [comment:3 robertwb]:\n> I'd rather it looked for `__name__ == '__main__'` than `wiki_create_instance`.\n\nAh, excellent, that sure is the right way for doing this. I had missed this __name__ thing. \n\nThanks for the suggestion! Patch updated.",
    "created_at": "2010-01-03T16:17:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7776#issuecomment-66929",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:3 robertwb]:
> I'd rather it looked for `__name__ == '__main__'` than `wiki_create_instance`.

Ah, excellent, that sure is the right way for doing this. I had missed this __name__ thing. 

Thanks for the suggestion! Patch updated.



---

archive/issue_comments_066930.json:
```json
{
    "body": "This looks good to me.",
    "created_at": "2010-01-13T23:51:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7776#issuecomment-66930",
    "user": "https://github.com/mwhansen"
}
```

This looks good to me.



---

archive/issue_comments_066931.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-01-13T23:51:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7776#issuecomment-66931",
    "user": "https://github.com/mwhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_066932.json:
```json
{
    "body": "If I do\n\n```\nsage: inject_variable(3, 34)  # pass a non-string to inject_variable, which I probably shouldn't do\n```\n\nthen tab-completion is broken.  This is odd, and a little alarming.  Since this function isn't meant for casual users, maybe this isn't a big deal, but otherwise, perhaps we should check that the first argument is a string.\n\nHere's another question:\n\n```\nsage: from sage.misc.misc import inject_variable\nsage: inject_variable('a', 23)\nsage: inject_variable('a', 26)\n/Applications/sage/local/bin/sage-ipython:1: RuntimeWarning: redefining global value `a`\n  #!/usr/bin/env python\nsage: inject_variable('a', 29)\nsage: inject_variable('a', 33)\n```\n\nWhy is the warning only printed the first time?  Is that just the nature of these warnings?",
    "created_at": "2010-01-13T23:54:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7776#issuecomment-66932",
    "user": "https://github.com/jhpalmieri"
}
```

If I do

```
sage: inject_variable(3, 34)  # pass a non-string to inject_variable, which I probably shouldn't do
```

then tab-completion is broken.  This is odd, and a little alarming.  Since this function isn't meant for casual users, maybe this isn't a big deal, but otherwise, perhaps we should check that the first argument is a string.

Here's another question:

```
sage: from sage.misc.misc import inject_variable
sage: inject_variable('a', 23)
sage: inject_variable('a', 26)
/Applications/sage/local/bin/sage-ipython:1: RuntimeWarning: redefining global value `a`
  #!/usr/bin/env python
sage: inject_variable('a', 29)
sage: inject_variable('a', 33)
```

Why is the warning only printed the first time?  Is that just the nature of these warnings?



---

archive/issue_comments_066933.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-14T01:34:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7776#issuecomment-66933",
    "user": "https://github.com/rlmill"
}
```

Resolution: fixed



---

archive/issue_events_018603.json:
```json
{
    "actor": "https://github.com/rlmill",
    "created_at": "2010-01-14T01:34:18Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7776",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7776#event-18603"
}
```



---

archive/issue_comments_066934.json:
```json
{
    "body": "Replying to [comment:6 jhpalmieri]:\n> If I do\n> {{{\n> sage: inject_variable(3, 34)  # pass a non-string to inject_variable, which I probably shouldn't do\n> }}}\n> then tab-completion is broken.  This is odd, and a little alarming.  Since this function isn't meant for casual users, maybe this isn't a big deal, but otherwise, perhaps we should check that the first argument is a string.\n\nThanks for catching this. Please review the trivial #7928 follow up!\n\n> Here's another question:\n> {{{\n> sage: from sage.misc.misc import inject_variable\n> sage: inject_variable('a', 23)\n> sage: inject_variable('a', 26)\n> /Applications/sage/local/bin/sage-ipython:1: RuntimeWarning: redefining global value `a`\n>   #!/usr/bin/env python\n> sage: inject_variable('a', 29)\n> sage: inject_variable('a', 33)\n> }}}\n> Why is the warning only printed the first time?  Is that just the nature of these warnings?\n\nAh, I had not noticed this. It seems to be a feature of warn. I added a comment in #7928.",
    "created_at": "2010-01-14T08:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7776",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7776#issuecomment-66934",
    "user": "https://github.com/nthiery"
}
```

Replying to [comment:6 jhpalmieri]:
> If I do
> {{{
> sage: inject_variable(3, 34)  # pass a non-string to inject_variable, which I probably shouldn't do
> }}}
> then tab-completion is broken.  This is odd, and a little alarming.  Since this function isn't meant for casual users, maybe this isn't a big deal, but otherwise, perhaps we should check that the first argument is a string.

Thanks for catching this. Please review the trivial #7928 follow up!

> Here's another question:
> {{{
> sage: from sage.misc.misc import inject_variable
> sage: inject_variable('a', 23)
> sage: inject_variable('a', 26)
> /Applications/sage/local/bin/sage-ipython:1: RuntimeWarning: redefining global value `a`
>   #!/usr/bin/env python
> sage: inject_variable('a', 29)
> sage: inject_variable('a', 33)
> }}}
> Why is the warning only printed the first time?  Is that just the nature of these warnings?

Ah, I had not noticed this. It seems to be a feature of warn. I added a comment in #7928.
