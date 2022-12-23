# Issue 9276: sage notebook: jsmath image fonts -- optional package -- breakage

Issue created by migration from https://trac.sagemath.org/ticket/9276

Original creator: was

Original creation time: 2010-06-19 18:48:12

Assignee: jason, was

Here's the thread about this:


```



Forwarded conversation
Subject: [sage-support] jsmath image fonts
------------------------

From: marik
Date: Fri, May 28, 2010 at 11:56 PM
To: sage-support <sage-support@googlegroups.com>


Dear all

I installed jsmath image fonts in fresh 4.4.2, but these fonts remain
unavailable - the switch to these fonts is still inactive. Does
anybody have the same issue? Is it a bug in my configuration, or a bug
in sage? Many thanks and have a nice weekend.

Robert


----------
From: marik
Date: Mon, May 31, 2010 at 12:43 PM
To: sage-support <sage-support@googlegroups.com>


I copied png files manualy to the correct place and still get no image
fonts in Sage notebook. Any idea? Many thanks,

Robert

----------
From: William Stein <wstein@gmail.com>
Date: Mon, May 31, 2010 at 12:44 PM
To: sage-notebook <sage-notebook@googlegroups.com>


--
William Stein


----------
From: marik@
Date: Fri, Jun 11, 2010 at 8:44 AM
To: sage-notebook <sage-notebook@googlegroups.com>


Solved:
png files install into correct place, but the file /sage/local/LIB/
python/site-packages/sagenb-0.8-py2.6.egg/sagenb/data/sage/js/
jsmath.js contains lines like

   {% if jsmath_image_fonts %}
   noImageFonts: 0
   {% else %}
   noImageFonts: 1
   {% endif %}

Change it into

//    {% if jsmath_image_fonts %}
   noImageFonts: 0
//    {% else %}
//    noImageFonts: 1
//    {% endif %}

and image fonts will work. Tested on recent Sage 4.4.3

what is this  {% if jsmath_image_fonts %} ? Where does it come from?
Robert



```



---

Comment by robert.marik created at 2010-06-21 06:48:12

From [sage-notebok](http://groups.google.cz/group/sage-notebook/browse_thread/thread/79b7b217f4af6e36)

1) I installed jsmath_image_fonts-1.4.p3 with:
aquino`@`aquino-desktop:~$ sage -i jsmath_image_fonts-1.4.p3

2) I change the twist.py file:
from:

```
jsmath_image_fonts = is_package_installed("jsmath-image-fonts")
```

to:

```
jsmath_image_fonts = is_package_installed("jsmath_image_fonts")
```

3) I don't change anything in the jsmath.js

When I open the jsMath Control Panel (clicking on the small text
"jsMath" at the right bottom corner in the worksheet page), I can set
"Options > Use image fonts ([*] scalable)" and then use the fonts
installed.

Of course, that option was unavailable before I install
jsmath_image_fonts.

My configuration:
System: Ubuntu 10.04 32 bits
Browser: Firefox 3.6.3
Sage: Version 4.4.3, Release Date: 2010-06-04


---

Comment by knsam created at 2013-02-03 18:35:04

Changing status from new to needs_review.


---

Comment by knsam created at 2013-02-03 18:35:41

We use MathJaX now for the notebook! So, the ticket is no longer relevant.


---

Comment by novoselt created at 2013-02-03 23:13:06

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-02-08 13:25:48

Resolution: invalid
