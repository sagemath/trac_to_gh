# Issue 5489: add a non library level interface to 4ti2 to Sage

archive/issues_005489.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5489\n\n",
    "created_at": "2009-03-11T18:05:10Z",
    "labels": [
        "component: interfaces"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.4",
    "title": "add a non library level interface to 4ti2 to Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5489",
    "user": "https://github.com/mwhansen"
}
```
Assignee: @williamstein



Issue created by migration from https://trac.sagemath.org/ticket/5489





---

archive/issue_comments_042533.json:
```json
{
    "body": "Attachment [4ti2.sage](tarball://root/attachments/some-uuid/ticket5489/4ti2.sage) by @mwhansen created at 2009-03-11 18:05:25",
    "created_at": "2009-03-11T18:05:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5489#issuecomment-42533",
    "user": "https://github.com/mwhansen"
}
```

Attachment [4ti2.sage](tarball://root/attachments/some-uuid/ticket5489/4ti2.sage) by @mwhansen created at 2009-03-11 18:05:25



---

archive/issue_comments_042534.json:
```json
{
    "body": "Attachment [4ti2_interface.patch](tarball://root/attachments/some-uuid/ticket5489/4ti2_interface.patch) by broune created at 2009-06-26 16:42:10",
    "created_at": "2009-06-26T16:42:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5489#issuecomment-42534",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```

Attachment [4ti2_interface.patch](tarball://root/attachments/some-uuid/ticket5489/4ti2_interface.patch) by broune created at 2009-06-26 16:42:10



---

archive/issue_comments_042535.json:
```json
{
    "body": "The patch 4ti2_interface.patch builds on mhansens work. It adds the method groebner, which computes Toric grobner bases, and adds documentation and doctests. It also updates the code so that it can be built as part of Sage.\n\nYou need 4ti2 installed to review this, but the experimental spkg from 2006 is incompatible with this patch. Download 4ti2 from www.4ti2.de and put the binaries from that somewhere on your Sage path. E.g. dumping them in sage/local/bin will work.\n\nPatch applies cleanly to Sage 4.0.1 and doctests pass on my Mac.",
    "created_at": "2009-06-26T16:47:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5489#issuecomment-42535",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```

The patch 4ti2_interface.patch builds on mhansens work. It adds the method groebner, which computes Toric grobner bases, and adds documentation and doctests. It also updates the code so that it can be built as part of Sage.

You need 4ti2 installed to review this, but the experimental spkg from 2006 is incompatible with this patch. Download 4ti2 from www.4ti2.de and put the binaries from that somewhere on your Sage path. E.g. dumping them in sage/local/bin will work.

Patch applies cleanly to Sage 4.0.1 and doctests pass on my Mac.



---

archive/issue_comments_042536.json:
```json
{
    "body": "**Review**\n\n* the docstrings are not according to the current Sage standard.\n* IMHO one should update the experimental 4ti2 spkg in parallel with accepting this patch\n* how much hassle would it be to replace docs like \n\n```\nRuns the 4ti2 program ``qsolve`` on the parameters. See ``http://www.4ti2.de/`` for details. \n```\n\n   with docs which describe the program somewhat?\n* patch applies cleanly against 4.1.1.\n* `devel/sage/sage/interfaces/four_ti_2.py # 9 doctests failed` if 4ti2 is not installed, because `#optional` tag is missing",
    "created_at": "2009-08-18T10:58:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5489#issuecomment-42536",
    "user": "https://github.com/malb"
}
```

**Review**

* the docstrings are not according to the current Sage standard.
* IMHO one should update the experimental 4ti2 spkg in parallel with accepting this patch
* how much hassle would it be to replace docs like 

```
Runs the 4ti2 program ``qsolve`` on the parameters. See ``http://www.4ti2.de/`` for details. 
```

   with docs which describe the program somewhat?
* patch applies cleanly against 4.1.1.
* `devel/sage/sage/interfaces/four_ti_2.py # 9 doctests failed` if 4ti2 is not installed, because `#optional` tag is missing



---

archive/issue_comments_042537.json:
```json
{
    "body": "Thank you for the review. Could you tell me what needs to change in the docstring format? I'm willing to fix this, as well as add the #optional tags, if that is all that is needed for acceptance of the patch.\n\nInlining the 4ti2 documentation from 4ti2 into Sage opens the issue of licenses. I do not know what license is used for the 4ti2 documentation, and I don't think this is explicit anywhere. I agree it would be an improvement, though this would have to wait until someone (not me) in future volunteers to investigate the 4ti2 license for documentation.\n\nI agree it would be good to update the experimental 4ti2 spkg, which is however beyond the scope of what I'm willing to do on this at this time. If this is a requirement of acceptance of the patch, it will have to wait until someone chooses to update the 4ti2 spkg.",
    "created_at": "2009-08-22T00:09:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5489#issuecomment-42537",
    "user": "https://trac.sagemath.org/admin/accounts/users/broune"
}
```

Thank you for the review. Could you tell me what needs to change in the docstring format? I'm willing to fix this, as well as add the #optional tags, if that is all that is needed for acceptance of the patch.

Inlining the 4ti2 documentation from 4ti2 into Sage opens the issue of licenses. I do not know what license is used for the 4ti2 documentation, and I don't think this is explicit anywhere. I agree it would be an improvement, though this would have to wait until someone (not me) in future volunteers to investigate the 4ti2 license for documentation.

I agree it would be good to update the experimental 4ti2 spkg, which is however beyond the scope of what I'm willing to do on this at this time. If this is a requirement of acceptance of the patch, it will have to wait until someone chooses to update the 4ti2 spkg.



---

archive/issue_comments_042538.json:
```json
{
    "body": "Replying to [comment:3 broune]:\n> Thank you for the review. Could you tell me what needs to change in the docstring format? I'm willing to fix this, as well as add the #optional tags, if that is all that is needed for acceptance of the patch.\n\nI don't have answers for your other questions, but for this one:\n\n(1) \"EXAMPLES:\" should be changed to \"EXAMPLES::\"  (double colon), and it should be followed by a blank line.\n\n(2) In the `__init__` method at the beginning of the file, the INPUT block is not formatted correctly: after the first line, the other lines should be indented so that they line up with ```directory``` (as you've done later).\n\n(3) In all of your INPUT blocks, the leading hyphens should not be indented: they should line up with the \"I\" in \"INPUT\".\n\n(4) A few methods have blank lines after the initial `r\"\"\"`.  I think those should be deleted.",
    "created_at": "2009-11-19T22:36:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5489#issuecomment-42538",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:3 broune]:
> Thank you for the review. Could you tell me what needs to change in the docstring format? I'm willing to fix this, as well as add the #optional tags, if that is all that is needed for acceptance of the patch.

I don't have answers for your other questions, but for this one:

(1) "EXAMPLES:" should be changed to "EXAMPLES::"  (double colon), and it should be followed by a blank line.

(2) In the `__init__` method at the beginning of the file, the INPUT block is not formatted correctly: after the first line, the other lines should be indented so that they line up with ```directory``` (as you've done later).

(3) In all of your INPUT blocks, the leading hyphens should not be indented: they should line up with the "I" in "INPUT".

(4) A few methods have blank lines after the initial `r"""`.  I think those should be deleted.



---

archive/issue_comments_042539.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2011-03-29T03:16:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5489#issuecomment-42539",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_042540.json:
```json
{
    "body": "I believe I have addressed all the comments of jhpalmieri above.  It is true that better descriptions of the functionality would be nice, but I think this is OK for inclusion anyway - sometimes the perfect is the enemy of the good.\n\nAlthough it does not have a positive review (please someone take a look!) please test this against [http://trac.sagemath.org/sage_trac/ticket/8217](http://trac.sagemath.org/sage_trac/ticket/8217).",
    "created_at": "2011-03-29T03:20:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5489#issuecomment-42540",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

I believe I have addressed all the comments of jhpalmieri above.  It is true that better descriptions of the functionality would be nice, but I think this is OK for inclusion anyway - sometimes the perfect is the enemy of the good.

Although it does not have a positive review (please someone take a look!) please test this against [http://trac.sagemath.org/sage_trac/ticket/8217](http://trac.sagemath.org/sage_trac/ticket/8217).



---

archive/issue_comments_042541.json:
```json
{
    "body": "Attachment [trac_5489_4ti2_interface.patch](tarball://root/attachments/some-uuid/ticket5489/trac_5489_4ti2_interface.patch) by mhampton created at 2011-03-29 03:24:58\n\nCumulative patch",
    "created_at": "2011-03-29T03:24:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5489#issuecomment-42541",
    "user": "https://trac.sagemath.org/admin/accounts/users/mhampton"
}
```

Attachment [trac_5489_4ti2_interface.patch](tarball://root/attachments/some-uuid/ticket5489/trac_5489_4ti2_interface.patch) by mhampton created at 2011-03-29 03:24:58

Cumulative patch



---

archive/issue_comments_042542.json:
```json
{
    "body": "Apply trac_5489_4ti2_interface.patch\n\n(for the patchbot)",
    "created_at": "2012-03-10T17:16:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5489#issuecomment-42542",
    "user": "https://github.com/loefflerd"
}
```

Apply trac_5489_4ti2_interface.patch

(for the patchbot)



---

archive/issue_comments_042543.json:
```json
{
    "body": "The code looks good, the doc coverage is 100% and the tests pass. I am almost ready to give a positive review.\n\nI have only some basic comments:\n\n* there is a typo here in \"does\" (in the method directory)\n\n\n```\n# method since apparently importing sage.misc.misc oes not\n```\n\n\n* Why not gather these import statements at the beginning ?\n\n\n```\n from sage.matrix.constructor import matrix \n from sage.matrix.matrix import is_Matrix \n from sage.rings.integer_ring import ZZ \n import subprocess\n```\n\n\nIf there is no technical difficulty (as for sage.misc.misc), it seems better to import them once and for all. At least those about matrices and integers ?\n\n* There seem to be some 'trailing whitespaces' that could be removed. All the lines just after an EXAMPLES:: should rather be empty.\n\n* The minimize method is NotImplemented. This can of course wait for another ticket.",
    "created_at": "2012-07-24T20:15:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5489#issuecomment-42543",
    "user": "https://github.com/fchapoton"
}
```

The code looks good, the doc coverage is 100% and the tests pass. I am almost ready to give a positive review.

I have only some basic comments:

* there is a typo here in "does" (in the method directory)


```
# method since apparently importing sage.misc.misc oes not
```


* Why not gather these import statements at the beginning ?


```
 from sage.matrix.constructor import matrix 
 from sage.matrix.matrix import is_Matrix 
 from sage.rings.integer_ring import ZZ 
 import subprocess
```


If there is no technical difficulty (as for sage.misc.misc), it seems better to import them once and for all. At least those about matrices and integers ?

* There seem to be some 'trailing whitespaces' that could be removed. All the lines just after an EXAMPLES:: should rather be empty.

* The minimize method is NotImplemented. This can of course wait for another ticket.



---

archive/issue_comments_042544.json:
```json
{
    "body": "Please fill in your real name as Author.",
    "created_at": "2012-07-27T20:43:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5489#issuecomment-42544",
    "user": "https://github.com/jdemeyer"
}
```

Please fill in your real name as Author.



---

archive/issue_comments_042545.json:
```json
{
    "body": "Attachment [trac_5489_4ti2_interface-reviewer.patch](tarball://root/attachments/some-uuid/ticket5489/trac_5489_4ti2_interface-reviewer.patch) by @fchapoton created at 2012-08-26 19:23:34",
    "created_at": "2012-08-26T19:23:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5489#issuecomment-42545",
    "user": "https://github.com/fchapoton"
}
```

Attachment [trac_5489_4ti2_interface-reviewer.patch](tarball://root/attachments/some-uuid/ticket5489/trac_5489_4ti2_interface-reviewer.patch) by @fchapoton created at 2012-08-26 19:23:34



---

archive/issue_comments_042546.json:
```json
{
    "body": "Apply only: trac_5489_4ti2_interface-reviewer.patch",
    "created_at": "2012-08-26T19:25:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5489#issuecomment-42546",
    "user": "https://github.com/fchapoton"
}
```

Apply only: trac_5489_4ti2_interface-reviewer.patch



---

archive/issue_comments_042547.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-08-26T19:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5489#issuecomment-42547",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_042548.json:
```json
{
    "body": "I have made some small changes that I suggested, in a new patch. The bot is green, and everything looks good. Positive review !",
    "created_at": "2012-08-26T19:49:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5489#issuecomment-42548",
    "user": "https://github.com/fchapoton"
}
```

I have made some small changes that I suggested, in a new patch. The bot is green, and everything looks good. Positive review !



---

archive/issue_events_012841.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-08-27T11:09:27Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5489",
    "milestone": "sage-5.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5489#event-12841"
}
```



---

archive/issue_events_012842.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-09-03T12:51:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5489",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5489#event-12842"
}
```



---

archive/issue_comments_042549.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-09-03T12:51:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5489",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5489#issuecomment-42549",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
