# Issue 2150: vmware sage image -- switch to using optimal 7zip compression

archive/issues_002150.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nThe best compression I got was with the following command\n\n\nc:\\\"program files\"\\7-zip\\7z a -t7z sage.7z sage -mx=9 -mfb=256\n\n\nthis breaks down as follows :  c:\\\"program files\"\\7-zip\\7z : path to the executable\n                           : 7z requires \"dll's\" 7za is complete\n                           : a : this is the add command\n                           : -t7z : use LZMA compression\n                           : sage.7z : output file name\n                           : sage  : input directory name\n                           : -mx9  : use ultra compression options\n                           : -mfb=256 : increase bit compare string to 256 bytes\ntime differential from base compression is roughly 30% 1:20 VS 1:00\n\nthis cuts the size from 522 to about 467\n\nI hope this is useful It should save your downloaders 10min to who knows what\n\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2150\n\n",
    "created_at": "2008-02-13T20:18:22Z",
    "labels": [
        "distribution",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "vmware sage image -- switch to using optimal 7zip compression",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2150",
    "user": "was"
}
```
Assignee: mabshoff


```
The best compression I got was with the following command


c:\"program files"\7-zip\7z a -t7z sage.7z sage -mx=9 -mfb=256


this breaks down as follows :  c:\"program files"\7-zip\7z : path to the executable
                           : 7z requires "dll's" 7za is complete
                           : a : this is the add command
                           : -t7z : use LZMA compression
                           : sage.7z : output file name
                           : sage  : input directory name
                           : -mx9  : use ultra compression options
                           : -mfb=256 : increase bit compare string to 256 bytes
time differential from base compression is roughly 30% 1:20 VS 1:00

this cuts the size from 522 to about 467

I hope this is useful It should save your downloaders 10min to who knows what


```


Issue created by migration from https://trac.sagemath.org/ticket/2150





---

archive/issue_comments_014112.json:
```json
{
    "body": "For 2.10.4 we the 7z compressed image is ` sage-vmware-2.10.3.7z   11-Mar-2008 21:35  486M ` in size. So it looks like this might have been fixed. \n\nWilliam, can you gives me some input on this? If you fixed this ticket please close it.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-20T04:24:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2150#issuecomment-14112",
    "user": "mabshoff"
}
```

For 2.10.4 we the 7z compressed image is ` sage-vmware-2.10.3.7z   11-Mar-2008 21:35  486M ` in size. So it looks like this might have been fixed. 

William, can you gives me some input on this? If you fixed this ticket please close it.

Cheers,

Michael



---

archive/issue_comments_014113.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-20T10:29:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2150",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2150#issuecomment-14113",
    "user": "was"
}
```

Resolution: fixed
