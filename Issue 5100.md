# Issue 5100: worksheets: can't empty the trash (safari only?)

Issue created by migration from https://trac.sagemath.org/ticket/5100

Original creator: jhpalmieri

Original creation time: 2009-01-25 17:01:45

Assignee: boothby

CC:  jason mhansen was

Keywords: trash, safari

With Safari on an Intel iMac, sage 3.3.alpha1:

From the notebook interface, if I select "Trash" to get the list of deleted worksheets, then clicking "Empty trash" doesn't actually empty the trash.  It sends me back to the list of active worksheets, but if I click on "Trash" again, I see the same list of deleted worksheets.

With Firefox on the same iMac, emptying the trash works just fine.


---

Comment by mabshoff created at 2009-01-25 20:10:40

This sounds similar to #5095. There were also some places where Safari acted differently than Firefox, so this is likely due to the work around TinyMCE.

Jason, Mike: Any idea what might be going on?

Cheers,

Michael


---

Comment by mhansen created at 2009-01-25 20:16:34

Changing status from new to assigned.


---

Comment by mhansen created at 2009-01-25 20:16:34

Changing priority from minor to blocker.


---

Comment by mhansen created at 2009-01-25 20:16:34

Changing assignee from boothby to mhansen.


---

Comment by mhansen created at 2009-01-25 20:18:08

This is definitely different than #5095.  I will try to get access to Safari to see what's going on, but nothing leaps out at me at this point.  I guess I'll go through the TinyMCE patches and see what all was changed.


---

Comment by jhpalmieri created at 2009-01-25 21:39:00

To confirm mhansen's comment, I applied the patch for #5095 (I gave it a positive review, in fact), and it doesn't fix this problem.


---

Comment by kcrisman created at 2009-01-26 01:48:40

I get this behavior on 3.2.1 with Safari, not Firefox (both on a version without TinyMCE and one where I had applied TinyMCE).  So this probably has been around for a bit, and should be unrelated to TinyMCE.


---

Comment by jason created at 2009-01-26 12:51:07

The issue we had with TinyMCE acting different under Safari vs. Firefox had to do with the browser executing javascript code when html was inserted dynamically into the DOM of the browser page.  Apparently Firefox automatically executes code inside of <script> tags that are inserted into the DOM, while Safari doesn't.  To overcome this, we ended up stripping out the <script> tags from any HTML that was inserted into the DOM and running the script code separately.

Of course, the above comment only applies to <script> blocks loaded dynamically; any <script> blocks in the original HTML page should execute just normally.

I don't know if that is the issue, but since mabshoff asked, I thought I'd mention it.


---

Comment by mhansen created at 2009-01-26 18:47:58

For those that can reproduce the problem, could you please give me the specific versions of OS X and Safari that you are using?

I just tried this in Safari 3.2.1 on Mac OS X 10.5.6 and it worked fine.


---

Comment by mhansen created at 2009-01-26 19:03:08

Also, one can run (while Safari is not running), "defaults write com.apple.Safari IncludeDebugMenu 1" in the terminal to enable the debug menu in Safari.    Choosing Develop -> Show WebInspector before trying to delete the worksheets may yield some useful information.


---

Comment by kcrisman created at 2009-01-26 19:59:28

I am on a PPC OSX.4 using Safari 3.2.1.  

I'll try this other debugging thing tonight if I get a chance.


---

Comment by kcrisman created at 2009-01-27 03:10:47

Replying to [comment:8 mhansen]:
> Also, one can run (while Safari is not running), "defaults write com.apple.Safari IncludeDebugMenu 1" in the terminal to enable the debug menu in Safari.    Choosing Develop -> Show WebInspector before trying to delete the worksheets may yield some useful information.

"Unmatched </input> encountered.  Ignoring tag."

This linked to line 38 of my HTML, which was:

```
<input id="search_worksheets" size=20 onkeypress="return search_worksheets_enter_pressed(event, 'trash');" value""></input>
```


By the way, this *also* happened pretty much any time I used the Current Folder links in any way, so I'm not sure how this error report actually has anything to do with the onClick="empty_trash(); return false;" (should that be False?), but it did generate an error, so perhaps it will be useful to someone.


---

Comment by jhpalmieri created at 2009-01-27 03:44:50

