# Issue 2963: make it so that strings pass as arguments and keyword arguments for the expect interfaces are passed down as string.

Issue created by migration from Trac.

Original creator: mhansen

Original creation time: 2008-04-20 01:46:25

Assignee: mhansen

One should be able to do 


```
r.png(file="myplot3.png")
```


instead of 


```
sage: r.png(file='"myplot3.png"')
```



---

Comment by SimonKing created at 2009-09-21 20:38:38

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

Comment by SimonKing created at 2009-09-21 20:59:33

Replying to [comment:1 SimonKing]:
> I don't know in what way png is usually called: Frequently and with many arguments? Then my suggestion might involve a performance problem. Also I don't know if the application of `f` to `args` is needed as well, or if the application to `kwds` would be enough.

Sorry, perhaps I misunderstood the role of png: It is just one example, isn't it? But actually you want that in _all_ expect interfaces the transition from 'bla' to '"bla"' is done, right? Then still my suggestion would solve the problem, but I guess the above lambda function should be defined in expect.py on module level, so that there is no need to create  the function over and over again.

Then, one would go through _all_ methods of all expect interfaces, and do changes to the arguments, if they might be strings. Wow, that would be much to do! And then I don't know how much performance regression would occur and if that price would be worth to pay for making the input more comfortable.

Cheers,
Simon


---

Comment by kcrisman created at 2012-05-18 01:26:02

See also #12948, as many many people have asked how to do this in R and we still don't really have a nice solution for this in general.
