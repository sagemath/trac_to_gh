# Issue 9228: Bring doctests for interfaces/mwrank.py up to 100% (from 20% (2 of 10)  )

archive/issues_009228.json:
```json
{
    "body": "Assignee: @JohnCremona\n\nKeywords: mwrank\n\n```\ndevel/sage-main/sage/interfaces/mwrank.py\nERROR: Please add a `TestSuite(s).run()` doctest.\nSCORE devel/sage-main/sage/interfaces/mwrank.py: 20% (2 of 10)\n\nMissing documentation:\n* __getattr__(self, attrname):\n* __reduce__(self):\n* __call__(self, cmd):\n* console(self):\n* _reduce_load_mwrank():\n* mwrank_console():\n\n\nMissing doctests:\n* Mwrank(options=\"\", server=None, server_tmpdir=None):\n* __init__(self, options=\"\", server=None,server_tmpdir=None):\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9228\n\n",
    "closed_at": "2011-01-25T08:14:46Z",
    "created_at": "2010-06-12T13:42:01Z",
    "labels": [
        "component: doctest coverage",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.2",
    "title": "Bring doctests for interfaces/mwrank.py up to 100% (from 20% (2 of 10)  )",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9228",
    "user": "https://github.com/JohnCremona"
}
```
Assignee: @JohnCremona

Keywords: mwrank

```
devel/sage-main/sage/interfaces/mwrank.py
ERROR: Please add a `TestSuite(s).run()` doctest.
SCORE devel/sage-main/sage/interfaces/mwrank.py: 20% (2 of 10)

Missing documentation:
* __getattr__(self, attrname):
* __reduce__(self):
* __call__(self, cmd):
* console(self):
* _reduce_load_mwrank():
* mwrank_console():


Missing doctests:
* Mwrank(options="", server=None, server_tmpdir=None):
* __init__(self, options="", server=None,server_tmpdir=None):
```


Issue created by migration from https://trac.sagemath.org/ticket/9228





---

archive/issue_comments_086455.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-12-21T17:23:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9228#issuecomment-86455",
    "user": "https://github.com/JohnCremona"
}
```

Changing priority from major to minor.



---

archive/issue_comments_086456.json:
```json
{
    "body": "After the patch:\n\n```\n%sage -coverage sage/interfaces/mwrank.py \n----------------------------------------------------------------------\nsage/interfaces/mwrank.py\nSCORE sage/interfaces/mwrank.py: 100% (10 of 10)\n----------------------------------------------------------------------\n```\nand the reference manual markup has also been corrected.",
    "created_at": "2010-12-21T17:23:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9228#issuecomment-86456",
    "user": "https://github.com/JohnCremona"
}
```

After the patch:

```
%sage -coverage sage/interfaces/mwrank.py 
----------------------------------------------------------------------
sage/interfaces/mwrank.py
SCORE sage/interfaces/mwrank.py: 100% (10 of 10)
----------------------------------------------------------------------
```
and the reference manual markup has also been corrected.



---

archive/issue_comments_086457.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-12-21T17:23:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9228#issuecomment-86457",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from new to needs_review.



---

archive/issue_events_022720.json:
```json
{
    "actor": "https://github.com/JohnCremona",
    "created_at": "2010-12-21T17:23:49Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9228",
    "milestone": "sage-4.6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9228#event-22720"
}
```



---

archive/issue_comments_086458.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-09T23:48:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9228#issuecomment-86458",
    "user": "https://github.com/adeines"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086459.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-19T22:20:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9228#issuecomment-86459",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_022721.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-19T22:20:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9228",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9228#event-22721"
}
```



---

archive/issue_comments_086460.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2011-01-20T09:01:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9228#issuecomment-86460",
    "user": "https://github.com/jdemeyer"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_086461.json:
```json
{
    "body": "For some reason, the '\\t' (tab) is replaced by a series of spaces on Solaris, giving doctest errors:\n\n```\n**********************************************************************\nFile \"/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.6.2.alpha1/devel/sage-main/sage/interfaces/mwrank.py\", line 107:\n    sage: M('0 -1 1 0 0')\nExpected:\n    'Curve [0,-1,1,0,0] :\\tRank = 0\\n\\n\\nRegulator = 1\\n'\nGot:\n    'Curve [0,-1,1,0,0] :    Rank = 0\\n\\n\\nRegulator = 1\\n'\n**********************************************************************\n```",
    "created_at": "2011-01-20T09:01:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9228#issuecomment-86461",
    "user": "https://github.com/jdemeyer"
}
```

For some reason, the '\t' (tab) is replaced by a series of spaces on Solaris, giving doctest errors:

```
**********************************************************************
File "/export/home/buildbot/build/sage/hawk-1/hawk_full/build/sage-4.6.2.alpha1/devel/sage-main/sage/interfaces/mwrank.py", line 107:
    sage: M('0 -1 1 0 0')
