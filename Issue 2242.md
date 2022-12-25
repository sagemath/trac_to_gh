# Issue 2242: [with spkg and patch, positive review] optional nauty package

archive/issues_002242.json:
```json
{
    "body": "Assignee: @rlmill\n\nIt's available here:\n\nhttp://sage.math.washington.edu/home/jason/nauty-24b7.spkg\n\nIt is the 2.4 beta 7 version, since Brendan says that it is pretty stable.  It would be trivial to make a nauty 2.2 stable version if people wanted it.\n\nThis is the spkg for #1301.  Now we just need to make the interface in Sage.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2242\n\n",
    "closed_at": "2008-04-07T21:40:41Z",
    "created_at": "2008-02-21T00:41:09Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with spkg and patch, positive review] optional nauty package",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2242",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @rlmill

It's available here:

http://sage.math.washington.edu/home/jason/nauty-24b7.spkg

It is the 2.4 beta 7 version, since Brendan says that it is pretty stable.  It would be trivial to make a nauty 2.2 stable version if people wanted it.

This is the spkg for #1301.  Now we just need to make the interface in Sage.

Issue created by migration from https://trac.sagemath.org/ticket/2242





---

archive/issue_comments_014821.json:
```json
{
    "body": "I mean, it is the spkg for #1301 (not #1306).",
    "created_at": "2008-02-21T00:41:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2242#issuecomment-14821",
    "user": "https://github.com/jasongrout"
}
```

I mean, it is the spkg for #1301 (not #1306).



---

archive/issue_comments_014822.json:
```json
{
    "body": "To use this right now, for example, to generate the graphs of order 3, do:\n\n```\nsage: a=os.popen(\"nauty-geng 3\").read().split()\n>A nauty-geng -d0D2 n=3 e=0-3\n>Z 4 graphs generated in 0.00 sec\nsage: a\n['B?', 'BO', 'BW', 'Bw']\nsage: graph_list = [Graph(i) for i in a]\nsage: graph_list\n\n[Graph on 3 vertices,\n Graph on 3 vertices,\n Graph on 3 vertices,\n Graph on 3 vertices]\n```",
    "created_at": "2008-02-21T00:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2242#issuecomment-14822",
    "user": "https://github.com/jasongrout"
}
```

To use this right now, for example, to generate the graphs of order 3, do:

```
sage: a=os.popen("nauty-geng 3").read().split()
>A nauty-geng -d0D2 n=3 e=0-3
>Z 4 graphs generated in 0.00 sec
sage: a
['B?', 'BO', 'BW', 'Bw']
sage: graph_list = [Graph(i) for i in a]
sage: graph_list

[Graph on 3 vertices,
 Graph on 3 vertices,
 Graph on 3 vertices,
 Graph on 3 vertices]
