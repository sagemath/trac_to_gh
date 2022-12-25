# Issue 3726: stats/finance -- add support for hidden markov models to sage

archive/issues_003726.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe spkg:\n\n  http://sage.math.washington.edu/home/was/patches/ghmm-20080725.spkg\n\nbuilds ghmm and doesn't depend on anything not in sage (I hope).  It does not\nbuild the official GHMM bindings.  I am replacing those bindings with cleaner\nCython bindings that have better documentation, but initially expose less\nfunctionality.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3726\n\n",
    "created_at": "2008-07-25T16:21:26Z",
    "labels": [
        "component: finance"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.1.2",
    "title": "stats/finance -- add support for hidden markov models to sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3726",
    "user": "https://github.com/williamstein"
}
```
Assignee: @williamstein

The spkg:

  http://sage.math.washington.edu/home/was/patches/ghmm-20080725.spkg

builds ghmm and doesn't depend on anything not in sage (I hope).  It does not
build the official GHMM bindings.  I am replacing those bindings with cleaner
Cython bindings that have better documentation, but initially expose less
functionality.

Issue created by migration from https://trac.sagemath.org/ticket/3726





---

archive/issue_comments_026380.json:
```json
{
    "body": "Attachment [sage-3726-part1.patch](tarball://root/attachments/some-uuid/ticket3726/sage-3726-part1.patch) by @williamstein created at 2008-07-25 16:22:51",
    "created_at": "2008-07-25T16:22:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3726#issuecomment-26380",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3726-part1.patch](tarball://root/attachments/some-uuid/ticket3726/sage-3726-part1.patch) by @williamstein created at 2008-07-25 16:22:51



---

archive/issue_comments_026381.json:
```json
{
    "body": "Attachment [sage-3726-part2.patch](tarball://root/attachments/some-uuid/ticket3726/sage-3726-part2.patch) by @williamstein created at 2008-07-26 09:49:49",
    "created_at": "2008-07-26T09:49:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3726#issuecomment-26381",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3726-part2.patch](tarball://root/attachments/some-uuid/ticket3726/sage-3726-part2.patch) by @williamstein created at 2008-07-26 09:49:49



---

archive/issue_comments_026382.json:
```json
{
    "body": "Attachment [sage-3726-part3.patch](tarball://root/attachments/some-uuid/ticket3726/sage-3726-part3.patch) by @williamstein created at 2008-07-30 01:33:06",
    "created_at": "2008-07-30T01:33:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3726#issuecomment-26382",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3726-part3.patch](tarball://root/attachments/some-uuid/ticket3726/sage-3726-part3.patch) by @williamstein created at 2008-07-30 01:33:06



---

archive/issue_comments_026383.json:
```json
{
    "body": "Attachment [sage-3726-part4.patch](tarball://root/attachments/some-uuid/ticket3726/sage-3726-part4.patch) by @williamstein created at 2008-08-02 07:06:10",
    "created_at": "2008-08-02T07:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3726#issuecomment-26383",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3726-part4.patch](tarball://root/attachments/some-uuid/ticket3726/sage-3726-part4.patch) by @williamstein created at 2008-08-02 07:06:10



---

archive/issue_comments_026384.json:
```json
{
    "body": "Attachment [sage-3726-part6.patch](tarball://root/attachments/some-uuid/ticket3726/sage-3726-part6.patch) by @williamstein created at 2008-08-03 04:07:39",
    "created_at": "2008-08-03T04:07:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3726#issuecomment-26384",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3726-part6.patch](tarball://root/attachments/some-uuid/ticket3726/sage-3726-part6.patch) by @williamstein created at 2008-08-03 04:07:39



---

archive/issue_comments_026385.json:
```json
{
    "body": "Attachment [sage-3726-part7.patch](tarball://root/attachments/some-uuid/ticket3726/sage-3726-part7.patch) by @williamstein created at 2008-08-04 01:38:13\n\nThe attached patches bring the coverage of this code to 100% and cleanly wrap a solid set of functionality.",
    "created_at": "2008-08-04T01:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3726#issuecomment-26385",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3726-part7.patch](tarball://root/attachments/some-uuid/ticket3726/sage-3726-part7.patch) by @williamstein created at 2008-08-04 01:38:13

The attached patches bring the coverage of this code to 100% and cleanly wrap a solid set of functionality.



---

archive/issue_comments_026386.json:
```json
{
    "body": "Attachment [sage-3726-part8.patch](tarball://root/attachments/some-uuid/ticket3726/sage-3726-part8.patch) by @williamstein created at 2008-08-04 12:33:02",
    "created_at": "2008-08-04T12:33:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3726#issuecomment-26386",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3726-part8.patch](tarball://root/attachments/some-uuid/ticket3726/sage-3726-part8.patch) by @williamstein created at 2008-08-04 12:33:02



---

archive/issue_comments_026387.json:
```json
{
    "body": "Attachment [sage-3726-part9.patch](tarball://root/attachments/some-uuid/ticket3726/sage-3726-part9.patch) by @williamstein created at 2008-08-04 12:34:03\n\npatches 1 - 8 in a clean bundle against 3.0.5",
    "created_at": "2008-08-04T12:34:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3726#issuecomment-26387",
    "user": "https://github.com/williamstein"
}
```

Attachment [sage-3726-part9.patch](tarball://root/attachments/some-uuid/ticket3726/sage-3726-part9.patch) by @williamstein created at 2008-08-04 12:34:03

patches 1 - 8 in a clean bundle against 3.0.5



---

archive/issue_comments_026388.json:
```json
{
    "body": "Attachment [hmm-bundle-3.0.5.hg](tarball://root/attachments/some-uuid/ticket3726/hmm-bundle-3.0.5.hg) by @williamstein created at 2008-08-05 01:05:49",
    "created_at": "2008-08-05T01:05:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3726#issuecomment-26388",
    "user": "https://github.com/williamstein"
}
```

Attachment [hmm-bundle-3.0.5.hg](tarball://root/attachments/some-uuid/ticket3726/hmm-bundle-3.0.5.hg) by @williamstein created at 2008-08-05 01:05:49



---

archive/issue_comments_026389.json:
```json
{
    "body": "Code quality is of course excellent and of course positive review\n\nbut\n\nActual Bugs \n\n1. No checks are made that matrices given are valid stochastic matrices (rows add to 1).  Or more importantly that the probabilities are actually positive.  There is a function to normalize but it isn't called by default. Actually I'm not sure if this is a bug but there should be some documentation about what to expect  if the inputs matrices are not stochastic, does it do reasonable things or is the result numerical junk. \n\n\n2. For continuous hidden markov models baum welch does not accept a set of sequences only a single sequence.\n\n\nMiscellaneous comments\n\n1. Doc string locations are sort of hidden. It would be nice if hmm? or hmm.DiscreteHiddenMarkovModel? hit something. \n  \n\n2. (very minor) sample vs sample_single annoyed me, I would have rather sample had the number of sequences be optional which defaulted to 1. \n\n3. Does there need to be a discussion as to whether or not we want to support this in standard or optional since it involves adding another spkg.",
    "created_at": "2008-08-11T05:59:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3726#issuecomment-26389",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

Code quality is of course excellent and of course positive review

but

Actual Bugs 

1. No checks are made that matrices given are valid stochastic matrices (rows add to 1).  Or more importantly that the probabilities are actually positive.  There is a function to normalize but it isn't called by default. Actually I'm not sure if this is a bug but there should be some documentation about what to expect  if the inputs matrices are not stochastic, does it do reasonable things or is the result numerical junk. 


2. For continuous hidden markov models baum welch does not accept a set of sequences only a single sequence.


Miscellaneous comments

1. Doc string locations are sort of hidden. It would be nice if hmm? or hmm.DiscreteHiddenMarkovModel? hit something. 
  

2. (very minor) sample vs sample_single annoyed me, I would have rather sample had the number of sequences be optional which defaulted to 1. 

3. Does there need to be a discussion as to whether or not we want to support this in standard or optional since it involves adding another spkg.



---

archive/issue_comments_026390.json:
```json
{
    "body": ">   1. No checks are made that matrices given are valid stochastic matrices (rows add to 1). Or more \n> importantly that the probabilities are actually positive. There is a function to normalize but it\n>  isn't called by default. Actually I'm not sure if this is a bug but there should be some \n> documentation about what to expect if the inputs matrices are not stochastic, does it do \n> reasonable things or is the result numerical junk. \n\nI have no idea what it will do :-).  I will find out by looking at the GHMM docs.   I'm not sure what the best behavior would be on invalid input yet. \n\n>   2. For continuous hidden markov models baum welch does not accept a set of sequences only a single sequence. \n\nYou're right, this is a bug.  It does take multiple sequences but only like this with a weight:\n\n```\nsage: z.baum_welch([([1,2,3], 1), ([1,2,8], 2)])\n```\n\n\nIt should also work with no weights. \n\nDiscreteMarkovModels in this patch don't take single sequences (only multiple), but I fixed that in #3773 (I think).\n\n>   1. Doc string locations are sort of hidden. It would be nice if hmm? or hmm.DiscreteHiddenMarkovModel?? hit something. \n\nThanks for finding this.  I consider this a serious problem and will fix it. \n\n2. (very minor) sample vs sample_single annoyed me, I would have rather sample had the number of sequences be optional which defaulted to 1. \n\nI'm annoyed by not having it since foo.sample(n) returns something like [This is the Trac macro *1,2,5,3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1,2,5,3-macro) so one ends up typing foo.sample(n)[0] a lot, which seems odd.   Wait, this is easy.  Do this:\n\n```\n23:08 < wstein-3514> I can just make M.sample(n, None) give a single list,\n23:08 < wstein-3514> whereas M.sample(n, k) with k >= 1 give a list of lists.\n23:08 < jkantor> right\n23:08 < wstein-3514> That is way better.\n23:08 < wstein-3514> Thanks.\n```\n\n\n>   3. Does there need to be a discussion as to whether or not we want to support this in standard or > optional since it involves adding another spkg. \n\nYes.  This will not go in standard until the spkg is officially voted on in sage-devel.\nThis will happen in the next day, as soon as I fix all the problems you point out above.",
    "created_at": "2008-08-11T06:11:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3726#issuecomment-26390",
    "user": "https://github.com/williamstein"
}
```

>   1. No checks are made that matrices given are valid stochastic matrices (rows add to 1). Or more 
> importantly that the probabilities are actually positive. There is a function to normalize but it
>  isn't called by default. Actually I'm not sure if this is a bug but there should be some 
> documentation about what to expect if the inputs matrices are not stochastic, does it do 
> reasonable things or is the result numerical junk. 

I have no idea what it will do :-).  I will find out by looking at the GHMM docs.   I'm not sure what the best behavior would be on invalid input yet. 

>   2. For continuous hidden markov models baum welch does not accept a set of sequences only a single sequence. 

You're right, this is a bug.  It does take multiple sequences but only like this with a weight:

```
sage: z.baum_welch([([1,2,3], 1), ([1,2,8], 2)])
```


It should also work with no weights. 

DiscreteMarkovModels in this patch don't take single sequences (only multiple), but I fixed that in #3773 (I think).

>   1. Doc string locations are sort of hidden. It would be nice if hmm? or hmm.DiscreteHiddenMarkovModel?? hit something. 

Thanks for finding this.  I consider this a serious problem and will fix it. 

2. (very minor) sample vs sample_single annoyed me, I would have rather sample had the number of sequences be optional which defaulted to 1. 

I'm annoyed by not having it since foo.sample(n) returns something like [This is the Trac macro *1,2,5,3* that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#1,2,5,3-macro) so one ends up typing foo.sample(n)[0] a lot, which seems odd.   Wait, this is easy.  Do this:

```
23:08 < wstein-3514> I can just make M.sample(n, None) give a single list,
23:08 < wstein-3514> whereas M.sample(n, k) with k >= 1 give a list of lists.
23:08 < jkantor> right
23:08 < wstein-3514> That is way better.
23:08 < wstein-3514> Thanks.
```


>   3. Does there need to be a discussion as to whether or not we want to support this in standard or > optional since it involves adding another spkg. 

Yes.  This will not go in standard until the spkg is officially voted on in sage-devel.
This will happen in the next day, as soon as I fix all the problems you point out above.



---

archive/issue_comments_026391.json:
```json
{
    "body": "1. Regarding invalid input, I would suggest accepting positive inputs and normalizing but printing a message to that affect (that the probabilities didn't sum to 1  and were normalized) and I would raise an exception on negative inputs.\n\n\n2. The solution to 2 in what I had in mind.",
    "created_at": "2008-08-11T06:20:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3726#issuecomment-26391",
    "user": "https://trac.sagemath.org/admin/accounts/users/jkantor"
}
```

1. Regarding invalid input, I would suggest accepting positive inputs and normalizing but printing a message to that affect (that the probabilities didn't sum to 1  and were normalized) and I would raise an exception on negative inputs.


2. The solution to 2 in what I had in mind.



---

archive/issue_comments_026392.json:
```json
{
    "body": "The latest spkg seems to be\n\n  http://sage.math.washington.edu/home/was/patches/ghmm-20080813.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-08-18T23:43:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3726#issuecomment-26392",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

The latest spkg seems to be

  http://sage.math.washington.edu/home/was/patches/ghmm-20080813.spkg

Cheers,

Michael



---

archive/issue_events_008526.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-08-19T00:12:37Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/3726",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/3726#event-8526"
}
```



---

archive/issue_comments_026393.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-19T00:12:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3726#issuecomment-26393",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_026394.json:
```json
{
    "body": "Merged hmm-bundle-3.0.5.hg in Sage 3.1.2.alpha0. This bundle contains 12 changesets, so there are some patches missing in the broken out series. Oh well ...\n\nCheers,\n\nMichael",
    "created_at": "2008-08-19T00:12:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3726",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3726#issuecomment-26394",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged hmm-bundle-3.0.5.hg in Sage 3.1.2.alpha0. This bundle contains 12 changesets, so there are some patches missing in the broken out series. Oh well ...

Cheers,

Michael
