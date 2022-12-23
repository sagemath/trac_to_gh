# Issue 9675: New package: Brian, a simulator for spiking neural networks

Issue created by migration from https://trac.sagemath.org/ticket/9675

Original creator: uri

Original creation time: 2010-08-03 16:02:16

Assignee: tbd

CC:  mhansen mvngu schilly

Keywords: brian brain simulator neuronal dynamics

I've created a Sage package from an already existing Python package called Brian (see http://www.briansimulator.org/ for more information). The description that is provided in this webpage is the following:

_Brian is a simulator for spiking neural networks available on almost all platforms. The motivation for this project is that a simulator should not only save the time of processors, but also the time of scientists. It is easy to learn and use, highly flexible and easily extensible. The Brian package itself and simulations using it are all written in the Python programming language._

I'm not sure whether this package should be proposed as experimental or optional. For the moment I've put it as an experimental package. However, I think it could be optional, because as a Python package it has been widely tested and works perfectly, so I don't think there'll be a lot of problems as a Sage package. Please, let me know your opinion on that.

I must say I detected some problems with Brian units related to the Sage classes 'RealNumber' and 'Integer', so I created a patch so that when Brian is imported these two classes are redefined as follows:


```
RealNumber=float
Integer=int
```


This solves the problems. 

I attach the .spkg here (I know it's better just to provide a link, but I don't have anywhere else to upload it to).

Please, let me know what you think!


---

Comment by uri created at 2010-08-03 16:23:40

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-08-03 17:21:17

