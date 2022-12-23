# Issue 8216: Make David Perkinson's sandpile 2.0 module an optional package

Issue created by migration from https://trac.sagemath.org/ticket/8216

Original creator: mhampton

Original creation time: 2010-02-08 20:20:14

Assignee: tbd

CC:  dperkinson wdj jdemeyer

Keywords: sandpile

Recently the sandpile-1.51 spkg was included in the experimental components.  This ticket updates the source to version 2.0.

In addition to updating the source, the installation script has been simplified and the SPKG.txt has been improved in an effort to get this package to optional status.  

This package does depend on the 4ti2.p0 spkg, which is currently experimental.  As a separate but dependent ticket 4ti2 will be upgraded to an optional package as well to harmonize this dependency.

New package is at:
[http://sage.math.washington.edu/home/mhampton/sandpile-2.0.spkg](http://sage.math.washington.edu/home/mhampton/sandpile-2.0.spkg)


---

Comment by mhampton created at 2010-02-08 20:20:24

Changing status from new to needs_review.


---

Comment by wdj created at 2010-02-09 18:04:58

I'm not sure what needs review means here. Isn't this supposed to be voted on on sage-devel? Also, does this come after/depend on the 4ti2.p0 spkg ticket/vote http://trac.sagemath.org/sage_trac/ticket/8217 ?


---

Comment by mhampton created at 2010-02-09 18:19:38

I don't optional packages require a vote, no.  Making a package standard does.

Yes, I guess this does depend on 8217, although for review purposes it isn't in the sense that "sage -i 4ti2.p0" will work wether or not its experimental or optional.


---

Comment by wdj created at 2010-02-09 21:04:43

Replying to [comment:4 mhampton]:
> I don't optional packages require a vote, no.  Making a package standard does.
> 

Okay.

> Yes, I guess this does depend on 8217, although for review purposes it isn't in the sense that "sage -i 4ti2.p0" will work 
> wether or not its experimental or optional.

What would you like the review to consist of? 

I have read the documentation and used the functions in the spkg and the sandpile.sage file. Is sandpile.sage in this spkg?


---

Comment by drkirkby created at 2010-02-22 00:38:29

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2010-02-22 00:38:29

My understanding was that experimental packages did not require a vote, but optional did. As such, this would require a vote. 

This is severely broken on Solaris, but reports it is successfully installed. One obvious problem is the use of a non-POSIX option to grep. 


```
sandpile-2.0/src/
sandpile-2.0/src/sandpile.py
Finished extraction
****************************************************
Host system
uname -a:
SunOS redstart 5.10 Generic sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
gcc -v
Using built-in specs.
Target: sparc-sun-solaris2.10
Configured with: ../gcc-4.4.3/configure --prefix=/usr/local/gcc-4.4.3 --with-mpfr=/usr/local/gcc-4.4.3 --with-build-time-tools=/usr/ccs/bin --with-gmp=/usr/local/gcc-4.4.3 --enable-languages=c,c++,fortran
Thread model: posix
gcc version 4.4.3 (GCC) 
****************************************************
Installing glpk-4.38.p4
Calling sage-spkg on glpk-4.38.p4
Warning: Attempted to overwrite SAGE_ROOT environment variable
glpk-4.38.p4
Machine:
SunOS redstart 5.10 Generic sun4u sparc SUNW,Sun-Blade-1000
Deleting directories from past builds of previous/current versions of glpk-4.38.p4
/export/home/drkirkby/sage-4.3.3.alpha1/local/bin/sage-spkg: file glpk-4.38.p4 does not exist
Attempting to download it.
grep: illegal option -- o
Usage: grep -hblcnsviw pattern file . . .
Searching for latest version of glpk-4.38.p4
Traceback (most recent call last):
  File "/export/home/drkirkby/sage-4.3.3.alpha1/local/bin/sage-latest-online-package", line 54, in <module>
    packages = spkg_list(repository)
  File "/export/home/drkirkby/sage-4.3.3.alpha1/local/bin/sage-latest-online-package", line 43, in spkg_list
    data = urllib2.urlopen(web_url)
  File "/export/home/drkirkby/sage-4.3.3.alpha1/local/lib/python/urllib2.py", line 124, in urlopen
    return _opener.open(url, data, timeout)
  File "/export/home/drkirkby/sage-4.3.3.alpha1/local/lib/python/urllib2.py", line 389, in open
    response = self._open(req, data)
  File "/export/home/drkirkby/sage-4.3.3.alpha1/local/lib/python/urllib2.py", line 407, in _open
    '_open', req)
  File "/export/home/drkirkby/sage-4.3.3.alpha1/local/lib/python/urllib2.py", line 367, in _call_chain
    result = func(*args)
  File "/export/home/drkirkby/sage-4.3.3.alpha1/local/lib/python/urllib2.py", line 1146, in http_open
    return self.do_open(httplib.HTTPConnection, req)
  File "/export/home/drkirkby/sage-4.3.3.alpha1/local/lib/python/urllib2.py", line 1121, in do_open
    raise URLError(err)
urllib2.URLError: <urlopen error [Errno 8] node name or service name not known>

Installing 4ti2.p0
Calling sage-spkg on 4ti2.p0
Warning: Attempted to overwrite SAGE_ROOT environment variable
4ti2.p0
Machine:
SunOS redstart 5.10 Generic sun4u sparc SUNW,Sun-Blade-1000
Deleting directories from past builds of previous/current versions of 4ti2.p0
/export/home/drkirkby/sage-4.3.3.alpha1/local/bin/sage-spkg: file 4ti2.p0 does not exist
Attempting to download it.
grep: illegal option -- o
Usage: grep -hblcnsviw pattern file . . .
Searching for latest version of 4ti2.p0
Traceback (most recent call last):
  File "/export/home/drkirkby/sage-4.3.3.alpha1/local/bin/sage-latest-online-package", line 54, in <module>
    packages = spkg_list(repository)
  File "/export/home/drkirkby/sage-4.3.3.alpha1/local/bin/sage-latest-online-package", line 43, in spkg_list
    data = urllib2.urlopen(web_url)
  File "/export/home/drkirkby/sage-4.3.3.alpha1/local/lib/python/urllib2.py", line 124, in urlopen
    return _opener.open(url, data, timeout)
  File "/export/home/drkirkby/sage-4.3.3.alpha1/local/lib/python/urllib2.py", line 389, in open
    response = self._open(req, data)
  File "/export/home/drkirkby/sage-4.3.3.alpha1/local/lib/python/urllib2.py", line 407, in _open
    '_open', req)
  File "/export/home/drkirkby/sage-4.3.3.alpha1/local/lib/python/urllib2.py", line 367, in _call_chain
    result = func(*args)
  File "/export/home/drkirkby/sage-4.3.3.alpha1/local/lib/python/urllib2.py", line 1146, in http_open
    return self.do_open(httplib.HTTPConnection, req)
  File "/export/home/drkirkby/sage-4.3.3.alpha1/local/lib/python/urllib2.py", line 1121, in do_open
    raise URLError(err)
urllib2.URLError: <urlopen error [Errno 8] node name or service name not known>


real    0m1.394s
user    0m0.631s
sys     0m0.710s
Successfully installed sandpile-2.0
```


It would need to be able to build on Solaris before it could be incorporated into Sage

There's general information about building on Solaris at

  http://wiki.sagemath.org/solaris

 Information specifically for 't2' at

  http://wiki.sagemath.org/devel/Building-Sage-on-the-T5240-t2

 Both the source (4.3.0.1 is the latest to build on Solaris) and a binary
 which will run on any SPARC can be found at http://www.sagemath.org
 /download-source.html

 Dave


---

Comment by mhampton created at 2010-02-22 14:19:42

No, optional packages do not require a vote.  Making a package standard does.  However, the expectations for an optional package keep rising.  I think building on Solaris is probably considered a requirement.

I'm not sure where these grep calls are coming from, they look like the installation script uses them somehow when adding glpk and 4ti2 but it just uses "sage -i".


---

Comment by drkirkby created at 2010-02-22 15:54:30

Replying to [comment:8 mhampton]:
> No, optional packages do not require a vote. 

Thank you for clarification on this. 

So what (if any) additional requirements are there for 'optional' as opposed to 'experimental' packages? 

http://www.sagemath.org/packages/optional/

gives no warnings that the optional packages may be seriously broken, whereas 'experimental'

http://www.sagemath.org/packages/experimental/

has in great big bold letters that *These are EXPERIMENTAL! They probably won't work at all for you! Use at your own risk! Many of these have *never* been successfully built on any platform! (But still, if you can figure out how to build them, I'd like to know about it.) These also may not be available under a GPL-compatible license*

