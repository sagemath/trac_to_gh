# Issue 9777: Addition of LaTeX and better support of SI prefixes on units module

archive/issues_009777.json:
```json
{
    "body": "Assignee: burcin\n\nCC:  was eviatarbach\n\nKeywords: latex, SI prefixes, units\n\nSince maybe the developers are reluctant to implement the \"metrology\" module I submitted in #9763, when there's already a \"units\" module that has the same purpose, I'm trying to port the `LaTeX` capabilities to the already existing \"units\" module.\n\nTO DO: Complete the latexdict list of units and `LaTeX` representation (if a unit isn't there, its symbol will be replaced by its name)\n\nAlso, I'm implementing an easier way to use `SI` prefixes on the units module. The patch I submitted in #9759 wasn't very intuitive (you had to type \"units.length.meter.kilo\"), partly because I didn't know very well how did that module work. This new version allows you to simply type \"units.length.kilometer\" (even if it's not tab-completed) and it will do the rest.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9778\n\n",
    "created_at": "2010-08-21T20:42:35Z",
    "labels": [
        "symbolics",
        "minor",
        "enhancement"
    ],
    "title": "Addition of LaTeX and better support of SI prefixes on units module",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9777",
    "user": "cousteau"
}
```
Assignee: burcin

CC:  was eviatarbach

Keywords: latex, SI prefixes, units

Since maybe the developers are reluctant to implement the "metrology" module I submitted in #9763, when there's already a "units" module that has the same purpose, I'm trying to port the `LaTeX` capabilities to the already existing "units" module.

TO DO: Complete the latexdict list of units and `LaTeX` representation (if a unit isn't there, its symbol will be replaced by its name)

Also, I'm implementing an easier way to use `SI` prefixes on the units module. The patch I submitted in #9759 wasn't very intuitive (you had to type "units.length.meter.kilo"), partly because I didn't know very well how did that module work. This new version allows you to simply type "units.length.kilometer" (even if it's not tab-completed) and it will do the rest.

Issue created by migration from https://trac.sagemath.org/ticket/9778





---

archive/issue_comments_095953.json:
```json
{
    "body": "Attachment [trac_9778_latex_prefixes_units.patch](tarball://root/attachments/some-uuid/ticket9778/trac_9778_latex_prefixes_units.patch) by cousteau created at 2010-08-21 20:46:48\n\nAdds `LaTeX` symbols and `SI` prefixes to the units module",
    "created_at": "2010-08-21T20:46:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9777#issuecomment-95953",
    "user": "cousteau"
}
```

Attachment [trac_9778_latex_prefixes_units.patch](tarball://root/attachments/some-uuid/ticket9778/trac_9778_latex_prefixes_units.patch) by cousteau created at 2010-08-21 20:46:48

Adds `LaTeX` symbols and `SI` prefixes to the units module



---

archive/issue_comments_095954.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2010-08-21T20:47:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9777#issuecomment-95954",
    "user": "cousteau"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_095955.json:
```json
{
    "body": "Is the \"todo\" necessary, or could it be postponed to another ticket?",
    "created_at": "2012-05-26T07:25:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9777#issuecomment-95955",
    "user": "kcrisman"
}
```

Is the "todo" necessary, or could it be postponed to another ticket?



---

archive/issue_comments_095956.json:
```json
{
    "body": "Well, `latexdict` only contains a few units (10) and prefixes (5) so that it worked as an example; it would need to be completed with the names of all SI units and prefixes, at least for the LaTeX representation part.\n\nBy the way, I made this patch 2 years ago so I remember pretty little of it.",
    "created_at": "2012-05-28T14:19:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9777#issuecomment-95956",
    "user": "cousteau"
}
```

Well, `latexdict` only contains a few units (10) and prefixes (5) so that it worked as an example; it would need to be completed with the names of all SI units and prefixes, at least for the LaTeX representation part.

By the way, I made this patch 2 years ago so I remember pretty little of it.



---

archive/issue_comments_095957.json:
```json
{
    "body": "This supersedes #9759.\n\nIf someone wanted to complete this, they'd just have to make sure they implemented all the SI units etc. that Sage supports (see the 'todo' above).",
    "created_at": "2012-05-28T15:51:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9777#issuecomment-95957",
    "user": "kcrisman"
}
```

This supersedes #9759.

If someone wanted to complete this, they'd just have to make sure they implemented all the SI units etc. that Sage supports (see the 'todo' above).



---

archive/issue_comments_095958.json:
```json
{
    "body": "Changing keywords from \"latex, SI prefixes, units\" to \"latex, SI prefixes, units, sd40.5\".",
    "created_at": "2012-05-28T15:51:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9777#issuecomment-95958",
    "user": "kcrisman"
}
```

Changing keywords from "latex, SI prefixes, units" to "latex, SI prefixes, units, sd40.5".
