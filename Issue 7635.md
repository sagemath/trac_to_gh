# Issue 7635: notebook -- make it trivial for any user to restrict the notebook server to only listen on certain subdomain

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-12-09 06:14:09

Assignee: was




---

Attachment


---

Comment by was created at 2009-12-09 06:20:04

Changing status from new to needs_review.


---

Comment by was created at 2009-12-09 06:20:04

The attached patch implements the described capability.  The help from the notebook? output is:

```
        - ``subnets`` -- (default: None) a list of strings that define subnets;
          if given, requests to the notebook server from ip addresses
          that are not in any of the listed subnets are ignored.  See
          http://en.wikipedia.org/wiki/Subnetwork for more about subnets.
          An example input is ``subnets=['192.168.1.0/24', '216.34.0.0/16']``,
          which accepts any address of the form ``192.168.1.*`` or of the
          form ``216.34.*.*``.  For serious use, you may want to instead
          use your operating system's firewall, which is probably more
          robust and reduces the load on the server. 
```


NOTE: The patch includes ipaddr.py, which I understand will be in the next (major?) Python release, at which point it could be removed from sagenb (though this could impact standalone use).   Note that ipaddr.py is licensed PSF, so is OK to include.  It's copyright is owned by Google, I think.


---

Comment by was created at 2009-12-09 06:23:35

This depends on http://sage.math.washington.edu/home/wstein/patches/sagenb/sagenb-0.4.6.spkg


---

Comment by was created at 2009-12-09 07:01:23

add localhost to subnets by default, by request from dan drake.


---

Comment by ddrake created at 2009-12-09 08:07:32

Changing status from needs_review to needs_work.


---

Attachment

The code here is simple, and ipaddr.py will be in Python 2.7 and is (I think) in Python 3.1, so we can drop that later. The only thing I'm worried about now is something that confused me when testing this -- you have to specify `address=_` _in addition to'' `subnet=[...]`. That strikes me as confusing -- they seem to be saying the same thing.

Of course, if you read carefully and understand networking, they're not -- `address` refers to a network _interface_. So perhaps we can change `address` to `interface`, but continue accepting `address` for backwards compatibility? Something like this in the docstring:

```
            - ``interface``       -- (default: 'localhost'), address of network
              interface to listen on; give '' to listen on all interfaces. You may 
              use ``address`` here for backwards compatibility, but this is deprecated
              and will be removed in the future.
```

along with a warning issued when `notebook()` gets an `address=` keyword.

Or, we could have `subnets` imply `address=''`.

This will be a positive review once this small issue is sorted out.


---

Comment by ddrake created at 2009-12-09 08:11:49

Replying to [comment:1 was]:
> NOTE: The patch includes ipaddr.py, which I understand will be in the next (major?) Python release, at which point it could be removed from sagenb (though this could impact standalone use).   Note that ipaddr.py is licensed PSF, so is OK to include.  It's copyright is owned by Google, I think. 

The license is actually Apache 2.0. We already have a bunch of stuff in Sage with that license, so including this shouldn't be a problem.


---

Comment by was created at 2009-12-09 14:47:03

> The license is actually Apache 2.0. We already have a bunch of stuff 
> in Sage with that license, so including this shouldn't be a problem. 

Especially since the code will be in Python soon enough.   Also, there is a bunch of apache stuff in sagenb already.  Note that apache is GPLv2 incompatible, by the way, but it is GPLv3 compatible (hence GPLv2+ compatible), and everything in sage is GPLv2+. 

Dan -- regarding changing address=, would you be OK with that being a separate ticket.  I like tickets to be as small as possible, if possible.  I definitely agree with your suggested change.   See #7639.


---

Comment by was created at 2009-12-09 20:29:06

Changing status from needs_work to needs_review.


---

Comment by ddrake created at 2009-12-10 01:38:49

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2009-12-10 01:38:49

A separate ticket sounds good. Positive review.


---

Comment by ddrake created at 2009-12-10 01:47:09

Changing status from positive_review to needs_work.


---

Comment by ddrake created at 2009-12-10 01:47:09

Oops, I need to back up here...when I do `address="whatever.foo"`, it blocks localhost, since it's coming from 127.0.1.1 -- not 127.0.0.1. I think the localhost stuff should be 127.0.0.0/8 (http://en.wikipedia.org/wiki/Localhost). I'll upload a micro-patch for this.


---

Comment by ddrake created at 2009-12-10 02:04:42

William, can you test my little patch? Try something like `notebook(address='x.y.z', subnets=['blah'])` where x.y.z is the regular hostname of your computer and subnets is something reasonable with your external address. You should get denied access without my little patch and get access with it (presuming that your machine in this situation routes requests to the notebook via 127.0.1.1).


---

Comment by was created at 2009-12-10 06:53:18

Replying to [comment:8 ddrake]:
> Oops, I need to back up here...when I do `address="whatever.foo"`, it blocks localhost, since it's coming from 127.0.1.1 -- not 127.0.0.1. I think the localhost stuff should be 127.0.0.0/8 (http://en.wikipedia.org/wiki/Localhost). I'll upload a micro-patch for this.

