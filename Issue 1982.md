# Issue 1982: [with patch that needs to be integrated into spkg] workaround the billions of problems with matplotlib and locales on _real world_ computers

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-01-30 12:32:25

Assignee: was


```


Forwarded conversation
Subject: [sage-support] problems with p.show()
------------------------

From: Reineke <the_legendary_reineke_Fuchs`@`web.de>
Date: Jan 29, 2008 3:57 AM
To: sage-support <sage-support`@`googlegroups.com>



Hi,

I get the following error when I'm trying to use show or save:

-----
 File "/Applications/sage/local/lib/python2.5/site-packages/sympy/
plotting/", line 1, in <module>

 File "/Applications/sage/local/lib/python2.5/site-packages/sympy/
plotting/plot.py", line 721, in show

 File "/Applications/sage/local/lib/python2.5/site-packages/sympy/
plotting/plot.py", line 792, in save

 File "/Users/was/build/sage-2.10/local/lib/python2.5/site-packages/
matplotlib/figure.py", line 8, in <module>
 File "/Users/was/build/sage-2.10/local/lib/python2.5/site-packages/
matplotlib/artist.py", line 3, in <module>
 File "/Users/was/build/sage-2.10/local/lib/python2.5/site-packages/
matplotlib/cbook.py", line 18, in <module>
 File "/Applications/sage/local/lib/python/locale.py", line 507, in
getpreferredencoding
   return getdefaultlocale()[1]
 File "/Applications/sage/local/lib/python/locale.py", line 443, in
getdefaultlocale
   return _parse_localename(localename)
 File "/Applications/sage/local/lib/python/locale.py", line 375, in
_parse_localename
   raise ValueError, 'unknown locale: %s' % localename
ValueError: unknown locale: UTF-8
----

I'm a total newbie and installed sage 2.10 from a .dmg on Mac Os 10.5.
It seems to be a python error, but I have no idea about python as
well.

Thanks for your help
Cheers
Matthias

--~--~---------~--~----~------------~-------~--~----~
To post to this group, send email to sage-support`@`googlegroups.com
To unsubscribe from this group, send email to sage-support-unsubscribe`@`googlegroups.com
For more options, visit this group at http://groups.google.com/group/sage-support
URLs: http://www.sagemath.org
-~----------~----~----~----~------~----~------~--~---

----------
From: William Stein <wstein`@`gmail.com>
Date: Jan 29, 2008 4:48 AM
To: sage-support`@`googlegroups.com


Could you try carefully replacing  the file

  /Applications/sage/local/lib/python2.5/site-packages/matplotlib/cbook.py

on your computer by the attached file, then report back to us whether this
fixes the problem or not?  Thanks!  If so, we'll be able to easily patch Sage
so that this problem doesn't happen for you in the future (when you upgrade).

Thanks for reporting this issue with running Sage!

 - William
----------
From: Reineke <the_legendary_reineke_Fuchs`@`web.de>
Date: Jan 30, 2008 4:18 AM
To: sage-support <sage-support`@`googlegroups.com>



Hi William,

thanks for your help. The file worked perfectly fine!
Kudos to the program, I'm just starting to use it and already it seems
REALLY powerful!

Cheers
Matthias




On Jan 29, 10:48 am, "William Stein" <wst...`@`gmail.com> wrote:
>  cbook.py
> 37KDownload



-- 
William Stein
Associate Professor of Mathematics
University of Washington
http://wstein.org 
```



---

Comment by was created at 2008-01-30 12:32:57

This has to be made part of the matplotlib spkg


---

Attachment

I think there is also a need version of matplotlib, so probably when looking into this patch, one should also upgrade matplotlib, and see if this change is still needed. 

The changed cbook.py try except calling some locale function in the standard Python library, because on REAL LIFE computers often that function often blows up (!), even
though it probably "shouldn't" if everybody's computers were setup perfectly.  Honestely, I've even had related problems on my office mac pro, which is pretty weird since it's fairly plain vanilla.


---

Comment by mabshoff created at 2008-02-01 05:00:44

This is a dupe of #1967. `cbook.py` is identical in both cases.


---

Comment by mabshoff created at 2008-02-01 05:00:44

Resolution: duplicate
