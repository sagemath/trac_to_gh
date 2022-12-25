# Issue 9260: missing pointer in documentation

archive/issues_009260.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @kcrisman\n\nThe documentation from `RealIntervalField` says:\n\n```\n       See the documentation for ``RealIntervalField_class`` for many more\n       examples.\n```\n\nHowever there is no documentation for `RealIntervalField_class`:\n\n```\nsage: RealIntervalField_class?\nObject `RealIntervalField_class` not found.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/9260\n\n",
    "created_at": "2010-06-18T09:52:05Z",
    "labels": [
        "component: documentation",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.1",
    "title": "missing pointer in documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9260",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: mvngu

CC:  @kcrisman

The documentation from `RealIntervalField` says:

```
       See the documentation for ``RealIntervalField_class`` for many more
       examples.
```

However there is no documentation for `RealIntervalField_class`:

```
sage: RealIntervalField_class?
Object `RealIntervalField_class` not found.
```


Issue created by migration from https://trac.sagemath.org/ticket/9260





---

archive/issue_comments_086992.json:
```json
{
    "body": "Current code is actually\n\n```\n\n    See the documentation for :class:`RealIntervalField_class` for many more\n    examples.\n\n```\n\n\nSo this would just have to add a little so that users at the command line could see where to find this; in the documentation it would still look the same and have the right link.",
    "created_at": "2012-01-12T15:50:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9260#issuecomment-86992",
    "user": "https://github.com/kcrisman"
}
```

Current code is actually

```

    See the documentation for :class:`RealIntervalField_class` for many more
    examples.

```


So this would just have to add a little so that users at the command line could see where to find this; in the documentation it would still look the same and have the right link.



---

archive/issue_comments_086993.json:
```json
{
    "body": "Karl-Dieter,\ndo you know how to find the documentation from the command line?\n\n```\nsage: :class:RealIntervalField_class?\nObject `:class:RealIntervalField_class` not found.\n```\n\nPaul",
    "created_at": "2012-01-13T08:24:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9260#issuecomment-86993",
    "user": "https://github.com/zimmermann6"
}
```

Karl-Dieter,
do you know how to find the documentation from the command line?

```
sage: :class:RealIntervalField_class?
Object `:class:RealIntervalField_class` not found.
```

Paul



---

archive/issue_comments_086994.json:
```json
{
    "body": "Yes, and I thought one of my students had made a patch for this.  It turns out to live in `sage.rings.real_mpfi.RealIntervalField_class?`",
    "created_at": "2012-01-13T19:31:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9260#issuecomment-86994",
    "user": "https://github.com/kcrisman"
}
```

Yes, and I thought one of my students had made a patch for this.  It turns out to live in `sage.rings.real_mpfi.RealIntervalField_class?`



---

archive/issue_comments_086995.json:
```json
{
    "body": "I see what you were asking now in comment:3.  Most Sage documentation now has these hyperlinks, but it does mean one has to ignore the backticks and things like `:class` or `:meth:`.  I think this is standard now.\n\n```\nsage.rings.real_mpfi.RealIntervalField_class?\n```\n\nis the correct command, and the patch coming up changes the doc so that this can at least be found, modulo the extra formatting.",
    "created_at": "2012-05-26T19:57:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9260#issuecomment-86995",
    "user": "https://github.com/kcrisman"
}
```

I see what you were asking now in comment:3.  Most Sage documentation now has these hyperlinks, but it does mean one has to ignore the backticks and things like `:class` or `:meth:`.  I think this is standard now.

```
sage.rings.real_mpfi.RealIntervalField_class?
```

is the correct command, and the patch coming up changes the doc so that this can at least be found, modulo the extra formatting.



---

archive/issue_comments_086996.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-05-26T19:57:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9260#issuecomment-86996",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_086997.json:
```json
{
    "body": "Based on Sage 5.1.beta0",
    "created_at": "2012-05-26T19:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9260#issuecomment-86997",
    "user": "https://github.com/kcrisman"
}
```

Based on Sage 5.1.beta0



---

archive/issue_comments_086998.json:
```json
{
    "body": "Attachment [trac_9260.patch](tarball://root/attachments/some-uuid/ticket9260/trac_9260.patch) by @kcrisman created at 2012-05-26 19:59:31",
    "created_at": "2012-05-26T19:59:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9260#issuecomment-86998",
    "user": "https://github.com/kcrisman"
}
```

Attachment [trac_9260.patch](tarball://root/attachments/some-uuid/ticket9260/trac_9260.patch) by @kcrisman created at 2012-05-26 19:59:31



---

archive/issue_comments_086999.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd40.5\".",
    "created_at": "2012-05-26T19:59:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9260#issuecomment-86999",
    "user": "https://github.com/kcrisman"
}
```

Changing keywords from "" to "sd40.5".



---

