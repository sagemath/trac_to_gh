# Issue 3375: Fix building ntl on Solaris with make and ld [with patch needs review]

archive/issues_003375.json:
```json
{
    "body": "Assignee: mabshoff\n\nCC:  polybori-discuss@lists.sourceforge.net\n\nOK so here is what got me through ntl on David's box.\nThe mfile patch is against the copy in the ntl patch folder \nnot the source. It also patch ntl spkg-install to properly\nsetup and tune ntl as well as cleaning the installation bits\nintroduced to accommodate Tim & I.\nI guess Tim and I will have to fend for ourselves separately.\nAlso we submitted a lot of patch in the ntl style. Since\nI used some GNU-ism for building shared objects most of\nthem will have to be revised.\n\nFrancois\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3375\n\n",
    "created_at": "2008-06-06T01:22:51Z",
    "labels": [
        "component: build",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Fix building ntl on Solaris with make and ld [with patch needs review]",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3375",
    "user": "https://github.com/kiwifb"
}
```
Assignee: mabshoff

CC:  polybori-discuss@lists.sourceforge.net

OK so here is what got me through ntl on David's box.
The mfile patch is against the copy in the ntl patch folder 
not the source. It also patch ntl spkg-install to properly
setup and tune ntl as well as cleaning the installation bits
introduced to accommodate Tim & I.
I guess Tim and I will have to fend for ourselves separately.
Also we submitted a lot of patch in the ntl style. Since
I used some GNU-ism for building shared objects most of
them will have to be revised.

Francois


Issue created by migration from https://trac.sagemath.org/ticket/3375





---

archive/issue_comments_023553.json:
```json
{
    "body": "patch for ntl spkg-install and patch/mfile",
    "created_at": "2008-06-06T01:23:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3375#issuecomment-23553",
    "user": "https://github.com/kiwifb"
}
```

patch for ntl spkg-install and patch/mfile



---

archive/issue_comments_023554.json:
```json
{
    "body": "Changing keywords from \"\" to \"editor_mabshoff\".",
    "created_at": "2008-06-15T21:52:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3375#issuecomment-23554",
    "user": "https://github.com/craigcitro"
}
```

Changing keywords from "" to "editor_mabshoff".



---

archive/issue_comments_023555.json:
```json
{
    "body": "Attachment [ntl-sun.patch](tarball://root/attachments/some-uuid/ticket3375/ntl-sun.patch) by @craigcitro created at 2008-06-15 21:52:48",
    "created_at": "2008-06-15T21:52:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3375#issuecomment-23555",
    "user": "https://github.com/craigcitro"
}
```

Attachment [ntl-sun.patch](tarball://root/attachments/some-uuid/ticket3375/ntl-sun.patch) by @craigcitro created at 2008-06-15 21:52:48



---

archive/issue_comments_023556.json:
```json
{
    "body": "Hi Francois, \n\nUnless I am overlooking something you are removing the \"-fPIC\" lines from the link phase. Are you sure that will work?\n\nCheers,\n\nMichael",
    "created_at": "2008-06-20T04:10:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3375#issuecomment-23556",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi Francois, 

Unless I am overlooking something you are removing the "-fPIC" lines from the link phase. Are you sure that will work?

Cheers,

Michael



---

archive/issue_comments_023557.json:
```json
{
    "body": "It works all right on linux (no text relocations) but I indeed \ncannot guaranty it on other platform. I just checked the gcc \nmanual and they recommand passing the PIC flag used during \ncompilation as well when using -shared so best to put it back:\n\n`-shared'\n     Produce a shared object which can then be linked with other\n     objects to form an executable.  Not all systems support this\noption.  For predictable results, you must also specify the same\n     set of options that were used to generate code (`-fpic', `-fPIC',\n     or model suboptions) when you specify this option.(1)",
    "created_at": "2008-06-20T08:43:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3375#issuecomment-23557",
    "user": "https://github.com/kiwifb"
}
```

It works all right on linux (no text relocations) but I indeed 
cannot guaranty it on other platform. I just checked the gcc 
manual and they recommand passing the PIC flag used during 
compilation as well when using -shared so best to put it back:

`-shared'
     Produce a shared object which can then be linked with other
     objects to form an executable.  Not all systems support this
option.  For predictable results, you must also specify the same
     set of options that were used to generate code (`-fpic', `-fPIC',
     or model suboptions) when you specify this option.(1)



---

archive/issue_events_007606.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3375",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3375#event-7606"
}
```



---

archive/issue_events_007607.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3375",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3375#event-7607"
}
```



---

archive/issue_events_007608.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3375",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3375#event-7608"
}
```



---

archive/issue_events_007609.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3375",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3375#event-7609"
}
```



---

archive/issue_events_007610.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3375",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3375#event-7610"
}
```



---

archive/issue_events_007611.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3375",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3375#event-7611"
}
```



---

archive/issue_events_007612.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3375",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3375#event-7612"
}
```



---

archive/issue_comments_023558.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-02-22T23:05:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3375#issuecomment-23558",
    "user": "https://github.com/kiwifb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_023559.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-02-22T23:07:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3375#issuecomment-23559",
    "user": "https://github.com/kiwifb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_023560.json:
```json
{
    "body": "Looking through old tickets this is sooo obsolete. Won't fix/invalid.",
    "created_at": "2015-02-22T23:07:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3375#issuecomment-23560",
    "user": "https://github.com/kiwifb"
}
```

Looking through old tickets this is sooo obsolete. Won't fix/invalid.



---

archive/issue_events_007613.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-02-23T21:00:19Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3375",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3375#event-7613"
}
```



---

archive/issue_events_007614.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-02-23T21:00:19Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/3375",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3375#event-7614"
}
```



---

archive/issue_comments_023561.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2015-02-23T21:00:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3375",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3375#issuecomment-23561",
    "user": "https://github.com/vbraun"
}
```

Resolution: invalid



---

archive/issue_events_007615.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2015-02-23T21:00:19Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3375",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3375#event-7615"
}
```
