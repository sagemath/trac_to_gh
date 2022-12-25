# Issue 3686: trivial problems in extcode.spkg

archive/issues_003686.json:
```json
{
    "body": "Assignee: mabshoff\n\nBelow is a list trivial problems in the excode spkg that were found by Debian's automatic package quality checking tools:\n\n# Scripts missing #!/bin/sh lines in extcode-3.0.5.spkg:\nmirror\npari/dokchitser/testall\nspkg-dist\n\n# Files unnecessarily marked as executable in extcode-3.0.5.spkg\njavascript/jsmath/plugins/autoload.js\njavascript/jsmath/plugins/CHMmode.js\nnotebook/javascript/jsmath/plugins/autoload.js\nnotebook/javascript/jsmath/plugins/CHMmode.js\nnotebook/javascript/farbtastic/marker.png\n\n# Empty directories in extcode-3.0.5.spkg\n# (These look like they might have a purpose, but I'm not sure)\ndist/\ngap/user/\ngenus2reduction/\ngnuplot/\nmacaulay2/user/\nmaple/user/\nmathematica/user/\nmatlab/user/\noctave/user/\nsage/user/\nsingular/user/\nsobj/\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3686\n\n",
    "created_at": "2008-07-21T05:44:51Z",
    "labels": [
        "component: packages: standard",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.1",
    "title": "trivial problems in extcode.spkg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3686",
    "user": "https://github.com/timabbott"
}
```
Assignee: mabshoff

Below is a list trivial problems in the excode spkg that were found by Debian's automatic package quality checking tools:

# Scripts missing #!/bin/sh lines in extcode-3.0.5.spkg:
mirror
pari/dokchitser/testall
spkg-dist

# Files unnecessarily marked as executable in extcode-3.0.5.spkg
javascript/jsmath/plugins/autoload.js
javascript/jsmath/plugins/CHMmode.js
notebook/javascript/jsmath/plugins/autoload.js
notebook/javascript/jsmath/plugins/CHMmode.js
notebook/javascript/farbtastic/marker.png

# Empty directories in extcode-3.0.5.spkg
# (These look like they might have a purpose, but I'm not sure)
dist/
gap/user/
genus2reduction/
gnuplot/
macaulay2/user/
maple/user/
mathematica/user/
matlab/user/
octave/user/
sage/user/
singular/user/
sobj/


Issue created by migration from https://trac.sagemath.org/ticket/3686





---

archive/issue_comments_026076.json:
```json
{
    "body": "Let's display that readably:\n\n# Scripts missing #!/bin/sh lines in extcode-3.0.5.spkg:\n\n```\nmirror\npari/dokchitser/testall\nspkg-dist\n```\n\n\n# Files unnecessarily marked as executable in extcode-3.0.5.spkg\n\n```\njavascript/jsmath/plugins/autoload.js\njavascript/jsmath/plugins/CHMmode.js\nnotebook/javascript/jsmath/plugins/autoload.js\nnotebook/javascript/jsmath/plugins/CHMmode.js\nnotebook/javascript/farbtastic/marker.png\n```\n\n\n# Empty directories in extcode-3.0.5.spkg\n# (These look like they might have a purpose, but I'm not sure)\n\n```\ndist/\ngap/user/\ngenus2reduction/\ngnuplot/\nmacaulay2/user/\nmaple/user/\nmathematica/user/\nmatlab/user/\noctave/user/\nsage/user/\nsingular/user/\nsobj/\n```\n",
    "created_at": "2008-07-21T05:51:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3686#issuecomment-26076",
    "user": "https://github.com/timabbott"
}
```

Let's display that readably:

# Scripts missing #!/bin/sh lines in extcode-3.0.5.spkg:

```
mirror
pari/dokchitser/testall
spkg-dist
```


# Files unnecessarily marked as executable in extcode-3.0.5.spkg

```
javascript/jsmath/plugins/autoload.js
javascript/jsmath/plugins/CHMmode.js
notebook/javascript/jsmath/plugins/autoload.js
notebook/javascript/jsmath/plugins/CHMmode.js
notebook/javascript/farbtastic/marker.png
```