Wow! Your localhost is 127.0.1.1?  What operating system is that on?  For me on OS X and sage.math, localhost is 127.0.0.1.  On Wikipedia it says "Localhost always translates to the loopback IP address 127.0.0.1 in IPv4."  (same page you reference).  That said, also according to wikipedia using 127.0.0.0/8 is safe.   Your patch has 127.0.0.1/8 by the way. 

I guess your micro patch doesn't quite work because of the line `if '127.0.0.1' not in subnets:` right above the insert line.

Also, are you sure about your patch?  You say: Try `notebook(address='x.y.z', subnets=['blah'])`  But as soon as you explicitly specify the address then Twisted only listens on that interface and ignores localhost or any other interface (localhost is just a network interface like any other).  

So unless I'm missing something (I usually am!) we shouldn't apply your micro patch and should change this back to "positive review".   What do you think?


---

Comment by was created at 2009-12-10 06:53:18

Changing status from needs_work to needs_review.


---

Comment by ddrake created at 2009-12-10 11:32:54

Replying to [comment:10 was]:
> Wow! Your localhost is 127.0.1.1?  What operating system is that on?  For me on OS X and sage.math, localhost is 127.0.0.1.  On Wikipedia it says "Localhost always translates to the loopback IP address 127.0.0.1 in IPv4."

I'm using Ubuntu 9.10. You're right that localhost always resolves to 127.0.0.1, but apparently connections over the loopback network interface can get assigned IP addresses other than that.

The source of all this confusion is that I've never actually given a real value to `address`! I have only ever given `address=''` to listen to everything, or not specified it at all to make it do localhost only. My computer is klee.kaist.ac.kr and I tried address='klee', so maybe I should go back and try some more.

> Your patch has 127.0.0.1/8 by the way. 

I noticed. I should change that, although the /8 bitmask means that the last three octets don't matter.

> I guess your micro patch doesn't quite work because of the line `if '127.0.0.1' not in subnets:` right above the insert line.

I noticed that before, but it's not going to make a big difference -- if someone puts '127.0.0.1/8' or whatever into subnets, then the resulting list in memory would be something like

```
['127.0.0.0/8', something, '127.0.0.1/8']
```

which won't make any real difference with access control.

 
> Also, are you sure about your patch?  You say: Try `notebook(address='x.y.z', subnets=['blah'])`  But as soon as you explicitly specify the address then Twisted only listens on that interface and ignores localhost or any other interface (localhost is just a network interface like any other).  
> 
> So unless I'm missing something (I usually am!) we shouldn't apply your micro patch and should change this back to "positive review".   What do you think?

I think I'm going to play around with the address keyword some more until I understand how it works. Maybe the patch at #7639 isn't quite right; do we need the name of an _interface_ (such as "eth0" or "lo") or an IP address to which that interface is bound? I'll play around a bit more and report back.


---

Comment by was created at 2009-12-10 18:26:03

> do we need the name of an interface (such as "eth0" or "lo") or an 
> IP address to which that interface is bound? I'll play around a bit 
> more and report back. 

I think we need the *address* to which that interface is bound.  That's why I called the parameter "address" before.  However, in twisted it is called "interface", so your suggestion to change that name is definitely correct.  See e.g., this diff there:

```
152	 	            strport = 'tcp:%s:interface=%s'%(port, address) 
 	161	            strport = 'tcp:%s:interface=%s'%(port, interface) 
```

Here strport gets passed on to twisted and has "interface=" in it. 

William


---

Attachment

use 127.0.0.0/8 instead of only 127.0.0.1


---

Comment by ddrake created at 2009-12-11 02:52:37

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2009-12-11 02:52:37

I've uploaded an improved version of the micro-patch.

Now I understand `address`. If you do something like

```
notebook(address='123.456.1.2', subnets=['123.456.0.0/16'])
```

(which, yes, I know is silly), then nothing we do with `subnets` will allow access via the loopback interface, since Twisted is simply not listening there. So getting denied access via loopback with the above is correct behavior. OTOH, with

```
notebook(address='', subnets=['123.456.0.0/16'])
```

I think it's more reasonable to put our own "127.0.0.0/8" into `subnets`, since the user did implicitly ask for Twisted to listen on the loopback interface.

I see that [Debian puts 127.0.1.1](http://www.debian.org/doc/manuals/reference/ch05.en.html#_the_hostname_resolution) into /etc/hosts. On my machine, that has the effect of having "localhost" resolve to 127.0.0.1, and "klee" resolve to 127.0.1.1. So we should definitely support the whole 127.*.*.* range.

Now that I understand the address/interface keyword, I'm putting your patches back to positive review. I also think we should allow 127.0.0.0/8; what do you think of my patch? Should the help text be modified to match the code?


---

Comment by was created at 2010-01-04 06:52:51

Merged into sagenb-0.4.8.


---

Comment by was created at 2010-01-04 06:52:51

Resolution: fixed
