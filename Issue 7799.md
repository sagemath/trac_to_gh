# Issue 7799: install_scripts should not install M2

archive/issues_007799.json:
```json
{
    "body": "Assignee: tbd\n\nI have done\n\n\n```\ninstall_scripts(\"/usr/local/bin/\")\n```\n\n\non a Ubuntu machine with installed Macaulay2 and it stopped working. Apparently, M2 is one of the scripts that the above command has copied and it tries to use M2 shipped with Sage. However, Sage does not include Macaulay2, the package for it is broken and the recommended way to use them together is to install Macaulay2 separately. This works fine before installing scripts and after, if I remove M2 from /usr/local/bin manually.\n\nIssue created by migration from https://trac.sagemath.org/ticket/7799\n\n",
    "created_at": "2009-12-31T01:50:51Z",
    "labels": [
        "distribution",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "install_scripts should not install M2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7799",
    "user": "novoselt"
}
```
Assignee: tbd

I have done


```
install_scripts("/usr/local/bin/")
```


on a Ubuntu machine with installed Macaulay2 and it stopped working. Apparently, M2 is one of the scripts that the above command has copied and it tries to use M2 shipped with Sage. However, Sage does not include Macaulay2, the package for it is broken and the recommended way to use them together is to install Macaulay2 separately. This works fine before installing scripts and after, if I remove M2 from /usr/local/bin manually.

Issue created by migration from https://trac.sagemath.org/ticket/7799





---

archive/issue_comments_067481.json:
```json
{
    "body": "Here's a patch.  I think that the problem is, in the old version, the command 'which M2' was executed, and if it didn't return a system error (meaning that M2 didn't exist), then it installed the Sage script.  The patch changes it so it checks if 'which M2' returns an error, and if not, then whether 'which M2' starts with SAGE_ROOT.  If not, then M2 is already installed elsewhere, so don't install the Sage script.  (Of course it does this for all of the scripts, not just for M2.)\n\nI've also added a doctest.\n\nWe could also worry about whether M2 should be included here at all, given its status.  I suggest that we keep it, since if my patch works the way I think, we should never install the script as long as we don't distribute a working version of M2, but if someone fixes the spkg for it, then we don't have to remember to reinstate it in 'install_scripts'.",
    "created_at": "2009-12-31T07:07:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7799#issuecomment-67481",
    "user": "jhpalmieri"
}
```

Here's a patch.  I think that the problem is, in the old version, the command 'which M2' was executed, and if it didn't return a system error (meaning that M2 didn't exist), then it installed the Sage script.  The patch changes it so it checks if 'which M2' returns an error, and if not, then whether 'which M2' starts with SAGE_ROOT.  If not, then M2 is already installed elsewhere, so don't install the Sage script.  (Of course it does this for all of the scripts, not just for M2.)

I've also added a doctest.

We could also worry about whether M2 should be included here at all, given its status.  I suggest that we keep it, since if my patch works the way I think, we should never install the script as long as we don't distribute a working version of M2, but if someone fixes the spkg for it, then we don't have to remember to reinstate it in 'install_scripts'.



---

archive/issue_comments_067482.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-31T07:07:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7799#issuecomment-67482",
    "user": "jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_067483.json:
```json
{
    "body": "Attachment [trac_7799-install-scripts.patch](tarball://root/attachments/some-uuid/ticket7799/trac_7799-install-scripts.patch) by jhpalmieri created at 2009-12-31 07:07:44\n\npatch for main Sage repository",
    "created_at": "2009-12-31T07:07:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7799#issuecomment-67483",
    "user": "jhpalmieri"
}
```

Attachment [trac_7799-install-scripts.patch](tarball://root/attachments/some-uuid/ticket7799/trac_7799-install-scripts.patch) by jhpalmieri created at 2009-12-31 07:07:44

patch for main Sage repository



---

archive/issue_comments_067484.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-31T19:46:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7799#issuecomment-67484",
    "user": "novoselt"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_067485.json:
```json
{
    "body": "Works fine for me, install_scripts does not break Macaulay2 with this patch.",
    "created_at": "2009-12-31T19:46:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7799#issuecomment-67485",
    "user": "novoselt"
}
```

Works fine for me, install_scripts does not break Macaulay2 with this patch.



---

archive/issue_comments_067486.json:
```json
{
    "body": "Another positive review from me.",
    "created_at": "2009-12-31T19:50:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7799#issuecomment-67486",
    "user": "was"
}
```

Another positive review from me.



---

archive/issue_comments_067487.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-03T20:42:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7799",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7799#issuecomment-67487",
    "user": "mhansen"
}
```

Resolution: fixed
