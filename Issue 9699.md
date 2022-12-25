# Issue 9699: Barycentric embedding for planar graphs.

archive/issues_009699.json:
```json
{
    "body": "Assignee: jason, ncohen, rlm\n\nCC:  @rlmill boothby\n\nPositions of vertices returned by planar_layout can be set to have the vertices of an equilateral triangle as exterior vertices.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9699\n\n",
    "created_at": "2010-08-06T19:24:42Z",
    "labels": [
        "component: graph theory"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "Barycentric embedding for planar graphs.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9699",
    "user": "https://trac.sagemath.org/admin/accounts/users/fidelbarrera"
}
```
Assignee: jason, ncohen, rlm

CC:  @rlmill boothby

Positions of vertices returned by planar_layout can be set to have the vertices of an equilateral triangle as exterior vertices.

Issue created by migration from https://trac.sagemath.org/ticket/9699





---

archive/issue_comments_094137.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-06T19:26:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94137",
    "user": "https://trac.sagemath.org/admin/accounts/users/fidelbarrera"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_094138.json:
```json
{
    "body": "Updated patch, it includes an example.",
    "created_at": "2010-08-07T00:20:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94138",
    "user": "https://trac.sagemath.org/admin/accounts/users/fidelbarrera"
}
```

Updated patch, it includes an example.



---