> Making a package standard does.  

Yes, I was aware of that. There would be complete chaos if not. 

> However, the expectations for an optional package keep rising.  I think building on Solaris is probably considered a requirement.
 
I'd hope so. http://www.sagemath.org/doc/developer/inclusion.html says 

*Some Sage developers are willing to help you port to OS X, Solaris and Windows. But this is no guarantee and you or your project are expected to do the heavy lifting and also support those ports upstream if there is no Sage developer who is willing to share the burden.*

I feel at the minute that I'm personally sharing too much responsibility for making sure the packages don't break on Solaris. William sends me a recent email:

'''David,

*(1) I couldn't get anywhere building Sage on x86 Solaris on skynet (fulvia).  Can you?  This was pretty annoying to the people that bought us fulvia.*

*(2) Sun wants to know if we have a Sage available yet for t2.  See below.*

*I really need to shift into the mode of actually providing something that *works* on Solaris, despite hickups, rather than just polishing foundations...*

Unfortunately, without more testing on Solaris, this is just not going to happen. I'm personally not in a position to test everyones patches on Solaris. 

> I'm not sure where these grep calls are coming from, they look like the installation script uses them somehow when adding glpk and 4ti2 but it just uses "sage -i".  

Me neither. But neither do I have the time to resolve this. A quick check on the man page for 'grep' on Linux shows the option 'o' being:


```
      -o, --only-matching
              Print  only  the  matched  (non-empty) parts of a matching line,
              with each such part on a separate output line.
```


I'll leave it to others to work out how to implement this in a POSIX compatible way. The POSIX options for 'grep' can be found at http://www.opengroup.org/onlinepubs/9699919799/utilities/grep.html 

I hope these comments are helpful, and I'll answer any questions I can, but I'm simply not in a position to sort out these issues. 

*PS I realise the author of this package has not requested any help on Solaris, so I'm not suggesting he is personally to blame for my frustration.*

Dave


---

Comment by mhampton created at 2010-11-25 17:25:02

Changing status from needs_work to needs_review.


---

Comment by mhampton created at 2010-11-25 17:25:02

I am quite frustrated by the lack of movement on this.  

A new package for the 2.1 version of the sandpile module is at:

http://sage.math.washington.edu/home/mhampton/sandpile-2.1.spkg


---

Comment by wdj created at 2010-11-25 17:34:12

Replying to [comment:10 mhampton]:
> I am quite frustrated by the lack of movement on this.  
> 
> A new package for the 2.1 version of the sandpile module is at:
> 
> http://sage.math.washington.edu/home/mhampton/sandpile-2.1.spkg
> 

I'm happy to review this over the winter break. Please ping me if I forget.


---

Comment by drkirkby created at 2010-12-01 15:28:29

There has been agreement over what are the requires for 
 * standard
 * optional
 * experimental

It's not yet in the developers guide, but soon will be - see #9690. 

Since one requirement for optional is *sage project as a whole is responsible* I think that probably means there should be a vote. I would think that pretty much a formality, but it does not seem reasonable for others to support a package if nobody feels it's worth having. 

Dave


---

Comment by wdj created at 2010-12-11 19:39:02

This new version applies fine to sage 4.6 (on an ubuntu linux machine) 
and to 4.6.1.a2 (on a 10.6.5 imac), and does not introduce any 
failures in the sage -testall suite.

However, some commands in the sandpile.sage file
http://people.reed.edu/~davidp/sand/sage/1.51/sandpile.sage
now fail. It seems to me that this should work as well.
I can work on trying to update that file, since it seems to be
the main source of the documentation
http://people.reed.edu/~davidp/sand/sage/2.0/html/sandpile.html
Because of this, I'm marking this as "needs info", so as to
get further feedback on this issue.

I know people who are working in the field of research, so I think
this is a useful optional package at least for some.


---

Comment by wdj created at 2010-12-11 19:39:02

Changing status from needs_review to needs_info.


---

Comment by mhampton created at 2010-12-31 21:45:12

Changing status from needs_info to needs_review.


---

Comment by drkirkby created at 2011-01-02 01:27:50

There's no 


```
## Special Update/Build Instructions
```


section in the spkg-install file. It would be worth adding it. There's no spkg-check file. Are there any self-tests? 

This bit of code is a bit dubious. First it's not a good idea to test on an empty string (though I'm aware lots of bits of Sage do it, but also there's an unnecessary semi-colon. 



```
if [ "$SAGE_LOCAL" = "" ]; then
   echo "SAGE_LOCAL undefined ... exiting";
   echo "Maybe run 'sage -sh'?"
   exit 1
fi
```


Better would be


```
if [ "x$SAGE_LOCAL" = x ]; then
   echo "SAGE_LOCAL undefined ... exiting"
   echo "Maybe run 'sage -sh'?"
   exit 1
fi
```


That semi-colon obviously got put in one file at one point, and has been copy/pasted to lots of spkg-install files, but it serves no useful function. 

I believe an earlier version of this did not work on Solaris. Has anyone checked if this one does work? I don't see any comments to suggest the issue was resolved. 

Dave


---

Comment by wdj created at 2011-01-03 12:33:26

I installed this spkg on a 10.6.5 mac running sage 4.6.1.rc0. This seemed to create a number of failed doctests. I'm guessing it is because the spkg-install file has the line


```
sage -i glpk-4.42.p0
```

whereas the standard version included with Sage is 4.44, according to http://www.sagemath.org/packages/standard/. Is there a reason why glpk-4.42 is loaded? If not, then this line should be deleted.


---

Comment by wdj created at 2011-01-03 12:33:26

Changing status from needs_review to needs_info.


---

Comment by mhampton created at 2011-01-13 04:41:19

Resolution: wontfix


---

Comment by mhampton created at 2011-01-13 04:41:19

It seems to make a lot more sense to me to just move this into the Sage library, since it is already effectively a Sage add-on (as opposed to a truly external component which doesn't depend on Sage).  So I have created ticket #10618 and modified David Perkinson's latest version (2.2) slightly so that it can be directly included.

Apparently the incompatibilities with the 1.51 version are unavoidable.  Once in the Sage library, future incompatibilities would have to be first deprecated.


---

Comment by mhampton created at 2011-01-13 04:43:48

Sorry, I didn't realize that resolving as "wontfix" automatically closes the ticket.  But no other status really makes sense.
