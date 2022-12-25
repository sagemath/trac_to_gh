# Issue 4746: [with patch, positive review] Bug in srange

archive/issues_004746.json:
```json
{
    "body": "Assignee: cwitty\n\nOne can produce almost every (wrong) behavior concerning the endpoint\nof the returned list. Here are some examples:\n\n\n```\nsage: srange(0.5,1.1,0.1,include_endpoint=False)\n[0.500000000000000,\n 0.600000000000000,\n 0.700000000000000,\n 0.800000000000000,\n 0.900000000000000,\n 1.00000000000000,\n 1.10000000000000]\n\nsage: srange(0.5,1,0.1,include_endpoint=False)\n[0.500000000000000,\n 0.600000000000000,\n 0.700000000000000,\n 0.800000000000000,\n 0.900000000000000]\n\nsage: srange(0.5,0.9,0.1,include_endpoint=False)\n[0.500000000000000, 0.600000000000000, 0.700000000000000,\n0.800000000000000]\n\nsage: srange(0,1.1,0.1,include_endpoint=True)\n[0.000000000000000,\n 0.100000000000000,\n 0.200000000000000,\n 0.300000000000000,\n 0.400000000000000,\n 0.500000000000000,\n 0.600000000000000,\n 0.700000000000000,\n 0.800000000000000,\n 0.900000000000000,\n 1.00000000000000,\n 1.10000000000000,\n 1.20000000000000]\n\nsage: srange(0,0.2,0.1,include_endpoint=True)\n[0.000000000000000, 0.100000000000000, 0.200000000000000]\n\nsage: srange(0,0.3,0.1,include_endpoint=True)\n[0.000000000000000, 0.100000000000000, 0.200000000000000]\n```\n\n-MRK- \n\nIssue created by migration from https://trac.sagemath.org/ticket/4746\n\n",
    "closed_at": "2009-02-20T07:37:32Z",
    "created_at": "2008-12-09T09:42:20Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "[with patch, positive review] Bug in srange",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4746",
    "user": "https://github.com/m-r-k"
}
```
Assignee: cwitty

One can produce almost every (wrong) behavior concerning the endpoint
of the returned list. Here are some examples:


```
sage: srange(0.5,1.1,0.1,include_endpoint=False)
[0.500000000000000,
 0.600000000000000,
 0.700000000000000,
 0.800000000000000,
 0.900000000000000,
 1.00000000000000,
 1.10000000000000]

sage: srange(0.5,1,0.1,include_endpoint=False)
[0.500000000000000,
 0.600000000000000,
 0.700000000000000,
 0.800000000000000,
 0.900000000000000]

sage: srange(0.5,0.9,0.1,include_endpoint=False)
[0.500000000000000, 0.600000000000000, 0.700000000000000,
0.800000000000000]

sage: srange(0,1.1,0.1,include_endpoint=True)
[0.000000000000000,
 0.100000000000000,
 0.200000000000000,
 0.300000000000000,
 0.400000000000000,
 0.500000000000000,
 0.600000000000000,
 0.700000000000000,
 0.800000000000000,
 0.900000000000000,
 1.00000000000000,
 1.10000000000000,
 1.20000000000000]

sage: srange(0,0.2,0.1,include_endpoint=True)
[0.000000000000000, 0.100000000000000, 0.200000000000000]

sage: srange(0,0.3,0.1,include_endpoint=True)
[0.000000000000000, 0.100000000000000, 0.200000000000000]
```

-MRK- 

Issue created by migration from https://trac.sagemath.org/ticket/4746





---

archive/issue_comments_035837.json:
```json
{
    "body": "what if we added a tolerance option, which it would use in comparing the endpoint?  If you were within tolerance of the endpoint, you would compare as equal to the endpoint.",
    "created_at": "2008-12-09T09:46:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4746#issuecomment-35837",
    "user": "https://github.com/jasongrout"
}
```

what if we added a tolerance option, which it would use in comparing the endpoint?  If you were within tolerance of the endpoint, you would compare as equal to the endpoint.



---