archive/issue_comments_094139.json:
```json
{
    "body": "Attachment [trac_9699.patch](tarball://root/attachments/some-uuid/ticket9699/trac_9699.patch) by @rlmill created at 2010-08-07 11:58:53",
    "created_at": "2010-08-07T11:58:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94139",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_9699.patch](tarball://root/attachments/some-uuid/ticket9699/trac_9699.patch) by @rlmill created at 2010-08-07 11:58:53



---

archive/issue_comments_094140.json:
```json
{
    "body": "I wonder if the default for `barycentric` shouldn't be True instead of False. It looks a bit nicer that way, so why not make it the default?",
    "created_at": "2010-08-07T12:00:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94140",
    "user": "https://github.com/rlmill"
}
```

I wonder if the default for `barycentric` shouldn't be True instead of False. It looks a bit nicer that way, so why not make it the default?



---

archive/issue_comments_094141.json:
```json
{
    "body": "Attachment [trac_9699_2.patch](tarball://root/attachments/some-uuid/ticket9699/trac_9699_2.patch) by fidelbarrera created at 2010-08-08 01:59:45\n\nPlease apply instead of trac_9699.patch.",
    "created_at": "2010-08-08T01:59:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94141",
    "user": "https://trac.sagemath.org/admin/accounts/users/fidelbarrera"
}
```

Attachment [trac_9699_2.patch](tarball://root/attachments/some-uuid/ticket9699/trac_9699_2.patch) by fidelbarrera created at 2010-08-08 01:59:45

Please apply instead of trac_9699.patch.



---

archive/issue_comments_094142.json:
```json
{
    "body": "Replying to [comment:3 rlm]:\n> I wonder if the default for `barycentric` shouldn't be True instead of False. It looks a bit nicer that way, so why not make it the default?\n\nThe option `barycentric` is now set to True by default.",
    "created_at": "2010-08-08T02:02:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94142",
    "user": "https://trac.sagemath.org/admin/accounts/users/fidelbarrera"
}
```

Replying to [comment:3 rlm]:
> I wonder if the default for `barycentric` shouldn't be True instead of False. It looks a bit nicer that way, so why not make it the default?

The option `barycentric` is now set to True by default.



---

archive/issue_comments_094143.json:
```json
{
    "body": "Replying to [comment:3 rlm]:\n> I wonder if the default for `barycentric` shouldn't be True instead of False. It looks a bit nicer that way, so why not make it the default?\n\nSorry, I forgot to be more specific. Please apply trac_9699_2.patch instead of trac_9699.patch.\n\n\nIn trac_9699_2.patch the option `barycentric` is now set to be True by default.",
    "created_at": "2010-08-08T02:06:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94143",
    "user": "https://trac.sagemath.org/admin/accounts/users/fidelbarrera"
}
```

Replying to [comment:3 rlm]:
> I wonder if the default for `barycentric` shouldn't be True instead of False. It looks a bit nicer that way, so why not make it the default?

Sorry, I forgot to be more specific. Please apply trac_9699_2.patch instead of trac_9699.patch.


In trac_9699_2.patch the option `barycentric` is now set to be True by default.



---

archive/issue_comments_094144.json:
```json
{
    "body": "Well, if such an option is the default, shouldn't we just replace the actual code with it ? As these barycentric coordinates are as valid as the previous ones in the general case, I except the code used by barycentric = False never to be used again... `:-p`\n\nWhat about just replacing the current code to compute barycentric coordinates, and add this information as notes in the documentation ?\n\nNathann",
    "created_at": "2010-09-05T07:49:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94144",
    "user": "https://github.com/nathanncohen"
}
```

Well, if such an option is the default, shouldn't we just replace the actual code with it ? As these barycentric coordinates are as valid as the previous ones in the general case, I except the code used by barycentric = False never to be used again... `:-p`

What about just replacing the current code to compute barycentric coordinates, and add this information as notes in the documentation ?

Nathann



---

archive/issue_comments_094145.json:
```json
{
    "body": "Changing status from needs_review to needs_info.",
    "created_at": "2010-09-05T07:49:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94145",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to needs_info.



---

archive/issue_comments_094146.json:
```json
{
    "body": "Replying to [comment:6 ncohen]:\n\n> Well, if such an option is the default, shouldn't we just replace the actual code with it ?\n\nI think the previous implementation features interesting properties. It provided a straightline embedding in an O(n) by O(n) grid, so in particular all the coordinates are integers. Would you still suggest to replace the code completely?\n\nFidel",
    "created_at": "2010-09-13T01:45:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94146",
    "user": "https://trac.sagemath.org/admin/accounts/users/fidelbarrera"
}
```

Replying to [comment:6 ncohen]:

> Well, if such an option is the default, shouldn't we just replace the actual code with it ?

I think the previous implementation features interesting properties. It provided a straightline embedding in an O(n) by O(n) grid, so in particular all the coordinates are integers. Would you still suggest to replace the code completely?

Fidel



---

archive/issue_comments_094147.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-09-13T01:45:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94147",
    "user": "https://trac.sagemath.org/admin/accounts/users/fidelbarrera"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_094148.json:
```json
{
    "body": "> I think the previous implementation features interesting properties. It provided a straightline embedding in an O(n) by O(n) grid, so in particular all the coordinates are integers. Would you still suggest to replace the code completely?\n\nNo, not anymore... But now I would suggest to mention these properties in the docstring. Sorry for asking it this late, but I am concerned about avoiding to have in Sage at the same time two pieces of code doing the same thing in different ways, and writing it in such a way that one of them is never used.. That's why I wondered whether it would be better to completely replace the current implementation with yours instead of having two version. If the current version has properties that yours do not have, then you are right : it should remain available, but this is not very useful if nobody knows these properties exists.... Hence, where you documented the keyword ``barycentric`` \n\n\n```\n- ``barycentric`` - whether or not to use barycentric coordinates. \n```\n\n\nit would be nice to also mention that setting it to ``None`` means having an embedding in a O(n)*O(n) grid with integer coordinates, as you just taught me.. Otherwise it's very unlikely people would disable a feature with no computation time to earn...nothing `:-)`\n\nNathann",
    "created_at": "2010-09-13T07:08:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94148",
    "user": "https://github.com/nathanncohen"
}
```

> I think the previous implementation features interesting properties. It provided a straightline embedding in an O(n) by O(n) grid, so in particular all the coordinates are integers. Would you still suggest to replace the code completely?

