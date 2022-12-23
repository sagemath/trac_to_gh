# Issue 259: axiom bug

archive/issues_000259.json:
```json
{
    "body": "Assignee: was\n\n\n```\nIn sage-2.0 and sage-2.1.0.1 the first Axiom command that I enter\nhangs the sage process but if I hit control-c and re-enter the\ncommand, it works as it used to work. This also affects Axiom\ncommands entered via the notebook.\n \n  sage: axiom('1+1')\n  ... waits indefinitely ...\n  ^C\n  ...\n  sage: axiom('1+1')\n \n     2\n \n  sage:\n \n---------------\n \nI will take a look at the axiom inteface code when I get time\nbut perhaps someone already knows what might have changed in\nthe way the interface works?\n \nBTW, I am using the axiom4sage-0.1 download from sage.math but\nI had a problem with the simple\n \n  sage -I axiom4sage-0.1.spkg\n \ncommand. I apparently received only a partial download and the\ninstall failed. Later, I downloaded axiom4sage-0.1.spkg directly\nto the sage root directory and repeated the command:\n \n  sage -I axiom4sage-0.1.spkg\n \nThen Axiom was built and installed as expected on my OpenSuSE 10.2\nx86 linux system.\n \nRegards,\nBill Page.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/259\n\n",
    "created_at": "2007-02-11T23:01:58Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "axiom bug",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/259",
    "user": "was"
}
```
Assignee: was


```
In sage-2.0 and sage-2.1.0.1 the first Axiom command that I enter
hangs the sage process but if I hit control-c and re-enter the
command, it works as it used to work. This also affects Axiom
commands entered via the notebook.
 
  sage: axiom('1+1')
  ... waits indefinitely ...
  ^C
  ...
  sage: axiom('1+1')
 
     2
 
  sage:
 
---------------
 
I will take a look at the axiom inteface code when I get time
but perhaps someone already knows what might have changed in
the way the interface works?
 
BTW, I am using the axiom4sage-0.1 download from sage.math but
I had a problem with the simple
 
  sage -I axiom4sage-0.1.spkg
 
command. I apparently received only a partial download and the
install failed. Later, I downloaded axiom4sage-0.1.spkg directly
to the sage root directory and repeated the command:
 
  sage -I axiom4sage-0.1.spkg
 
Then Axiom was built and installed as expected on my OpenSuSE 10.2
x86 linux system.
 
Regards,
Bill Page.
```


Issue created by migration from https://trac.sagemath.org/ticket/259





---

archive/issue_comments_001204.json:
```json
{
    "body": "axiom is in too much flux right now.",
    "created_at": "2007-08-18T09:50:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/259#issuecomment-1204",
    "user": "was"
}
```

axiom is in too much flux right now.



---

archive/issue_comments_001205.json:
```json
{
    "body": "Can somebody test if this is still the case? The bug report is rather stale and the current optional axiom4sage.spkg is around version number 0.3.\n\nCheers,\n\nMichael",
    "created_at": "2007-09-10T02:33:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/259#issuecomment-1205",
    "user": "mabshoff"
}
```

Can somebody test if this is still the case? The bug report is rather stale and the current optional axiom4sage.spkg is around version number 0.3.

Cheers,

Michael



---

archive/issue_comments_001206.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2007-10-20T22:37:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/259#issuecomment-1206",
    "user": "cwitty"
}
```

Resolution: worksforme



---

archive/issue_comments_001207.json:
```json
{
    "body": "In sage 2.8.7.2 with axiom4sage 0.3.1, this works for me on 32-bit and 64-bit x86 linux.",
    "created_at": "2007-10-20T22:37:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/259",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/259#issuecomment-1207",
    "user": "cwitty"
}
```

In sage 2.8.7.2 with axiom4sage 0.3.1, this works for me on 32-bit and 64-bit x86 linux.
