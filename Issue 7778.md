# Issue 7778: Update jsMath-image-fonts install path detection

Issue created by migration from https://trac.sagemath.org/ticket/7778

Original creator: mpatel

Original creation time: 2009-12-28 05:32:11

Assignee: was

CC:  drkirkby robert.marik timdumol was

Post-#7467, the SageNB install path depends on its version, but `jsmath-image-fonts-1.4.p2.spkg` expects a slightly different format.

This ticket just updates `spkg-install`.

See [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/82304cb7adbb22f9), [sage-devel](http://groups.google.com/group/sage-devel/msg/10b3e588e9110322).

Related tickets: #7196, #7229, #7467, #7755.


---

Comment by mpatel created at 2009-12-28 06:12:56

There's a trial package at

 * [http://sage.math.washington.edu/home/mpatel/trac/7778/jsmath-image-fonts-1.4.p3.spkg](http://sage.math.washington.edu/home/mpatel/trac/7778/jsmath-image-fonts-1.4.p3.spkg)
 * [http://boxen.math.washington.edu/home/mpatel/trac/7778/jsmath-image-fonts-1.4.p3.spkg](http://boxen.math.washington.edu/home/mpatel/trac/7778/jsmath-image-fonts-1.4.p3.spkg)

I've CC'd Dr. Kirkby, because I see

```sh
$ checkbashisms -x -f spkg-install
possible bashism in spkg-install line 36 (bash arrays, ${name[0|*|@]}):
for DIR in ${CANDIDATES[@]}; do
possible bashism in spkg-install line 44 (bash arrays, ${name[0|*|@]}):
    echo "${CANDIDATES[*]}"
```

I don't know if these are problems on Solaris or, if they are, how to work around them.


---

Comment by mpatel created at 2009-12-28 06:12:56

Changing status from new to needs_review.


---

Comment by robert.marik created at 2009-12-28 11:54:53

Works with Sage 4.3. Positive review. Thanks for fixing.


---

Comment by robert.marik created at 2009-12-28 11:54:53

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-01-04 02:08:04

Resolution: fixed


---

Comment by mhansen created at 2010-01-04 02:08:04

I've merged this in with the optional spkgs.


---

Comment by was created at 2010-01-10 04:52:30

Hi,

I upgraded sagenb.org to use sagenb-0.5.  I then tried to install this spkg.  It definitely got confused and didn't work, for some reason (maybe because of an old sagenb from before).   I eventually *manually* copied the fonts to:

/usr/local/sage/local/lib/python/site-packages/sagenb/data/jsmath/fonts

where sagenb is a symlink to sagenb-0.5-*egg/sagenb, and this did work. 

Notice that:

```
root@boxen:/usr/local/sage/local/lib/python/site-packages/sagenb/data/jsmath/fonts# python
Python 2.5.2 (r252:60911, Jul 22 2009, 15:33:10) 
[GCC 4.2.4 (Ubuntu 4.2.4-1ubuntu3)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> import os
>>> from pkg_resources import Requirement, working_set
>>> sagenb_path = working_set.find(Requirement.parse('sagenb')).location
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'NoneType' object has no attribute 'location'
```


I'm really just recording this for posterity in case there really is something wrong.  I don't have time to delve deeper now.


---

Comment by mpatel created at 2010-01-10 06:08:17

I would not be surprised, if it really is wrong.  The Python script embedded in `spkg-install` is run with `/usr/bin/env python`.  Maybe this doesn't always use Sage's `python`?
