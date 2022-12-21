# Issue 7213: "sage -upgrade" to 4.1.2 results in issue with symbolic link and ecl

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-10-14 20:28:16

Assignee: tbd

CC:  schilly

when doing an upgrade:

```
ln: target `ecl' is not a directory
Failed to create ecl library symbolic link ... exiting

real    1m55.950s
user    1m38.540s
sys     0m12.430s
```



---

Comment by was created at 2009-10-14 21:41:57

The fixed spkg is here (it's a 3-character change).

http://sage.math.washington.edu/home/wstein/patches/ecl-9.8.4-20090913cvs.p3.spkg


---

Comment by was created at 2009-10-14 21:42:07

Changing status from new to needs_review.


---

Comment by mvngu created at 2009-10-15 13:48:55

Both of the following cases worked OK:

 * Replace the ECL spkg of Sage 4.1.2 with the above updated spkg. Make a new source tarball and compile that new tarball from scratch. That works OK.
 * From Sage 4.1.1, upgrade to this new source tarball with the above ECL spkg. This also works fine. The original problem with upgrading from Sage 4.1.1 is now gone.

Positive review.


---

Comment by mvngu created at 2009-10-15 13:48:55

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2009-10-15 14:51:46

This can be closed now. The updated ECL spkg is up in the standard spkg repository on sagemath.org and has been mirrored out. See

http://mirror.switch.ch/mirror/sagemath/spkg/standard/ecl-9.8.4-20090913cvs.p3.spkg

```
07:39 < mvngu> schilly: But you should note ticket #7213.
07:40 < mvngu> schilly: If people upgrade to Sage 4.1.2 and they have problem
               with ECL, then ticket #7213
07:40 < mvngu> is the answer.
07:40 < mvngu> schilly: I just gave it a postive review.
07:41 < mvngu> schilly: So the standard packages respository on sagemath.org
               should have that updated ECL spkg.
07:41 < mvngu> schilly: Otherwise upgrade would result in a path error with ECL.
07:42 < schilly> mhm, ok ...
07:42 < schilly> if it is updated in the usual place, it will be on the mirrors
07:43 < mvngu> schilly: I mean update the standard spkg on sagemath.org with
               that ECL spkg, and mirror out this updated spkg.
07:43 < schilly> ok, filename is the same
07:43 < schilly> yes, just looked at www-files/packages/standard ... it's the
                 same
07:44 < mvngu> schilly: It says ".p3"?
07:44 < schilly> http://mirror.switch.ch/mirror/sagemath/spkg/standard/
07:45 < mvngu> schilly: cool.
07:45 < schilly> ;)
07:45 < mvngu> schilly: Maybe wstein took care of updating that repo.
07:46 < schilly> he copied over to the usual place
                 (www-files/packages/standard) and that's all he has to do
07:46 < schilly> then he mirrored it together with the new source
07:46 < schilly> or i did it when i checked the mirror-ing earlier this day
07:47 < schilly> so, it's already on the servers
07:47 < mvngu> That's good to know.
07:48 < schilly> the only thing i don't understand is, why the source tarball 
                 of 4.1.1 is newer than the newer one for 4.1.2
07:48 < schilly> probably some copy-activity or replacement. i'll move 4.1.1 to 
                 the older files anyways
```



---

Comment by mhansen created at 2009-10-19 04:55:24

Resolution: fixed
