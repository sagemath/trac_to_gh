# Issue 6283: Make it so NUM_THREADS is set intelligently instead of idiotically in makefile so doing "make ptest" or "make ptestlong" doesn't kill some computers

archive/issues_006283.json:
```json
{
    "body": "Assignee: tbd\n\nThe top of SAGE_ROOT/makefile is\n\n```\n# How many threads should be used when doing parallel testing (and\n# sometime in the future, parallel building)?\nNUM_THREADS=20\n\n```\n\n\nI've many times accidently done \"make ptest\" and with extremely unpleasant results the next day.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6283\n\n",
    "created_at": "2009-06-14T09:57:54Z",
    "labels": [
        "component: doctest coverage",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "Make it so NUM_THREADS is set intelligently instead of idiotically in makefile so doing \"make ptest\" or \"make ptestlong\" doesn't kill some computers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6283",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

The top of SAGE_ROOT/makefile is

```
# How many threads should be used when doing parallel testing (and
# sometime in the future, parallel building)?
NUM_THREADS=20

```


I've many times accidently done "make ptest" and with extremely unpleasant results the next day.

Issue created by migration from https://trac.sagemath.org/ticket/6283





---

archive/issue_comments_050066.json:
```json
{
    "body": "Attachment [trac_6283-numthreads.patch](tarball://root/attachments/some-uuid/ticket6283/trac_6283-numthreads.patch) by @jhpalmieri created at 2009-09-21 23:08:42\n\napply to scripts repository.  depends on #2624.",
    "created_at": "2009-09-21T23:08:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6283#issuecomment-50066",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_6283-numthreads.patch](tarball://root/attachments/some-uuid/ticket6283/trac_6283-numthreads.patch) by @jhpalmieri created at 2009-09-21 23:08:42

apply to scripts repository.  depends on #2624.



---

archive/issue_comments_050067.json:
```json
{
    "body": "patch for SAGE_ROOT/makefile",
    "created_at": "2009-09-21T23:12:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6283#issuecomment-50067",
    "user": "https://github.com/jhpalmieri"
}
```

patch for SAGE_ROOT/makefile



---

archive/issue_comments_050068.json:
```json
{
    "body": "Attachment [makefile](tarball://root/attachments/some-uuid/ticket6283/makefile) by @jhpalmieri created at 2009-09-21 23:12:51\n\nthe file SAGE_ROOT/makefile",
    "created_at": "2009-09-21T23:12:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6283#issuecomment-50068",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [makefile](tarball://root/attachments/some-uuid/ticket6283/makefile) by @jhpalmieri created at 2009-09-21 23:12:51

the file SAGE_ROOT/makefile



---

archive/issue_comments_050069.json:
```json
{
    "body": "I'm not sure what \"intelligently\" means, but here is a patch which sets it to be the number of processors, as detected by `multiprocessing.cpu_count()`.  This also changes the command `sage -tp N <files>`: if N is 0, then replace it with the number of processors.\n\nThis depends on the patch at #2624.",
    "created_at": "2009-09-21T23:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6283#issuecomment-50069",
    "user": "https://github.com/jhpalmieri"
}
```

I'm not sure what "intelligently" means, but here is a patch which sets it to be the number of processors, as detected by `multiprocessing.cpu_count()`.  This also changes the command `sage -tp N <files>`: if N is 0, then replace it with the number of processors.

This depends on the patch at #2624.



---

archive/issue_comments_050070.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-09-21T23:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6283#issuecomment-50070",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from new to assigned.



---

archive/issue_comments_050071.json:
```json
{
    "body": "Changing assignee from tbd to @jhpalmieri.",
    "created_at": "2009-09-21T23:13:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6283#issuecomment-50071",
    "user": "https://github.com/jhpalmieri"
}
```

Changing assignee from tbd to @jhpalmieri.



---

archive/issue_comments_050072.json:
```json
{
    "body": "I really want this patch in, since I am very very tired of editing the makefile on every tarball I unpack. One question: do we know what multiprocessing.cpu_count() returns on something like the Sun T2 machine? That machine has many \"threads\" but not terribly many cores, and I'm not sure what cpu_count does. Also, does this work in Cygwin or Windows? We are trying to revive the Cygwin port.",
    "created_at": "2009-09-23T01:24:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6283#issuecomment-50072",
    "user": "https://github.com/dandrake"
}
```

I really want this patch in, since I am very very tired of editing the makefile on every tarball I unpack. One question: do we know what multiprocessing.cpu_count() returns on something like the Sun T2 machine? That machine has many "threads" but not terribly many cores, and I'm not sure what cpu_count does. Also, does this work in Cygwin or Windows? We are trying to revive the Cygwin port.



---

archive/issue_comments_050073.json:
```json
{
    "body": "Hrm, I just checked on T2, and multiprocessing.cpu_count() returns 128 on that machine, which perhaps is not ideal. The whole issue of cpus/cores/threads is really complicated -- see our own drkirkby [on comp.os.solaris](http://unix.derkeiler.com/Newsgroups/comp.unix.solaris/2009-06/msg00454.html). I think we can ignore this issue for the moment, since Sage doesn't even really build on T2.",
    "created_at": "2009-09-23T01:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6283#issuecomment-50073",
    "user": "https://github.com/dandrake"
}
```

Hrm, I just checked on T2, and multiprocessing.cpu_count() returns 128 on that machine, which perhaps is not ideal. The whole issue of cpus/cores/threads is really complicated -- see our own drkirkby [on comp.os.solaris](http://unix.derkeiler.com/Newsgroups/comp.unix.solaris/2009-06/msg00454.html). I think we can ignore this issue for the moment, since Sage doesn't even really build on T2.



---

archive/issue_comments_050074.json:
```json
{
    "body": "Replying to [comment:3 ddrake]:\n> Hrm, I just checked on T2, and multiprocessing.cpu_count() returns 128 on that machine, which perhaps is not ideal. The whole issue of cpus/cores/threads is really complicated -- see our own drkirkby. I think we can ignore this issue for the moment, since Sage doesn't even really build on T2.\n\nI'm happy to ignore this.  If it returns the \"wrong\" number, that seems like a bug in Python.\n\nI don't have access to many different kinds of machines.  Should we ask people on sage-devel to test `multiprocessing.cpu_count()`?",
    "created_at": "2009-09-23T02:10:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6283#issuecomment-50074",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:3 ddrake]:
> Hrm, I just checked on T2, and multiprocessing.cpu_count() returns 128 on that machine, which perhaps is not ideal. The whole issue of cpus/cores/threads is really complicated -- see our own drkirkby. I think we can ignore this issue for the moment, since Sage doesn't even really build on T2.

I'm happy to ignore this.  If it returns the "wrong" number, that seems like a bug in Python.

I don't have access to many different kinds of machines.  Should we ask people on sage-devel to test `multiprocessing.cpu_count()`?



---

archive/issue_comments_050075.json:
```json
{
    "body": "After the [discussion on sage-devel](http://groups.google.com/group/sage-devel/t/7b767521e472e10a), I think we should merge this. The only concrete example of a machine where this doesn't work is t2.math, and anyone can fix it by editing the makefile -- which is what everyone has been doing all along anyway!\n\nRelease manager: merge attachment:trac_6283-numthreads.patch and also patch the makefile in $SAGE_ROOT with attachment:makefile.patch.",
    "created_at": "2009-09-25T00:11:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6283#issuecomment-50075",
    "user": "https://github.com/dandrake"
}
```

After the [discussion on sage-devel](http://groups.google.com/group/sage-devel/t/7b767521e472e10a), I think we should merge this. The only concrete example of a machine where this doesn't work is t2.math, and anyone can fix it by editing the makefile -- which is what everyone has been doing all along anyway!

Release manager: merge attachment:trac_6283-numthreads.patch and also patch the makefile in $SAGE_ROOT with attachment:makefile.patch.



---

archive/issue_comments_050076.json:
```json
{
    "body": "Attachment [trac_6283-warning.patch](tarball://root/attachments/some-uuid/ticket6283/trac_6283-warning.patch) by mvngu created at 2009-09-25 04:55:48\n\nadds warning about setting the number of threads to 0",
    "created_at": "2009-09-25T04:55:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6283#issuecomment-50076",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_6283-warning.patch](tarball://root/attachments/some-uuid/ticket6283/trac_6283-warning.patch) by mvngu created at 2009-09-25 04:55:48

adds warning about setting the number of threads to 0



---

archive/issue_comments_050077.json:
```json
{
    "body": "The file `SAGE_ROOT/makefile` has been manually patched to include the changes in `makefile.patch`. I have also included a warning about using the default value of zero, i.e. having `NUM_THREADS=0` which is the default:\n\n```\n# NUM_THREADS is the number of threads to use for parallel testing              \n# (and sometime in the future, parallel building).  If this is 0, then          \n# later it gets set to the number of processors -- see sage-ptest.              \n# The detection of number of processors might not be reliable on some           \n# platforms. On a Sun SPARC T5240 (t2.math), the reported number of processors  \n# might not correspond to the actual number of processors. See ticket #6283.    \n#                                                                               \n# WARNING: Unless you are certain that you want to use all the cores/processors\n# on your system for parallel doctesting, change the value of NUM_THREADS to    \n# a (sensible) positive integer. The default value is zero.                     \nNUM_THREADS=0  # default is zero\n```\n\nI think people should be made aware that having a value of zero means that all the cores/processors on their system would be devoted to parallel doctesting. On a personal machine, that's OK and any damage done would be localized to the person's own machine. But on a multi-user machine such as the machines making up the Sage cluster, bsd.math, etc., the default value of zero can be dangerous because on sage.math, say, this would use 24 cores for parallel doctesting. Most of the time, people are running very long jobs on sage.math, mod.math, and geom.math. Using all 24 cores on any of these machines can have unexpected consequences such as having doctest failures due to segfaults, out of memory error, and even bringing those machines offline. The patch `trac_6283-warning.patch` also adds a warning to this effect to the file `sage-ptest`. If you want to use the file `SAGE_ROOT/makefile` for parallel doctesting, be absolute sure that you have set a sensible positive integer for `NUM_THREADS`.",
    "created_at": "2009-09-25T05:11:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6283#issuecomment-50077",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The file `SAGE_ROOT/makefile` has been manually patched to include the changes in `makefile.patch`. I have also included a warning about using the default value of zero, i.e. having `NUM_THREADS=0` which is the default:

```
# NUM_THREADS is the number of threads to use for parallel testing              
# (and sometime in the future, parallel building).  If this is 0, then          
# later it gets set to the number of processors -- see sage-ptest.              
# The detection of number of processors might not be reliable on some           
# platforms. On a Sun SPARC T5240 (t2.math), the reported number of processors  
# might not correspond to the actual number of processors. See ticket #6283.    
#                                                                               
# WARNING: Unless you are certain that you want to use all the cores/processors
# on your system for parallel doctesting, change the value of NUM_THREADS to    
# a (sensible) positive integer. The default value is zero.                     
NUM_THREADS=0  # default is zero
```

I think people should be made aware that having a value of zero means that all the cores/processors on their system would be devoted to parallel doctesting. On a personal machine, that's OK and any damage done would be localized to the person's own machine. But on a multi-user machine such as the machines making up the Sage cluster, bsd.math, etc., the default value of zero can be dangerous because on sage.math, say, this would use 24 cores for parallel doctesting. Most of the time, people are running very long jobs on sage.math, mod.math, and geom.math. Using all 24 cores on any of these machines can have unexpected consequences such as having doctest failures due to segfaults, out of memory error, and even bringing those machines offline. The patch `trac_6283-warning.patch` also adds a warning to this effect to the file `sage-ptest`. If you want to use the file `SAGE_ROOT/makefile` for parallel doctesting, be absolute sure that you have set a sensible positive integer for `NUM_THREADS`.



---

archive/issue_comments_050078.json:
```json
{
    "body": "Your warnings are a good idea. Perhaps we can make it part of release manager boot camp to teach release managers to do doctests with `./sage -tp <sensible positive int> devel/sage` or `make ptest NUM_THREADS=<s.p.i>` instead of just doing `make ptest`. (Similar comments for ptestlong.)",
    "created_at": "2009-09-25T05:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6283#issuecomment-50078",
    "user": "https://github.com/dandrake"
}
```

Your warnings are a good idea. Perhaps we can make it part of release manager boot camp to teach release managers to do doctests with `./sage -tp <sensible positive int> devel/sage` or `make ptest NUM_THREADS=<s.p.i>` instead of just doing `make ptest`. (Similar comments for ptestlong.)



---

archive/issue_comments_050079.json:
```json
{
    "body": "Merged these patches in the script repository:\n\n1. `trac_6283-numthreads.patch`\n2. `trac_6283-warning.patch`\n\nManually patched the file `SAGE_ROOT/makefile` using `makefile.patch`, together with the above warning message.",
    "created_at": "2009-09-25T06:30:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6283#issuecomment-50079",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged these patches in the script repository:

1. `trac_6283-numthreads.patch`
2. `trac_6283-warning.patch`

Manually patched the file `SAGE_ROOT/makefile` using `makefile.patch`, together with the above warning message.



---

archive/issue_events_006527.json:
```json
{
    "actor": "mvngu",
    "created_at": "2009-09-25T06:30:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6283",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6283#event-6527"
}
```



---

archive/issue_comments_050080.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-25T06:30:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6283#issuecomment-50080",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_050081.json:
```json
{
    "body": "I realise this has got positive review, but I would have personally not given it that. I would have personally not allowed the default to exceed 8, since for 99% of machines with 8 or more 'CPUs/threads', they are mutli-user servers, not personal workstations. As such, people should not be exploiting them to the full. \n\nOn 't2' currently this would not cause an issue, since it is not used a lot. But it would be an issue once there are many users. I doubt it would be sensible on sage.math to exploit it to the full. \n\nDave",
    "created_at": "2009-09-25T06:49:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6283#issuecomment-50081",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I realise this has got positive review, but I would have personally not given it that. I would have personally not allowed the default to exceed 8, since for 99% of machines with 8 or more 'CPUs/threads', they are mutli-user servers, not personal workstations. As such, people should not be exploiting them to the full. 

On 't2' currently this would not cause an issue, since it is not used a lot. But it would be an issue once there are many users. I doubt it would be sensible on sage.math to exploit it to the full. 

Dave



---

archive/issue_comments_050082.json:
```json
{
    "body": "Replying to [comment:9 drkirkby]:\n> I realise this has got positive review, but I would have personally not given it that. I would have personally not allowed the default to exceed 8, since for 99% of machines with 8 or more 'CPUs/threads', they are mutli-user servers, not personal workstations. As such, people should not be exploiting them to the full. \nAgreed. \n\n\n\n\n\n> On 't2' currently this would not cause an issue, since it is not used a lot. But it would be an issue once there are many users. I doubt it would be sensible on sage.math to exploit it to the full. \nI think a value of 1 would be sensible. No matter if one runs doctest using `SAGE_ROOT/makefile` on a personal machine such as a Pentium 4, a dual core PC or sage.math, it would still use one thread as default. After manually merging changes to `SAGE_ROOT/makefile`, I did:\n\n```\nmake ptestlong\n```\n\nonly to realize that it spawned 24 cores on mod.math to parallel doctest. In panic mode, I hastily killed all of my threads. So how about opening another ticket to make `NUM_THREADS=1`?",
    "created_at": "2009-09-25T07:02:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6283#issuecomment-50082",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:9 drkirkby]:
> I realise this has got positive review, but I would have personally not given it that. I would have personally not allowed the default to exceed 8, since for 99% of machines with 8 or more 'CPUs/threads', they are mutli-user servers, not personal workstations. As such, people should not be exploiting them to the full. 
Agreed. 





> On 't2' currently this would not cause an issue, since it is not used a lot. But it would be an issue once there are many users. I doubt it would be sensible on sage.math to exploit it to the full. 
I think a value of 1 would be sensible. No matter if one runs doctest using `SAGE_ROOT/makefile` on a personal machine such as a Pentium 4, a dual core PC or sage.math, it would still use one thread as default. After manually merging changes to `SAGE_ROOT/makefile`, I did:

```
make ptestlong
```

only to realize that it spawned 24 cores on mod.math to parallel doctest. In panic mode, I hastily killed all of my threads. So how about opening another ticket to make `NUM_THREADS=1`?



---

archive/issue_comments_050083.json:
```json
{
    "body": "Replying to [comment:10 mvngu]:\n> So how about opening another ticket to make `NUM_THREADS=1`?\n\nI have a different idea, which we'll discuss at #7011.",
    "created_at": "2009-09-25T07:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6283#issuecomment-50083",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:10 mvngu]:
> So how about opening another ticket to make `NUM_THREADS=1`?

I have a different idea, which we'll discuss at #7011.



---

archive/issue_comments_050084.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T10:26:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6283",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6283#issuecomment-50084",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
