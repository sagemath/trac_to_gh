# Issue 3467: [with patch, needs review] implements @parallel decorator using dsage

archive/issues_003467.json:
```json
{
    "body": "Assignee: tbd\n\nHere's how to use it:\n\nsage: d = dsage.start_all()\nSpawned twistd -d /Users/yqiang/.sage/dsage --pidfile=server.pid --logfile=/Users/yqiang/.sage/dsage/server.log -y dsage_server.tac (pid = 73563)\n\nSpawned python /Users/yqiang/Software/sage-3.0.3.rc0/local/bin/dsage_worker.py -s localhost -p 8083 -u yqiang -w 2 --poll 1.0 -l 0 -f /Users/yqiang/.sage/dsage/worker.log --privkey=/Users/yqiang/.sage/dsage/dsage_key --pubkey=/Users/yqiang/.sage/dsage/dsage_key.pub --priority=20 --ssl --noblock (pid = 73571)\n\nsage: P = parallel(p_iter = d.parallel_iter)\nsage: `@`P\n....: def MS1(N,k):\n....:     return ModularSymbols(N,k,sign=1).decomposition(10)[0]\n....: \nsage: time v = MS1([(250,2), (11,2), (37,2)])\n\nIssue created by migration from https://trac.sagemath.org/ticket/3467\n\n",
    "created_at": "2008-06-19T02:11:52Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] implements @parallel decorator using dsage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3467",
    "user": "yi"
}
```
Assignee: tbd

Here's how to use it:

sage: d = dsage.start_all()
Spawned twistd -d /Users/yqiang/.sage/dsage --pidfile=server.pid --logfile=/Users/yqiang/.sage/dsage/server.log -y dsage_server.tac (pid = 73563)

Spawned python /Users/yqiang/Software/sage-3.0.3.rc0/local/bin/dsage_worker.py -s localhost -p 8083 -u yqiang -w 2 --poll 1.0 -l 0 -f /Users/yqiang/.sage/dsage/worker.log --privkey=/Users/yqiang/.sage/dsage/dsage_key --pubkey=/Users/yqiang/.sage/dsage/dsage_key.pub --priority=20 --ssl --noblock (pid = 73571)

sage: P = parallel(p_iter = d.parallel_iter)
sage: `@`P
....: def MS1(N,k):
....:     return ModularSymbols(N,k,sign=1).decomposition(10)[0]
....: 
sage: time v = MS1([(250,2), (11,2), (37,2)])

Issue created by migration from https://trac.sagemath.org/ticket/3467





---

archive/issue_comments_024443.json:
```json
{
    "body": "Changing assignee from tbd to yi.",
    "created_at": "2008-06-19T02:12:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3467#issuecomment-24443",
    "user": "yi"
}
```

Changing assignee from tbd to yi.



---

archive/issue_comments_024444.json:
```json
{
    "body": "Changing component from algebra to dsage.",
    "created_at": "2008-06-19T02:12:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3467#issuecomment-24444",
    "user": "yi"
}
```

Changing component from algebra to dsage.



---

archive/issue_comments_024445.json:
```json
{
    "body": "Attachment [dsage_interface.2.patch](tarball://root/attachments/some-uuid/ticket3467/dsage_interface.2.patch) by yi created at 2008-06-19 02:41:31",
    "created_at": "2008-06-19T02:41:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3467#issuecomment-24445",
    "user": "yi"
}
```

