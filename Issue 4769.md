# Issue 4769: add 5 people to devmap; update info for 2 people

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2008-12-12 08:04:27

Assignee: tba

CC:  mabshoff schilly

Keywords: devmap

As the subject says. This is a joint project with Michael Abshoff and Harald Schilly.


---

Comment by mvngu created at 2008-12-12 08:06:08

add 5 people to devmap and update info for 2 people


---

Attachment

The patch *trac_4769.patch* adds 5 people to the devmap at



http://www.sagemath.org/development-map.html



and updates info for 2 people. It should be patched against the file:



http://www.sagemath.org/res/contributors.xml



The following people are added:


 1. Wilfried Huss, PhD student, Graz University of Technology, Austria: calculus bug fixes; additions to the Maxima interface
 1. Sebastien Labbe, LaCIM, Universite du Quebec a  Montreal, Canada: bug fixes; plotting improvements: http://www.lacim.uqam.ca
 1. Michael Mardaus, Universitat Mainz, Germany: point counting code
 1. Tobias Nagel, Universitat Mainz, Germany: point counting code
 1. Dan Shumow, University of Washington, WA, USA: bug fixes


The following people have their info updated:

 1. Chris Swierczewski, University of Washington, WA, USA: doctests; financial data streaming and contributions to the finance module; documentation for the algebra module: http://cswiercz.blogspot.com
 1. Alex Ghitza, The University of Melbourne, Parkville, Melbourne, Australia: pari interface; modular forms, elliptic curves, number fields; miscellaneous algebra; documentation


---

Comment by schilly created at 2008-12-12 10:25:10

Hi, i've applied the patch, it's online now.

The patch was ok but i had to edit two things. Google maps doesn't know about a university of mainz, i think it's "johannes gutenberg university" but i simply just took the postal code number, that's fine and works if you zoom in. (there is also a public transport station called "universität")

secondly, something bad happens with utf8 unicode encoding in url strings [they are used in the query[, therefore no special signs in the location.

apart from that thanks and don't mind, those things just pop up when you work with the actual scripts. now it's ok and please base your next patch against the one on the server.

h


---

Comment by schilly created at 2008-12-12 10:25:10

Resolution: fixed


---

Comment by schilly created at 2008-12-12 10:25:10

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2008-12-12 11:04:56

Harald,

please remember to change the review status.

Cheers,

Michael
