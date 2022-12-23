# Issue 3633: [witch patch, needs review] use commands.getoutput in hostinfo

archive/issues_003633.json:
```json
{
    "body": "Assignee: rlm\n\nFor some reason twisted trial is not too happy with using os.popen. Switching to commands.getouput to fetch system information on the mac seems to work better.\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3633\n\n",
    "created_at": "2008-07-10T16:55:53Z",
    "labels": [
        "dsage",
        "major",
        "bug"
    ],
    "title": "[witch patch, needs review] use commands.getoutput in hostinfo",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3633",
    "user": "yi"
}
```
Assignee: rlm

For some reason twisted trial is not too happy with using os.popen. Switching to commands.getouput to fetch system information on the mac seems to work better.



Issue created by migration from https://trac.sagemath.org/ticket/3633





---

archive/issue_comments_025698.json:
```json
{
    "body": "Attachment\n\nRobert: commands.getoutput gets the output of a command. This is a little bit better than doing os.popen (what I was doing before) since it actually correctly opens/closes the pipes. \n\n\n```\nDefinition:\tcommands.getstatusoutput(cmd)\nSource:\ndef getstatusoutput(cmd):\n    \"\"\"Return (status, output) of executing cmd in a shell.\"\"\"\n    import os\n    pipe = os.popen('{ ' + cmd + '; } 2>&1', 'r')\n    text = pipe.read()\n    sts = pipe.close()\n    if sts is None: sts = 0\n    if text[-1:] == '\\n': text = text[:-1]\n    return sts, text\n```\n",
    "created_at": "2008-07-10T17:06:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3633#issuecomment-25698",
    "user": "yi"
}
```

Attachment

Robert: commands.getoutput gets the output of a command. This is a little bit better than doing os.popen (what I was doing before) since it actually correctly opens/closes the pipes. 


```
Definition:	commands.getstatusoutput(cmd)
Source:
def getstatusoutput(cmd):
    """Return (status, output) of executing cmd in a shell."""
    import os
    pipe = os.popen('{ ' + cmd + '; } 2>&1', 'r')
    text = pipe.read()
    sts = pipe.close()
    if sts is None: sts = 0
    if text[-1:] == '\n': text = text[:-1]
    return sts, text
```




---

archive/issue_comments_025699.json:
```json
{
    "body": "+1",
    "created_at": "2008-07-10T17:07:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3633#issuecomment-25699",
    "user": "rlm"
}
```

+1



---

archive/issue_comments_025700.json:
```json
{
    "body": "Changing assignee from rlm to yi.",
    "created_at": "2008-08-10T03:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3633#issuecomment-25700",
    "user": "rlm"
}
```

Changing assignee from rlm to yi.



---

archive/issue_comments_025701.json:
```json
{
    "body": "This is doctested indirectly, so I am not concerned here about the doctest. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-08-10T04:57:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3633#issuecomment-25701",
    "user": "mabshoff"
}
```

This is doctested indirectly, so I am not concerned here about the doctest. Positive review.

Cheers,

Michael



---

archive/issue_comments_025702.json:
```json
{
    "body": "Merged in Sage 3.1.alpha1",
    "created_at": "2008-08-10T05:13:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3633#issuecomment-25702",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.alpha1



---

archive/issue_comments_025703.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-10T05:13:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3633",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3633#issuecomment-25703",
    "user": "mabshoff"
}
```

Resolution: fixed
