# Issue 9597: Crap in pari-2.3.5.p1's spkg-install

Issue created by migration from https://trac.sagemath.org/ticket/9597

Original creator: leif

Original creation time: 2010-07-25 20:55:00

Assignee: tbd

CC:  mhansen

From `#sage-devel`:

```
<peter-}> Has anyone looked at the top line of pari-2.3.5.p1/spkg-install lately?
```


```sh
leif@portland:~/Sage/spkgs/pari-2.3.5.p1$ hg diff -r18 -r20 spkg-install | head
diff -r d622871cde08 -r eb10b79a288a spkg-install
--- a/spkg-install	Fri Mar 05 22:12:34 2010 -0800
+++ b/spkg-install	Tue Apr 27 09:04:49 2010 -0700
@@ -1,4 +1,4 @@
-#!/bin/sh
+B1;2000;0c#!/bin/sh
 ###########################################
 ## PARI
 ###########################################
@@ -163,7 +163,11 @@
leif@portland:~/Sage/spkgs/pari-2.3.5.p1$ hg blame spkg-install | head -n 1  
20: B1;2000;0c#!/bin/sh
```

(This has been introduced with #8782, which was merged into Sage 4.4.3.alpha0.)
 
The first line should be

```sh
#!/usr/bin/env bash
```

anyway. Other clean-ups should perhaps be on another ticket, s.t. this gets fixed immediately before someone runs into problems. 

The behavior is somewhat unpredictable and depends on the user's system configuration, the following is *just luck*:

```
...
****************************************************
./spkg-install: line 1: B1: command not found
./spkg-install: line 1: 2000: command not found
./spkg-install: line 1: 0c#!/bin/sh: No such file or directory
Configuring pari-2.3.5 (STABLE)
...
```



---

Comment by mpatel created at 2010-07-26 07:23:49

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-07-26 07:23:49

I've put a new spkg at

 http://sage.math.washington.edu/home/mpatel/trac/9597/pari-2.3.5.p2.spkg


---

Comment by mpatel created at 2010-07-26 07:24:13

Fix first line of `spkg-install`.  Also, use `/usr/bin/env bash`.


---

Attachment


---

Comment by ddrake created at 2010-07-26 07:46:56

How on earth did that ever work?!


---

Comment by ddrake created at 2010-07-26 07:46:56

Changing status from needs_review to positive_review.


---

Comment by ddrake created at 2010-07-26 07:47:27

Resolution: fixed


---

Comment by ddrake created at 2010-07-26 07:47:27

merged in 4.5.2.alpha1.


---

Comment by drkirkby created at 2010-07-27 18:21:53

Replying to [comment:3 ddrake]:
> How on earth did that ever work?!
I was wondering the same thing myself. I suspect 


```
$ /path/to/doggy/script 
```

would not work, as the script would not execute properly, but

```
$ sh /path/to/doggy/script 
```

will work, as the first line is just a syntax error.

Anyway, its good it's fixed. 

Dave


---

Comment by leif created at 2010-07-27 18:54:52

Replying to [comment:5 drkirkby]:
> Replying to [comment:3 ddrake]:
> > How on earth did that ever work?!
> I was wondering the same thing myself. I suspect  

```
$ /path/to/doggy/script 
```

> would not work, as the script would not execute properly,

Well, unless the loader interprets the first bytes as indicating something else, the script is fed to the default interpreter (which need not be a shell). (Some shells might interpret the header by themselves first.)

(Btw, `sage-spkg` does this:

```sh
...
chmod +x spkg-install
...
else # not Debian
    time ./spkg-install
fi
...
```

)

> but

```
$ sh /path/to/doggy/script 
```

> will work, as the first line is just a syntax error.

That depends on whether you have the programs `B1` and `2000` installed (or likewise defined a shell alias/function).


---

Comment by mpatel created at 2010-07-28 05:19:54

What do you think about creating a `sage-spkg-{check,checker,lint}` script that checks for various common spkg problems?  Or integrating the new checks into `sage-pkg`?


---

Comment by ddrake created at 2010-07-28 06:52:52

Replying to [comment:7 mpatel]:
> What do you think about creating a `sage-spkg-{check,checker,lint}` script that checks for various common spkg problems?  Or integrating the new checks into `sage-pkg`?

Sounds great. Doctesting for spkg packaging. So, you're volunteering? :)


---

Comment by mpatel created at 2010-07-28 08:42:59

At the moment, and probably over the next few months, I have several other incomplete projects that need more immediate attention.  But I've opened #9622.
