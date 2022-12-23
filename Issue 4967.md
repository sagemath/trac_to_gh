# Issue 4967: [with patch] Trouble with .gaprc file when compiling from source

archive/issues_004967.json:
```json
{
    "body": "Assignee: mabshoff\n\n## How to reproduce the problem\n\n* Create a file called `~/.gaprc' containing the following line\n\n```\nColorPrompt(true);\n```\n\n* Compile sage from source\n* Start sage and try the following\n\n```\nsage: gap._eval_line('1+3;')\n'4\\n\\x1b[1m\\x1b[34mgap> \\x1b[0m'\n```\n\n\n## Solution\nAs William Stein suggested on sage-devel (Sat, 11 Oct 2008), changing line 169 of `gap.py' from \n\n```\ngap_cmd = \"gap\"\n```\n\nto \n\n```\ngap_cmd = \"gap -r\"\n```\n\nsolve the problem.\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4967\n\n",
    "created_at": "2009-01-12T16:50:51Z",
    "labels": [
        "distribution",
        "trivial",
        "bug"
    ],
    "title": "[with patch] Trouble with .gaprc file when compiling from source",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4967",
    "user": "mmeulien"
}
```
Assignee: mabshoff

## How to reproduce the problem

* Create a file called `~/.gaprc' containing the following line

```
ColorPrompt(true);
```

* Compile sage from source
* Start sage and try the following

```
sage: gap._eval_line('1+3;')
'4\n\x1b[1m\x1b[34mgap> \x1b[0m'
```


## Solution
As William Stein suggested on sage-devel (Sat, 11 Oct 2008), changing line 169 of `gap.py' from 

```
gap_cmd = "gap"
```

to 

```
gap_cmd = "gap -r"
```

solve the problem.




Issue created by migration from https://trac.sagemath.org/ticket/4967





---

archive/issue_comments_037798.json:
```json
{
    "body": "diff -c a/sage/interfaces/gap.py b/sage/interfaces/gap.py >> ticket.patch",
    "created_at": "2009-01-12T16:51:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4967#issuecomment-37798",
    "user": "mmeulien"
}
```

diff -c a/sage/interfaces/gap.py b/sage/interfaces/gap.py >> ticket.patch



---

archive/issue_comments_037799.json:
```json
{
    "body": "Attachment\n\nHi,\n\nany chance you can post a proper mercurial patch? The attachment is \"just\" a diff, but I can commit it in your name.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-17T16:56:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4967#issuecomment-37799",
    "user": "mabshoff"
}
```

Attachment

Hi,

any chance you can post a proper mercurial patch? The attachment is "just" a diff, but I can commit it in your name.

Cheers,

Michael



---

archive/issue_comments_037800.json:
```json
{
    "body": "Attachment",
    "created_at": "2009-01-18T05:11:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4967#issuecomment-37800",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_037801.json:
```json
{
    "body": "Positive review. I have attached a proper hg patch with check in credit given to Matthias Meulien.\n\nCheers,\n\nMichael",
    "created_at": "2009-01-18T05:13:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4967#issuecomment-37801",
    "user": "mabshoff"
}
```

Positive review. I have attached a proper hg patch with check in credit given to Matthias Meulien.

Cheers,

Michael



---

archive/issue_comments_037802.json:
```json
{
    "body": "Merged in Sage 3.3.alpha0",
    "created_at": "2009-01-18T05:13:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4967#issuecomment-37802",
    "user": "mabshoff"
}
```

Merged in Sage 3.3.alpha0



---

archive/issue_comments_037803.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-01-18T05:13:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4967",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4967#issuecomment-37803",
    "user": "mabshoff"
}
```

Resolution: fixed