archive/issue_events_010843.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2008-12-10T00:41:15Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4746",
    "milestone": "sage-3.2.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4746#event-10843"
}
```



---

archive/issue_comments_035838.json:
```json
{
    "body": "```\nOn Tue, Dec 9, 2008 at 4:25 PM, Robert Bradshaw <robertwb@math.washington.edu> wrote:\n>\n> On Dec 9, 2008, at 2:00 AM, Jason Grout wrote:\n>\n>> John Cremona wrote:\n>>> I would not expect this to work perfectly with floating point numbers\n>>> which are not representable exactly in binary.\n>>\n>>\n>> But we could add some sort of tolerance argument that would allow some\n>> sort of user-settable fuzz factor.  Basically, the tolerance setting\n>> could be used when comparing with the ending value.\n>\n> Where would this be set? Whatever default it set, it would seem kind\n> of arbitrary.\n>\n> Perhaps this is a case where it could distinguish between RealLiteral\n> and RealNumber.\n>\n\nThis is not the answer.  Look at this example:\n\nsage: srange(0,1.1,0.1,include_endpoint=True)\n[0.000000000000000,\n 0.100000000000000,\n 0.200000000000000,\n 0.300000000000000,\n 0.400000000000000,\n 0.500000000000000,\n 0.600000000000000,\n 0.700000000000000,\n 0.800000000000000,\n 0.900000000000000,\n 1.00000000000000,\n 1.10000000000000,\n 1.20000000000000]\n\nThat's not right no matter what.  The documentation says:\n\"        Return list of numbers a, a+step, ..., a+k*step,\n        where a+k*step < b and a+(k+1)*step > b.\"\nwhere a,b are the first two inputs.\n\nThus the implementation of srange is simply buggy because the person (me!) who implemented didn't take proper care of how floating point numbers behave. \n\nWilliam\n```",
    "created_at": "2008-12-10T00:41:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4746#issuecomment-35838",
    "user": "https://github.com/williamstein"
}
```

```
On Tue, Dec 9, 2008 at 4:25 PM, Robert Bradshaw <robertwb@math.washington.edu> wrote:
>
> On Dec 9, 2008, at 2:00 AM, Jason Grout wrote:
>
>> John Cremona wrote:
>>> I would not expect this to work perfectly with floating point numbers
>>> which are not representable exactly in binary.
>>
>>
>> But we could add some sort of tolerance argument that would allow some
>> sort of user-settable fuzz factor.  Basically, the tolerance setting
>> could be used when comparing with the ending value.
>
> Where would this be set? Whatever default it set, it would seem kind
> of arbitrary.
>
> Perhaps this is a case where it could distinguish between RealLiteral
> and RealNumber.
>

This is not the answer.  Look at this example:

sage: srange(0,1.1,0.1,include_endpoint=True)
[0.000000000000000,
 0.100000000000000,
 0.200000000000000,
 0.300000000000000,
 0.400000000000000,
 0.500000000000000,
 0.600000000000000,
 0.700000000000000,
 0.800000000000000,
 0.900000000000000,
 1.00000000000000,
 1.10000000000000,
 1.20000000000000]

That's not right no matter what.  The documentation says:
"        Return list of numbers a, a+step, ..., a+k*step,
        where a+k*step < b and a+(k+1)*step > b."
where a,b are the first two inputs.

Thus the implementation of srange is simply buggy because the person (me!) who implemented didn't take proper care of how floating point numbers behave. 