Expected:
    'Curve [0,-1,1,0,0] :\tRank = 0\n\n\nRegulator = 1\n'
Got:
    'Curve [0,-1,1,0,0] :    Rank = 0\n\n\nRegulator = 1\n'
**********************************************************************
```



---

archive/issue_comments_086462.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2011-01-20T09:01:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9228#issuecomment-86462",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_events_022722.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-20T09:01:23Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/9228",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9228#event-22722"
}
```



---

archive/issue_comments_086463.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2011-01-20T09:01:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9228#issuecomment-86463",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_086464.json:
```json
{
    "body": "OK, so I know that some people don't like my programs putting tabs into output, which I do so the output looks pretty when viewed by humans!\n\nI suppose that one solution is to post-process the long string output by mwrank, replacing its tabs by an appropriate number of spaces.\n\nThis is just the sort of annoying triviality which makes adding doctests take so much longer than it ought!\n\nI'll post a revised patch shortly.",
    "created_at": "2011-01-20T09:30:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9228#issuecomment-86464",
    "user": "https://github.com/JohnCremona"
}
```

OK, so I know that some people don't like my programs putting tabs into output, which I do so the output looks pretty when viewed by humans!

I suppose that one solution is to post-process the long string output by mwrank, replacing its tabs by an appropriate number of spaces.

This is just the sort of annoying triviality which makes adding doctests take so much longer than it ought!

I'll post a revised patch shortly.



---

archive/issue_comments_086465.json:
```json
{
    "body": "Applies to 4.6.2.alpha0",
    "created_at": "2011-01-20T11:20:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9228#issuecomment-86465",
    "user": "https://github.com/JohnCremona"
}
```

Applies to 4.6.2.alpha0



---

archive/issue_comments_086466.json:
```json
{
    "body": "Attachment [trac_9228-mwrank-doctest.patch](tarball://root/attachments/some-uuid/ticket9228/trac_9228-mwrank-doctest.patch) by @JohnCremona created at 2011-01-20 11:22:00\n\nThe new version of the patch does what I suggested, i.e. replaces all tabs in mwrank output by three spaces;  the doctest which failed before has been adjusted accordingly.\n\nI could not find any other doctest which would be affected by this, and tested all sage/interfaces and sage/schemes/elliptic_curves.",
    "created_at": "2011-01-20T11:22:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9228#issuecomment-86466",
    "user": "https://github.com/JohnCremona"
}
```