archive/issue_comments_087000.json:
```json
{
    "body": "Other than the fact that you have created an excessively long line in the docstring, this ticket looks good to go.",
    "created_at": "2012-05-26T22:32:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9260#issuecomment-87000",
    "user": "https://github.com/kini"
}
```

Other than the fact that you have created an excessively long line in the docstring, this ticket looks good to go.



---

archive/issue_comments_087001.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-05-26T22:32:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9260#issuecomment-87001",
    "user": "https://github.com/kini"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_087002.json:
```json
{
    "body": "apply to $SAGE_ROOT/devel/sage",
    "created_at": "2012-05-27T17:00:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9260#issuecomment-87002",
    "user": "https://github.com/kini"
}
```

apply to $SAGE_ROOT/devel/sage



---

archive/issue_comments_087003.json:
```json
{
    "body": "Attachment [trac_9260.reviewer.patch](tarball://root/attachments/some-uuid/ticket9260/trac_9260.reviewer.patch) by @kini created at 2012-05-27 17:00:23\n\nHere's a reviewer patch to fix the \"excessively long line\", per your suggestion :)",
    "created_at": "2012-05-27T17:00:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9260#issuecomment-87003",
    "user": "https://github.com/kini"
}
```

Attachment [trac_9260.reviewer.patch](tarball://root/attachments/some-uuid/ticket9260/trac_9260.reviewer.patch) by @kini created at 2012-05-27 17:00:23

Here's a reviewer patch to fix the "excessively long line", per your suggestion :)



---

archive/issue_comments_087004.json:
```json
{
    "body": "patchbot, please, please, please apply trac_9260.patch trac_9260.reviewer.patch (pretty please)",
    "created_at": "2012-05-27T17:00:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9260#issuecomment-87004",
    "user": "https://github.com/kini"
}
```

patchbot, please, please, please apply trac_9260.patch trac_9260.reviewer.patch (pretty please)



---

archive/issue_comments_087005.json:
```json
{
    "body": "Please fill in your real name in the Author / Reviewer fields.",
    "created_at": "2012-06-09T19:23:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9260#issuecomment-87005",
    "user": "https://github.com/jdemeyer"
}
```

Please fill in your real name in the Author / Reviewer fields.



---

archive/issue_comments_087006.json:
```json
{
    "body": "Done.",
    "created_at": "2012-06-09T19:29:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9260#issuecomment-87006",
    "user": "https://github.com/kini"
}
```

Done.



---

archive/issue_comments_087007.json:
```json
{
    "body": "Hmm, that is a good change in the reviewer patch - I wasn't aware that syntax was an option.\n\nJeroen, I think you know who kini is - wouldn't that have taken fewer characters?  ;-)",
    "created_at": "2012-06-10T00:39:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9260#issuecomment-87007",
    "user": "https://github.com/kcrisman"
}
```

Hmm, that is a good change in the reviewer patch - I wasn't aware that syntax was an option.

Jeroen, I think you know who kini is - wouldn't that have taken fewer characters?  ;-)



---

archive/issue_comments_087008.json:
```json
{
    "body": "Jeroen is correct in asking me to add my name. Ideally a release manager should need to do as little work as possible - and what work he does do should be limited to administrative oversight. The more automation we can add to the system of getting Sage releases out, the better.",
    "created_at": "2012-06-10T01:06:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9260#issuecomment-87008",
    "user": "https://github.com/kini"
}
```

Jeroen is correct in asking me to add my name. Ideally a release manager should need to do as little work as possible - and what work he does do should be limited to administrative oversight. The more automation we can add to the system of getting Sage releases out, the better.



---

archive/issue_comments_087009.json:
```json
{
    "body": "I agree that you (or I) should have done it!  I was just pointing out that in this particular case it actually took him more effort than doing it himself - hence the winky emoticon.  Presumably this will save him effort in the long run, though, I agree.",
    "created_at": "2012-06-10T04:47:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9260#issuecomment-87009",
    "user": "https://github.com/kcrisman"
}
```

I agree that you (or I) should have done it!  I was just pointing out that in this particular case it actually took him more effort than doing it himself - hence the winky emoticon.  Presumably this will save him effort in the long run, though, I agree.



---

archive/issue_comments_087010.json:
```json
{
    "body": "Well, since he left exactly the same message on two other tickets which I had forgotten to put my name on, there's a strong possibility that he had scripted it :) And that's a good thing!",
    "created_at": "2012-06-11T03:01:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9260#issuecomment-87010",
    "user": "https://github.com/kini"
}
```

Well, since he left exactly the same message on two other tickets which I had forgotten to put my name on, there's a strong possibility that he had scripted it :) And that's a good thing!



---

archive/issue_events_022804.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-06-18T10:22:07Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9260",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9260#event-22804"
}
```



---

archive/issue_comments_087011.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-06-18T10:22:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9260",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9260#issuecomment-87011",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
