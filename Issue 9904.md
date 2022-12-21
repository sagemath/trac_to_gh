# Issue 9904: Spkg logs should get timestamps

Issue created by migration from Trac.

Original creator: justin

Original creation time: 2010-09-13 20:49:39

Assignee: GeorgSWeber

CC:  leif

Put timestamps into the spkg logs, both at the beginning and the end of each build run for the spkg in question.

This aids both in debugging problems with the build and with evaluating performance issues in the build.


---

Comment by leif created at 2010-09-14 06:59:39

The only "problem": In which format?


---

Comment by leif created at 2010-09-16 12:15:44

I'd suggest using

```sh
date "+%F %T %z"
```

which is independent of the current locale, such that we get something like:

```
SPKG BUILD STARTED:  2010-09-16 13:52:21 +0200
...
SPKG BUILD FINISHED: 2010-09-16 13:52:30 +0200
```


Does anyone also want nanoseconds (`%N`)? (I'm not sure how portable that would be.)

Opinions? Substitute "BUILD" by "INSTALLATION" (since we might also run a test suite after successful installation)? Or should we add _additional_ timestamps for checks?

`spkg/installed/<package name>` currently looks like this:

```
PACKAGE NAME: pari-2.4.3.svn-12577.p5
INSTALL DATE: Sat Sep 11 20:54:15 CEST 2010
UNAME: Linux quadriga 2.6.32-24-generic #41-Ubuntu SMP Thu Aug 19 01:38:40 UTC 2010 x86_64 GNU/Linux
Sage VERSION: | Sage Version 4.6.alpha0, Release Date: 2010-09-10                  |
```

(I.e. uses "plain" `date`, which I don't like. The Sage version also has to be fixed, as already noted somewhere else.)


---

Comment by leif created at 2010-09-16 12:39:16

Replying to [comment:2 leif]:
> 

```
...
Sage VERSION: | Sage Version 4.6.alpha0, Release Date: 2010-09-10                  |
```

> The Sage version also has to be fixed, as already noted somewhere else.

See #9434.


---

Comment by drkirkby created at 2010-09-30 06:08:05

Replying to [comment:2 leif]:
> I'd suggest using
> {{{
> #!sh
> date "+%F %T %z"
> }}}
> which is independent of the current locale, such that we get something like:
> {{{
> SPKG BUILD STARTED:  2010-09-16 13:52:21 +0200
> ...
> SPKG BUILD FINISHED: 2010-09-16 13:52:30 +0200
> }}}


But that would be a portability problem, as %F is not in the [POSIX specification for date](http://www.opengroup.org/onlinepubs/009695399/utilities/date.html). Looking at the man page for date on a Linux machine I see:


```
%F     full date; same as %Y-%m-%d
```



So that would be an obvious improvement. 

> Does anyone also want nanoseconds (`%N`)? (I'm not sure how portable that would be.)

Just take a look at http://www.opengroup.org/onlinepubs/009695399/utilities/date.html and you will find it is not portable. 

> Opinions? Substitute "BUILD" by "INSTALLATION" (since we might also run a test suite after successful installation)? Or should we add _additional_ timestamps for checks?


I think it would be useful to add the output from 'uname -a' too, so when people post logs, we know what system they were built on. 

I probably have some other thoughts on this, but I'm very busy today and don't have time to look at tickets in much detail. Just adding an odd comment where I feel I can contribute something. 

Dave


---

Comment by drkirkby created at 2010-09-30 06:44:25

For performance evaluation, storing the time as seconds since the Epoch would be useful. A portable way to do this is below:


```
# Compute seconds since the Epoch.

# Call 'date'. Note that
# %Y = year including century
# %j = day number (1-365)
# %H = hour (0-23)
# %M = minute (0-59)
# %S = seconds (0-60)  - leap seconds mean 60 is permissible. 

if type env >/dev/null 2>&1 ; then
    set -- `env LC_ALL=C LC_TIME=C LANG=C date -u '+%Y %j %H %M %S'`
else
    set -- `date -u '+%Y %j %H %M %S'`
fi

# $1 = year including century
# $2 = day number (1-365)
# $3 = hour (0-23)
# $4 = minute (0-59)
# $5 = seconds (0-60)  - leap seconds mean 60 is permissible. 

if [ $? -ne 0 ] || [ $# -lt 5 ] ; then
  TIME="Error computing seconds since the Epoch"
fi

DAYS=`expr 365 \* \( $1 - 1970 \) + \( $1 - 1969 \) / 4 + $2 - 1`
TIME=`expr $5 + 60 \* \( $4 + 60 \* \( $3 + 24 \* $DAYS \) \)`
echo $TIME
```


This was checked by a lot of people on sage-devel

http://groups.google.com/group/sage-devel/browse_thread/thread/1cf804eeb4f88c27/af8893705de4f513?hl=en&lnk=gst&q=please+check+if+this+#af8893705de4f513

and found to work for everyone. It was tested on 

 * Linux
 * Solaris
 * AIX
 * HP-UX
 * FreeBSD
 * OS X

I've played around with it, setting the dates back in years gone by, and dates in the future, and it always works. It was posted originally on comp.unix.shell. 

If we could save 
 * Start time in seconds since the Epoch
 * End time in seconds since the Ephoch
 * Compute the difference, and record that as "TIME TO BUILD" or something like that

we could use the information to determine if certain components are taking significantly longer to build. 

I'm *not* suggesting we only store the time in such a non-human readable format, but storing seconds since the Epoch in addition to a more human friendly format seems a good idea to me. 

Dave
