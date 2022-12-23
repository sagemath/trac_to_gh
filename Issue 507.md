# Issue 507: Bad error message when running a script

Issue created by migration from https://trac.sagemath.org/ticket/507

Original creator: was

Original creation time: 2007-08-29 08:16:40

Assignee: was

1. Create a script test.sage with this 1 line

```
solve([x==1], x)
```


2. Run it like so:

```
  $ sage test.sage
  Exception exceptions.AttributeError: "'NoneType' object has no attribute 'ExceptionPexpect'" in  ignored
```


3. If you put instead

```
print solve([x==1], x)
```

then everything works fine.

Clearly there is a bug there, probably with quitting the pexpect interface to maxima. 



---

Attachment

I've attached a work-around for this bug (6116.patch). It is probably best to understand the behaviour first, but the attached patch works around it for now.


---

Comment by mabshoff created at 2007-09-17 08:23:39


```
[09:58] <mabshoff> But it would still be interesting to see what causes the problem.
[09:59] <janwil> yes, it's a mystery to me right now ...
[09:59] <mabshoff> Not only to you :)
[09:59] <janwil> :)
[10:01] <mhansen_> Yeah, that worked for me.
[10:01] <mabshoff> malb's patch?
[10:02] <mhansen_> Yep.
[10:02] <mabshoff> Well, we should get it merged in 2.8.4.3 then. We can always revert it in case it causes 
[10:02] <mhansen_> I was also getting that error when I was running some of the tests with nose.   The tests would pass, but those would come up at the end.
[10:03] <mabshoff> trouble on a range of platforms.
[10:03] <mabshoff> Interesting.
```



---

Comment by was created at 2007-09-20 19:03:05

Resolution: fixed
