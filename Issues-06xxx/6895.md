# Issue 6895: Detect discontinuities when plotting the ceil function

archive/issues_006895.json:
```json
{
    "body": "Assignee: @williamstein\n\nThe discontinuities in the ceil function are not detected.\n\nExample: plot(lambda x: ceil(x), (-5,5), detect_poles='show') should not display vertical lines between the steps.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6895\n\n",
    "created_at": "2009-09-05T21:16:21Z",
    "labels": [
        "component: graphics",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-wishlist",
    "title": "Detect discontinuities when plotting the ceil function",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6895",
    "user": "https://trac.sagemath.org/admin/accounts/users/nbonifas"
}
```
Assignee: @williamstein

The discontinuities in the ceil function are not detected.

Example: plot(lambda x: ceil(x), (-5,5), detect_poles='show') should not display vertical lines between the steps.

Issue created by migration from https://trac.sagemath.org/ticket/6895





---

archive/issue_comments_056847.json:
```json
{
    "body": "*detect_poles* is only meant for the case when the left/right side limits of the function are +/-Infinity.\nIt was never intended to detect other discontinuities.\n\nBut ticket #6878 implements something like this. It does not automatically detect the discontinuities but\nlets you specify which points to exclude from the plot.\n\nThe following would have the effect you want:\n\n```\nsage: plot(ceil(x), (x, 1, 10), exclude = [1..10])\n```",
    "created_at": "2009-09-07T10:35:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6895#issuecomment-56847",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

*detect_poles* is only meant for the case when the left/right side limits of the function are +/-Infinity.
It was never intended to detect other discontinuities.

But ticket #6878 implements something like this. It does not automatically detect the discontinuities but
lets you specify which points to exclude from the plot.

The following would have the effect you want:

```
sage: plot(ceil(x), (x, 1, 10), exclude = [1..10])
```



---

archive/issue_comments_056848.json:
```json
{
    "body": "I was thinking of implementing some kind of general automatic discontinuity detection, either numerical (when the numerical derivative of the function is locally above a threshold, consider this point to be a discontinuity) or via algebraic means, as in the Maple \"discont\" function.",
    "created_at": "2009-09-07T13:09:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6895",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6895#issuecomment-56848",
    "user": "https://trac.sagemath.org/admin/accounts/users/nbonifas"
}
```

I was thinking of implementing some kind of general automatic discontinuity detection, either numerical (when the numerical derivative of the function is locally above a threshold, consider this point to be a discontinuity) or via algebraic means, as in the Maple "discont" function.
