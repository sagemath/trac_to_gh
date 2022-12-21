# Issue 9487: Have an acurate description of what "supported platforms" are, and have one list - not numerous different ones.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-07-12 23:58:20

Assignee: mvngu

CC:  jhpalmieri rlm mariah georgsweber pjeremy leif mkoeppe slelievre

As has been noted several times before, the list of "supported platforms" for Sage varies very depending on what particular file/web-page you read. Different sources which include a list of supported platforms include:

 * README.txt
 * http://www.sagemath.org/doc/installation/source.html
 * http://wiki.sagemath.org/SupportedPlatforms

A proposal of mine is at 

http://wiki.sagemath.org/suggested-for-supported-platforms

which is based on the method used by Mathworks for MATLAB in their list of [System Requirements for Linux](http://www.mathworks.com/support/sysreq/current_release/linux.html). Mathworks break "supported" into two lists. 
 * List systems which MATLAB is tested on, and so they can give good support. (In this case, exact version numbers are listed e.g. Ubuntu 8.04, 8.10, 9.04, and 9.10) 
 * List systems on which MATLAB should work, but which they don't test. 

I generalised that to four for Sage, 

 * Fully supported (Sage is always tested on *every* system in this list before a release is made) 
 * Expected to work 
 * Probably will not work, but porting is ongoing 
 * Will not work and porting will require substantial effort 

The first two are basically the same as Mathworks use. The last two are applicable to Sage, but not for a closed source system like MATLAB. 

It would be good if the list could be maintained in such a way that there are not several different sources giving a different list of "supported" systems. 


Dave


---

Comment by drkirkby created at 2010-07-18 22:25:08

Did anyone have any comments on this? Several people have added themselves to the 'cc' list, but so far I have had little or no feedback.


---

Comment by was created at 2011-08-24 23:45:12

Changing keywords from "" to "sd32".


---

Comment by mkoeppe created at 2021-04-03 18:16:50

I think we can close this ticket as outdated. `README.md` and the installation manual are in good shape; and since version 9.0, the release tours have a section in the end that talk about the version-specific details of tested platforms.


---

Comment by mkoeppe created at 2021-04-03 18:16:50

Changing status from new to needs_review.


---

Comment by chapoton created at 2022-05-13 09:17:31

Resolution: invalid


---

Comment by chapoton created at 2022-05-13 09:17:31

ok, closing
