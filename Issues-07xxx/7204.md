# Issue 7204: issue building sage docs since notebook moved

archive/issues_007204.json:
```json
{
    "body": "Assignee: tba\n\nCC:  @jhpalmieri\n\n```\n>> If nobody finds any serious problems with it, something close to it\n>> will get released (though I'm not in a hurry).\n>\n> Here's a nonserious problem: running \"sage -docbuild developer html --\n> jsmath\" prints an error message.  At the end of the build process, I\n> get this error:\n>\n> copying static files... Exception occurred:\n>  File \"/Applications/sage_builds/sage-4.1.2.rc2-64-bit/local/lib/\n> python2.6/site-packages/Sphinx-0.5.1-py2.6.egg/sphinx/builder.py\",\n> line 668, in finish\n>    for filename in os.listdir(staticdirname):\n> OSError: [Errno 2] No such file or directory: '/Applications/\n> sage_builds/sage-4.1.2.rc2-64-bit/local/notebook/javascript/jsmath'\n> The full traceback has been saved in /var/folders/JV/\n> JVYCpshdHd4FFoThuUgD8k+++TI/-Tmp-/sphinx-err-X1Sd6B.log, if you want\n> to report the issue to the author.\n> Please also report this if it was a user error, so that a better error\n> message can be provided next time.\n> Send reports to sphinx-dev@googlegroups.com. Thanks!\n> Build finished.  The built documents can be found in /Applications/\n> sage_builds/sage-4.1.2.rc2-64-bit/devel/sage/doc/output/html/en/\n> developer\n>\n> Did the directory \"SAGE_ROOT/local/notebook\" move some place else?\n\nYes, it did move -- it's now part of the sagenb spkg, and gets installed into python's site-package using Python's standard package data protocol. \n\nIs the build OK, but there is an error?  I.e., can this be safely fixed in the next SAge release.  Or do we have to fix it ASAP?\n\n\n\n> (Replace \"developer\" by \"tutorial\" or \"reference\" or whatever and the\n> same thing happens.  Omit \"--jsmath\" and it works just fine.  Building\n> PDF documentation seems to work fine, too, although I haven't finished\n> building the reference manual yet.)\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/7204\n\n",
    "closed_at": "2009-10-31T15:30:36Z",
    "created_at": "2009-10-14T02:19:49Z",
    "labels": [
        "component: documentation",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2.1",
    "title": "issue building sage docs since notebook moved",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7204",
    "user": "https://github.com/williamstein"
}
```
Assignee: tba

CC:  @jhpalmieri

```
>> If nobody finds any serious problems with it, something close to it
>> will get released (though I'm not in a hurry).
>
> Here's a nonserious problem: running "sage -docbuild developer html --
> jsmath" prints an error message.  At the end of the build process, I
> get this error:
>
> copying static files... Exception occurred:
>  File "/Applications/sage_builds/sage-4.1.2.rc2-64-bit/local/lib/
> python2.6/site-packages/Sphinx-0.5.1-py2.6.egg/sphinx/builder.py",
> line 668, in finish
>    for filename in os.listdir(staticdirname):
> OSError: [Errno 2] No such file or directory: '/Applications/
> sage_builds/sage-4.1.2.rc2-64-bit/local/notebook/javascript/jsmath'
> The full traceback has been saved in /var/folders/JV/
> JVYCpshdHd4FFoThuUgD8k+++TI/-Tmp-/sphinx-err-X1Sd6B.log, if you want
> to report the issue to the author.
> Please also report this if it was a user error, so that a better error
> message can be provided next time.
> Send reports to sphinx-dev@googlegroups.com. Thanks!
> Build finished.  The built documents can be found in /Applications/
> sage_builds/sage-4.1.2.rc2-64-bit/devel/sage/doc/output/html/en/
> developer
>
> Did the directory "SAGE_ROOT/local/notebook" move some place else?

Yes, it did move -- it's now part of the sagenb spkg, and gets installed into python's site-package using Python's standard package data protocol. 

Is the build OK, but there is an error?  I.e., can this be safely fixed in the next SAge release.  Or do we have to fix it ASAP?



> (Replace "developer" by "tutorial" or "reference" or whatever and the
> same thing happens.  Omit "--jsmath" and it works just fine.  Building
> PDF documentation seems to work fine, too, although I haven't finished
> building the reference manual yet.)
```

Issue created by migration from https://trac.sagemath.org/ticket/7204





---

archive/issue_comments_059664.json:
```json
{
    "body": "Depends on #7196.",
    "created_at": "2009-10-14T11:34:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7204#issuecomment-59664",
    "user": "https://github.com/qed777"
}
```

Depends on #7196.



---

archive/issue_comments_059665.json:
```json
{
    "body": "Attachment [trac_7204-sagenb_doc_jsmath.patch](tarball://root/attachments/some-uuid/ticket7204/trac_7204-sagenb_doc_jsmath.patch) by @qed777 created at 2009-10-14 11:34:55",
    "created_at": "2009-10-14T11:34:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7204#issuecomment-59665",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7204-sagenb_doc_jsmath.patch](tarball://root/attachments/some-uuid/ticket7204/trac_7204-sagenb_doc_jsmath.patch) by @qed777 created at 2009-10-14 11:34:55



---

archive/issue_comments_059666.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-14T11:34:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7204#issuecomment-59666",
    "user": "https://github.com/qed777"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_059667.json:
```json
{
    "body": "Note that a version of this was already merged into 4.1.2, though not depending on the #7196.  This will probably necessitate a change in the patch.",
    "created_at": "2009-10-15T19:35:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7204#issuecomment-59667",
    "user": "https://github.com/kcrisman"
}
```

Note that a version of this was already merged into 4.1.2, though not depending on the #7196.  This will probably necessitate a change in the patch.



---

archive/issue_comments_059668.json:
```json
{
    "body": "Attachment [trac_7204-sagenb_doc_jsmath_v2.patch](tarball://root/attachments/some-uuid/ticket7204/trac_7204-sagenb_doc_jsmath_v2.patch) by @qed777 created at 2009-10-15 20:05:23\n\nDepends on the released 4.1.2 and #7196.  Apply only this patch.",
    "created_at": "2009-10-15T20:05:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7204#issuecomment-59668",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_7204-sagenb_doc_jsmath_v2.patch](tarball://root/attachments/some-uuid/ticket7204/trac_7204-sagenb_doc_jsmath_v2.patch) by @qed777 created at 2009-10-15 20:05:23

Depends on the released 4.1.2 and #7196.  Apply only this patch.



---

archive/issue_comments_059669.json:
```json
{
    "body": "Thanks for pointing that out.  Version 2 applies on top of the patch with no name.",
    "created_at": "2009-10-15T20:07:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7204#issuecomment-59669",
    "user": "https://github.com/qed777"
}
```

Thanks for pointing that out.  Version 2 applies on top of the patch with no name.



---

archive/issue_comments_059670.json:
```json
{
    "body": "It should also be pointed out that I plan to count this ticket as closed for 4.1.2, but that it should ALSO be counted as being close for 4.2.alpha0 in the official notes; it's silly to open a new ticket for this as long as attribution is somewhere.  I'm changing authorship to indicate this, since I just finished Minh's work on the release announcement for 4.1.2.",
    "created_at": "2009-10-15T20:12:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7204#issuecomment-59670",
    "user": "https://github.com/kcrisman"
}
```

It should also be pointed out that I plan to count this ticket as closed for 4.1.2, but that it should ALSO be counted as being close for 4.2.alpha0 in the official notes; it's silly to open a new ticket for this as long as attribution is somewhere.  I'm changing authorship to indicate this, since I just finished Minh's work on the release announcement for 4.1.2.



---

archive/issue_comments_059671.json:
```json
{
    "body": "Patch v3 at #6673 subsumes v2 here.  If/when the former merges, please close this ticket.",
    "created_at": "2009-10-21T18:48:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7204#issuecomment-59671",
    "user": "https://github.com/qed777"
}
```

Patch v3 at #6673 subsumes v2 here.  If/when the former merges, please close this ticket.



---

archive/issue_events_017066.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-31T15:30:36Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7204",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7204#event-17066"
}
```



---

archive/issue_comments_059672.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-31T15:30:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7204",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7204#issuecomment-59672",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