Attachment [dsage_interface.2.patch](tarball://root/attachments/some-uuid/ticket3467/dsage_interface.2.patch) by yi created at 2008-06-19 02:41:31



---

archive/issue_comments_024446.json:
```json
{
    "body": "Attachment [dsage_interface.patch](tarball://root/attachments/some-uuid/ticket3467/dsage_interface.patch) by yi created at 2008-06-19 04:04:33\n\nnew patch with doctests.",
    "created_at": "2008-06-19T04:04:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3467#issuecomment-24446",
    "user": "yi"
}
```

Attachment [dsage_interface.patch](tarball://root/attachments/some-uuid/ticket3467/dsage_interface.patch) by yi created at 2008-06-19 04:04:33

new patch with doctests.



---

archive/issue_comments_024447.json:
```json
{
    "body": "Attachment [dsage_interface.3.patch](tarball://root/attachments/some-uuid/ticket3467/dsage_interface.3.patch) by yi created at 2008-06-19 04:04:58\n\nOk, doctests are added.",
    "created_at": "2008-06-19T04:04:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3467#issuecomment-24447",
    "user": "yi"
}
```

Attachment [dsage_interface.3.patch](tarball://root/attachments/some-uuid/ticket3467/dsage_interface.3.patch) by yi created at 2008-06-19 04:04:58

Ok, doctests are added.



---

archive/issue_comments_024448.json:
```json
{
    "body": "Replying to [comment:3 yi]:\n> Ok, doctests are added.\nAlso, be sure to remove nodoctest.py in dsage/interface. For some reason MQ doesn't pick up that I removed the file.",
    "created_at": "2008-06-19T04:07:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3467#issuecomment-24448",
    "user": "yi"
}
```

Replying to [comment:3 yi]:
> Ok, doctests are added.
Also, be sure to remove nodoctest.py in dsage/interface. For some reason MQ doesn't pick up that I removed the file.



---

archive/issue_comments_024449.json:
```json
{
    "body": "All tests pass AFTER removing nodoctest.py from sage/dsage/interface .  Also, you should explicitly note the patches that this depends on (if any).",
    "created_at": "2008-06-19T21:24:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3467#issuecomment-24449",
    "user": "mhansen"
}
```

All tests pass AFTER removing nodoctest.py from sage/dsage/interface .  Also, you should explicitly note the patches that this depends on (if any).



---

archive/issue_comments_024450.json:
```json
{
    "body": "Attachment [dsage_interface.4.patch](tarball://root/attachments/some-uuid/ticket3467/dsage_interface.4.patch) by yi created at 2008-06-19 21:27:50",
    "created_at": "2008-06-19T21:27:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3467#issuecomment-24450",
    "user": "yi"
}
```

Attachment [dsage_interface.4.patch](tarball://root/attachments/some-uuid/ticket3467/dsage_interface.4.patch) by yi created at 2008-06-19 21:27:50



---

archive/issue_comments_024451.json:
```json
{
    "body": "dsage_interface.4.patch uses git style diffs which will remove nodoctest.py",
    "created_at": "2008-06-19T21:30:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3467#issuecomment-24451",
    "user": "yi"
}
```

dsage_interface.4.patch uses git style diffs which will remove nodoctest.py



---

archive/issue_comments_024452.json:
```json
{
    "body": "Yi,\n\ncould you please clarify which patches should be applied in which order? This likely also depends on some other patches to be applied first I assume in which case it would be great to note that on the ticket first, too.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-23T05:58:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3467#issuecomment-24452",
    "user": "mabshoff"
}
```

Yi,

could you please clarify which patches should be applied in which order? This likely also depends on some other patches to be applied first I assume in which case it would be great to note that on the ticket first, too.

Cheers,

Michael



---

archive/issue_comments_024453.json:
```json
{
    "body": "Please apply dsage_interface.4.patch. It is the only one you need. Also, this patch depends on getting #3458 merged in.",
    "created_at": "2008-06-23T20:00:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3467#issuecomment-24453",
    "user": "yi"
}
```

Please apply dsage_interface.4.patch. It is the only one you need. Also, this patch depends on getting #3458 merged in.



---

archive/issue_comments_024454.json:
```json
{
    "body": "Merged dsage_interface.3.patch in Sage 3.0.4.alpha1. I also removed the nodoctest manually.",
    "created_at": "2008-06-26T04:29:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3467#issuecomment-24454",
    "user": "mabshoff"
}
```

Merged dsage_interface.3.patch in Sage 3.0.4.alpha1. I also removed the nodoctest manually.



---

archive/issue_comments_024455.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-26T04:29:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3467",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3467#issuecomment-24455",
    "user": "mabshoff"
}
```

Resolution: fixed
