# Issue 4255: WYSIWYG in-place editing of text cells (using tinyMCE and jEditable)

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2008-10-09 01:49:42

Assignee: boothby

This provides in-place editing of text cells using tinyMCE and jEditable (spkgs provided below).  Basically, you create a text cell by inserting something between the cells (between the ending }}} and the starting {{{ of the next cell) in the "Edit" view.  Switching back to the worksheet view, you can then doubleclick on the html text and an in-place TinyMCE editor pops up letting you edit the html text.


---

Attachment


---

Comment by jason created at 2008-10-09 01:52:05

Apply the patch above and install the two spkgs here:

http://sage.math.washington.edu/home/jason/jeditable-1.6.1.spkg

http://sage.math.washington.edu/home/jason/tinyMCE-3.2.0.2.spkg

Create a worksheet and make a text cell by editing it in the "Edit" mode and putting text between the cells.  Switch back to the worksheet view and doubleclick on that text.  A TinyMCE editor should pop up, letting you edit the text.  Save your changes and the worksheet is updated.


---

Comment by jason created at 2008-10-09 01:57:54

As usual, $x^2$ and $$x^2$$ give you jsmath latex output.


---

Comment by jason created at 2008-10-09 01:58:23

As usual, `$x^2$` and `$$x^2$$` in the tinyMCE editor give you jsmath latex output.


---

Comment by jason created at 2008-10-09 02:06:19

The bad news is that the above javascript adds about 225K to the javascript downloaded on a page.  That's about double the amount of javascript.

Figuring out how to do automatic gzip compression with Twisted would significantly probably alleviate the amount of javascript that we were downloading, I think.  it's built-in, but there don't seem to be *any* docs for setting up gzip compression automatically.


---

Comment by jason created at 2008-10-09 02:07:19

Of course, the good news is that your browser usually caches all of that javascript, so you're only downloading it once or so.


---

Comment by jason created at 2008-10-09 02:14:11

This work was done on 3.1.3alpha1


---

Comment by mhampton created at 2008-10-09 03:41:00

This works well for me, and I think it is worth adding.  It would be nice to remove the jsmath popups since they conflict with this addition, and I think the editor is far more useful.


---

Comment by jason created at 2008-10-10 03:59:39

I should also add that the patch does not assume the spkgs are installed; it should only enhance behavior if the spkgs are installed.


---

Comment by mabshoff created at 2008-10-10 17:44:30

Jason,

please bring up the inclusion of these spkgs on [sage-devel]. I did take a look and they seem to be very cross platform and support all major browsers, so I do not see a problem there. One thing discussed should be if this editor is the "best out there" since we will likely end up supporting it for the foreseeable future. From what I have seen at the website it is actively maintained so I am in favor of merging it.

Cheers,

Michael


---

Comment by jason created at 2008-10-10 20:26:52

Michael,

I'll bring it up on sage-devel.  William suggested a different way of dealing with javascript spkgs (not installing them under the extcode repository, but instead in the $SAGE_ROOT/local directory).  I'm converting the existing javascript code to spkgs first, then I'll do these.  Also, I'd like to implement mhamtpon's idea of shift-click for creating non-output (i.e., text) cells.

I'll also bring up my reasons for choosing tinyMCE over FCKEditor (and the other editors).


---

Comment by mabshoff created at 2008-10-10 20:39:42

Replying to [comment:10 jason]:
> Michael,
> 
> I'll bring it up on sage-devel.  William suggested a different way of dealing with javascript spkgs (not installing them under the extcode repository, but instead in the $SAGE_ROOT/local directory).  

I agree that they should be moved, but straight under $SAGE_ROOT/local seems like a bad location. I would prefer something like $SAGE_ROOT/local/jsript/$FOO.spkg for easy maintainability.

>I'm converting the existing javascript code to spkgs first, then I'll do these.  Also, I'd like to implement mhamtpon's idea of shift-click for creating non-output (i.e., text) cells.

Sure, but at least the jquery.spkg is another ticket and we don't need to vote on that one since it is already in Sage :)

> I'll also bring up my reasons for choosing tinyMCE over FCKEditor (and the other editors).

Excellent.

Cheers,

Michael


---

Comment by jason created at 2008-10-10 21:07:56

Right now I'm putting them under:

$SAGE_ROOT/local/notebook/javascript/$PKG

to mirror the directory structure in extcode.

Right now I have

$SAGE_ROOT/local/notebook/javascript/jquery
$SAGE_ROOT/local/notebook/javascript/jqueryui

etc.


---

Comment by jason created at 2008-10-10 23:37:09

Note to self: Install the jquery extendedclick plugin: http://plugins.jquery.com/project/extendedclick

This allows for a shiftclick event.  If we support creation with a shift-click, then I think editing also ought to be a shift-click.


---

Comment by mabshoff created at 2008-10-11 09:01:22

This one needs to wait for a vote on [sage-devel], so let's bump it :)

Cheers,

Michael


---

Comment by jason created at 2008-10-12 02:24:14

Ignore the spkgs above; instead, use the spkgs from #4267.


---

Comment by jason created at 2008-10-14 01:54:18

Because of the way that the spkgs at #4267 are set up, to test this patch, you need to apply the patch at #4267 on top of it.  This is because the spkgs at #4267 are installed in a new directory and the necessary setup for this new directory is contained in the patch there.  The patch there contains the patch here.

So, to test this:

  1. Apply the patch here.
  2. Apply the patch at #4267
  3. Install all of the spkgs listed at #4267.
  4. Optionally, apply the extcode patch at #4267, which deletes the packages from the extcode directory.

Then follow the instructions above to create a text cell and edit it (i.e., create it by editing the worksheet, then double-click on the text to bring up TinyMCE).


---

Comment by jason created at 2008-10-18 04:07:43

Okay, *ignore* all patches here.  Instead, apply the edit-in-place-and-javascript-spkgs.patch patch at #4267 and install the spkgs there.

That patch enables easy creation of text cells--just shift-click on the "new cell" bar in the notebook.


---

Comment by mabshoff created at 2008-12-06 06:37:39

Resolution: invalid