Attachment [trac_9228-mwrank-doctest.patch](tarball://root/attachments/some-uuid/ticket9228/trac_9228-mwrank-doctest.patch) by @JohnCremona created at 2011-01-20 11:22:00

The new version of the patch does what I suggested, i.e. replaces all tabs in mwrank output by three spaces;  the doctest which failed before has been adjusted accordingly.

I could not find any other doctest which would be affected by this, and tested all sage/interfaces and sage/schemes/elliptic_curves.



---

archive/issue_comments_086467.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-01-20T11:22:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9228#issuecomment-86467",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_086468.json:
```json
{
    "body": "I can't help noticing that you've replaced tabs with 3 spaces, but Solaris seems to replace them with 4 spaces -- so I suspect that it still won't work (groan).",
    "created_at": "2011-01-20T12:13:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9228#issuecomment-86468",
    "user": "https://github.com/loefflerd"
}
```

I can't help noticing that you've replaced tabs with 3 spaces, but Solaris seems to replace them with 4 spaces -- so I suspect that it still won't work (groan).



---

archive/issue_comments_086469.json:
```json
{
    "body": "Replying to [comment:9 davidloeffler]:\n> I can't help noticing that you've replaced tabs with 3 spaces, but Solaris seems to replace them with 4 spaces -- so I suspect that it still won't work (groan).\n\n\nThink again.  I have removed the tabs so Solaris will not need to do anything!",
    "created_at": "2011-01-20T12:36:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9228#issuecomment-86469",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:9 davidloeffler]:
> I can't help noticing that you've replaced tabs with 3 spaces, but Solaris seems to replace them with 4 spaces -- so I suspect that it still won't work (groan).


Think again.  I have removed the tabs so Solaris will not need to do anything!



---

archive/issue_comments_086470.json:
```json
{
    "body": "The question is: why is the output on Solaris different in the first place?  Is it the `mwrank` program itself?  Is it pexpect?  Is it Python?",
    "created_at": "2011-01-20T12:39:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9228#issuecomment-86470",
    "user": "https://github.com/jdemeyer"
}
```

The question is: why is the output on Solaris different in the first place?  Is it the `mwrank` program itself?  Is it pexpect?  Is it Python?



---

archive/issue_comments_086471.json:
```json
{
    "body": "Replying to [comment:11 jdemeyer]:\n> The question is: why is the output on Solaris different in the first place?  Is it the `mwrank` program itself?  Is it pexpect?  Is it Python?\n\n\nHere's a test:  on the solaris machine, do\n\n```\necho 0 -1 1 0 0 0 0 0 0 0 | sage -mwrank -v 0 -q -l > t\n```\nand see if the file t contains any tab characters.  If it does, then mwrank is behaving normally and the tab conversion is happening further downstream.",
    "created_at": "2011-01-20T13:02:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9228#issuecomment-86471",
    "user": "https://github.com/JohnCremona"
}
```

Replying to [comment:11 jdemeyer]:
> The question is: why is the output on Solaris different in the first place?  Is it the `mwrank` program itself?  Is it pexpect?  Is it Python?


Here's a test:  on the solaris machine, do

```
echo 0 -1 1 0 0 0 0 0 0 0 | sage -mwrank -v 0 -q -l > t
```
and see if the file t contains any tab characters.  If it does, then mwrank is behaving normally and the tab conversion is happening further downstream.



---

archive/issue_comments_086472.json:
```json
{
    "body": "Replying to [comment:12 cremona]:\n> Here's a test:  on the solaris machine, do\n> \n> ```\n> echo 0 -1 1 0 0 0 0 0 0 0 | sage -mwrank -v 0 -q -l\n> ```\n\n\nThis is producing an actual tab character.",
    "created_at": "2011-01-20T20:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9228#issuecomment-86472",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:12 cremona]:
> Here's a test:  on the solaris machine, do
> 
> ```
> echo 0 -1 1 0 0 0 0 0 0 0 | sage -mwrank -v 0 -q -l
> ```


This is producing an actual tab character.



---

archive/issue_comments_086473.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-01-20T20:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9228#issuecomment-86473",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_086474.json:
```json
{
    "body": "Tested on fulvia (i386 Solaris).",
    "created_at": "2011-01-20T20:47:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9228#issuecomment-86474",
    "user": "https://github.com/jdemeyer"
}
```

Tested on fulvia (i386 Solaris).



---

archive/issue_comments_086475.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-01-25T08:14:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9228",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9228#issuecomment-86475",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed



---

archive/issue_events_022723.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2011-01-25T08:14:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9228",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9228#event-22723"
}
```
