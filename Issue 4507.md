# Issue 4507: compile warning for planarity code

archive/issues_004507.json:
```json
{
    "body": "Assignee: @rlmill\n\nCC:  ekirkman bober\n\nI get the following compile warning:\n\n\n```\ngcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/home/jason/sage/local//include -I/home/jason/sage/local//include/csage -I/home/jason/sage/devel//sage/sage/ext -I/home/jason/sage/local/include/python2.5 -c sage/graphs/planarity/graphEmbed.c -o build/temp.linux-i686-2.5/sage/graphs/planarity/graphEmbed.o\nsage/graphs/planarity/graphEmbed.c: In function \u2018_CreateSortedSeparatedDFSChildLists\u2019:\nsage/graphs/planarity/graphEmbed.c:84: warning: implicit declaration of function \u2018memset\u2019\nsage/graphs/planarity/graphEmbed.c:84: warning: incompatible implicit declaration of built-in function \u2018memset\u2019\n\n```\n\n\nI fixed this by adding #include <string.h> (which declares the memset function) to listcoll.h (where the LCReset macro is defined).\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4507\n\n",
    "created_at": "2008-11-13T01:24:07Z",
    "labels": [
        "component: graph theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2",
    "title": "compile warning for planarity code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4507",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @rlmill

CC:  ekirkman bober

I get the following compile warning:


```
gcc -fno-strict-aliasing -DNDEBUG -g -fwrapv -O3 -Wall -Wstrict-prototypes -fPIC -I/home/jason/sage/local//include -I/home/jason/sage/local//include/csage -I/home/jason/sage/devel//sage/sage/ext -I/home/jason/sage/local/include/python2.5 -c sage/graphs/planarity/graphEmbed.c -o build/temp.linux-i686-2.5/sage/graphs/planarity/graphEmbed.o
sage/graphs/planarity/graphEmbed.c: In function ‘_CreateSortedSeparatedDFSChildLists’:
sage/graphs/planarity/graphEmbed.c:84: warning: implicit declaration of function ‘memset’
sage/graphs/planarity/graphEmbed.c:84: warning: incompatible implicit declaration of built-in function ‘memset’

```


I fixed this by adding #include <string.h> (which declares the memset function) to listcoll.h (where the LCReset macro is defined).


Issue created by migration from https://trac.sagemath.org/ticket/4507





---

archive/issue_comments_033351.json:
```json
{
    "body": "Attachment [memset-not-declared.patch](tarball://root/attachments/some-uuid/ticket4507/memset-not-declared.patch) by @jasongrout created at 2008-11-13 01:24:59",
    "created_at": "2008-11-13T01:24:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4507#issuecomment-33351",
    "user": "https://github.com/jasongrout"
}
```

Attachment [memset-not-declared.patch](tarball://root/attachments/some-uuid/ticket4507/memset-not-declared.patch) by @jasongrout created at 2008-11-13 01:24:59



---

archive/issue_comments_033352.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-13T03:24:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4507#issuecomment-33352",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_comments_033353.json:
```json
{
    "body": "Merged in Sage 3.2.rc1",
    "created_at": "2008-11-13T04:50:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4507#issuecomment-33353",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.rc1



---

archive/issue_comments_033354.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-13T04:50:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4507",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4507#issuecomment-33354",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