# Empty directories in extcode-3.0.5.spkg
# (These look like they might have a purpose, but I'm not sure)

```
dist/
gap/user/
genus2reduction/
gnuplot/
macaulay2/user/
maple/user/
mathematica/user/
matlab/user/
octave/user/
sage/user/
singular/user/
sobj/
```




---

archive/issue_comments_026077.json:
```json
{
    "body": "Attachment [extcode_shebang.patch](tarball://root/attachments/some-uuid/ticket3686/extcode_shebang.patch) by @timabbott created at 2008-08-03 05:45:46\n\nThe Debian people made me fix all these problems myself, so I've attached patches to fix the #! lines to each of these tickets.  You'll have to remove the executable bits yourself, since I seem to recall mercurial doesn't support that.\n\nBy the way, the empty directories in the extcode spkg are for the Sage pexpect wrapper, and can't be deleted.  The others can.",
    "created_at": "2008-08-03T05:45:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3686#issuecomment-26077",
    "user": "https://github.com/timabbott"
}
```

Attachment [extcode_shebang.patch](tarball://root/attachments/some-uuid/ticket3686/extcode_shebang.patch) by @timabbott created at 2008-08-03 05:45:46

The Debian people made me fix all these problems myself, so I've attached patches to fix the #! lines to each of these tickets.  You'll have to remove the executable bits yourself, since I seem to recall mercurial doesn't support that.

By the way, the empty directories in the extcode spkg are for the Sage pexpect wrapper, and can't be deleted.  The others can.



---

archive/issue_comments_026078.json:
```json
{
    "body": "As well as applying the attached patch, one should run\n\n```\nchmod -x notebook/javascript/farbtastic/marker.png javascript/jsmath/plugins/CHMmode.js \nchmod -x javascript/jsmath/plugins/autoload.js notebook/javascript/jsmath/plugins/CHMmode.js \nchmod -x javascript/jsmath/plugins/CHMmode.js\n```\n\nfrom the root of the extcode spkg in order to close this ticket.",
    "created_at": "2009-04-26T05:31:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3686#issuecomment-26078",
    "user": "https://github.com/timabbott"
}
```

As well as applying the attached patch, one should run

```
chmod -x notebook/javascript/farbtastic/marker.png javascript/jsmath/plugins/CHMmode.js 
chmod -x javascript/jsmath/plugins/autoload.js notebook/javascript/jsmath/plugins/CHMmode.js 
chmod -x javascript/jsmath/plugins/CHMmode.js
```

from the root of the extcode spkg in order to close this ticket.



---

archive/issue_comments_026079.json:
```json
{
    "body": "notebook/javascript/jsmath/plugins/CHMmode.js does not seem to exist in extcode-4.1 otherwise the rest seems OK.",
    "created_at": "2009-07-21T16:26:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3686#issuecomment-26079",
    "user": "https://github.com/maxthemouse"
}
```

notebook/javascript/jsmath/plugins/CHMmode.js does not seem to exist in extcode-4.1 otherwise the rest seems OK.



---

archive/issue_comments_026080.json:
```json
{
    "body": "I applied the patch and ran the chmod commands as suggested above. Ignoring the change in one file, everything else worked. \n\nNote: I applied #3686, #3687, #3688 and #3689 at the same time as my machine is a bit slow (8800 s to run all tests). I changed the packages, did a full build from source and ran 'make testlong'. Everything built and all tests passed. This is with Sage-4.1.",
    "created_at": "2009-07-22T06:00:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3686#issuecomment-26080",
    "user": "https://github.com/maxthemouse"
}
```

I applied the patch and ran the chmod commands as suggested above. Ignoring the change in one file, everything else worked. 

Note: I applied #3686, #3687, #3688 and #3689 at the same time as my machine is a bit slow (8800 s to run all tests). I changed the packages, did a full build from source and ran 'make testlong'. Everything built and all tests passed. This is with Sage-4.1.



---

archive/issue_events_003908.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-07-23T09:52:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3686",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3686#event-3908"
}
```



---

archive/issue_comments_026081.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-23T09:52:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3686",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3686#issuecomment-26081",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
