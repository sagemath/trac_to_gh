# Issue 7438: the graphviz-2.16.1.p0 optional spkg fails to build on ubuntu-9.10 with a sage-4.2.1 install

Issue created by migration from https://trac.sagemath.org/ticket/7438

Original creator: was

Original creation time: 2009-11-12 05:24:09

Assignee: tbd

CC:  nthiery rlm mhansen ncohen jdemeyer dimpase

I installed ubuntu-9.10, sage-4.2.1 and tried to install all optional spkg.  Graphviz fails after a long time with:

```
gcc -DHAVE_CONFIG_H -I. -I../..  -I../../lib/common -I../../lib/gvc -I../../lib/pathplan -I../../lib/graph -I../../lib/cdt -I/home/sage/sage/local/include -I/home/sage/sage/local/include  -g -O2 -Wno-unknown-pragmas -Wstrict-prototypes -Wpointer-arith -Wall -ffast-math -MT no_demand_loading.o -MD -MP -MF .deps/no_demand_loading.Tpo -c -o no_demand_loading.o `test -f '../../lib/gvc/no_demand_loading.c' || echo './'`../../lib/gvc/no_demand_loading.c
mv -f .deps/no_demand_loading.Tpo .deps/no_demand_loading.Po
make[3]: *** No rule to make target `../../plugin/pango/libgvplugin_pango.la', needed by `dot_builtins'.  Stop.
make[3]: Leaving directory `/home/sage/sage/spkg/build/graphviz-2.16.1.p0/src/cmd/dot'
make[2]: *** [all-recursive] Error 1
make[2]: Leaving directory `/home/sage/sage/spkg/build/graphviz-2.16.1.p0/src/cmd'
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/home/sage/sage/spkg/build/graphviz-2.16.1.p0/src'
make: *** [all] Error 2
Error building Graphviz

real    14m54.042s
user    3m50.614s
sys     10m25.267s
sage: An error occurred while installing graphviz-2.16.1.p0
```



---

Comment by drkirkby created at 2010-03-13 01:29:55

It also fails on Solaris 10 (SPARC) with the same error message with Sage 4.3.4.alpha1. 

Should this be moved to 'experimental' as it appears to be broken?


---

Comment by rbeezer created at 2010-06-17 04:55:01

Me too.  Same setup, same result - except on 4.4.2.rc0 and failure came in about 2 minutes of runtime.

I've cc'ed Nicolas Thiery who may be interested.


---

Comment by drkirkby created at 2010-06-17 07:05:20

I've added Robert Miller, as he is listed in SPKG.txt as the package maintainer. 

Any attempt to fix this broken package should probably start at updating to the latest version, as the version in Sage is very old. 

I had a *quick* look at spkg-install and see some odd things. 

 * On OS X, the option --enable-shared=yes is given twice. 
 * There's no code to make this build 64-bit if SAGE64 is set to "yes" - it needs something like the following added near the top of spkg-install. 

```
if [ "x$SAGE64" = xyes ] ; then 
  CFLAGS="$CFLAGS -m64"
  CXXFLAGS="$CXXFLAGS -m64"
  LDFLAGS="$LDFLAGS -m64"
  CPPFLAGS="CPPFLAGS -m64"
  export CFLAGS
  export CXXFLAGS
  export LDFLAGS
  export CPPFLAGS
fi
```

 * Although iconv is in Sage, and this package wants iconv, the configure option to specify the location of iconv is not used. 
 * Same as above, but with freetype2. 
 * The program seems to want many libraries and gives warnings they are not present. How essential they are I don't know, but Sage does not include pango, which is one of the libraries this checks for. The final error message is related to pango. 
 * Lots of the recommended libraries are not in Sage, so it's not clear how useful this would be even if one did manage to build it. (I don't think building it should be too hard, but I don't have the inclination myself). 

#9208 could be useful to this, as it would resolve at least the freetype2 issue. 

I changed the title slightly to reflect the fact this fails to build on several operating systems (Ubunta, OpenSolaris and Solaris 10 to my knowledge), and that it is not specific to version 4.2.1 of Sage - I just tried it on 4.4.3 on Solaris 10 and 4.4.4.alpha0 on OpenSolaris - both fail. 

Dave


---

Comment by dimpase created at 2011-11-21 12:59:48

I cannot install graphviz on MacOSX 10.6.8 in 64-bit mode (Sage 4.7.1).
I get exactly the same error.


---

Comment by kcrisman created at 2013-04-02 13:45:12

According to #11433 and #4864, this is a simple lack of dependencies - pango, and perhaps some version of perl dev stuff.  See #14398 also, which is probably a duplicate of this ticket, for a little more discussion.

----

Update: actually, maybe not: something seems to have confused the freetype thing.  On boxen.math:

```

