# Issue 6900: Sage pexpect problems - suggestion to use upstream release

archive/issues_006900.json:
```json
{
    "body": "Assignee: boothby\n\nKeywords: pexpect\n\nSince pexpect is a very important package, I would like to point one problem that happens when DOT_SAGE is set to a long pathname, causing the SaveWorkspace(\"/path/to/$DOT_SAGE/gap/workspace-ext\");\ncommand in interfaces/gap.py fail (and possibly others).\n\n  Sample test case to reproduce the problem:\n\n% mkdir -p /tmp/0123456789/0123456789/0123456789/0123456789/0123456789/0123456789/0123456789/.sage\n<<make sure DOT_SAGE will point to that directory>>\n% sage\n<<exit sage>>\n% ls /tmp/0123456789/0123456789/0123456789/0123456789/0123456789/0123456789/0123456789/.sage/gap/\nREADME.txt\n<<change DOT_SAGE to something like just /tmp/0123456789/>>\n% sage\n<<exit sage>>\n% ls /tmp/0123456789/.sage/gap\nREADME.txt  workspace-1328071335\n\n  The problem is due to the command having more then 80 characters.\n\n  Currently sage uses pexpect-2.0 (patchlevel 4). And this is also one special case in my rpm packages of sage, because if using the latest upstream, in my case:\n% rpm -q python-pexpect\npython-pexpect-2.4-1mdv2010.0\nit works correctly in the terminal interface, but doesn't work correctly in the notebook interface.\n\n  A quick and dirty way to test a newer pexpect would be:\n% mkdir $HOME/tmp/sage-pexpect\n% mv $SAGE_ROOT/lib/python/site-packages/{ANSI,FSM,pexpect,pxssh,screen}.py $HOME/tmp/sage-pexpect\n% cp newer-python-pexpect/{ANSI,FSM,pexpect,pxssh,screen}.py $SAGE_ROOT/lib/python/site-packages\n% sage\nsage: notebook()\n\n  After starting the notebook, and using a newer pexpect, try some command that causes a background processes to be created, like the first singular example in the tutorial.\nA screenshot of the problem, that happens the first time a background process is started is:\nhttp://img134.imageshack.us/img134/557/sagewithnewerpexpect1.jpg\nbut, as also shown in the screenshot, in subsequent evaluations, it works correctly in the notebook.\n\n  Since it always works correct in the terminal interface of sage, I suspect it is an issue in the notebook/worksheet code. And in that case, it actually may be a different way to debug problems in the sage pexpect interface (also a suggestion :-)\n\nIssue created by migration from https://trac.sagemath.org/ticket/6900\n\n",
    "created_at": "2009-09-07T04:32:43Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Sage pexpect problems - suggestion to use upstream release",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6900",
    "user": "pcpa"
}
```
Assignee: boothby

Keywords: pexpect

Since pexpect is a very important package, I would like to point one problem that happens when DOT_SAGE is set to a long pathname, causing the SaveWorkspace("/path/to/$DOT_SAGE/gap/workspace-ext");
command in interfaces/gap.py fail (and possibly others).

  Sample test case to reproduce the problem:

% mkdir -p /tmp/0123456789/0123456789/0123456789/0123456789/0123456789/0123456789/0123456789/.sage
<<make sure DOT_SAGE will point to that directory>>
% sage
<<exit sage>>
% ls /tmp/0123456789/0123456789/0123456789/0123456789/0123456789/0123456789/0123456789/.sage/gap/
README.txt
<<change DOT_SAGE to something like just /tmp/0123456789/>>
% sage
<<exit sage>>
% ls /tmp/0123456789/.sage/gap
README.txt  workspace-1328071335

  The problem is due to the command having more then 80 characters.

  Currently sage uses pexpect-2.0 (patchlevel 4). And this is also one special case in my rpm packages of sage, because if using the latest upstream, in my case:
% rpm -q python-pexpect
python-pexpect-2.4-1mdv2010.0
it works correctly in the terminal interface, but doesn't work correctly in the notebook interface.

  A quick and dirty way to test a newer pexpect would be:
