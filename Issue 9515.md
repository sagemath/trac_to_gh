# Issue 9515: make an optional spkg for PyCryptoPlus

Issue created by migration from https://trac.sagemath.org/ticket/9515

Original creator: malb

Original creation time: 2010-07-16 09:26:40

Assignee: mvngu

CC:  mhansen mvngu was

See

  http://wiki.yobi.be/wiki/PyCryptoPlus

and 

  http://groups.google.com/group/sage-devel/browse_thread/thread/500063cfaa2961b0/ 


---

Comment by malb created at 2010-08-09 11:32:41

I've uploaded an SPKG to

http://sage.math.washington.edu/home/malb/spkgs/pycryptoplus-20100809-git.spkg


---

Comment by malb created at 2010-08-09 11:32:47

Changing status from new to needs_review.


---

Comment by wdj created at 2010-08-09 13:57:27

Replying to [comment:2 malb]:

Applied find and passed sage -testall to 4.5.2.rc0 on a 10.6.4 mac. Testing on ubuntu now.


---

Comment by wdj created at 2010-08-10 16:44:08

Replying to [comment:3 wdj]:
> Replying to [comment:2 malb]:
> 
> Applied find and passed sage -testall to 4.5.2.rc0 on a 10.6.4 mac. Testing on ubuntu now.

Applied fine to 4.5.2 on 32bit ubuntu 10.04 and passed sage -testall.

Are there other tests needed, such as solaris or cygwin?


---

Comment by malb created at 2010-08-10 17:21:26

Replying to [comment:4 wdj]:

> Applied fine to 4.5.2 on 32bit ubuntu 10.04 and passed sage -testall. Are there other tests needed, such as solaris or cygwin?

I doubt it, since (a) this is a pure Python package and (b) this is an optional SPKG anyway.


---

Comment by wdj created at 2010-08-10 17:56:59

Replying to [comment:5 malb]:
> Replying to [comment:4 wdj]:
> 
> > Applied fine to 4.5.2 on 32bit ubuntu 10.04 and passed sage -testall. Are there other tests needed, such as solaris or cygwin?
> 
> I doubt it, since (a) this is a pure Python package and (b) this is an optional SPKG anyway.

I also checked that the SPKG.txt and
spkg-install file follow the conventions in 
http://www.sagemath.org/doc/developer/producing_spkgs.html#creating-a-new-spkg

I have emailed D Kirkby separately regarding the solaris issue. I'm
about to give this a positive review after hearing back from him.


---

Comment by wdj created at 2010-08-10 17:56:59

Changing status from needs_review to positive_review.


---

Comment by wdj created at 2010-08-10 18:41:12

Replying to [comment:6 wdj]:

> 
> I have emailed D Kirkby separately regarding the solaris issue. I'm
> about to give this a positive review after hearing back from him.
> 


Dave Kirkby replied that the script will run on solaris as well.


---

Comment by mpatel created at 2010-08-14 23:00:58

I've updated the Author(s) and Reviewer(s) fields.  Please correct them, if I'm wrong.

Mike, Minh, or William, could one of you merge this package into the optional spkg repository?  I don't have the privileges to do this.


---

Comment by mvngu created at 2010-08-15 04:39:48

Replying to [comment:8 mpatel]:
> Mike, Minh, or William, could one of you merge this package into the optional spkg repository?  I don't have the privileges to do this.

Done. See the updated page

http://www.sagemath.org/packages/optional/


---

Comment by mpatel created at 2010-08-15 06:55:10

Resolution: fixed


---

Comment by mpatel created at 2010-08-15 06:55:10

Thank you, Minh.
