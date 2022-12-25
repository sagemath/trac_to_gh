# Issue 2347: [with bundle, positive review] better parsing for symbolics

archive/issues_002347.json:
```json
{
    "body": "Assignee: @robertwb\n\nThis is a security risk, and limits the potential uses of Sage. For example, if I wanted to put a text box on my website where people could type in a function and it would return the derivative (computed using Sage) someone could \"ask\" for the derivative of `2*os.system('rm -rf /')`. Symbolic expressions should be able to be parsed in such a way that one can safely reject expressions using unknown (or non-whitelisted) functions. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2347\n\n",
    "closed_at": "2008-04-14T22:55:58Z",
    "created_at": "2008-02-28T09:26:58Z",
    "labels": [
        "component: calculus",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with bundle, positive review] better parsing for symbolics",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2347",
    "user": "https://github.com/robertwb"
}
```
Assignee: @robertwb

This is a security risk, and limits the potential uses of Sage. For example, if I wanted to put a text box on my website where people could type in a function and it would return the derivative (computed using Sage) someone could "ask" for the derivative of `2*os.system('rm -rf /')`. Symbolic expressions should be able to be parsed in such a way that one can safely reject expressions using unknown (or non-whitelisted) functions. 

Issue created by migration from https://trac.sagemath.org/ticket/2347





---

archive/issue_comments_015690.json:
```json
{
    "body": "Changing assignee from @williamstein to @robertwb.",
    "created_at": "2008-02-28T11:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2347#issuecomment-15690",
    "user": "https://github.com/robertwb"
}
```

Changing assignee from @williamstein to @robertwb.



---