```



---

archive/issue_comments_014823.json:
```json
{
    "body": "Or, for a pretty picture:\n\n```\nsage: graph_list = [Graph(g) for g in os.popen(\"nauty-geng -l 4\").read().split()]\n>A nauty-geng -ld0D3 n=4 e=0-6\n>Z 11 graphs generated in 0.00 sec\nsage: show(graph_list)\nsage: # to compare to Robert Miller's NICE algorithm in Sage:\nsage: show(graphs(4))\n```",
    "created_at": "2008-02-21T01:01:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2242#issuecomment-14823",
    "user": "https://github.com/jasongrout"
}
```

Or, for a pretty picture:

```
sage: graph_list = [Graph(g) for g in os.popen("nauty-geng -l 4").read().split()]
>A nauty-geng -ld0D3 n=4 e=0-6
>Z 11 graphs generated in 0.00 sec
sage: show(graph_list)
sage: # to compare to Robert Miller's NICE algorithm in Sage:
sage: show(graphs(4))
```



---

archive/issue_comments_014824.json:
```json
{
    "body": "I've added a patch which implements the graphs.nauty_geng() command (basically doing what the examples above do).\n\nThe patch depends on the is_package_installed function, which won't appear until 2.10.2.",
    "created_at": "2008-02-21T01:33:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2242#issuecomment-14824",
    "user": "https://github.com/jasongrout"
}
```

I've added a patch which implements the graphs.nauty_geng() command (basically doing what the examples above do).

The patch depends on the is_package_installed function, which won't appear until 2.10.2.



---

archive/issue_comments_014825.json:
```json
{
    "body": "Attachment [nauty_geng.patch](tarball://root/attachments/some-uuid/ticket2242/nauty_geng.patch) by @rlmill created at 2008-02-21 07:15:51\n\nIs there a better way to call nauty than from the command line? Is there some way to call the functions directly, by compiling nauty as a shared object, dynamic library, or something?",
    "created_at": "2008-02-21T07:15:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2242#issuecomment-14825",
    "user": "https://github.com/rlmill"
}
```

Attachment [nauty_geng.patch](tarball://root/attachments/some-uuid/ticket2242/nauty_geng.patch) by @rlmill created at 2008-02-21 07:15:51

Is there a better way to call nauty than from the command line? Is there some way to call the functions directly, by compiling nauty as a shared object, dynamic library, or something?



---

archive/issue_comments_014826.json:
```json
{
    "body": "Excuse my ignorance, but isn't Nauty *obsolete* since rlm implemented Nice? Why is there the need for Nauty? You guys probably have a good reason but it would be nice to mention it somewhere :-)",
    "created_at": "2008-02-21T09:57:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2242#issuecomment-14826",
    "user": "https://github.com/malb"
}
```

Excuse my ignorance, but isn't Nauty *obsolete* since rlm implemented Nice? Why is there the need for Nauty? You guys probably have a good reason but it would be nice to mention it somewhere :-)



---

archive/issue_comments_014827.json:
```json
{
    "body": "rlm: It is best to call the automorphism group computation or the canonical label computation from the library function.  However, many utility programs (like the planarity checker, etc.) are not readily available as libraries.  The geng program (generates graphs with certain constraints) can be modified to compile as a library.  This was clearly a quick \"get it working\" solution to generate feedback and get something that was useful.  It sounds like it's succeeding on both accounts.\n\nmalb: NICE does implement the main algorithms that are implemented in nauty.  However, nauty is more comprehensive and much more mature.  It is also much faster in some cases that I checked (automorphism groups of cycles and generation of graphs).  Having an optional spkg allows us to use the functionality while NICE continues to improve and also provides a timing and correctness benchmark for NICE.",
    "created_at": "2008-02-21T10:11:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2242#issuecomment-14827",
    "user": "https://github.com/jasongrout"
}
```

rlm: It is best to call the automorphism group computation or the canonical label computation from the library function.  However, many utility programs (like the planarity checker, etc.) are not readily available as libraries.  The geng program (generates graphs with certain constraints) can be modified to compile as a library.  This was clearly a quick "get it working" solution to generate feedback and get something that was useful.  It sounds like it's succeeding on both accounts.

malb: NICE does implement the main algorithms that are implemented in nauty.  However, nauty is more comprehensive and much more mature.  It is also much faster in some cases that I checked (automorphism groups of cycles and generation of graphs).  Having an optional spkg allows us to use the functionality while NICE continues to improve and also provides a timing and correctness benchmark for NICE.



---

archive/issue_comments_014828.json:
```json
{
    "body": "rlm: is there a way to create a cython library interface for an optional spkg?  I would love to create a cython interface to the library functions, but the cython needs to be compiled and put into the sage system when the nauty package is installed, not when sage is compiled.",
    "created_at": "2008-02-21T10:15:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2242#issuecomment-14828",
    "user": "https://github.com/jasongrout"
}
```

rlm: is there a way to create a cython library interface for an optional spkg?  I would love to create a cython interface to the library functions, but the cython needs to be compiled and put into the sage system when the nauty package is installed, not when sage is compiled.



---

archive/issue_comments_014829.json:
```json
{
    "body": "Replying to [comment:11 jason]:\n> rlm: is there a way to create a cython library interface for an optional spkg?  I would love to create a cython interface to the library functions, but the cython needs to be compiled and put into the sage system when the nauty package is installed, not when sage is compiled.\n> \n\n\nSo far there is now way to do this, at least I am not aware of any way to do this. The ticket to fix this is #2088.\n\nCheers,\n\nMichael",
    "created_at": "2008-02-21T12:22:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2242#issuecomment-14829",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Replying to [comment:11 jason]:
> rlm: is there a way to create a cython library interface for an optional spkg?  I would love to create a cython interface to the library functions, but the cython needs to be compiled and put into the sage system when the nauty package is installed, not when sage is compiled.
> 


So far there is now way to do this, at least I am not aware of any way to do this. The ticket to fix this is #2088.

Cheers,

Michael



---

archive/issue_comments_014830.json:
```json
{
    "body": "Attachment [2242.patch](tarball://root/attachments/some-uuid/ticket2242/2242.patch) by @mwhansen created at 2008-04-07 08:45:48\n\nI think this should go in now.  I've updated the patch against 3.0.alpha2, and only 2242.patch should be applied.  The spkg installs fine on sage.math, and the code passes tests.",
    "created_at": "2008-04-07T08:45:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2242#issuecomment-14830",
    "user": "https://github.com/mwhansen"
}
```

Attachment [2242.patch](tarball://root/attachments/some-uuid/ticket2242/2242.patch) by @mwhansen created at 2008-04-07 08:45:48

I think this should go in now.  I've updated the patch against 3.0.alpha2, and only 2242.patch should be applied.  The spkg installs fine on sage.math, and the code passes tests.



---

archive/issue_comments_014831.json:
```json
{
    "body": "I agree that the spkg is alright. Some things like the license confirmation are unavoidable, the internal structure of the spkg is a little odd. But for an optional spkg it ought to be enough.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-07T21:37:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2242#issuecomment-14831",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I agree that the spkg is alright. Some things like the license confirmation are unavoidable, the internal structure of the spkg is a little odd. But for an optional spkg it ought to be enough.

Cheers,

Michael



---

archive/issue_events_005328.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-04-07T21:40:41Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2242",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2242#event-5328"
}
```



---

archive/issue_comments_014832.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-07T21:40:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2242#issuecomment-14832",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_014833.json:
```json
{
    "body": "Merged 2242.patch in Sage 3.0.alpha3. Add nauty-24b7.spkg into the optional spkg repo on sagemath.org and mirrored it out.",
    "created_at": "2008-04-07T21:40:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2242",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2242#issuecomment-14833",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 2242.patch in Sage 3.0.alpha3. Add nauty-24b7.spkg into the optional spkg repo on sagemath.org and mirrored it out.
