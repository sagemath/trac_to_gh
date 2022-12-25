# Issue 2174: [bug day?] upgrade -- make upgrade() so that when run in the notebook it is not very verbose

archive/issues_002174.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  @williamstein\n\nMake it so in the notebook the upgrade command is very non-verbose.\nIn order to make this happen, we'll need to have an option to \n\"sage -i\" that makes sage-spkg much less verbose, i.e., just display\neach package is being built, and whether the install failed or\nsucceeded. \n\nAlso, upgrade() run in the notebook should autodect that it should\nrun non-verbosely by checking whether it is run in embedded mode (the\nsame as is done in plotting). \n\n \nThis is a defect, because right now if one types `upgrade()` into the notebook, because of verbosity of the output it can take 20 HOURS to upgrade, as reported by Jim Morrow. \n\nIssue created by migration from https://trac.sagemath.org/ticket/2174\n\n",
    "created_at": "2008-02-16T01:31:11Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "[bug day?] upgrade -- make upgrade() so that when run in the notebook it is not very verbose",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2174",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

CC:  @williamstein

Make it so in the notebook the upgrade command is very non-verbose.
In order to make this happen, we'll need to have an option to 
"sage -i" that makes sage-spkg much less verbose, i.e., just display
each package is being built, and whether the install failed or
succeeded. 

Also, upgrade() run in the notebook should autodect that it should
run non-verbosely by checking whether it is run in embedded mode (the
same as is done in plotting). 

 
This is a defect, because right now if one types `upgrade()` into the notebook, because of verbosity of the output it can take 20 HOURS to upgrade, as reported by Jim Morrow. 

Issue created by migration from https://trac.sagemath.org/ticket/2174





---

archive/issue_comments_014247.json:
```json
{
    "body": "This is related to #1439.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-16T01:37:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2174#issuecomment-14247",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This is related to #1439.

Cheers,

Michael



---

archive/issue_comments_014248.json:
```json
{
    "body": "Since how notebook runs commands has been massively redone, I believe this is fixed (#1439 is definitely fixed, and this is just an extension of it).",
    "created_at": "2010-01-18T00:58:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2174#issuecomment-14248",
    "user": "https://github.com/TimDumol"
}
```

Since how notebook runs commands has been massively redone, I believe this is fixed (#1439 is definitely fixed, and this is just an extension of it).



---

archive/issue_comments_014249.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-01-19T03:39:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2174",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2174#issuecomment-14249",
    "user": "https://github.com/TimDumol"
}
```

Resolution: fixed
