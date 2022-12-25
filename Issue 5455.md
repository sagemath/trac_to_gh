# Issue 5455: gap-4.4.12 -- broken on iras (itanium Linux)

archive/issues_005455.json:
```json
{
    "body": "Assignee: mabshoff\n\nSaving and loading workspaces is broke in gap Itanium (SUSE). Also, loading of any packages is now mysteriously broken:\n\n```\nsage: !gap\n    \n            #########           ######         ###########           ###  \n         #############          ######         ############         ####  \n        ##############         ########        #############       #####  \n       ###############         ########        #####   ######      #####  \n      ######         #         #########       #####    #####     ######  \n     ######                   ##########       #####    #####    #######  \n     #####                    ##### ####       #####   ######   ########  \n     ####                    #####  #####      #############   ###  ####  \n     #####     #######       ####    ####      ###########    ####  ####  \n     #####     #######      #####    #####     ######        ####   ####  \n     #####     #######      #####    #####     #####         #############\n      #####      #####     ################    #####         #############\n      ######     #####     ################    #####         #############\n      ################    ##################   #####                ####  \n       ###############    #####        #####   #####                ####  \n         #############    #####        #####   #####                ####  \n          #########      #####          #####  #####                ####  \n                                                                          \n     Information at:  http://www.gap-system.org\n     Try '?help' for help. See also  '?copyright' and  '?authors'\n    \n   Loading the library. Please be patient, this may take a while.\nGAP4, Version: 4.4.12 of 17-Dec-2008, ia64-unknown-linux-gnu-gcc\ngap> LoadPackage(\"braid\");\nfail\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/5455\n\n",
    "created_at": "2009-03-08T05:53:51Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "gap-4.4.12 -- broken on iras (itanium Linux)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5455",
    "user": "https://github.com/williamstein"
}
```
Assignee: mabshoff

Saving and loading workspaces is broke in gap Itanium (SUSE). Also, loading of any packages is now mysteriously broken:

```
sage: !gap
    
            #########           ######         ###########           ###  
         #############          ######         ############         ####  
        ##############         ########        #############       #####  
       ###############         ########        #####   ######      #####  
      ######         #         #########       #####    #####     ######  
     ######                   ##########       #####    #####    #######  
     #####                    ##### ####       #####   ######   ########  
     ####                    #####  #####      #############   ###  ####  
     #####     #######       ####    ####      ###########    ####  ####  
     #####     #######      #####    #####     ######        ####   ####  
     #####     #######      #####    #####     #####         #############
      #####      #####     ################    #####         #############
      ######     #####     ################    #####         #############
      ################    ##################   #####                ####  
       ###############    #####        #####   #####                ####  
         #############    #####        #####   #####                ####  
          #########      #####          #####  #####                ####  
                                                                          
     Information at:  http://www.gap-system.org
     Try '?help' for help. See also  '?copyright' and  '?authors'
    
   Loading the library. Please be patient, this may take a while.
GAP4, Version: 4.4.12 of 17-Dec-2008, ia64-unknown-linux-gnu-gcc
gap> LoadPackage("braid");
fail
```

Issue created by migration from https://trac.sagemath.org/ticket/5455





---

archive/issue_comments_042194.json:
```json
{
    "body": "Basically the filename option to SaveWorkspace seems to be randomly corrupted.",
    "created_at": "2009-03-08T06:09:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5455#issuecomment-42194",
    "user": "https://github.com/williamstein"
}
```

Basically the filename option to SaveWorkspace seems to be randomly corrupted.



---

archive/issue_comments_042195.json:
```json
{
    "body": "Attachment [trac_5455.patch](tarball://root/attachments/some-uuid/ticket5455/trac_5455.patch) by @williamstein created at 2009-03-08 06:13:18\n\nI've posted a patch that just disables the workspace caching optimization completely for Itanium.    I wrote workspace caching for gap (long ago) and it is 100% just an optimization -- things should be functionally equivalent but just the first time one does \"gap(...)\" it is slower.  \n\n\nNOTE: I also tried compiling gap with -O0 and that didn't fix this problem.",
    "created_at": "2009-03-08T06:13:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5455#issuecomment-42195",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5455.patch](tarball://root/attachments/some-uuid/ticket5455/trac_5455.patch) by @williamstein created at 2009-03-08 06:13:18

I've posted a patch that just disables the workspace caching optimization completely for Itanium.    I wrote workspace caching for gap (long ago) and it is 100% just an optimization -- things should be functionally equivalent but just the first time one does "gap(...)" it is slower.  


NOTE: I also tried compiling gap with -O0 and that didn't fix this problem.



---

archive/issue_comments_042196.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2009-03-08T06:13:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5455#issuecomment-42196",
    "user": "https://github.com/williamstein"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_042197.json:
```json
{
    "body": "I'm testing my patch.  I noticed that this fails:\n\n```\nFile \"/home/wstein/iras/build/sage-3.4.alpha0/devel/sage/doc/en/constructions/linear_codes.rst\", line 29:\n    sage: C.minimum_distance()\nException raised:\n    RuntimeError: Gap produced error output\n    Variable: 'GeneratorMatCode' must have a value\n```\n\nI'm guessing the problem is that when use_workspace_cache is False, then certain packages don't get loaded, maybe.   This would be another separate bug in the gap interface.",
    "created_at": "2009-03-08T06:16:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5455#issuecomment-42197",
    "user": "https://github.com/williamstein"
}
```

I'm testing my patch.  I noticed that this fails:

```
File "/home/wstein/iras/build/sage-3.4.alpha0/devel/sage/doc/en/constructions/linear_codes.rst", line 29:
    sage: C.minimum_distance()
Exception raised:
    RuntimeError: Gap produced error output
    Variable: 'GeneratorMatCode' must have a value
```

I'm guessing the problem is that when use_workspace_cache is False, then certain packages don't get loaded, maybe.   This would be another separate bug in the gap interface.



---

archive/issue_comments_042198.json:
```json
{
    "body": "Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-09T19:45:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5455#issuecomment-42198",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Positive review.

Cheers,

Michael



---

archive/issue_events_012741.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-09T19:45:39Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/5455",
    "milestone": "sage-3.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5455#event-12741"
}
```



---

archive/issue_comments_042199.json:
```json
{
    "body": "Merged in Sage 3.4.final.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-10T16:23:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5455#issuecomment-42199",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.4.final.

Cheers,

Michael



---

archive/issue_comments_042200.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-10T16:23:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5455#issuecomment-42200",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_012742.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-03-10T16:23:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5455",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5455#event-12742"
}
```