No, not anymore... But now I would suggest to mention these properties in the docstring. Sorry for asking it this late, but I am concerned about avoiding to have in Sage at the same time two pieces of code doing the same thing in different ways, and writing it in such a way that one of them is never used.. That's why I wondered whether it would be better to completely replace the current implementation with yours instead of having two version. If the current version has properties that yours do not have, then you are right : it should remain available, but this is not very useful if nobody knows these properties exists.... Hence, where you documented the keyword ``barycentric`` 


```
- ``barycentric`` - whether or not to use barycentric coordinates. 
```


it would be nice to also mention that setting it to ``None`` means having an embedding in a O(n)*O(n) grid with integer coordinates, as you just taught me.. Otherwise it's very unlikely people would disable a feature with no computation time to earn...nothing `:-)`

Nathann



---

archive/issue_comments_094149.json:
```json
{
    "body": "Attachment [trac_9699_3.patch](tarball://root/attachments/some-uuid/ticket9699/trac_9699_3.patch) by fidelbarrera created at 2010-09-22 04:06:46\n\nPlease apply instead of previous patches.",
    "created_at": "2010-09-22T04:06:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94149",
    "user": "https://trac.sagemath.org/admin/accounts/users/fidelbarrera"
}
```

Attachment [trac_9699_3.patch](tarball://root/attachments/some-uuid/ticket9699/trac_9699_3.patch) by fidelbarrera created at 2010-09-22 04:06:46

Please apply instead of previous patches.



---

archive/issue_comments_094150.json:
```json
{
    "body": "Replying to [comment:8 ncohen]:\n\n> But now I would suggest to mention these properties in the docstring.\n\nThese properties are now mentioned in the docstring :)\n\nFidel",
    "created_at": "2010-09-22T04:09:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94150",
    "user": "https://trac.sagemath.org/admin/accounts/users/fidelbarrera"
}
```

Replying to [comment:8 ncohen]:

> But now I would suggest to mention these properties in the docstring.

These properties are now mentioned in the docstring :)

Fidel



---

archive/issue_comments_094151.json:
```json
{
    "body": "Hello !!\n\nI noticed a typo in your patch \n\n```\nthen coordinates will bi in the grid. \n```\n\n\nSo I first wrote a small one to fix it, then ended up fixing one or two other docstrings, or adding to them the information you had put in the first description or ``barycentric``.. Well, if somebody can test my patch, he can set this ticket to \"positive review\", as yours is good to go !\n\nThanksssssssssssssss ! :-)\n\nNathann",
    "created_at": "2010-09-22T08:14:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94151",
    "user": "https://github.com/nathanncohen"
}
```

Hello !!

I noticed a typo in your patch 

```
then coordinates will bi in the grid. 
```


So I first wrote a small one to fix it, then ended up fixing one or two other docstrings, or adding to them the information you had put in the first description or ``barycentric``.. Well, if somebody can test my patch, he can set this ticket to "positive review", as yours is good to go !

Thanksssssssssssssss ! :-)

Nathann



---

archive/issue_comments_094152.json:
```json
{
    "body": "Attachment [trac_9699 - docstring fixes.patch](tarball://root/attachments/some-uuid/ticket9699/trac_9699 - docstring fixes.patch) by @rlmill created at 2010-11-11 13:15:42\n\nDoctest fail:\n\n\n```\nsage -t -long ./sage/graphs/generic_graph.py\n**********************************************************************\nFile \"/home/rlmill/sage-4.6/devel/sage-main/sage/graphs/generic_graph.py\", line 2620:\n    sage: g.layout(layout = \"planar\", save_pos = True)\nExpected:\n    {0: [1, 1], 1: [2, 2], 2: [3, 2], 3: [1, 4], 4: [5, 1], 5: [0, 5], 6: [1, 0]}\nGot:\n    {0: (-0.433012701892, -0.25), 1: (1.11022302463e-16, -7.40148683083e-17), 2: (0.144337567297, 0.25), 3: (0.433012701892, -0.25), 4: [0.0, 1.0], 5: [0.866025403784, -0.5], 6: [-0.866025403784, -0.5]}\n**********************************************************************\n```\n\n\nAlso, all of the positions should be the same format: here some are tuples and others are lists.",
    "created_at": "2010-11-11T13:15:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94152",
    "user": "https://github.com/rlmill"
}
```

Attachment [trac_9699 - docstring fixes.patch](tarball://root/attachments/some-uuid/ticket9699/trac_9699 - docstring fixes.patch) by @rlmill created at 2010-11-11 13:15:42

Doctest fail:


```
sage -t -long ./sage/graphs/generic_graph.py
**********************************************************************
File "/home/rlmill/sage-4.6/devel/sage-main/sage/graphs/generic_graph.py", line 2620:
    sage: g.layout(layout = "planar", save_pos = True)
