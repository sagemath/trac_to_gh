# Issue 3101: pbuild: mwrank.so needs to be build as a C++ extension

archive/issues_003101.json:
```json
{
    "body": "Assignee: gfurnish\n\nSome people have reported mwrank.so missing some symbols at startup when compiled with pbuild, but the old build system is fine.\n\nWorking:\n\n```\ng++ -pthread -shared build/temp.linux-x86_64-2.5/sage/libs/mwrank/mwrank.o \nbuild/temp.linux-x86_64-2.5/sage/libs/mwrank/wrap.o -L/scratch/mabshoff/\nrelease-cycle/sage-3.0.1.final/local//lib -lcsage -lcurvesntl -lg0nntl \n-ljcntl -lrankntl -lntl -lgmp -lgmpxx -lstdc++ -lm -lpari -lstdc++ -lntl \n-o build/lib.linux-x86_64-2.5/sage/libs/mwrank/mwrank.so\n```\n\n\nNon-working:\n\n```\ngcc -O3 -g -fwrapv -shared -fno-strict-aliasing /mnt/drive_hda1/sagefiles/\nsage-3.0.1.rc0/devel/sage/build/temp/sage/libs/mwrank/mwrank.o -L/home/wdj/\nwdj/sagefiles/sage-3.0.1.rc0/local/lib  -lcsage  -lcurvesntl  -lg0nntl  \n-ljcntl  -lrankntl  -lntl -lgmp  -lgmpxx  -lstdc++  -lm  -lpari  -lstdc++  \n-lntl  -o /mnt/drive_hda1/sagefiles/sage-3.0.1.rc0/devel/sage-main/build/\nsage/libs/mwrank/mwrank.so\n```\n\n\nmwrank.so is a C wrapper around a C++ extension, so on some systems the linker ends up either being stupid or clever depending on your perspective. \n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/3101\n\n",
    "created_at": "2008-05-04T04:12:24Z",
    "labels": [
        "pbuild",
        "blocker",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0.1",
    "title": "pbuild: mwrank.so needs to be build as a C++ extension",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3101",
    "user": "mabshoff"
}
```
Assignee: gfurnish

Some people have reported mwrank.so missing some symbols at startup when compiled with pbuild, but the old build system is fine.

Working:

```
g++ -pthread -shared build/temp.linux-x86_64-2.5/sage/libs/mwrank/mwrank.o 
build/temp.linux-x86_64-2.5/sage/libs/mwrank/wrap.o -L/scratch/mabshoff/
release-cycle/sage-3.0.1.final/local//lib -lcsage -lcurvesntl -lg0nntl 
-ljcntl -lrankntl -lntl -lgmp -lgmpxx -lstdc++ -lm -lpari -lstdc++ -lntl 
-o build/lib.linux-x86_64-2.5/sage/libs/mwrank/mwrank.so
```


Non-working:

```
gcc -O3 -g -fwrapv -shared -fno-strict-aliasing /mnt/drive_hda1/sagefiles/
sage-3.0.1.rc0/devel/sage/build/temp/sage/libs/mwrank/mwrank.o -L/home/wdj/
wdj/sagefiles/sage-3.0.1.rc0/local/lib  -lcsage  -lcurvesntl  -lg0nntl  
-ljcntl  -lrankntl  -lntl -lgmp  -lgmpxx  -lstdc++  -lm  -lpari  -lstdc++  
-lntl  -o /mnt/drive_hda1/sagefiles/sage-3.0.1.rc0/devel/sage-main/build/
sage/libs/mwrank/mwrank.so
```


mwrank.so is a C wrapper around a C++ extension, so on some systems the linker ends up either being stupid or clever depending on your perspective. 

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/3101





---

archive/issue_comments_021416.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-05-04T07:45:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3101#issuecomment-21416",
    "user": "gfurnish"
}
```

Changing status from new to assigned.



---

archive/issue_comments_021417.json:
```json
{
    "body": "Attachment [trac_extcode_3101.patch](tarball://root/attachments/some-uuid/ticket3101/trac_extcode_3101.patch) by gfurnish created at 2008-05-04 07:45:51",
    "created_at": "2008-05-04T07:45:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3101#issuecomment-21417",
    "user": "gfurnish"
}
```

Attachment [trac_extcode_3101.patch](tarball://root/attachments/some-uuid/ticket3101/trac_extcode_3101.patch) by gfurnish created at 2008-05-04 07:45:51



---

archive/issue_comments_021418.json:
```json
{
    "body": "Patch looks good to me.\n\nCheers,\n\nMichael",
    "created_at": "2008-05-04T08:08:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3101#issuecomment-21418",
    "user": "mabshoff"
}
```

Patch looks good to me.

Cheers,

Michael



---

archive/issue_comments_021419.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-04T08:08:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3101#issuecomment-21419",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_021420.json:
```json
{
    "body": "Merged in Sage 3.0.1.final",
    "created_at": "2008-05-04T08:08:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3101",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3101#issuecomment-21420",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.1.final
