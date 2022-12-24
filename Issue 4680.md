# Issue 4680: [with diff, needs new spkg] matplotlib configuration finds system-wide files on OSX

archive/issues_004680.json:
```json
{
    "body": "Assignee: mabshoff\n\nThe matplotlib install on OSX can find the system-wide files, leading to problems like this:\n\n\n```\nsage: from matplotlib import _png\nImportError: dlopen(/sage/local/lib/python/site-packages/matplotlib/_png.so, 2): Library not loaded: /usr/X11/lib/libpng12.0.dylib\n      Referenced from: /sage/local/lib/python/site-packages/matplotlib/_png.so\n      Reason: Incompatible library version: _png.so requires version 27.0.0 or later, but libpng12.0.dylib provides version 23.0.0\n```\n\n\nThe matplotlib config tries to look all over for libpng, but we only want it to find the sage specific one. The attached diff of `setupext.py` in `matplotlib-0.98.3.p3/patches/` tells it not to.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4680\n\n",
    "created_at": "2008-12-02T23:59:37Z",
    "labels": [
        "build",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.2",
    "title": "[with diff, needs new spkg] matplotlib configuration finds system-wide files on OSX",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4680",
    "user": "@craigcitro"
}
```
Assignee: mabshoff

The matplotlib install on OSX can find the system-wide files, leading to problems like this:


```
sage: from matplotlib import _png
ImportError: dlopen(/sage/local/lib/python/site-packages/matplotlib/_png.so, 2): Library not loaded: /usr/X11/lib/libpng12.0.dylib
      Referenced from: /sage/local/lib/python/site-packages/matplotlib/_png.so
      Reason: Incompatible library version: _png.so requires version 27.0.0 or later, but libpng12.0.dylib provides version 23.0.0
```


The matplotlib config tries to look all over for libpng, but we only want it to find the sage specific one. The attached diff of `setupext.py` in `matplotlib-0.98.3.p3/patches/` tells it not to.

Issue created by migration from https://trac.sagemath.org/ticket/4680





---

archive/issue_comments_035256.json:
```json
{
    "body": "Attachment [setupext.py.diff](tarball://root/attachments/some-uuid/ticket4680/setupext.py.diff) by @williamstein created at 2008-12-04 23:00:08\n\nlooks good to me...",
    "created_at": "2008-12-04T23:00:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4680#issuecomment-35256",
    "user": "@williamstein"
}
```

Attachment [setupext.py.diff](tarball://root/attachments/some-uuid/ticket4680/setupext.py.diff) by @williamstein created at 2008-12-04 23:00:08

looks good to me...



---

archive/issue_comments_035257.json:
```json
{
    "body": "I am building an updated spkg with the fix now. Sorry that this slipped off my radar.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-11T16:31:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4680#issuecomment-35257",
    "user": "mabshoff"
}
```

I am building an updated spkg with the fix now. Sorry that this slipped off my radar.

Cheers,

Michael



---

archive/issue_comments_035258.json:
```json
{
    "body": "The new spkg can be found at\n\nhttp://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.2/alpha2/matplotlib-0.98.3.p4.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-12-12T16:32:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4680#issuecomment-35258",
    "user": "mabshoff"
}
```

The new spkg can be found at

http://sage.math.washington.edu/home/mabshoff/release-cycles-3.2.2/alpha2/matplotlib-0.98.3.p4.spkg

Cheers,

Michael



---

archive/issue_comments_035259.json:
```json
{
    "body": "Merged in Sage 3.2.2.alpha2",
    "created_at": "2008-12-12T16:33:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4680#issuecomment-35259",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.2.alpha2



---

archive/issue_comments_035260.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-12-12T16:33:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4680",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4680#issuecomment-35260",
    "user": "mabshoff"
}
```

Resolution: fixed