Expected:
    {0: [1, 1], 1: [2, 2], 2: [3, 2], 3: [1, 4], 4: [5, 1], 5: [0, 5], 6: [1, 0]}
Got:
    {0: (-0.433012701892, -0.25), 1: (1.11022302463e-16, -7.40148683083e-17), 2: (0.144337567297, 0.25), 3: (0.433012701892, -0.25), 4: [0.0, 1.0], 5: [0.866025403784, -0.5], 6: [-0.866025403784, -0.5]}
**********************************************************************
```


Also, all of the positions should be the same format: here some are tuples and others are lists.



---

archive/issue_comments_094153.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-11-11T13:15:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94153",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_094154.json:
```json
{
    "body": "Attachment [trac_9699_4.patch](tarball://root/attachments/some-uuid/ticket9699/trac_9699_4.patch) by fidelbarrera created at 2010-11-21 04:01:01\n\nPlease apply instead of previous patches.",
    "created_at": "2010-11-21T04:01:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94154",
    "user": "https://trac.sagemath.org/admin/accounts/users/fidelbarrera"
}
```

Attachment [trac_9699_4.patch](tarball://root/attachments/some-uuid/ticket9699/trac_9699_4.patch) by fidelbarrera created at 2010-11-21 04:01:01

Please apply instead of previous patches.



---

archive/issue_comments_094155.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-21T04:04:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94155",
    "user": "https://trac.sagemath.org/admin/accounts/users/fidelbarrera"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_094156.json:
```json
{
    "body": "Hello,\n\nThe patch file trac_9699_4.patch includes a fix to the doctest fail. It also includes a fix to the problem having tuples and lists for the positions. Now, all of the positions are lists.\n\nFidel",
    "created_at": "2010-11-21T04:04:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94156",
    "user": "https://trac.sagemath.org/admin/accounts/users/fidelbarrera"
}
```

Hello,

The patch file trac_9699_4.patch includes a fix to the doctest fail. It also includes a fix to the problem having tuples and lists for the positions. Now, all of the positions are lists.

Fidel



---

archive/issue_comments_094157.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-26T16:23:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94157",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_024234.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2010-11-26T22:22:36Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "milestone": "sage-4.6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9699#event-24234"
}
```



---

archive/issue_comments_094158.json:
```json
{
    "body": "Has this been tested on various systems?  The kind of output like\n\n```\n{0: [0.0, 1.0], 1: [0.866025403784, -0.5], 2: [-0.866025403784, -0.5], 3: [0.433012701892, -0.25], 4: [-0.288675134595, -1.85037170771e-16], 5: [0.288675134595, 3.70074341542e-17], 6: [0.144337567297, 0.25]}\n```\n\nhas a tendency of being quite system-dependent because of precision issues.\n\nIn any case, if all you did was add an option, why did the output change?",
    "created_at": "2010-11-26T22:25:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94158",
    "user": "https://github.com/jdemeyer"
}
```

Has this been tested on various systems?  The kind of output like

