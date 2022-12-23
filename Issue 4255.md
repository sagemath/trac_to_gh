# Issue 4255: WYSIWYG in-place editing of text cells (using tinyMCE and jEditable)

archive/issues_004255.json:
```json
{
    "body": "Assignee: boothby\n\nThis provides in-place editing of text cells using tinyMCE and jEditable (spkgs provided below).  Basically, you create a text cell by inserting something between the cells (between the ending }}} and the starting {{{ of the next cell) in the \"Edit\" view.  Switching back to the worksheet view, you can then doubleclick on the html text and an in-place TinyMCE editor pops up letting you edit the html text.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4255\n\n",
    "created_at": "2008-10-09T01:49:42Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "title": "WYSIWYG in-place editing of text cells (using tinyMCE and jEditable)",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4255",
    "user": "jason"
}
```
Assignee: boothby

This provides in-place editing of text cells using tinyMCE and jEditable (spkgs provided below).  Basically, you create a text cell by inserting something between the cells (between the ending }}} and the starting {{{ of the next cell) in the "Edit" view.  Switching back to the worksheet view, you can then doubleclick on the html text and an in-place TinyMCE editor pops up letting you edit the html text.

Issue created by migration from https://trac.sagemath.org/ticket/4255





---

archive/issue_comments_030951.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-10-09T01:50:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4255#issuecomment-30951",
    "user": "jason"
}
```

Attachment



---

archive/issue_comments_030952.json:
```json
{
    "body": "Apply the patch above and install the two spkgs here:\n\nhttp://sage.math.washington.edu/home/jason/jeditable-1.6.1.spkg\n\nhttp://sage.math.washington.edu/home/jason/tinyMCE-3.2.0.2.spkg\n\nCreate a worksheet and make a text cell by editing it in the \"Edit\" mode and putting text between the cells.  Switch back to the worksheet view and doubleclick on that text.  A TinyMCE editor should pop up, letting you edit the text.  Save your changes and the worksheet is updated.",
    "created_at": "2008-10-09T01:52:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4255#issuecomment-30952",
    "user": "jason"
}
```

Apply the patch above and install the two spkgs here:

http://sage.math.washington.edu/home/jason/jeditable-1.6.1.spkg

http://sage.math.washington.edu/home/jason/tinyMCE-3.2.0.2.spkg

Create a worksheet and make a text cell by editing it in the "Edit" mode and putting text between the cells.  Switch back to the worksheet view and doubleclick on that text.  A TinyMCE editor should pop up, letting you edit the text.  Save your changes and the worksheet is updated.



---

archive/issue_comments_030953.json:
```json
{
    "body": "As usual, $x^2$ and $$x^2$$ give you jsmath latex output.",
    "created_at": "2008-10-09T01:57:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4255#issuecomment-30953",
    "user": "jason"
}
```

As usual, $x^2$ and $$x^2$$ give you jsmath latex output.



---

archive/issue_comments_030954.json:
```json
{
    "body": "As usual, `$x^2$` and `$$x^2$$` in the tinyMCE editor give you jsmath latex output.",
    "created_at": "2008-10-09T01:58:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4255#issuecomment-30954",
    "user": "jason"
}
```

As usual, `$x^2$` and `$$x^2$$` in the tinyMCE editor give you jsmath latex output.



---

archive/issue_comments_030955.json:
```json
{
    "body": "The bad news is that the above javascript adds about 225K to the javascript downloaded on a page.  That's about double the amount of javascript.\n\nFiguring out how to do automatic gzip compression with Twisted would significantly probably alleviate the amount of javascript that we were downloading, I think.  it's built-in, but there don't seem to be *any* docs for setting up gzip compression automatically.",
    "created_at": "2008-10-09T02:06:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4255#issuecomment-30955",
    "user": "jason"
}
```

The bad news is that the above javascript adds about 225K to the javascript downloaded on a page.  That's about double the amount of javascript.

Figuring out how to do automatic gzip compression with Twisted would significantly probably alleviate the amount of javascript that we were downloading, I think.  it's built-in, but there don't seem to be *any* docs for setting up gzip compression automatically.



---

archive/issue_comments_030956.json:
```json
{
    "body": "Of course, the good news is that your browser usually caches all of that javascript, so you're only downloading it once or so.",
    "created_at": "2008-10-09T02:07:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4255#issuecomment-30956",
    "user": "jason"
}
```

Of course, the good news is that your browser usually caches all of that javascript, so you're only downloading it once or so.



---

archive/issue_comments_030957.json:
```json
{
    "body": "This work was done on 3.1.3alpha1",
    "created_at": "2008-10-09T02:14:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4255#issuecomment-30957",
    "user": "jason"
}
```

This work was done on 3.1.3alpha1



---

archive/issue_comments_030958.json:
```json
{
    "body": "This works well for me, and I think it is worth adding.  It would be nice to remove the jsmath popups since they conflict with this addition, and I think the editor is far more useful.",
    "created_at": "2008-10-09T03:41:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4255#issuecomment-30958",
    "user": "mhampton"
}
```

This works well for me, and I think it is worth adding.  It would be nice to remove the jsmath popups since they conflict with this addition, and I think the editor is far more useful.



---

archive/issue_comments_030959.json:
```json
{
    "body": "I should also add that the patch does not assume the spkgs are installed; it should only enhance behavior if the spkgs are installed.",
    "created_at": "2008-10-10T03:59:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4255#issuecomment-30959",
    "user": "jason"
}
```

I should also add that the patch does not assume the spkgs are installed; it should only enhance behavior if the spkgs are installed.



---

archive/issue_comments_030960.json:
```json
{
    "body": "Jason,\n\nplease bring up the inclusion of these spkgs on [sage-devel]. I did take a look and they seem to be very cross platform and support all major browsers, so I do not see a problem there. One thing discussed should be if this editor is the \"best out there\" since we will likely end up supporting it for the foreseeable future. From what I have seen at the website it is actively maintained so I am in favor of merging it.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-10T17:44:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4255#issuecomment-30960",
    "user": "mabshoff"
}
```

Jason,

please bring up the inclusion of these spkgs on [sage-devel]. I did take a look and they seem to be very cross platform and support all major browsers, so I do not see a problem there. One thing discussed should be if this editor is the "best out there" since we will likely end up supporting it for the foreseeable future. From what I have seen at the website it is actively maintained so I am in favor of merging it.

Cheers,

Michael



---

archive/issue_comments_030961.json:
```json
{
    "body": "Michael,\n\nI'll bring it up on sage-devel.  William suggested a different way of dealing with javascript spkgs (not installing them under the extcode repository, but instead in the $SAGE_ROOT/local directory).  I'm converting the existing javascript code to spkgs first, then I'll do these.  Also, I'd like to implement mhamtpon's idea of shift-click for creating non-output (i.e., text) cells.\n\nI'll also bring up my reasons for choosing tinyMCE over FCKEditor (and the other editors).",
    "created_at": "2008-10-10T20:26:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4255#issuecomment-30961",
    "user": "jason"
}
```

Michael,

I'll bring it up on sage-devel.  William suggested a different way of dealing with javascript spkgs (not installing them under the extcode repository, but instead in the $SAGE_ROOT/local directory).  I'm converting the existing javascript code to spkgs first, then I'll do these.  Also, I'd like to implement mhamtpon's idea of shift-click for creating non-output (i.e., text) cells.

I'll also bring up my reasons for choosing tinyMCE over FCKEditor (and the other editors).



---

archive/issue_comments_030962.json:
```json
{
    "body": "Replying to [comment:10 jason]:\n> Michael,\n> \n> I'll bring it up on sage-devel.  William suggested a different way of dealing with javascript spkgs (not installing them under the extcode repository, but instead in the $SAGE_ROOT/local directory).  \n\nI agree that they should be moved, but straight under $SAGE_ROOT/local seems like a bad location. I would prefer something like $SAGE_ROOT/local/jsript/$FOO.spkg for easy maintainability.\n\n>I'm converting the existing javascript code to spkgs first, then I'll do these.  Also, I'd like to implement mhamtpon's idea of shift-click for creating non-output (i.e., text) cells.\n\nSure, but at least the jquery.spkg is another ticket and we don't need to vote on that one since it is already in Sage :)\n\n> I'll also bring up my reasons for choosing tinyMCE over FCKEditor (and the other editors).\n\nExcellent.\n\nCheers,\n\nMichael",
    "created_at": "2008-10-10T20:39:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4255#issuecomment-30962",
    "user": "mabshoff"
}
```

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

archive/issue_comments_030963.json:
```json
{
    "body": "Right now I'm putting them under:\n\n$SAGE_ROOT/local/notebook/javascript/$PKG\n\nto mirror the directory structure in extcode.\n\nRight now I have\n\n$SAGE_ROOT/local/notebook/javascript/jquery\n$SAGE_ROOT/local/notebook/javascript/jqueryui\n\netc.",
    "created_at": "2008-10-10T21:07:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4255#issuecomment-30963",
    "user": "jason"
}
```

Right now I'm putting them under:

$SAGE_ROOT/local/notebook/javascript/$PKG

to mirror the directory structure in extcode.

Right now I have

$SAGE_ROOT/local/notebook/javascript/jquery
$SAGE_ROOT/local/notebook/javascript/jqueryui

etc.



---

archive/issue_comments_030964.json:
```json
{
    "body": "Note to self: Install the jquery extendedclick plugin: http://plugins.jquery.com/project/extendedclick\n\nThis allows for a shiftclick event.  If we support creation with a shift-click, then I think editing also ought to be a shift-click.",
    "created_at": "2008-10-10T23:37:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4255#issuecomment-30964",
    "user": "jason"
}
```

Note to self: Install the jquery extendedclick plugin: http://plugins.jquery.com/project/extendedclick

This allows for a shiftclick event.  If we support creation with a shift-click, then I think editing also ought to be a shift-click.



---

archive/issue_comments_030965.json:
```json
{
    "body": "This one needs to wait for a vote on [sage-devel], so let's bump it :)\n\nCheers,\n\nMichael",
    "created_at": "2008-10-11T09:01:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4255#issuecomment-30965",
    "user": "mabshoff"
}
```

This one needs to wait for a vote on [sage-devel], so let's bump it :)

Cheers,

Michael



---

archive/issue_comments_030966.json:
```json
{
    "body": "Ignore the spkgs above; instead, use the spkgs from #4267.",
    "created_at": "2008-10-12T02:24:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4255#issuecomment-30966",
    "user": "jason"
}
```

Ignore the spkgs above; instead, use the spkgs from #4267.



---

archive/issue_comments_030967.json:
```json
{
    "body": "Because of the way that the spkgs at #4267 are set up, to test this patch, you need to apply the patch at #4267 on top of it.  This is because the spkgs at #4267 are installed in a new directory and the necessary setup for this new directory is contained in the patch there.  The patch there contains the patch here.\n\nSo, to test this:\n\n1. Apply the patch here.\n2. Apply the patch at #4267\n3. Install all of the spkgs listed at #4267.\n4. Optionally, apply the extcode patch at #4267, which deletes the packages from the extcode directory.\n\nThen follow the instructions above to create a text cell and edit it (i.e., create it by editing the worksheet, then double-click on the text to bring up TinyMCE).",
    "created_at": "2008-10-14T01:54:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4255#issuecomment-30967",
    "user": "jason"
}
```

Because of the way that the spkgs at #4267 are set up, to test this patch, you need to apply the patch at #4267 on top of it.  This is because the spkgs at #4267 are installed in a new directory and the necessary setup for this new directory is contained in the patch there.  The patch there contains the patch here.

So, to test this:

1. Apply the patch here.
2. Apply the patch at #4267
3. Install all of the spkgs listed at #4267.
4. Optionally, apply the extcode patch at #4267, which deletes the packages from the extcode directory.

Then follow the instructions above to create a text cell and edit it (i.e., create it by editing the worksheet, then double-click on the text to bring up TinyMCE).



---

archive/issue_comments_030968.json:
```json
{
    "body": "Okay, *ignore* all patches here.  Instead, apply the edit-in-place-and-javascript-spkgs.patch patch at #4267 and install the spkgs there.\n\nThat patch enables easy creation of text cells--just shift-click on the \"new cell\" bar in the notebook.",
    "created_at": "2008-10-18T04:07:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4255#issuecomment-30968",
    "user": "jason"
}
```

Okay, *ignore* all patches here.  Instead, apply the edit-in-place-and-javascript-spkgs.patch patch at #4267 and install the spkgs there.

That patch enables easy creation of text cells--just shift-click on the "new cell" bar in the notebook.



---

archive/issue_comments_030969.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-12-06T06:37:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4255",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4255#issuecomment-30969",
    "user": "mabshoff"
}
```

Resolution: invalid
