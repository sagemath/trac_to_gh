# Issue 7188: GNUism in $SAGE_ROOT/spkg/install

Issue created by migration from https://trac.sagemath.org/ticket/7188

Original creator: drkirkby

Original creation time: 2009-10-11 10:40:13

Assignee: tbd

CC:  embray jdemeyer fbissey

Keywords: GNUism AIX HP-UX Solaris

Once one runs make it runs the script $SAGE_ROOT/spkg/install. 

Unfortunately, the very first command in there, the result of ticket #6744 has a GNUism. 


```
 echo `date -u "+%s"` > .BUILDSTART
```


The '%s is *not* part of the current POSIX standard and fails to work on both the latest version of Solaris (which is a supported operating system), and with HP-UX 11i, which is not supported 
by Sage, but I think we should try to build Sage in such a way 
that is should run on any decent operating system. 

There are at least two ways around this issue of find the number of seconds since 1//1/1970:

http://shell.cfajohnson.com/cus-faq.html#Q6

One requires 'perl' (which is not tested for at this point), the other relies on 'awk' being POSIX complaint, which we can't assume, but is probably the safer of the two assumptions. A third way would be a way to make it work with any 'date' command using some maths with 'bc' but that looks like a lot of work, for little gain. 



```
# The method below looks a bit odd, as one uses a
# random number generator to get the time! However,
# it will work with any 'awk' supporting the
# POSIX spec for srand().

# David Kirkby has tested this on the following operating systems.
# AIX, HP-UX, Linux, OS X and Solaris. (versions as available).

# The trick is to first seed the srand random number generator
# generator with the default value (which is the number
# of seconds since 1/1/1970) then call srand() again, to give the
# first random number, which will be the seed. Neat I think!

# See  http://shell.cfajohnson.com/cus-faq.html#Q6

if [ `uname` = "SunOS" ] ; then
  # The standard awk in Solaris is not POSIX complaint, and so will not be
  # acceptable. But Sun ship a POSIX complient version at nawk (new awk)
  nawk 'BEGIN {srand(); printf("%d\n", srand())}' > .BUILDSTART
else
  awk 'BEGIN {srand(); printf("%d\n", srand())}' > .BUILDSTART
fi

```


The updated install script, can be found at 

http://sage.math.washington.edu/home/kirkby/Solaris-fixes/top-level-install-script/

I've tested this on

 * AIX 6.1, compliments of http://www.metamodul.com/10.html
 * HP-UX 11i (my own HP C3600)
 * Linux (sage.math)
 * Solaris 10 update 7 SPARC (t2.math)
 * OpenSolaris 2008.11 (disk.math)
 * OS X (bsd.math)

 
According to #6744 this needs to be manually integrated into Sage. Note I stuck a readme file in the directory highlighting the fact this needs to have execute permissions too.
 

Dave 


---

Comment by drkirkby created at 2009-10-11 10:40:31

Changing status from new to needs_review.


---

Comment by drkirkby created at 2009-10-11 12:47:22

I just added a new comment to the file 


```
# We would like to thank http://www.metamodul.com/ for free
# access to the the IBM machine running AIX 6.1
```


That site is providing the AIX machine which allowed me to test the patch under AIX, which I would not otherwise had been able to do so easily, even though I have an old RS6000 in my garage.


---

Comment by was created at 2009-10-11 17:56:23

Just for the record this BUILDSTART thing was added to Sage very recently by Harald Schilly, evidently in trac #6744, and it is *completely ignored* at present, and used absolutely nowhere else in Sage.


---

Comment by drkirkby created at 2009-10-17 11:20:08

Changing status from needs_review to needs_work.


---

Comment by drkirkby created at 2009-10-17 11:20:08

I understand this will not work on OpenBSD, which though not supported, I am aware of a method now which should work on any OS. Apparently POSIX states the random number generator must be seeded from the time, but does not state in which way. Most OS's uses seconds since the epoch, but OpenBSD does not. A more portable solution has been posted, which should work for any OS. 

I believe this issue should be resolved. If nothing else, it does not look very good to be generating unnecessary error messages on some platforms. (Solaris and AIX).


---

Comment by chapoton created at 2018-12-17 20:13:57

here is a branch that just get rid of the unused BUILDSTART file
----
New commits:


---

Comment by chapoton created at 2018-12-17 20:13:57

Changing status from needs_work to needs_review.


---

Comment by fbissey created at 2018-12-17 20:24:33

Changing status from needs_review to positive_review.


---

Comment by fbissey created at 2018-12-17 20:24:33

Looks good to me.


---

Comment by vbraun created at 2018-12-23 23:41:10

Resolution: fixed