```
{0: [0.0, 1.0], 1: [0.866025403784, -0.5], 2: [-0.866025403784, -0.5], 3: [0.433012701892, -0.25], 4: [-0.288675134595, -1.85037170771e-16], 5: [0.288675134595, 3.70074341542e-17], 6: [0.144337567297, 0.25]}
```

has a tendency of being quite system-dependent because of precision issues.

In any case, if all you did was add an option, why did the output change?



---

archive/issue_comments_094159.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2010-11-26T22:25:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94159",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_094160.json:
```json
{
    "body": "Replying to [comment:15 jdemeyer]:\n> Has this been tested on various systems?  \nI have not tested it on various systems.\n\n> In any case, if all you did was add an option, why did the output change?\n\nThe option barycentric was no just added, it was made the default option, as suggested by rlm in \n\n[http://trac.sagemath.org/sage_trac/ticket/9699?replyto=15#comment:3](http://trac.sagemath.org/sage_trac/ticket/9699?replyto=15#comment:3)",
    "created_at": "2010-11-26T23:16:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94160",
    "user": "https://trac.sagemath.org/admin/accounts/users/fidelbarrera"
}
```

Replying to [comment:15 jdemeyer]:
> Has this been tested on various systems?  
I have not tested it on various systems.

> In any case, if all you did was add an option, why did the output change?

The option barycentric was no just added, it was made the default option, as suggested by rlm in 

