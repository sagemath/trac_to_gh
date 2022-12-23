# Issue 4682: Add about 36 people missing from the DevMap for Sage 3.0.6-3.2.1

Issue created by migration from https://trac.sagemath.org/ticket/4682

Original creator: mabshoff

Original creation time: 2008-12-03 00:38:16

Assignee: was

CC:  mvngu schilly

There are about 36 people missing at 


  http://sagemath.org/development-map.html

that have contributed to Sage. Contact them and if they would like to be added get them on there. This is a join project by Michael Abshoff, Minh Van Nguyen and Harald Schilly.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-03 00:38:47

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-12-03 00:38:47

Changing assignee from was to mabshoff.


---

Attachment

first draft of revised devmap


---

Comment by mvngu created at 2008-12-04 21:25:26

The patch *trac_4682.patch* is an updated contributors list as found on the development map. I've re-organized the whole XML file for consistency, and added new details since they've arrived in the last few days.


---

Comment by schilly created at 2008-12-04 21:55:45

Resolution: fixed


---

Comment by schilly created at 2008-12-04 21:55:45

Replying to [comment:2 mvngu]:
> The patch *trac_4682.patch* is an updated contributors list as found on the development map. I've re-organized the whole XML file for consistency, and added new details since they've arrived in the last few days.

thx and very cool, worked out of the box ;)

patch added, site online, for future patches please use the current version to avoid confusions: http://www.sagemath.org/res/contributors.xml

h


---

Comment by schilly created at 2008-12-04 21:55:45

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2008-12-04 23:31:03

Well, the idea of this ticket was to add all people and then close it. Since now the first dozen has been added I changed the subject.

Minh: You should open a ticket for the next batch of say a dozen people once you are ready to go.

Cheers,

Michae


---

Comment by mabshoff created at 2008-12-04 23:41:47

Harald,

You also need to give the ticket a formal positive review. Then usually the release manager will close the ticket. For website tickets this might be handled slightly different.

One more thing: Minh, can you give us a listing which people were added in the patch? Since it is a reorg it is hard to follow. For future reference please post two patches in the future: One to move things around, one with the actual changes.

Cheers,

Michael


---

Comment by mvngu created at 2008-12-05 00:24:22

Replying to [comment:6 mabshoff]:
> One more thing: Minh, can you give us a listing which people were added in the patch? Since it is a reorg it is hard to follow. 


The following people were added to the devmap by *trac_4682.patch*:

 1. Arnaud Bergeron
 1. Nicolas Borie
 1. Hamish Ivey-Law
 1. Kwankyu Lee
 1. David Loeffler
 1. Jason Merrill
 1. Guillaume Moroz
 1. Brett Nakashima
 1. John Perry
 1. Nils-Peter Skoruppa
 1. Philippe Theveny
 1. Igor Tolkov

The above list is sorted in alphabetical order by last name.



> For future reference please post two patches in the future: One to move things around, one with the actual changes.


Sure. I'll keep this in mind.