Cool!  
You may also want to see [this](http://groups.google.com/group/sage-devel/browse_thread/thread/9cec3d5595044b4f/ef8474417a60fbfa?show_docid=ef8474417a60fbfa) thread on sage-devel about where to put spkgs.  

As to the redefining, that seems... problematic.  There are other Sage Python packages that must encounter the same problems - you may want to ask on the list about how they deal with this.  (I suppose numpy and matplotlib would be likely candidates for this.)

What platforms does Brian work on out of the box?


---

Comment by uri created at 2010-08-04 14:45:01

Replying to [comment:2 kcrisman]:
> Cool!  
> You may also want to see [this](http://groups.google.com/group/sage-devel/browse_thread/thread/9cec3d5595044b4f/ef8474417a60fbfa?show_docid=ef8474417a60fbfa) thread on sage-devel about where to put spkgs.  

Thanks, I didn't know about Google Code!

> As to the redefining, that seems... problematic.  There are other Sage Python packages that must encounter the same problems - you may want to ask on the list about how they deal with this.  (I suppose numpy and matplotlib would be likely candidates for this.)
Yes, I'll give it a try, but I'm not sure if I'll be able to find another solution. I'll let you know.

> What platforms does Brian work on out of the box?   
Well, in the website they say: _All platforms running Python, so at least Windows, Linux and Mac_. I can't say more than that, as I've tried it just on Linux.


---

Comment by uri created at 2010-08-04 19:29:45

Replying to [comment:2 kcrisman]:
> As to the redefining, that seems... problematic.

And turning of the preparser via:


```
preparser(false)
```


would also be problematic?


---

Comment by kcrisman created at 2010-08-04 19:49:26

Replying to [comment:4 uri]:
> Replying to [comment:2 kcrisman]:
> > As to the redefining, that seems... problematic.
> 
> And turning of the preparser via:
> 
> {{{
> preparser(false)
> }}}
> 
> would also be problematic?
Well, the issues is that a lot of Sage would no longer work as advertised.  That is fine if one is only using Brian, but presumably the point of having Brian as an optional package is that one could go back and forth with other parts of Sage.  I don't know exactly what other such packages do, though.  I highly suggest just emailing sage-devel (perhaps in reply to your original message) and asking what ways around this there are; I assume they exist.  Good luck!


---

Comment by uri created at 2010-08-09 15:25:58

Finally, Brian developers helped me to find a way to solve the problem without needing to redefine any Sage class nor to turn off the preparser. I've upload it on Google Code, you can download it [here](http://spkg-upload.googlecode.com/files/brian-1.2.1.p0.spkg). However, I'll re-upload it here in Trac page to avoid confusions.


---

Comment by kcrisman created at 2010-08-18 15:04:26

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-08-18 15:04:26

This seems to build fine, the script is ok.   In terms of experimental, positive review - it didn't crash anything, and commands actually do things and give output that is consistent with it.

To release manager - what happens now?  It gets uploaded to the Sage mirrors as experimental package, maybe?  Who does that?

But in the interests of improving it - I don't see why this couldn't be an optional package, if you can find another potential maintainer (different ticket).  If so, you'd definitely want to have a SPKG-TEST file or whatever, since there are builtin tests.  But...

When I do

```
sage: import brian
sage: brian.tests()
```

I get that I'm missing `nose`.    I doubt that `nose` will be a Sage package anytime soon - or should it, if it makes tests that much easier?  Perhaps upstream would consider having a non-`nose` option for testing.

When I try the brian website examples, it tells me that the Sage matplotlib backend doesn't support `show()`.  That would be another thing to figure out.


---

Comment by mpatel created at 2010-08-24 07:05:28

Changing status from positive_review to needs_work.


---

Comment by mpatel created at 2010-08-24 07:05:28

The package has unchecked-in changes:

```sh
$ hg stat
? .hgignore
? SPKG.txt
? patches/units.py
? patches/units.py.patch
? spkg-install
```

Oriol, could you add these files to the repository and commit the changes with the ticket number in the commit string.

Also, could you please add yourself to the [account name-real name map](http://trac.sagemath.org/sage_trac/wiki/WikiStart#AccountNamesmappedtoRealNames)?  Thanks!


---

Comment by kcrisman created at 2010-08-24 11:37:23

Oh, I'm so sorry, Mitesh - here I was checking whether the spkg worked but forgot to actually rebuild the spkg from its constituents.  If I ran sage-pkg on it would it have shown this?


---

Comment by uri created at 2010-08-31 10:56:20

Replying to [comment:8 mpatel]:
> The package has unchecked-in changes:
> {{{
> #!sh
> $ hg stat
> ? .hgignore
> ? SPKG.txt
> ? patches/units.py
> ? patches/units.py.patch
> ? spkg-install
> }}}
> Oriol, could you add these files to the repository and commit the changes with the ticket number in the commit string.

Ok, done. Please, let me know if it's allright, it's the first time I added files to the repository and I want to be sure I did everything correctly.

> Also, could you please add yourself to the [account name-real name map](http://trac.sagemath.org/sage_trac/wiki/WikiStart#AccountNamesmappedtoRealNames)?  
Done!

> Thanks!
Thanks to you for your commments!!


---

Comment by uri created at 2010-08-31 11:07:36

Replying to [comment:7 kcrisman]:
> But in the interests of improving it - I don't see why this couldn't be an optional package, if you can find another potential maintainer (different ticket).  If so, you'd definitely want to have a SPKG-TEST file or whatever, since there are builtin tests.  But...
> 
> When I do
> {{{
> sage: import brian
> sage: brian.tests()
> }}}
> I get that I'm missing `nose`.    I doubt that `nose` will be a Sage package anytime soon - or should it, if it makes tests that much easier?  Perhaps upstream would consider having a non-`nose` option for testing.

I don't really know what to say about that... I don't know `nose` and haven't looked at these tests much. I'll think about it, though. However, is it really necessary to include tests on the packages, in order to be set as optional instead of experimental?

> When I try the brian website examples, it tells me that the Sage matplotlib backend doesn't support `show()`.  That would be another thing to figure out.

Yes, I had already seen that. The problem is not in Brian but in the matplotlib package itself... there're other ways to see the images, for example replacing the show() command for:

```
sage: savefig('figure.png')
```

which creates the file _figure.png_ in the working directory. Maybe that should be specified in the documentation. What do you think?


---

Comment by mpatel created at 2010-08-31 21:46:01

Replying to [comment:10 uri]:
> Replying to [comment:8 mpatel]:
> > Oriol, could you add these files to the repository and commit the changes with the ticket number in the commit string.
> 
> Ok, done. Please, let me know if it's allright, it's the first time I added files to the repository and I want to be sure I did everything correctly.

I apologize if I've missed it, but is there a link to the updated package?


---

Comment by uri created at 2010-09-01 09:14:17

Replying to [comment:12 mpatel]:
> I apologize if I've missed it, but is there a link to the updated package?

You can download it clicking [here](http://spkg-upload.googlecode.com/files/brian-1.2.1.p0.spkg), but it's the same link I provided before (there's been no update, I just added the files to the repository).


---

Comment by uri created at 2010-09-01 09:32:11

Replying to [comment:13 uri]:
> ..but it's the same link I provided before (there's been no update, I just added the files to the repository).

ok, just to avoid confusions, what I mean by that is that the link is the same because I didn't change the name of the package (from brian-1.2.1.p0 to  brian-1.2.1.p1) because there's been no update. So you'll download the right file with the old link.


---

Comment by uri created at 2010-09-01 09:32:46

Brian package (.spkg  file)


---

Comment by mpatel created at 2010-09-01 09:36:14

Changing status from needs_work to needs_review.


---

Attachment


---

Comment by kcrisman created at 2010-09-17 00:28:06

# 9221 is related (making nose an optional/standard package).


---

Comment by kcrisman created at 2010-09-17 20:17:02

Changing status from needs_review to positive_review.


---

Comment by kcrisman created at 2010-09-17 20:17:02

Okay, I checked this all out again, and now the HG is fine, and I can't find any garbage files, and it still applies fine to Sage 4.5.3, and I think this is more than ready to be an experimental package. 

If you want, you can find people to test it on a couple other platforms to make sure it's ready for optional package status - I'm not sure exactly what the protocol for that is, though it seems to me that it's more than ready compared to other denizens of http://www.sagemath.org/packages/optional/.  But that could also be another ticket.  At the very least it should get loaded up to the mirrors.  Make it so!


---

Comment by mpatel created at 2010-09-17 20:42:25

Harald, Mike, or Minh, could one of you add [attachment:brian-1.2.1.p0.spkg] to the experimental / contributed package repository?


---

Comment by mpatel created at 2010-09-17 20:47:45

Replying to [comment:16 kcrisman]:
> # 9221 is related (making nose an optional/standard package).

Small correction: #9921 is about this, though there is a discussion about nose at #9221.


---

Comment by kcrisman created at 2010-09-18 00:16:11

Replying to [comment:19 mpatel]:
> Replying to [comment:16 kcrisman]:
> > # 9221 is related (making nose an optional/standard package).
> 
> Small correction: #9921 is about this, though there is a discussion about nose at #9221.
Aagh!  That's the same mistake Jason made on #9221 in referring (or not) to #9921... sorry.


---

Comment by mvngu created at 2010-09-19 06:27:56

Resolution: fixed


---

Comment by mvngu created at 2010-09-19 06:27:56

Replying to [comment:18 mpatel]:
> Harald, Mike, or Minh, could one of you add [attachment:brian-1.2.1.p0.spkg] to the experimental / contributed package repository?

Done. See

http://www.sagemath.org/packages/experimental/


---

Comment by mpatel created at 2010-09-19 06:33:41

Thanks, Minh!


---

Comment by uri created at 2010-09-19 17:06:21

Great, thank you all!
I'll open a new ticket to see if it can be accepted as an optional package.


---

Comment by mhampton created at 2010-10-01 02:54:24

There's been some discussion on other tickets about the virtues of nose, so it might not be that unlikely to make it standard in Sage.