[http://trac.sagemath.org/sage_trac/ticket/9699?replyto=15#comment:3](http://trac.sagemath.org/sage_trac/ticket/9699?replyto=15#comment:3)



---

archive/issue_comments_094161.json:
```json
{
    "body": "Replying to [comment:15 jdemeyer]:\n> {{{\n> {0: [0.0, 1.0], 1: [0.866025403784, -0.5], 2: [-0.866025403784, -0.5], 3: [0.433012701892, -0.25], 4: [-0.288675134595, -1.85037170771e-16], 5: [0.288675134595, 3.70074341542e-17], 6: [0.144337567297, 0.25]}\n> }}}\n\nJeroen is right. You should replace things like `0.866025403784` with `0.86...` so that numerical issues don't crop up.",
    "created_at": "2010-11-26T23:39:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94161",
    "user": "https://github.com/rlmill"
}
```

Replying to [comment:15 jdemeyer]:
> {{{
> {0: [0.0, 1.0], 1: [0.866025403784, -0.5], 2: [-0.866025403784, -0.5], 3: [0.433012701892, -0.25], 4: [-0.288675134595, -1.85037170771e-16], 5: [0.288675134595, 3.70074341542e-17], 6: [0.144337567297, 0.25]}
> }}}

Jeroen is right. You should replace things like `0.866025403784` with `0.86...` so that numerical issues don't crop up.



---

archive/issue_comments_094162.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2010-11-26T23:39:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94162",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_094163.json:
```json
{
    "body": "Please apply instead of previous patches.",
    "created_at": "2010-11-27T04:31:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94163",
    "user": "https://trac.sagemath.org/admin/accounts/users/fidelbarrera"
}
```

Please apply instead of previous patches.



---

archive/issue_comments_094164.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-11-27T04:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94164",
    "user": "https://trac.sagemath.org/admin/accounts/users/fidelbarrera"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_094165.json:
```json
{
    "body": "Attachment [trac_9699_5.patch](tarball://root/attachments/some-uuid/ticket9699/trac_9699_5.patch) by fidelbarrera created at 2010-11-27 04:33:49\n\nReplying to [comment:17 rlm]: \n> Jeroen is right. You should replace things like `0.866025403784` with `0.86...` so that numerical issues don't crop up. \n\nReplaced things like `0.866025403784` with `0.86...`.\n\nPlease see trac_9699_5.patch instead of previous versions.",
    "created_at": "2010-11-27T04:33:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94165",
    "user": "https://trac.sagemath.org/admin/accounts/users/fidelbarrera"
}
```

Attachment [trac_9699_5.patch](tarball://root/attachments/some-uuid/ticket9699/trac_9699_5.patch) by fidelbarrera created at 2010-11-27 04:33:49

Replying to [comment:17 rlm]: 
> Jeroen is right. You should replace things like `0.866025403784` with `0.86...` so that numerical issues don't crop up. 

Replaced things like `0.866025403784` with `0.86...`.

Please see trac_9699_5.patch instead of previous versions.



---

archive/issue_comments_094166.json:
```json
{
    "body": "Okay, I tested all long doctests on a 64 bit Linux machine, and all passed. I also tested long doctests in `sage/graphs` on a 32 bit Linux machine, and again all tests pass. Things look good.",
    "created_at": "2010-11-28T16:32:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94166",
    "user": "https://github.com/rlmill"
}
```

Okay, I tested all long doctests on a 64 bit Linux machine, and all passed. I also tested long doctests in `sage/graphs` on a 32 bit Linux machine, and again all tests pass. Things look good.



---

archive/issue_comments_094167.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-28T16:32:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94167",
    "user": "https://github.com/rlmill"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_094168.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-11-28T16:59:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94168",
    "user": "https://github.com/rlmill"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_094169.json:
```json
{
    "body": "It seems I pressed submit too soon. Indeed all tests pass on the 64 bit system.\n\nHowever on the 32-bit system, things seem to freeze at the following test:\n\n```\nTrying:\n    g = graphs.BalancedTree(Integer(3),Integer(4))###line 2658:_sage_    >>> g = graphs.BalancedTree(3,4)\nExpecting nothing\nok\nTrying:\n    g.set_planar_positions(test=True)###line 2659:_sage_    >>> g.set_planar_positions(test=True)\nExpecting:\n    True\n```\n",
    "created_at": "2010-11-28T16:59:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94169",
    "user": "https://github.com/rlmill"
}
```

It seems I pressed submit too soon. Indeed all tests pass on the 64 bit system.

However on the 32-bit system, things seem to freeze at the following test:

```
Trying:
    g = graphs.BalancedTree(Integer(3),Integer(4))###line 2658:_sage_    >>> g = graphs.BalancedTree(3,4)
Expecting nothing
ok
Trying:
    g.set_planar_positions(test=True)###line 2659:_sage_    >>> g.set_planar_positions(test=True)
Expecting:
    True
```




---

archive/issue_comments_094170.json:
```json
{
    "body": "Ugh. Once again I spoke too soon.\n\nThe real problem is just that the doctests take *much* longer after the patch than before.\n\nOn the 32 bit system it went from 243.2 s for `generic_graph.py` up to 623.8 s after the patch.\n\nOn the (much faster) 64 bit system it was 130.4 s before and 441.2 s after.\n\nThis definitely counts as a regression, and I can't let things through with so much of a slowdown.",
    "created_at": "2010-11-28T17:12:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9699#issuecomment-94170",
    "user": "https://github.com/rlmill"
}
```

Ugh. Once again I spoke too soon.

The real problem is just that the doctests take *much* longer after the patch than before.

On the 32 bit system it went from 243.2 s for `generic_graph.py` up to 623.8 s after the patch.

On the (much faster) 64 bit system it was 130.4 s before and 441.2 s after.

This definitely counts as a regression, and I can't let things through with so much of a slowdown.



---

archive/issue_events_024235.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "milestone": "sage-4.6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9699#event-24235"
}
```



---

archive/issue_events_024236.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9699#event-24236"
}
```



---

archive/issue_events_024237.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9699#event-24237"
}
```



---

archive/issue_events_024238.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9699#event-24238"
}
```



---

archive/issue_events_024239.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9699#event-24239"
}
```



---

archive/issue_events_024240.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9699#event-24240"
}
```



---

archive/issue_events_024241.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9699#event-24241"
}
```



---

archive/issue_events_024242.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/9699",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9699#event-24242"
}
```