William
```



---

archive/issue_comments_035839.json:
```json
{
    "body": "To whoever works on this problem: I would also request that the options 'universe' and 'check' be documented (or removed).  The documentation for 'include_endpoint' should say something like \"whether or not to include the right-hand endpoint\" or \"whether to include 'end' \" or something.  (I mean, it's more or less clear that you will include `start` and the issue is whether `end` is included, but this could be phrased better, I think.)\n\nAlong these lines, what does 'include_endpoint=True' mean if `start+k*step` is never equal to `end`?  For example, is\n\n```\nsrange(start=1, end=3.5, step=1, include_endpoint=True)\n```\nsupposed to behave differently from\n\n```\nsrange(start=1, end=3.5, step=1, include_endpoint=False)\n```\nMy guess is no, but this could be clarified in the documentation.  (\"whether to include 'end' if end == start+k*step for some k\"?)\n\nFinally, if you want to set a tolerance, would a default value of `step * epsilon` be good, for some choice of epsilon (e.g. 10^-5)?",
    "created_at": "2008-12-10T05:22:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4746#issuecomment-35839",
    "user": "https://github.com/jhpalmieri"
}
```

To whoever works on this problem: I would also request that the options 'universe' and 'check' be documented (or removed).  The documentation for 'include_endpoint' should say something like "whether or not to include the right-hand endpoint" or "whether to include 'end' " or something.  (I mean, it's more or less clear that you will include `start` and the issue is whether `end` is included, but this could be phrased better, I think.)

Along these lines, what does 'include_endpoint=True' mean if `start+k*step` is never equal to `end`?  For example, is

```
srange(start=1, end=3.5, step=1, include_endpoint=True)
```
supposed to behave differently from

```
srange(start=1, end=3.5, step=1, include_endpoint=False)
```
My guess is no, but this could be clarified in the documentation.  ("whether to include 'end' if end == start+k*step for some k"?)

Finally, if you want to set a tolerance, would a default value of `step * epsilon` be good, for some choice of epsilon (e.g. 10^-5)?



---

archive/issue_comments_035840.json:
```json
{
    "body": "Maybe one could use Numpy's arange() to do the heavy lifting.\n\nThe only problem is that coercing it back could impact performance.",
    "created_at": "2008-12-12T21:42:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4746#issuecomment-35840",
    "user": "https://trac.sagemath.org/admin/accounts/users/ronanpaixao"
}
```

Maybe one could use Numpy's arange() to do the heavy lifting.

The only problem is that coercing it back could impact performance.



---

archive/issue_comments_035841.json:
```json
{
    "body": "Numpy's arange suffers from the same difficulties. \n\n```\nsage: numpy.arange(0.5r, 1.1r, .1r)\narray([ 0.5,  0.6,  0.7,  0.8,  0.9,  1. ,  1.1])\n```",
    "created_at": "2009-01-23T05:05:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4746#issuecomment-35841",
    "user": "https://github.com/robertwb"
}
```

Numpy's arange suffers from the same difficulties. 

```
sage: numpy.arange(0.5r, 1.1r, .1r)
array([ 0.5,  0.6,  0.7,  0.8,  0.9,  1. ,  1.1])
```



---

archive/issue_comments_035842.json:
```json
{
    "body": "Attachment [4746-srange.patch](tarball://root/attachments/some-uuid/ticket4746/4746-srange.patch) by @robertwb created at 2009-01-23 10:43:39\n\nBetter documentation, and hopefully a bit easier to follow.",
    "created_at": "2009-01-23T10:43:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4746#issuecomment-35842",
    "user": "https://github.com/robertwb"
}
```

Attachment [4746-srange.patch](tarball://root/attachments/some-uuid/ticket4746/4746-srange.patch) by @robertwb created at 2009-01-23 10:43:39

Better documentation, and hopefully a bit easier to follow.



---

archive/issue_comments_035843.json:
```json
{
    "body": "Attachment [4746-srange-rebased.patch](tarball://root/attachments/some-uuid/ticket4746/4746-srange-rebased.patch) by cwitty created at 2009-02-20 03:15:28",
    "created_at": "2009-02-20T03:15:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4746#issuecomment-35843",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [4746-srange-rebased.patch](tarball://root/attachments/some-uuid/ticket4746/4746-srange-rebased.patch) by cwitty created at 2009-02-20 03:15:28



---

archive/issue_comments_035844.json:
```json
{
    "body": "Attachment [4746-referee.patch](tarball://root/attachments/some-uuid/ticket4746/4746-referee.patch) by cwitty created at 2009-02-20 03:19:52\n\nI had to rebase the patch (the added/removed lines are unchanged).  Also, three doctests failed in interact.py; William said in IRC to change the expected results:\n\n```\n Should I just change the expected result?\n<wstein> The Got definitely looks more sensible.\n So yes, do change the expected result.\n```\n\nCode looks good, all doctests pass.  Positive review.  Apply 4746-srange-rebased.patch and 4746-referee.patch.",
    "created_at": "2009-02-20T03:19:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4746#issuecomment-35844",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```

Attachment [4746-referee.patch](tarball://root/attachments/some-uuid/ticket4746/4746-referee.patch) by cwitty created at 2009-02-20 03:19:52

I had to rebase the patch (the added/removed lines are unchanged).  Also, three doctests failed in interact.py; William said in IRC to change the expected results:

```
 Should I just change the expected result?
<wstein> The Got definitely looks more sensible.
 So yes, do change the expected result.
```

Code looks good, all doctests pass.  Positive review.  Apply 4746-srange-rebased.patch and 4746-referee.patch.



---

archive/issue_events_010844.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-20T07:37:32Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4746",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4746#event-10844"
}
```



---

archive/issue_comments_035845.json:
```json
{
    "body": "Merged 4746-srange-rebased.patch and 4746-referee.patch in Sage 3.3.rc3.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-20T07:37:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4746#issuecomment-35845",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged 4746-srange-rebased.patch and 4746-referee.patch in Sage 3.3.rc3.

Cheers,

Michael



---

archive/issue_comments_035846.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-20T07:37:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4746",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4746#issuecomment-35846",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_010845.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-20T07:37:41Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4746",
    "milestone": "sage-3.2.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4746#event-10845"
}
```



---

archive/issue_events_010846.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-20T07:37:41Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4746",
    "milestone": "sage-3.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4746#event-10846"
}
```
