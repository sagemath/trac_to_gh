# Issue 5390: install_package, optional_package etc might pick the wrong sage installation

archive/issues_005390.json:
```json
{
    "body": "Assignee: mabshoff\n\nKeywords: package installation\n\n`package.py` provides various functions for obtaining a list of installed packages or installing new ones. In all these functions, `os.popen('sage')` is called.\n\nBut wouldn't this always try to call a system-wide sage installation? Then it would result in an error, if the running sage instance is from a local installation, and it may install packages in a wrong location if there is both a system wide and a local version of sage.\n\nIf this is really the case, then it might be better to give the full path to the currently running sage version, hence\n\n```\nos.popen('%s/sage'%(SAGE_ROOT))\n```\n\n\nThis is what the attached patch does.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5390\n\n",
    "created_at": "2009-02-27T09:45:02Z",
    "labels": [
        "packages: standard",
        "minor",
        "bug"
    ],
    "title": "install_package, optional_package etc might pick the wrong sage installation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5390",
    "user": "SimonKing"
}
```
Assignee: mabshoff

Keywords: package installation

`package.py` provides various functions for obtaining a list of installed packages or installing new ones. In all these functions, `os.popen('sage')` is called.

But wouldn't this always try to call a system-wide sage installation? Then it would result in an error, if the running sage instance is from a local installation, and it may install packages in a wrong location if there is both a system wide and a local version of sage.

If this is really the case, then it might be better to give the full path to the currently running sage version, hence

```
os.popen('%s/sage'%(SAGE_ROOT))
```


This is what the attached patch does.

Issue created by migration from https://trac.sagemath.org/ticket/5390





---

archive/issue_comments_041512.json:
```json
{
    "body": "Attachment\n\nMake sure that install_package picks the right sage version (sorry, it seems the previous attachment was corrupted)",
    "created_at": "2009-02-27T09:53:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5390#issuecomment-41512",
    "user": "SimonKing"
}
```

Attachment

Make sure that install_package picks the right sage version (sorry, it seems the previous attachment was corrupted)



---

archive/issue_comments_041513.json:
```json
{
    "body": "Replying to [ticket:5390 SimonKing]:\n> `package.py` provides various functions for obtaining a list of installed packages or installing new ones. In all these functions, `os.popen('sage')` is called.\n\nDetail: In one case, `os.system('sage -f ...') was called, which the patch also changes into SAGE_ROOT+'/sage'.",
    "created_at": "2009-02-27T10:02:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5390#issuecomment-41513",
    "user": "SimonKing"
}
```

Replying to [ticket:5390 SimonKing]:
> `package.py` provides various functions for obtaining a list of installed packages or installing new ones. In all these functions, `os.popen('sage')` is called.

Detail: In one case, `os.system('sage -f ...') was called, which the patch also changes into SAGE_ROOT+'/sage'.



---

archive/issue_comments_041514.json:
```json
{
    "body": "Hi Simon,\n\nonce Sage has been started `sage-env` sets PATH and LD_LIBRARY_PATH, so from inside Sage the right `sage` script is called. I do not really see a scenario where this patch would fix anything.\n\nI am marking this as needs work, but I really consider this as invalid.\n\nThoughts?\n\nCheers,\n\nMichael",
    "created_at": "2009-02-27T12:18:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5390#issuecomment-41514",
    "user": "mabshoff"
}
```

Hi Simon,

once Sage has been started `sage-env` sets PATH and LD_LIBRARY_PATH, so from inside Sage the right `sage` script is called. I do not really see a scenario where this patch would fix anything.

I am marking this as needs work, but I really consider this as invalid.

Thoughts?

Cheers,

Michael



---

archive/issue_comments_041515.json:
```json
{
    "body": "Hi Michael,\n\nReplying to [comment:2 mabshoff]:\n> once Sage has been started `sage-env` sets PATH and LD_LIBRARY_PATH, so from inside Sage the right `sage` script is called. I do not really see a scenario where this patch would fix anything.\n\nI know that Sage sets PATH, but I thought it would merely add `SAGE_LOCAL/bin` in front, but this folder does not contain `sage` (only `sage.bin`). \n\nBut if I am mistaken then certainly that ticket is invalid. It just struck me when by coincidence I was reading the code.\n\nCheers\n Simon",
    "created_at": "2009-02-27T18:56:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5390#issuecomment-41515",
    "user": "SimonKing"
}
```

Hi Michael,

Replying to [comment:2 mabshoff]:
> once Sage has been started `sage-env` sets PATH and LD_LIBRARY_PATH, so from inside Sage the right `sage` script is called. I do not really see a scenario where this patch would fix anything.

I know that Sage sets PATH, but I thought it would merely add `SAGE_LOCAL/bin` in front, but this folder does not contain `sage` (only `sage.bin`). 

But if I am mistaken then certainly that ticket is invalid. It just struck me when by coincidence I was reading the code.

Cheers
 Simon



---

archive/issue_comments_041516.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2009-02-27T22:58:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5390#issuecomment-41516",
    "user": "mabshoff"
}
```

Resolution: invalid



---

archive/issue_comments_041517.json:
```json
{
    "body": "Replying to [comment:3 SimonKing]:\n> Hi Michael,\n\nHi Simon,\n\n<SNIP>\n\n> I know that Sage sets PATH, but I thought it would merely add `SAGE_LOCAL/bin` in front, but this folder does not contain `sage` (only `sage.bin`). \n> \n> But if I am mistaken then certainly that ticket is invalid. It just struck me when by coincidence I was reading the code.\n\nYeah, but even *if* the env was messed up your fix does not resolve the problem since `$SAGE_ROOT` does in that case not get overwritten in sage-env, so you would call the wrong Sage even with your patch.\n\n> Cheers\n>  Simon\n\nCheers,\n\nMichael",
    "created_at": "2009-02-27T22:58:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5390",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5390#issuecomment-41517",
    "user": "mabshoff"
}
```

Replying to [comment:3 SimonKing]:
> Hi Michael,

Hi Simon,

<SNIP>

> I know that Sage sets PATH, but I thought it would merely add `SAGE_LOCAL/bin` in front, but this folder does not contain `sage` (only `sage.bin`). 
> 
> But if I am mistaken then certainly that ticket is invalid. It just struck me when by coincidence I was reading the code.

Yeah, but even *if* the env was messed up your fix does not resolve the problem since `$SAGE_ROOT` does in that case not get overwritten in sage-env, so you would call the wrong Sage even with your patch.

> Cheers
>  Simon

Cheers,

Michael
