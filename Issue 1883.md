# Issue 1883: Sage distribution includes Windows executables

archive/issues_001883.json:
```json
{
    "body": "Assignee: mabshoff\n\nMy Sage installation includes 5 Windows executables: \n\n```\n./local/lib/gap-4.4.10/bin/gapw95.exe\n./local/lib/gap-4.4.10/bin/regtool.exe\n./local/lib/gap-4.4.10/bin/._regtool.exe\n./local/lib/gap-4.4.10/bin/rxvt.exe\n./local/lib/gap-4.4.10/bin/._rxvt.exe\n./local/lib/gap-4.4.10/bin/._gapw95.exe\n./local/lib/python2.5/distutils/command/wininst-6.exe\n./local/lib/python2.5/distutils/command/wininst-7.1.exe\n```\n\n(as well as three Macintosh resource forks for the corresponding Windows executable -- those files are doubly useless).\n\nThese files should be deleted from the corresponding spkgs.\n\nIssue created by migration from https://trac.sagemath.org/ticket/1883\n\n",
    "created_at": "2008-01-22T01:45:25Z",
    "labels": [
        "distribution",
        "major",
        "bug"
    ],
    "title": "Sage distribution includes Windows executables",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1883",
    "user": "cwitty"
}
```
Assignee: mabshoff

My Sage installation includes 5 Windows executables: 

```
./local/lib/gap-4.4.10/bin/gapw95.exe
./local/lib/gap-4.4.10/bin/regtool.exe
./local/lib/gap-4.4.10/bin/._regtool.exe
./local/lib/gap-4.4.10/bin/rxvt.exe
./local/lib/gap-4.4.10/bin/._rxvt.exe
./local/lib/gap-4.4.10/bin/._gapw95.exe
./local/lib/python2.5/distutils/command/wininst-6.exe
./local/lib/python2.5/distutils/command/wininst-7.1.exe
```

(as well as three Macintosh resource forks for the corresponding Windows executable -- those files are doubly useless).

These files should be deleted from the corresponding spkgs.

Issue created by migration from https://trac.sagemath.org/ticket/1883





---

archive/issue_comments_011923.json:
```json
{
    "body": "The updated gap spkg at \n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha1/gap-4.4.10.p1.spkg\n\nremoves the executables, a number of DLLs and about 1500 other files created by OSX, i.e. `._*`. As a result it shrunk from 8.4mb to 7.0mb\n\nCheers,\n\nMichael",
    "created_at": "2008-01-22T03:21:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1883#issuecomment-11923",
    "user": "mabshoff"
}
```

The updated gap spkg at 

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha1/gap-4.4.10.p1.spkg

removes the executables, a number of DLLs and about 1500 other files created by OSX, i.e. `._*`. As a result it shrunk from 8.4mb to 7.0mb

Cheers,

Michael



---

archive/issue_comments_011924.json:
```json
{
    "body": "The python spkg at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha1/python-2.5.1.p13.spkg\n\nremoves the two executables mentioned above.\n\nCheers,\n\nMichael",
    "created_at": "2008-01-22T05:54:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1883#issuecomment-11924",
    "user": "mabshoff"
}
```

The python spkg at

http://sage.math.washington.edu/home/mabshoff/release-cycles-2.10.1/alpha1/python-2.5.1.p13.spkg

removes the two executables mentioned above.

Cheers,

Michael



---

archive/issue_comments_011925.json:
```json
{
    "body": "Both spkgs merged in Sage 2.10.1.alpha1",
    "created_at": "2008-01-22T05:54:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1883#issuecomment-11925",
    "user": "mabshoff"
}
```

Both spkgs merged in Sage 2.10.1.alpha1



---

archive/issue_comments_011926.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-22T05:54:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1883",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1883#issuecomment-11926",
    "user": "mabshoff"
}
```

Resolution: fixed
