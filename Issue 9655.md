# Issue 9655: Add an example ploting spherical harmonics to spherical_plot3d's docstring

Issue created by migration from Trac.

Original creator: olazo

Original creation time: 2010-08-01 01:43:52

Assignee: olazo

Keywords: spherical,harmonics

Ploting Spherical Harmonics is one of the most useful ways to use spherical_plot3d. Adding an example of that would be nice.


---

Comment by olazo created at 2010-10-28 00:45:53

Changing status from new to needs_review.


---

Comment by olazo created at 2010-10-28 00:46:09

Changing priority from major to minor.


---

Attachment


---

Attachment

Here are some issues with olazo's patch:

 * The "User" should be filled with your real name and preferred contact email address. I have fixed this in my update of olazo's patch; see [attachment:trac-9655_spherical-harmonic-example.patch].
 * The code in olazo's patch does not conform to Python coding conventions. In particular, see [PEP 8](http://www.python.org/dev/peps/pep-0008/). This is fixed in my reviewer patch; see [attachment:trac-9655_reviewer.patch]. Someone other than me needs to review that. If my patch gets a positive review, the whole ticket gets a positive review.


---

Comment by olazo created at 2010-11-02 21:41:42

Replying to [comment:3 mvngu]:
> Here are some issues with olazo's patch:
> 
>  * The "User" should be filled with your real name and preferred contact email address. I have fixed this in my update of olazo's patch; see [attachment:trac-9655_spherical-harmonic-example.patch].

This is the first patch I produced using mecurial queues. At some point I recieved a warning about User not being defined, but how do I set it up? I mean other than directly editing the .patch

>  * The code in olazo's patch does not conform to Python coding conventions. In particular, see [PEP 8](http://www.python.org/dev/peps/pep-0008/). This is fixed in my reviewer patch; see [attachment:trac-9655_reviewer.patch]. Someone other than me needs to review that. If my patch gets a positive review, the whole ticket gets a positive review.

I was unaware of such conventions...


---

Comment by mvngu created at 2010-11-03 07:20:39

Replying to [comment:5 olazo]:
> At some point I recieved a warning about User not being defined, but how do I set it up? I mean other than directly editing the .patch

You should use the Mercurial configuration file `~/.hgrc`. Here's a template for your `~/.hgrc` file:


```sh
[ui]
editor = /usr/bin/vim
username = Carl Friedrich Gauss <cfgauss`@`uni-goettingen.de>

[extensions]
# Enable the Mercurial queues extension.
hgext.mq =
# Enable the record, qrecord and crecord extensions for cherry picking.
hgext.record =

[diff]
# Format diff output using Git style.
git = True
# Prevent qrefresh from updating timestamps. If you're keeping your patch
# queue under revision control, it can be quite annoying when every qrefresh
# updates the timestamps in your patch. The following prevents this from
# happening.
nodates = 1
```


Change your username accordingly.





> I was unaware of such conventions...

See [this page](http://www.sagemath.org/doc/developer/conventions.html) of the [Developer's Guide](http://www.sagemath.org/doc/developer/index.html) for more details about coding conventions used by the Sage library.


---

Comment by spice created at 2010-11-03 15:57:49

Changing status from needs_review to positive_review.


---

Comment by spice created at 2010-11-03 16:05:05

This is the first patch I've ever reviewed, so a second look by someone else might not be a bad idea.


---

Comment by mvngu created at 2010-11-04 04:33:02

Replying to [comment:8 spice]:
> This is the first patch I've ever reviewed, so a second look by someone else might not be a bad idea.

Please put down your real name in the field "Reviewer(s):".


---

Comment by spice created at 2010-11-04 17:40:46

Done.

Thanks Minh.


---

Comment by jdemeyer created at 2010-11-10 22:19:52

Resolution: fixed
