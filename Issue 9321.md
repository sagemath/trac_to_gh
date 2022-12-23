# Issue 9321: Documentation for sum() function should indicate Python syntax *first*

Issue created by migration from https://trac.sagemath.org/ticket/9321

Original creator: rlm

Original creation time: 2010-06-24 00:01:48

Assignee: mvngu

CC:  kcrisman

When did we hijack the sum function? Based on the documentation there, I have (today alone) had four different people come up to me and ask why something like the following doesn't work:


```
sage: sum(Integer(x), x, 0, 9)
```


I know the reasons this shouldn't work, but newbies definitely don't. It should say something about how to do

```
sage: sum( Integer(x) for x in range(10) )
```

before "getting all symbolic."


---

Comment by rws created at 2014-03-18 14:51:45

Changing priority from major to critical.


---

Comment by rws created at 2014-03-18 14:51:45

The sagenb bug spreadsheet has several examples, too.


---

Comment by rws created at 2014-03-18 15:59:07

Changing status from new to needs_review.


---

Comment by rws created at 2014-03-18 15:59:07

New commits:


---

Comment by kcrisman created at 2014-03-18 20:56:13

Nice first step.  I would also add some actual examples as the original reporter suggests - maybe with an explicit example showing what does and doesn't work along these lines.


---

Comment by git created at 2014-03-19 08:41:17

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by rws created at 2014-03-19 08:42:10

How about this? Cannot make it any shorter than that.


---

Comment by git created at 2014-03-19 08:51:54

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by tscrim created at 2014-03-19 16:05:28

Your warning messages are indented one too many times.


---

Comment by git created at 2014-03-19 16:31:05

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by rws created at 2014-03-19 17:24:37

Thanks for the review.


---

Comment by kcrisman created at 2014-03-20 02:57:19

Okay, I'm going to ask for one final thing.  Probably it isn't appropriate to have this warning be before one even sees the INPUT block!  Can you put this after the first few examples, and then have some wording indicating "now back to the examples" in a not-informal way?  Otherwise we'll have the opposite problem of everyone avoiding this function :)

Also, another nit-pick - try to put the `sum()` in double back ticks so that it typesets properly as code.  And... is there any general reference for the Python sum, or are all of them version-dependent?  (I think the latter, just checking in case you know).

Thanks! Sorry this is an incremental review but it will be more awesomer soon.


---

Comment by rws created at 2014-03-20 09:29:49

I moved the warning a bit lower and added necessary backticks. I also removed the version string from the python link, although you will still arrive at the 2.x version. It's no longer hardcoded however. Finally, I had to change the branch path because `git amend`ed commits are not accepted by `sage -dev push`.
----
New commits:


---

Comment by tscrim created at 2014-06-22 04:41:25

Karl-Dieter, are you happy with the current version? (Really this is an elaborate **ping**.)


---

Comment by kcrisman created at 2014-06-24 16:02:10

> I also removed the version string from the python link, although you will still arrive at the 2.x version. It's no longer hardcoded however. 
https://docs.python.org/{2,3}/library/functions.html#sum is the link, technically.  I won't hold it up for that, though, since they can just click on "sum" from the big list at that location.  Doc looks good now.
> Karl-Dieter, are you happy with the current version? (Really this is an elaborate ping.)
:-)  Sorry for the delay; I definitely have been having to cut back even on review time the past few months.


---

Comment by kcrisman created at 2014-06-24 16:02:10

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-06-26 01:50:41

Resolution: fixed