creating libgvplugin_gd_C.la
(cd .libs && rm -f libgvplugin_gd_C.la && ln -s ../libgvplugin_gd_C.la libgvplugin_gd_C.la)
/bin/bash ../../libtool --tag=CC   --mode=link gcc  -g -O2 -Wno-unknown-pragmas -Wstrict-prototypes -Wpointer-arith -Wall -ffast-math -version-info 5:0:0 -L/home/kcrisman/sage-5.8-sage.math.washington.edu-x86_64-Linux/local/lib -L/home/kcrisman/sage-5.8-sage.math.washington.edu-x86_64-Linux/local/lib -o libgvplugin_gd.la -rpath /home/kcrisman/sage-5.8-sage.math.washington.edu-x86_64-Linux/local/lib/graphviz gvplugin_gd.lo gvrender_gd.lo gvrender_gd_vrml.lo gvtextlayout_gd.lo gvloadimage_gd.lo gvdevice_gd.lo ../../lib/gvc/libgvc.la -L/home/kcrisman/sage-5.8-sage.math.washington.edu-x86_64-Linux/local/include -lgd -lfontconfig -lfreetype -lpng12 -lz -lm -lm 
libtool: link: warning: `/usr/lib64/libexpat.la' seems to be moved
libtool: link: warning: library `/home/kcrisman/sage-5.8-sage.math.washington.edu-x86_64-Linux/local/lib/libgd.la' was moved.
grep: /release/merger/sage-5.8/local/lib/libfreetype.la: No such file or directory
/bin/sed: can't read /release/merger/sage-5.8/local/lib/libfreetype.la: No such file or directory
libtool: link: `/release/merger/sage-5.8/local/lib/libfreetype.la' is not a valid libtool archive
make[3]: *** [libgvplugin_gd.la] Error 1
make[3]: Leaving directory `/home/kcrisman/sage-5.8-sage.math.washington.edu-x86_64-Linux/spkg/build/graphviz-2.16.1.p0/src/plugin/gd'
make[2]: *** [all-recursive] Error 1
make[2]: Leaving directory `/home/kcrisman/sage-5.8-sage.math.washington.edu-x86_64-Linux/spkg/build/graphviz-2.16.1.p0/src/plugin'
make[1]: *** [all-recursive] Error 1
make[1]: Leaving directory `/home/kcrisman/sage-5.8-sage.math.washington.edu-x86_64-Linux/spkg/build/graphviz-2.16.1.p0/src'
make: *** [all] Error 2
Error building Graphviz

real	3m39.740s
user	1m29.320s
sys	1m41.210s
************************************************************************
Error installing package graphviz-2.16.1.p0
************************************************************************
```



---

Comment by kcrisman created at 2013-04-02 13:49:30

Ah, I think the problem is that I didn't run Sage first to change those hardcoded paths.


---

Comment by kcrisman created at 2013-04-02 13:57:00

Yes, it still builds on sage.math, once you do run Sage once.


---

Comment by ncohen created at 2013-04-02 14:25:54

> If you want to open a sage-devel discussion about how non-broken experimental packages should be, that's fine.

I don't want to "start debates", again and again, and I don't want to debate generally about experimental spkg. We waste our lifetime discussing uselessly. Here's where the discussion is happening. I just talk about this very spkg, nothing else.

> In my view - and as you know, I am pretty conservative on such things - experimental can be as broken as they want to be. Someone probably does have the expertise to fix each of them, and removing them completely means no one will even have the chance.

* Here are the two spkg maintainers : Robert Miller, Michael Abshoff. They don't do much development here anymore, do they ?
* Last update of the spkg : 2008
* 3 tickets have been created since by people who tried to used it and only found this bug

Conservative as you may be, would you accept to take these elements as hints that this spkg is plainly *forgotten*, has no reason to be fixed tomorrow, and just makes some developpers waste a few hours of their life each year ?

We cannot advertise the spkg in the doc, as we cannot hope it to run on their machines. Hence, in the *best case*, nobody knows the spkg exist (if they do they will probably meet a bug).

We would be better without this in Sage's list of packages. We would be better with a "package no found" message to answer "`sage -i graphviz`". It would help users look the right way : this software should be installed manually.

Nathann


---

Comment by kcrisman created at 2013-04-02 16:51:18

Replying to [comment:9 ncohen]:
> > If you want to open a sage-devel discussion about how non-broken experimental packages should be, that's fine.
> 
> I don't want to "start debates", again and again, and I don't want to debate generally about experimental spkg. We waste our lifetime discussing uselessly. Here's where the discussion is happening. I just talk about this very spkg, nothing else.
> 
The problem is that most of the experimental packages are even worse than this package, if I recall correctly; this one actually builds on sage.math!   So it really does have to be "the whole discussion".

We even have standard spkgs that haven't been updated (essentially) in 4-5 years.  So I don't know that this holds water either, other than to say we need more people working on spkgs!

----

But all this is superseded by Jeroen's patch and your review at #14398.  So now I will change this ticket to being about something a little more specific.


---

Comment by kcrisman created at 2013-04-02 16:51:18

Changing component from packages: optional to packages: experimental.


---

Comment by kcrisman created at 2013-04-02 16:54:07

Amazingly, this also installed fine on my Mac 10.7 without any problems!


---

Comment by mderickx created at 2017-10-07 22:39:53

For what it is worth, it still builds on OS X 10.12.4 with sage.8.1.beta7.


---

Comment by mkoeppe created at 2020-08-17 16:38:58

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-08-17 16:38:58

Outdated spkg or build system ticket, should be closed


---

Comment by slelievre created at 2020-08-22 07:17:48

Resolution: invalid
