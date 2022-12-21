# Issue 8551: ace-5.0 package has gap version hardwired, etc.

Issue created by migration from Trac.

Original creator: dimpase

Original creation time: 2010-03-17 06:33:10

Assignee: tbd

CC:  wdj

the gap version 4.4.10 is hardwired there, and few other things are wrong, e.g no SPKG.txt
A new version with these fixes installs and on Sage >=4.3.3, can be found here:
http://sage.math.washington.edu/home/dima/packages/ace-5.0.p1.spkg


---

Comment by dimpase created at 2010-03-17 06:33:35

Changing status from new to needs_review.


---

Comment by dimpase created at 2010-03-25 12:47:33

and this too...
By the way, I don't see why ace ended up being a separate spkg.
Do you know, by any chance?
Thanks,
Dima


---

Comment by wdj created at 2010-03-26 11:06:37

Replying to [ticket:8551 dimpase]:
> the gap version 4.4.10 is hardwired there, and few other things are wrong, e.g no SPKG.txt
> 
> A new version, with these fixes installs and runs on Sage >=4.3.3, can be found here:
> http://sage.math.washington.edu/home/dima/packages/ace-5.0.p1.spkg


I think the link is wrong. http://boxen.math.washington.edu/home/dima/packages/
has no such spkg file.


---

Comment by dimpase created at 2010-03-27 07:24:04

Replying to [comment:4 wdj]:

> > A new version, with these fixes installs and runs on Sage >=4.3.3, can be found here:
> > http://sage.math.washington.edu/home/dima/packages/ace-5.0.p1.spkg
> 
> 
> I think the link is wrong. http://boxen.math.washington.edu/home/dima/packages/
> has no such spkg file.

Oops, sorry. Recovered from a daily backup and put back in place. The link works now. Long live backups!


---

Comment by wdj created at 2010-06-22 23:19:39

Replying to [comment:5 dimpase]:
> Replying to [comment:4 wdj]:
> 

...

> 
> Oops, sorry. Recovered from a daily backup and put back in place. 
> The link works now. Long live backups!
> 

Where is the distribution license? It is not clear that we are
legally allowed to distribute this code. I did not see any C code written by
Havas. Maybe he only contributed design ideas? Did you ask Ramsay 
if he licensed his C code under the GPL (or any code that allows for 
free distribution) ... ?


---

Comment by dimpase created at 2010-06-23 05:44:15

Replying to [comment:6 wdj]:
> Replying to [comment:5 dimpase]:
> > Replying to [comment:4 wdj]:
> > 
> 
> ...
> 
> > 
> > Oops, sorry. Recovered from a daily backup and put back in place. 
> > The link works now. Long live backups!
> > 
> 
> Where is the distribution license? It is not clear that we are
> legally allowed to distribute this code. I did not see any C code written by
> Havas. Maybe he only contributed design ideas? Did you ask Ramsay 
> if he licensed his C code under the GPL (or any code that allows for 
> free distribution) ... ?
> 

OK, I'll ask. As you know, ACE is distributed via GAP for ages...


---

Comment by dimpase created at 2010-08-02 10:30:04

Changing status from needs_review to needs_info.


---

Comment by leif created at 2013-04-25 18:30:47

[William is wondering](http://groups.google.com/group/sage-devel/browse_thread/thread/f1d69cfc0a3d220f#) whether we can remove this optional spkg.


---

Comment by kcrisman created at 2013-04-26 00:46:21


```
./spkg-install: line 36: cd: /Users/.../sage-5.9.rc0/local/lib//pkg//ace/: No such file or directory
./spkg-install: line 38: ./configure: No such file or directory
```

The problem (well, among others) is that it's using 

```
GAP0=`$SAGE_ROOT/spkg/standard/newest_version gap`
```

Also, it's first copied to the location and then configured there rather than built in `spkg/build` and then moved.  I don't know if that matters.

I think that until this is fixed, especially if this can just be installed as a GAP package, it would be okay to move ace to "experimental".


---

Comment by dimpase created at 2013-04-26 01:30:09

It seems that this package needs an update to work with GAP 4.5, anyway. I several times tried asking Havas about the license, no reply was ever received. One can look at how it is packaged with GAP 4.5.


---

Comment by jdemeyer created at 2015-04-09 10:11:26

Changing status from needs_info to positive_review.


---

Comment by jdemeyer created at 2015-04-09 10:11:26

`ace` is no longer an official Sage package, so this is obsolete.


---

Comment by dimpase created at 2015-04-09 10:25:37

Replying to [comment:16 jdemeyer]:
> `ace` is no longer an official Sage package, so this is obsolete.
hmm, what is an *official* gap package?
It's still here:
http://gap-system.org/Packages/ace.html


---

Comment by vbraun created at 2015-04-09 12:13:57

A package within Sage, I guess.

In any case, if we don't know the license we can't distribute it. So that settles it.


---

Comment by vbraun created at 2015-04-09 12:13:57

Resolution: wontfix