% mkdir $HOME/tmp/sage-pexpect
% mv $SAGE_ROOT/lib/python/site-packages/{ANSI,FSM,pexpect,pxssh,screen}.py $HOME/tmp/sage-pexpect
% cp newer-python-pexpect/{ANSI,FSM,pexpect,pxssh,screen}.py $SAGE_ROOT/lib/python/site-packages
% sage
sage: notebook()

  After starting the notebook, and using a newer pexpect, try some command that causes a background processes to be created, like the first singular example in the tutorial.
A screenshot of the problem, that happens the first time a background process is started is:
http://img134.imageshack.us/img134/557/sagewithnewerpexpect1.jpg
but, as also shown in the screenshot, in subsequent evaluations, it works correctly in the notebook.

  Since it always works correct in the terminal interface of sage, I suspect it is an issue in the notebook/worksheet code. And in that case, it actually may be a different way to debug problems in the sage pexpect interface (also a suggestion :-)

Issue created by migration from https://trac.sagemath.org/ticket/6900





---

archive/issue_comments_057004.json:
```json
{
    "body": "Replying to [ticket:6900 pcpa]:\n[Sorry for replying to myself]\n>   After starting the notebook, and using a newer pexpect, try some command that causes a background processes to be created, like the first singular example in the tutorial.\n> A screenshot of the problem, that happens the first time a background process is started is:\n> http://img134.imageshack.us/img134/557/sagewithnewerpexpect1.jpg\n> but, as also shown in the screenshot, in subsequent evaluations, it works correctly in the notebook.\n> \n>   Since it always works correct in the terminal interface of sage, I suspect it is an issue in the notebook/worksheet code. And in that case, it actually may be a different way to debug problems in the sage pexpect interface (also a suggestion :-)\n\n  For people familiar with the notebook code, I think what may be also a good hint as to what may be wrong is that the extra noise in the output is not \"really noise\", but the \"dancing\" / and \\ characters that go to the browser titlebar.",
    "created_at": "2009-09-08T14:17:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6900#issuecomment-57004",
    "user": "pcpa"
}
```

Replying to [ticket:6900 pcpa]:
[Sorry for replying to myself]
>   After starting the notebook, and using a newer pexpect, try some command that causes a background processes to be created, like the first singular example in the tutorial.
> A screenshot of the problem, that happens the first time a background process is started is:
> http://img134.imageshack.us/img134/557/sagewithnewerpexpect1.jpg
> but, as also shown in the screenshot, in subsequent evaluations, it works correctly in the notebook.
> 
>   Since it always works correct in the terminal interface of sage, I suspect it is an issue in the notebook/worksheet code. And in that case, it actually may be a different way to debug problems in the sage pexpect interface (also a suggestion :-)

  For people familiar with the notebook code, I think what may be also a good hint as to what may be wrong is that the extra noise in the output is not "really noise", but the "dancing" / and \ characters that go to the browser titlebar.



---

archive/issue_comments_057005.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-08-18T19:11:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6900#issuecomment-57005",
    "user": "aapitzsch"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_057006.json:
```json
{
    "body": "I cannot reproduce the problem.",
    "created_at": "2014-08-18T19:11:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6900#issuecomment-57006",
    "user": "aapitzsch"
}
```

I cannot reproduce the problem.



---

archive/issue_comments_057007.json:
```json
{
    "body": "You've got to do something with GAP, of course... but I agree that this seems to not be an issue now.\n\n```\n$ ls /tmp/0123456789/0123456789/0123456789/0123456789/0123456789/0123456789/0123456789/.sage/gap/\nREADME.txt                     workspace-8276014924322680366\n\n$ ls /tmp/0123456789/.sage/gap/\nREADME.txt\t\t\tworkspace-8276014924322680366\n```\n",
    "created_at": "2014-09-18T03:05:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6900#issuecomment-57007",
    "user": "kcrisman"
}
```

You've got to do something with GAP, of course... but I agree that this seems to not be an issue now.

```
$ ls /tmp/0123456789/0123456789/0123456789/0123456789/0123456789/0123456789/0123456789/.sage/gap/
README.txt                     workspace-8276014924322680366

$ ls /tmp/0123456789/.sage/gap/
README.txt			workspace-8276014924322680366
```




---

archive/issue_comments_057008.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-09-18T03:05:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6900#issuecomment-57008",
    "user": "kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_057009.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2014-09-18T17:58:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6900",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6900#issuecomment-57009",
    "user": "vbraun"
}
```

Resolution: worksforme