I see the same things as kcrisman, including the same error message, but with Safari 3.2.1 (5525.27.1), OS X 10.5.6 on an Intel iMac.


---

Comment by jason created at 2009-01-27 03:50:02

That is missing an equals sign between the value and the quotes.  Is that a typo or is that the error?

The template in server/notebook/templates/search.html doesn't seem to be missing the equals sign.


---

Comment by mhansen created at 2009-01-27 03:56:25

Replying to [comment:11 jhpalmieri]:
> I see the same things as kcrisman, including the same error message, but with Safari 3.2.1 (5525.27.1), OS X 10.5.6 on an Intel iMac.
> 

I don't think that error message has anything to do with it.  Are you doing this in Sage 3.3.alpha2 + #5095.


---

Comment by kcrisman created at 2009-01-27 04:11:42

Replying to [comment:12 jason]:
> That is missing an equals sign between the value and the quotes.  Is that a typo or is that the error?

Typo, I think.

Don't have 3.3.alpha2+anything, and unfortunately that won't happen for a bit.  Sorry the debugger didn't help.


---

Comment by jhpalmieri created at 2009-01-27 05:25:10

Now this is with 3.3.alpha2 + the 5095 patch.

When I click the Trash button to get the list of deleted worksheets, I get this in the error console:

```
Unmatched </input> encountered.  Ignoring tag.
http://localhost:8000/home/admin/?typ=trash (line 68)
```


This points to the line

```
<input id="search_worksheets" size=20 onkeypress="return search_worksheets_enter_pressed(event, 'trash');" 
```


Clicking "Empty Trash" then gives me

```
Unmatched </input> encountered.  Ignoring tag.
http://localhost:8000/home/admin/ (line 68)
```

This points to the line

```
<input id="search_worksheets" size=20 onkeypress="return search_worksheets_enter_pressed(event, 'active');" 
```


(By the way, for what it's worth, you can turn on the Develop menu in Safari from the "Advanced" tab in the preferences -- no need to quit and restart.)


---

Comment by mabshoff created at 2009-02-08 02:17:56

It would be nice to get this sorted out in 3.3 since we are doing an rc0 in about two days.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-01 02:51:10

Changing priority from blocker to critical.


---

Comment by mabshoff created at 2009-03-01 02:51:10

Can someone confirm this as a problem that is still happening?

Cheers,

Michael


---

Comment by mhansen created at 2009-03-01 02:55:15

I've never been able to reproduce it, and I've tried on like three different OS X boxes.


---

Comment by jhpalmieri created at 2009-03-01 17:53:15

It's still a problem for me: Sage 3.4.alpha0 (both an upgraded version and a version built from scratch), Intel iMac running OS X 10.5.6, and now with Safari 4 beta (build 5528.16), although I was having the problem before with Safari 3.2.1.  Just to test, I created a new .sage directory and I still have the problem, so it's not something weird in my .sage directory.  I'll try it on my MacBookPro, too. What else can I do to help debug this?


---

Comment by timdumol created at 2009-11-15 12:10:01

Can someone please try this out and see if this is still a problem? Thanks.


---

Comment by jhpalmieri created at 2009-11-15 16:22:33

It's still a problem for me: with Sage 4.2.1 on OS X 10.5, Safari 4.0.4, it still behaves as described in the summary.


---

Attachment

An attempt at fixing the bug.


---

Comment by timdumol created at 2009-12-05 12:05:17

I'm not sure if this patch fixes the bug -- I don't own a Mac, but can anyone check if it does? Thanks!


---

Comment by timdumol created at 2009-12-05 12:05:17

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2009-12-05 18:22:07

This patch fixes it for me on Mac OS X 10.6.

Can people without Macs test that this doesn't break things for them?


---

Comment by was created at 2009-12-08 19:11:34

This is very nice, sensible, and well researched patch. It's also the right pattern for how we should do other similar things in the future.  Very nice!


---

Comment by was created at 2009-12-08 19:11:34

Changing status from needs_review to positive_review.


---

Comment by was created at 2009-12-08 19:13:03

Resolution: fixed


---

Comment by was created at 2009-12-08 19:13:03

I merged this into sage-0.4.6.


---

Comment by mpatel created at 2010-01-05 03:59:37

I think this breaks emptying the trash in Firefox 3.5.6 on Linux and IE 8 on Windows XP.  Please see #7847 for a possible workaround.
