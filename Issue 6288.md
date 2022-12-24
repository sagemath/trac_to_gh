# Issue 6288: %lisp mode on the command line doesn't work.  why?

archive/issues_006288.json:
```json
{
    "body": "Assignee: was\n\n\n```\n> Another thing that does not work is \"sage -\n> lisp\" which gave the clisp prompt. I found this rather convenient\n> since I could just use the clisp within sage. Is there any plan/\n> interest to switch the this lisp interface to ecl? Does ecl use\n> readline?\n\nFor now you can at least start sage then type\n\nsage: !ecl\n\nto start ecl.  It appears to not make any use of ecl.  I don't know if this is just\na compilation problem or an ecl limitation.\n\nThe Sage <--> lisp interface already works fine:\n\nsage: lisp.eval('(+ 2 3)')\n'5'\n\nI'm not sure why %gap works but not %lisp:\n\nsage: %lisp\nERROR: Magic function `lisp` not found.\nsage: %gap\n  --> Switching to Gap <-- \ngap: \n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6288\n\n",
    "created_at": "2009-06-14T20:57:48Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.1",
    "title": "%lisp mode on the command line doesn't work.  why?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6288",
    "user": "was"
}
```
Assignee: was


```
> Another thing that does not work is "sage -
> lisp" which gave the clisp prompt. I found this rather convenient
> since I could just use the clisp within sage. Is there any plan/
> interest to switch the this lisp interface to ecl? Does ecl use
> readline?

For now you can at least start sage then type

sage: !ecl

to start ecl.  It appears to not make any use of ecl.  I don't know if this is just
a compilation problem or an ecl limitation.

The Sage <--> lisp interface already works fine:

sage: lisp.eval('(+ 2 3)')
'5'

I'm not sure why %gap works but not %lisp:

sage: %lisp
ERROR: Magic function `lisp` not found.
sage: %gap
  --> Switching to Gap <-- 
gap: 
```




Issue created by migration from https://trac.sagemath.org/ticket/6288





---

archive/issue_comments_050206.json:
```json
{
    "body": "Attachment [trac_6288.patch](tarball://root/attachments/some-uuid/ticket6288/trac_6288.patch) by mhansen created at 2013-07-23 13:23:57",
    "created_at": "2013-07-23T13:23:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6288#issuecomment-50206",
    "user": "mhansen"
}
```

Attachment [trac_6288.patch](tarball://root/attachments/some-uuid/ticket6288/trac_6288.patch) by mhansen created at 2013-07-23 13:23:57



---

archive/issue_comments_050207.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2013-07-23T13:24:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6288#issuecomment-50207",
    "user": "mhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_050208.json:
```json
{
    "body": "ok, here is a review patch.\n\nFirst I have made some minor formatting changes (pep8)\n\nNext, I have corrected the part handling the bad names\n\nHere is the list of interfaces with bad names:\n\n```\n[('gp', 'pari', PARI/GP interpreter),\n ('lisp', 'Lisp', Lisp Interpreter),\n ('sage0', 'sage', Sage),\n ('mupad', 'MuPAD', Mupad),\n ('lie', 'LiE', LiE Interpreter)]\n```\n\nI would prefer to avoid having the magic command \"%sage\" !\n\nI also wonder if it is necessary to deprecate the bad names, instead of just using them as an alternative ?",
    "created_at": "2013-08-21T11:55:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6288#issuecomment-50208",
    "user": "chapoton"
}
```

ok, here is a review patch.

First I have made some minor formatting changes (pep8)

Next, I have corrected the part handling the bad names

Here is the list of interfaces with bad names:

```
[('gp', 'pari', PARI/GP interpreter),
 ('lisp', 'Lisp', Lisp Interpreter),
 ('sage0', 'sage', Sage),
 ('mupad', 'MuPAD', Mupad),
 ('lie', 'LiE', LiE Interpreter)]
```

I would prefer to avoid having the magic command "%sage" !

I also wonder if it is necessary to deprecate the bad names, instead of just using them as an alternative ?



---

archive/issue_comments_050209.json:
```json
{
    "body": "Attachment [trac_6288_addon_pep8.patch](tarball://root/attachments/some-uuid/ticket6288/trac_6288_addon_pep8.patch) by chapoton created at 2013-08-25 13:25:46",
    "created_at": "2013-08-25T13:25:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6288#issuecomment-50209",
    "user": "chapoton"
}
```

Attachment [trac_6288_addon_pep8.patch](tarball://root/attachments/some-uuid/ticket6288/trac_6288_addon_pep8.patch) by chapoton created at 2013-08-25 13:25:46



---

archive/issue_comments_050210.json:
```json
{
    "body": "ping ?",
    "created_at": "2013-09-11T19:25:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6288#issuecomment-50210",
    "user": "chapoton"
}
```

ping ?



---

archive/issue_comments_050211.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-01-05T10:02:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6288#issuecomment-50211",
    "user": "chapoton"
}
```

New commits:



---

archive/issue_comments_050212.json:
```json
{
    "body": "The review patch looks good.  I would probably prefer \"%sage0\" to \"%sage\".  I'd rather deprecate the bad names so that there's just one consistent way to access them.  But, I'm not too fussed either way about those two points.",
    "created_at": "2014-01-09T12:19:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6288#issuecomment-50212",
    "user": "mhansen"
}
```

The review patch looks good.  I would probably prefer "%sage0" to "%sage".  I'd rather deprecate the bad names so that there's just one consistent way to access them.  But, I'm not too fussed either way about those two points.



---

archive/issue_comments_050213.json:
```json
{
    "body": "Ok, so is there still something to do or not ?",
    "created_at": "2014-01-09T19:28:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6288#issuecomment-50213",
    "user": "chapoton"
}
```

Ok, so is there still something to do or not ?



---

archive/issue_comments_050214.json:
```json
{
    "body": "I would say not.  I'm fine with your patch.",
    "created_at": "2014-01-09T19:40:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6288#issuecomment-50214",
    "user": "mhansen"
}
```

I would say not.  I'm fine with your patch.



---

archive/issue_comments_050215.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-01-09T19:40:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6288#issuecomment-50215",
    "user": "mhansen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_050216.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-01-17T04:16:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6288",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6288#issuecomment-50216",
    "user": "vbraun"
}
```

Resolution: fixed