archive/issue_comments_015691.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-02-28T11:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2347#issuecomment-15691",
    "user": "https://github.com/robertwb"
}
```

Changing status from new to assigned.



---

archive/issue_comments_015692.json:
```json
{
    "body": "Of course, we don't want to re-write the Python parser or try to certify generic code to be safe, but in this constrained situation we should be able to treat an expression as data without worrying about it being treated as code. \n\nThere is an added benefit that unknown tokens gan be treated as symbolic variables. I wrote up a parser in Cython that is actually 10 times faster than eval(...) and handles symbolic expressions that I think is ready to plug in, I just need to provide it with a good list of \"whitelist\" functions that may be called.",
    "created_at": "2008-02-28T11:18:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2347#issuecomment-15692",
    "user": "https://github.com/robertwb"
}
```

Of course, we don't want to re-write the Python parser or try to certify generic code to be safe, but in this constrained situation we should be able to treat an expression as data without worrying about it being treated as code. 

There is an added benefit that unknown tokens gan be treated as symbolic variables. I wrote up a parser in Cython that is actually 10 times faster than eval(...) and handles symbolic expressions that I think is ready to plug in, I just need to provide it with a good list of "whitelist" functions that may be called.



---

archive/issue_comments_015693.json:
```json
{
    "body": "Attachment [2347-parsing.hg](tarball://root/attachments/some-uuid/ticket2347/2347-parsing.hg) by @robertwb created at 2008-04-11 11:25:10",
    "created_at": "2008-04-11T11:25:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2347#issuecomment-15693",
    "user": "https://github.com/robertwb"
}
```

Attachment [2347-parsing.hg](tarball://root/attachments/some-uuid/ticket2347/2347-parsing.hg) by @robertwb created at 2008-04-11 11:25:10



---

archive/issue_comments_015694.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2008-04-11T19:35:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2347#issuecomment-15694",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_015695.json:
```json
{
    "body": "Attachment [2347.patch](tarball://root/attachments/some-uuid/ticket2347/2347.patch) by @mwhansen created at 2008-04-11 20:45:53\n\nI've attached the bundle as a patch which I will review once 3.0.alpha4 comes out.  There were some problems applying the bundle against 3.0.alpha3.",
    "created_at": "2008-04-11T20:45:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2347#issuecomment-15695",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2347.patch](tarball://root/attachments/some-uuid/ticket2347/2347.patch) by @mwhansen created at 2008-04-11 20:45:53

I've attached the bundle as a patch which I will review once 3.0.alpha4 comes out.  There were some problems applying the bundle against 3.0.alpha3.



---

archive/issue_comments_015696.json:
```json
{
    "body": "I will rebase the bundle as I don't want to loose the history.",
    "created_at": "2008-04-11T23:52:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2347#issuecomment-15696",
    "user": "https://github.com/robertwb"
}
```

I will rebase the bundle as I don't want to loose the history.



---

archive/issue_comments_015697.json:
```json
{
    "body": "Sounds good although patches are much easier to deal with.",
    "created_at": "2008-04-11T23:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2347#issuecomment-15697",
    "user": "https://github.com/mwhansen"
}
```

Sounds good although patches are much easier to deal with.



---

archive/issue_comments_015698.json:
```json
{
    "body": "Just FYI, you could use queue repositories to be able to get patches that have history.  See the the help for qcommit, etc.",
    "created_at": "2008-04-12T23:44:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2347#issuecomment-15698",
    "user": "https://github.com/jasongrout"
}
```

Just FYI, you could use queue repositories to be able to get patches that have history.  See the the help for qcommit, etc.



---

archive/issue_comments_015699.json:
```json
{
    "body": "Attachment [2347-parsing-rebased.hg](tarball://root/attachments/some-uuid/ticket2347/2347-parsing-rebased.hg) by @robertwb created at 2008-04-13 06:14:19\n\nThe new bundle (against alpha3) works fine. There was only one minor conflict. Do you anticipate any major changes with alpha4? (If it's up before I go to bed I'll make sure it works against that.) \n\nJason: Using mercurial queues won't help here, the issue is that half a dozen commits were compressed into a single patch. When there are more than four or five separate changesets attached to a given ticket, I find bundles a lot easier to deal with (rather than attaching all the patches separately).",
    "created_at": "2008-04-13T06:14:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2347#issuecomment-15699",
    "user": "https://github.com/robertwb"
}
```

Attachment [2347-parsing-rebased.hg](tarball://root/attachments/some-uuid/ticket2347/2347-parsing-rebased.hg) by @robertwb created at 2008-04-13 06:14:19

The new bundle (against alpha3) works fine. There was only one minor conflict. Do you anticipate any major changes with alpha4? (If it's up before I go to bed I'll make sure it works against that.) 

Jason: Using mercurial queues won't help here, the issue is that half a dozen commits were compressed into a single patch. When there are more than four or five separate changesets attached to a given ticket, I find bundles a lot easier to deal with (rather than attaching all the patches separately).



---

archive/issue_comments_015700.json:
```json
{
    "body": "Attachment [2347-1.patch](tarball://root/attachments/some-uuid/ticket2347/2347-1.patch) by @robertwb created at 2008-04-13 07:26:46",
    "created_at": "2008-04-13T07:26:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2347#issuecomment-15700",
    "user": "https://github.com/robertwb"
}
```

Attachment [2347-1.patch](tarball://root/attachments/some-uuid/ticket2347/2347-1.patch) by @robertwb created at 2008-04-13 07:26:46



---

archive/issue_comments_015701.json:
```json
{
    "body": "Attachment [2347-2.patch](tarball://root/attachments/some-uuid/ticket2347/2347-2.patch) by @robertwb created at 2008-04-13 07:27:05",
    "created_at": "2008-04-13T07:27:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2347#issuecomment-15701",
    "user": "https://github.com/robertwb"
}
```

Attachment [2347-2.patch](tarball://root/attachments/some-uuid/ticket2347/2347-2.patch) by @robertwb created at 2008-04-13 07:27:05



---

archive/issue_comments_015702.json:
```json
{
    "body": "Attachment [2347-3.patch](tarball://root/attachments/some-uuid/ticket2347/2347-3.patch) by @robertwb created at 2008-04-13 07:27:15",
    "created_at": "2008-04-13T07:27:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2347#issuecomment-15702",
    "user": "https://github.com/robertwb"
}
```

Attachment [2347-3.patch](tarball://root/attachments/some-uuid/ticket2347/2347-3.patch) by @robertwb created at 2008-04-13 07:27:15



---

archive/issue_comments_015703.json:
```json
{
    "body": "Attachment [2347-5.patch](tarball://root/attachments/some-uuid/ticket2347/2347-5.patch) by @robertwb created at 2008-04-13 07:27:26",
    "created_at": "2008-04-13T07:27:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2347#issuecomment-15703",
    "user": "https://github.com/robertwb"
}
```

Attachment [2347-5.patch](tarball://root/attachments/some-uuid/ticket2347/2347-5.patch) by @robertwb created at 2008-04-13 07:27:26



---

archive/issue_comments_015704.json:
```json
{
    "body": "Attachment [2347-7.patch](tarball://root/attachments/some-uuid/ticket2347/2347-7.patch) by @robertwb created at 2008-04-13 07:27:44",
    "created_at": "2008-04-13T07:27:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2347#issuecomment-15704",
    "user": "https://github.com/robertwb"
}
```

Attachment [2347-7.patch](tarball://root/attachments/some-uuid/ticket2347/2347-7.patch) by @robertwb created at 2008-04-13 07:27:44



---

archive/issue_comments_015705.json:
```json
{
    "body": "For those of you who prefer patches, I've attached them. Patches 1-7 are exactly the same contents as the bundles, except the rebased bundle resolves a (trivial to fix) conflict in patch 2 against alpha3.",
    "created_at": "2008-04-13T07:31:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2347#issuecomment-15705",
    "user": "https://github.com/robertwb"
}
```

For those of you who prefer patches, I've attached them. Patches 1-7 are exactly the same contents as the bundles, except the rebased bundle resolves a (trivial to fix) conflict in patch 2 against alpha3.



---

archive/issue_comments_015706.json:
```json
{
    "body": "Attachment [2347.hg](tarball://root/attachments/some-uuid/ticket2347/2347.hg) by @mwhansen created at 2008-04-14 22:43:00",
    "created_at": "2008-04-14T22:43:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2347#issuecomment-15706",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2347.hg](tarball://root/attachments/some-uuid/ticket2347/2347.hg) by @mwhansen created at 2008-04-14 22:43:00



---

archive/issue_comments_015707.json:
```json
{
    "body": "I've looked at the changes and tested things out, and things look good to me.  This is a definite improvement than what was there before.  I included a change to combinat/root_system/dynkin_diagram.py.  2347.hg is the bundle that should be merged.",
    "created_at": "2008-04-14T22:44:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2347#issuecomment-15707",
    "user": "https://github.com/mwhansen"
}
```

I've looked at the changes and tested things out, and things look good to me.  This is a definite improvement than what was there before.  I included a change to combinat/root_system/dynkin_diagram.py.  2347.hg is the bundle that should be merged.



---

archive/issue_events_005535.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-14T22:55:58Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2347",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2347#event-5535"
}
```



---

archive/issue_comments_015708.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-14T22:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2347#issuecomment-15708",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_015709.json:
```json
{
    "body": "Merged in Sage 3.0.alpha5",
    "created_at": "2008-04-14T22:55:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2347#issuecomment-15709",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha5



---

archive/issue_comments_015710.json:
```json
{
    "body": "Robert,\n\nI am seeing one doctest failure:\n\n```\nsage -t -long devel/sage/sage/rings/number_field/number_field.py\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.alpha5/tmp/number_field.py\", line 4878:\n    sage: L.lift_to_base(b^4)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.alpha5/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_145[6]>\", line 1, in <module>\n        L.lift_to_base(b**Integer(4))###line 4878:\n    sage: L.lift_to_base(b^4)\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.alpha5/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 4892, in lift_to_base\n        f = QQ['y'](str_poly)\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.alpha5/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py\", line 225, in __call__\n        raise TypeError,\"Unable to coerce string\"\n    TypeError: Unable to coerce string\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.0.alpha5/tmp/number_field.py\", line 211:\n    sage: L.lift_to_base(b^3 + b)\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.alpha5/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_3[12]>\", line 1, in <module>\n        L.lift_to_base(b**Integer(3) + b)###line 211:\n    sage: L.lift_to_base(b^3 + b)\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.alpha5/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py\", line 4892, in lift_to_base\n        f = QQ['y'](str_poly)\n      File \"/scratch/mabshoff/release-cycle/sage-3.0.alpha5/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py\", line 225, in __call__\n        raise TypeError,\"Unable to coerce string\"\n    TypeError: Unable to coerce string\n**********************************************************************\n```\n\nCheers,\n\nMichael",
    "created_at": "2008-04-14T23:19:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2347#issuecomment-15710",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Robert,

I am seeing one doctest failure:

```
sage -t -long devel/sage/sage/rings/number_field/number_field.py
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.alpha5/tmp/number_field.py", line 4878:
    sage: L.lift_to_base(b^4)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha5/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_145[6]>", line 1, in <module>
        L.lift_to_base(b**Integer(4))###line 4878:
    sage: L.lift_to_base(b^4)
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha5/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 4892, in lift_to_base
        f = QQ['y'](str_poly)
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha5/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py", line 225, in __call__
        raise TypeError,"Unable to coerce string"
    TypeError: Unable to coerce string
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.0.alpha5/tmp/number_field.py", line 211:
    sage: L.lift_to_base(b^3 + b)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha5/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_3[12]>", line 1, in <module>
        L.lift_to_base(b**Integer(3) + b)###line 211:
    sage: L.lift_to_base(b^3 + b)
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha5/local/lib/python2.5/site-packages/sage/rings/number_field/number_field.py", line 4892, in lift_to_base
        f = QQ['y'](str_poly)
      File "/scratch/mabshoff/release-cycle/sage-3.0.alpha5/local/lib/python2.5/site-packages/sage/rings/polynomial/polynomial_ring.py", line 225, in __call__
        raise TypeError,"Unable to coerce string"
    TypeError: Unable to coerce string
**********************************************************************
```

Cheers,

Michael



---

archive/issue_comments_015711.json:
```json
{
    "body": "Hmm... I ran a -testall before rebasing the bundle, but I'll see if I can get a patch for this. Should be pretty simple. (Really, it's ugly that it's going via strings at all.) \n\nBTW, do you have a `sage-3.0.alpha4-sage.math-only-x86_64-Linux.tar.gz` I could grab?",
    "created_at": "2008-04-14T23:29:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2347#issuecomment-15711",
    "user": "https://github.com/robertwb"
}
```

Hmm... I ran a -testall before rebasing the bundle, but I'll see if I can get a patch for this. Should be pretty simple. (Really, it's ugly that it's going via strings at all.) 

BTW, do you have a `sage-3.0.alpha4-sage.math-only-x86_64-Linux.tar.gz` I could grab?



---

archive/issue_comments_015712.json:
```json
{
    "body": "An sage-3.0.alpha4-sage.math-only-x86_64-Linux.tar.gz should be up in the usual place in five minutes. Mike Hansen is also poking around in the general area.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-14T23:37:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2347#issuecomment-15712",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

An sage-3.0.alpha4-sage.math-only-x86_64-Linux.tar.gz should be up in the usual place in five minutes. Mike Hansen is also poking around in the general area.

Cheers,

Michael



---

archive/issue_comments_015713.json:
```json
{
    "body": "Attachment [2347-doctest.patch](tarball://root/attachments/some-uuid/ticket2347/2347-doctest.patch) by @mwhansen created at 2008-04-14 23:53:23",
    "created_at": "2008-04-14T23:53:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2347#issuecomment-15713",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2347-doctest.patch](tarball://root/attachments/some-uuid/ticket2347/2347-doctest.patch) by @mwhansen created at 2008-04-14 23:53:23



---

archive/issue_comments_015714.json:
```json
{
    "body": "I've added 2347-doctest.patch which fixes the issue.",
    "created_at": "2008-04-14T23:54:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2347#issuecomment-15714",
    "user": "https://github.com/mwhansen"
}
```

I've added 2347-doctest.patch which fixes the issue.



---

archive/issue_comments_015715.json:
```json
{
    "body": "Merged 2347-doctest.patch in Sage 3.0.alpha5",
    "created_at": "2008-04-15T00:04:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2347#issuecomment-15715",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 2347-doctest.patch in Sage 3.0.alpha5



---

archive/issue_comments_015716.json:
```json
{
    "body": "Thanks, good catch.",
    "created_at": "2008-04-15T00:16:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2347#issuecomment-15716",
    "user": "https://github.com/robertwb"
}
```

Thanks, good catch.



---

archive/issue_comments_015717.json:
```json
{
    "body": "For the record: Mike's patch fixes the issue.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-15T00:33:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2347",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2347#issuecomment-15717",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

For the record: Mike's patch fixes the issue.

Cheers,

Michael
