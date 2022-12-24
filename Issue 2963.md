# Issue 2963: make it so that strings pass as arguments and keyword arguments for the expect interfaces are passed down as string.

archive/issues_002963.json:
```json
{
    "body": "Assignee: mhansen\n\nOne should be able to do \n\n\n```\nr.png(file=\"myplot3.png\")\n```\n\n\ninstead of \n\n\n```\nsage: r.png(file='\"myplot3.png\"')\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2963\n\n",
    "created_at": "2008-04-20T01:46:25Z",
    "labels": [
        "interfaces",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.8",
    "title": "make it so that strings pass as arguments and keyword arguments for the expect interfaces are passed down as string.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2963",
    "user": "mhansen"
}
```
Assignee: mhansen

One should be able to do 


```
r.png(file="myplot3.png")
```


instead of 


```
sage: r.png(file='"myplot3.png"')
```


Issue created by migration from https://trac.sagemath.org/ticket/2963





---

archive/issue_comments_020433.json:
```json
{
    "body": "Hi Mike!\n\nJust a quick idea:\nCouldn't one simply do\n\n```\n    def png(self, *args, **kwds):\n        ...\n        f = lambda x: x if not isinstance(x,basestring) else ('%s'%x if x[0]==x[-1]=='\"' else '\"%s\"'%x)\n        return RFunction(self, 'png')(*[f(x) for x in args], **dict([(x,f(y)) for x,y in kwds.items()]))\n```\n\n\nThis would transform any string into a '\"string\"', unless string starts and ends with '\"' already, and any other input is untouched. In particular, my suggestion would not break existing code, since `r.png(file='\"myplot3.png\"')` would still be valid.\n\nI don't know in what way png is usually called: Frequently and with many arguments? Then my suggestion might involve a performance problem. Also I don't know if the application of `f` to `args` is needed as well, or if the application to `kwds` would be enough.\n\nRegards,\n   Simon",
    "created_at": "2009-09-21T20:38:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2963#issuecomment-20433",
    "user": "SimonKing"
}
```

Hi Mike!

Just a quick idea:
Couldn't one simply do

```
    def png(self, *args, **kwds):
        ...
        f = lambda x: x if not isinstance(x,basestring) else ('%s'%x if x[0]==x[-1]=='"' else '"%s"'%x)
        return RFunction(self, 'png')(*[f(x) for x in args], **dict([(x,f(y)) for x,y in kwds.items()]))
```


This would transform any string into a '"string"', unless string starts and ends with '"' already, and any other input is untouched. In particular, my suggestion would not break existing code, since `r.png(file='"myplot3.png"')` would still be valid.

I don't know in what way png is usually called: Frequently and with many arguments? Then my suggestion might involve a performance problem. Also I don't know if the application of `f` to `args` is needed as well, or if the application to `kwds` would be enough.

Regards,
   Simon



---

archive/issue_comments_020434.json:
```json
{
    "body": "Replying to [comment:1 SimonKing]:\n> I don't know in what way png is usually called: Frequently and with many arguments? Then my suggestion might involve a performance problem. Also I don't know if the application of `f` to `args` is needed as well, or if the application to `kwds` would be enough.\n\nSorry, perhaps I misunderstood the role of png: It is just one example, isn't it? But actually you want that in *all* expect interfaces the transition from 'bla' to '\"bla\"' is done, right? Then still my suggestion would solve the problem, but I guess the above lambda function should be defined in expect.py on module level, so that there is no need to create  the function over and over again.\n\nThen, one would go through *all* methods of all expect interfaces, and do changes to the arguments, if they might be strings. Wow, that would be much to do! And then I don't know how much performance regression would occur and if that price would be worth to pay for making the input more comfortable.\n\nCheers,\nSimon",
    "created_at": "2009-09-21T20:59:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2963#issuecomment-20434",
    "user": "SimonKing"
}
```

Replying to [comment:1 SimonKing]:
> I don't know in what way png is usually called: Frequently and with many arguments? Then my suggestion might involve a performance problem. Also I don't know if the application of `f` to `args` is needed as well, or if the application to `kwds` would be enough.

Sorry, perhaps I misunderstood the role of png: It is just one example, isn't it? But actually you want that in *all* expect interfaces the transition from 'bla' to '"bla"' is done, right? Then still my suggestion would solve the problem, but I guess the above lambda function should be defined in expect.py on module level, so that there is no need to create  the function over and over again.

Then, one would go through *all* methods of all expect interfaces, and do changes to the arguments, if they might be strings. Wow, that would be much to do! And then I don't know how much performance regression would occur and if that price would be worth to pay for making the input more comfortable.

Cheers,
Simon



---

archive/issue_comments_020435.json:
```json
{
    "body": "See also #12948, as many many people have asked how to do this in R and we still don't really have a nice solution for this in general.",
    "created_at": "2012-05-18T01:26:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2963",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2963#issuecomment-20435",
    "user": "kcrisman"
}
```

See also #12948, as many many people have asked how to do this in R and we still don't really have a nice solution for this in general.
