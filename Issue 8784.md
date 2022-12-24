# Issue 8784: remove quit_sage() command from all.py top level

archive/issues_008784.json:
```json
{
    "body": "Assignee: @jasongrout\n\nIt is stupid that it is this easy to accidentally destabilize and segfault Sage.    Also, having a function \"quit_sage()\" available at the sage: prompt by default that does not quit sage, is dumb. \n\n```\nwstein@boxen:~/build/sage-4.4$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nsage: quit_sage()\nExiting Sage (CPU time 0m0.04s, Wall time 0m3.16s).\nsage: quit\nExiting Sage (CPU time 0m0.07s, Wall time 0m4.80s).\n/virtual/scratch/wstein/build/sage-4.4/local/bin/sage-sage: line 206: 11559 Segmentation fault      sage-ipython \"$@\" -i\nwstein@boxen:~/build/sage-4.4$            \n```\n\n| Sage Version 4.4, Release Date: 2010-04-24                         |\n| Type notebook() for the GUI, and license() for information.        |\nThe fix is to rename quit_sage() somehow and change *all* code that calls it. \n\nIssue created by migration from https://trac.sagemath.org/ticket/8784\n\n",
    "created_at": "2010-04-27T20:47:41Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-9.6",
    "title": "remove quit_sage() command from all.py top level",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8784",
    "user": "@williamstein"
}
```
Assignee: @jasongrout

It is stupid that it is this easy to accidentally destabilize and segfault Sage.    Also, having a function "quit_sage()" available at the sage: prompt by default that does not quit sage, is dumb. 

```
wstein@boxen:~/build/sage-4.4$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: quit_sage()
Exiting Sage (CPU time 0m0.04s, Wall time 0m3.16s).
sage: quit
Exiting Sage (CPU time 0m0.07s, Wall time 0m4.80s).
/virtual/scratch/wstein/build/sage-4.4/local/bin/sage-sage: line 206: 11559 Segmentation fault      sage-ipython "$@" -i
wstein@boxen:~/build/sage-4.4$            
```

| Sage Version 4.4, Release Date: 2010-04-24                         |
| Type notebook() for the GUI, and license() for information.        |
The fix is to rename quit_sage() somehow and change *all* code that calls it. 

Issue created by migration from https://trac.sagemath.org/ticket/8784





---

archive/issue_comments_080422.json:
```json
{
    "body": "Maybe rename it to \"sage_library_cleanup\"?",
    "created_at": "2010-04-28T02:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80422",
    "user": "@jasongrout"
}
```

Maybe rename it to "sage_library_cleanup"?



---

archive/issue_comments_080423.json:
```json
{
    "body": "Now all of the cleanup happens automatically and `quit_sage()` is a no-op:\n\n\n```\nsage: quit_sage()\n<ipython-input-1-ce1781e96a1f>:1: DeprecationWarning: quit_sage is deprecated and now does nothing; please simply delete it\nSee http://trac.sagemath.org/8784 for details.\n  quit_sage()\nsage:\n```\n\n----\nNew commits:",
    "created_at": "2022-01-25T22:50:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80423",
    "user": "@orlitzky"
}
```

Now all of the cleanup happens automatically and `quit_sage()` is a no-op:


```
sage: quit_sage()
<ipython-input-1-ce1781e96a1f>:1: DeprecationWarning: quit_sage is deprecated and now does nothing; please simply delete it
See http://trac.sagemath.org/8784 for details.
  quit_sage()
sage:
```

----
New commits:



---

archive/issue_comments_080424.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2022-01-25T22:50:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80424",
    "user": "@orlitzky"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080425.json:
```json
{
    "body": "Does this mean that `sage-cleaner` may go, too?",
    "created_at": "2022-01-31T13:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80425",
    "user": "@dimpase"
}
```

Does this mean that `sage-cleaner` may go, too?



---

archive/issue_comments_080426.json:
```json
{
    "body": "Replying to [comment:8 dimpase]:\n> Does this mean that `sage-cleaner` may go, too?\n\nNot yet, although that's another long-term goal of mine. sage-cleaner also cleans up \"temporary\" files, which it wouldn't have to do if we used the OS's built-in tempfile functions instead of our home-grown `SAGE_TMP`. The first and easiest part of that cleanup is #33213.",
    "created_at": "2022-01-31T14:48:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80426",
    "user": "@orlitzky"
}
```

Replying to [comment:8 dimpase]:
> Does this mean that `sage-cleaner` may go, too?

Not yet, although that's another long-term goal of mine. sage-cleaner also cleans up "temporary" files, which it wouldn't have to do if we used the OS's built-in tempfile functions instead of our home-grown `SAGE_TMP`. The first and easiest part of that cleanup is #33213.



---

archive/issue_comments_080427.json:
```json
{
    "body": "Replying to [comment:8 dimpase]:\n> Does this mean that `sage-cleaner` may go, too?\n\nOk, I actually did this in #33213, which now depends on this ticket.",
    "created_at": "2022-02-18T00:31:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80427",
    "user": "@orlitzky"
}
```

Replying to [comment:8 dimpase]:
> Does this mean that `sage-cleaner` may go, too?

Ok, I actually did this in #33213, which now depends on this ticket.



---

archive/issue_comments_080428.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2022-03-11T12:41:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80428",
    "user": "@dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080429.json:
```json
{
    "body": "OK, looks and tests good.",
    "created_at": "2022-03-11T12:41:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80429",
    "user": "@dimpase"
}
```

OK, looks and tests good.



---

archive/issue_comments_080430.json:
```json
{
    "body": "perhaps you want to rebase on the latest beta",
    "created_at": "2022-03-11T12:42:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80430",
    "user": "@dimpase"
}
```

perhaps you want to rebase on the latest beta



---

archive/issue_comments_080431.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. This was a forced push. New commits:",
    "created_at": "2022-03-11T13:48:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80431",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1 and set ticket back to needs_review. This was a forced push. New commits:



---

archive/issue_comments_080432.json:
```json
{
    "body": "Changing status from positive_review to needs_review.",
    "created_at": "2022-03-11T13:48:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80432",
    "user": "git"
}
```

Changing status from positive_review to needs_review.



---

archive/issue_comments_080433.json:
```json
{
    "body": "oops, overlooked this, sorry. Looks good.",
    "created_at": "2022-03-29T10:28:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80433",
    "user": "@dimpase"
}
```

oops, overlooked this, sorry. Looks good.



---

archive/issue_comments_080434.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2022-03-29T10:28:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80434",
    "user": "@dimpase"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080435.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2022-04-02T10:53:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80435",
    "user": "@vbraun"
}
```

Resolution: fixed



---

archive/issue_comments_080436.json:
```json
{
    "body": "Follow up in #33706.",
    "created_at": "2022-04-17T19:43:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80436",
    "user": "@mkoeppe"
}
```

Follow up in #33706.



---

archive/issue_comments_080437.json:
```json
{
    "body": "We have a complaint about ipython processes staying alive in a patchbot.\nhttps://groups.google.com/d/msgid/sage-devel/20220717160807.GA13671%40metelu.net\n\nCould it be due to this ticket, perhaps the change for `src/sage/repl/ipython_extension.py`\nwas an overkill?",
    "created_at": "2022-07-17T16:44:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8784",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8784#issuecomment-80437",
    "user": "@dimpase"
}
```

We have a complaint about ipython processes staying alive in a patchbot.
https://groups.google.com/d/msgid/sage-devel/20220717160807.GA13671%40metelu.net

Could it be due to this ticket, perhaps the change for `src/sage/repl/ipython_extension.py`
was an overkill?
