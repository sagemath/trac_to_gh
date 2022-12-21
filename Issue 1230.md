# Issue 1230: Quit worksheet behaviour

Issue created by migration from Trac.

Original creator: nbruin

Original creation time: 2007-11-21 00:53:19

Assignee: boothby

Three points:

1) Currently, the notebook has a "quit worksheet" function that kills the background sage engine. Currently, this leaves the browser on the worksheet in question. I find that confusing: If I "quit" a worksheet, I expect that I leave the worksheet. Therefore, I think that the appropriate behaviour is that "quitting" a worksheet brings you to your index page (where it will not have the "active" attribute)

2) The fact that "active" worksheets are "not archived" worksheets is clashing terminology with a worksheet being "active" (there is a sage process associated to it) versus a worksheet being "not active".

The second use could be called "running" versus "not running" instead.

3) In the index page, it would be good to have an option to "quit" selected worksheets. After working for a bit, one can easily end up with a whole bunch of worksheets running. It is a pain to have to enter each of those worksheets to "quit" them.



---

Attachment


---

Comment by was created at 2008-05-10 21:05:02

The attached patch fixes all the above issues:

 
 class SendWorksheetToFolder(resource.PostableResource):
File Edit Options Buffers Tools Help                                                                                                 
Trac #1230: fix all the issues listed at trac #1230:
   1. Makes the quick worksheet menu item (under Action) actually return to the home screen
      after it saves and quits the worksheet.
   2. Change "active" to "running" in the home screen.
   3. Added a quit button to the main screen, which works just like the	archive	and delete buttons.


WARNING: This might depend on the patch at #2636 and its dependency (#336).


---

Comment by nbruin created at 2008-05-10 23:49:43

On sage-devel, William already pointed out that the second change in the patch dated 05/10/2008 02:04:01 PM. includes an erroneous deletion of an else clause. The patch "works for me" and the changes are very small. I am not familiar with the code, but just doing "pattern matching" on the code around it, gives confidence that it is coded consistent with what was already there.

COMMENT: The worksheet "list" page now also has a big fat "Quit" button, next to "Archive" and "Delete". The fact that "Quit" on a worksheet itself indeed means "close this page" might confuse users into thinking that the button logs them out or something.

Ticket #3147 should probably be closed if this gets accepted, since it solves the problem there as well (it's not really a duplicate of this ticket, though) -- never mind, it's been closed already.


---

Attachment

Quit --> Stop as recommended by referee


---

Comment by nbruin created at 2008-05-11 01:29:54

No issues with the code for me anymore.

Note that within the worksheet there is "Save and Quit", whereas on a worksheet list, there is "Stop" for the same function. I am in favour of this difference in naming, because it matches the difference in perspective (in one case you're standing in the worksheet and hence you "quit" (exit) it. In the other case, you're viewing the worksheet from outside and you "stop" it.

Someone more knowledgeable about the sage development model should decide if further refereeing is necessary. (It would probably be good if Tom Boothby could look at it)


---

Comment by mabshoff created at 2008-05-11 08:40:20

Merged all three patches in Sage 3.0.2.alpha0


---

Comment by mabshoff created at 2008-05-11 08:40:20

Resolution: fixed
