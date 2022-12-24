# Issue 4575: [with patch, needs review] Option to show nestet lists as html tables

archive/issues_004575.json:
```json
{
    "body": "Assignee: whuss\n\nThe attached patch adds the option table_form to the show() command.\n\nIf table_form = True, nested lists are shown in the notebook as nicely\nformatted html tables.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4575\n\n",
    "created_at": "2008-11-21T09:19:56Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "title": "[with patch, needs review] Option to show nestet lists as html tables",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4575",
    "user": "whuss"
}
```
Assignee: whuss

The attached patch adds the option table_form to the show() command.

If table_form = True, nested lists are shown in the notebook as nicely
formatted html tables.

Issue created by migration from https://trac.sagemath.org/ticket/4575





---

archive/issue_comments_034276.json:
```json
{
    "body": "Attachment [trac_4575.patch](tarball://root/attachments/some-uuid/ticket4575/trac_4575.patch) by was created at 2008-11-28 06:13:06\n\nREFEREE REPORT:\n\nPositive review.  Code looks solid and the result is really pretty to look at. \n\n1. Line 945 contains a trivial typo:\n\n```\n935\t    Print a nestet list as a html table. \n```\n\n\n2. The patch isn't a mercurial patch, so... :-(",
    "created_at": "2008-11-28T06:13:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34276",
    "user": "was"
}
```

Attachment [trac_4575.patch](tarball://root/attachments/some-uuid/ticket4575/trac_4575.patch) by was created at 2008-11-28 06:13:06

REFEREE REPORT:

Positive review.  Code looks solid and the result is really pretty to look at. 

1. Line 945 contains a trivial typo:

```
935	    Print a nestet list as a html table. 
```


2. The patch isn't a mercurial patch, so... :-(



---

archive/issue_comments_034277.json:
```json
{
    "body": "I turned this diff into a patch with credit to Wilfried and fixed the typo. I also fixed the typo in the summary :)\n\nCheers,\n\nMichael",
    "created_at": "2008-11-28T06:47:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34277",
    "user": "mabshoff"
}
```

I turned this diff into a patch with credit to Wilfried and fixed the typo. I also fixed the typo in the summary :)

Cheers,

Michael



---

archive/issue_comments_034278.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-28T06:48:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34278",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_034279.json:
```json
{
    "body": "Merged in Sage 3.2.1.rc0",
    "created_at": "2008-11-28T06:48:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34279",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.rc0



---

archive/issue_comments_034280.json:
```json
{
    "body": "I don't agree with William's positive review on this for some design reasons.  First off, it is only useful from the notebook as it just spits out HTML while all other cases of show work fine from the command-line.  Tacking random things and keywords onto show is not a maintainable solution especially since the new functionality is completely orthogonal to what's already there.\n\nInstead this should be some function in a module for creating HTML output of objects.",
    "created_at": "2008-11-29T18:11:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34280",
    "user": "mhansen"
}
```

I don't agree with William's positive review on this for some design reasons.  First off, it is only useful from the notebook as it just spits out HTML while all other cases of show work fine from the command-line.  Tacking random things and keywords onto show is not a maintainable solution especially since the new functionality is completely orthogonal to what's already there.

Instead this should be some function in a module for creating HTML output of objects.



---

archive/issue_comments_034281.json:
```json
{
    "body": "Replying to [comment:4 mhansen]:\n> I don't agree with William's positive review on this for some design reasons.  First off, it is only useful from the notebook as it just spits out HTML while all other cases of show work fine from the command-line.  Tacking random things and keywords onto show is not a maintainable solution especially since the new functionality is completely orthogonal to what's already there.\n> \n> Instead this should be some function in a module for creating HTML output of objects.\n\nOk, let's take this discussion to sage-devel. I might reverse this patch since Jaap oberved a doctest failure that seems impossible to happen. Another reason to reverse this is that we do not want to ship a show with this option if we are going to break it anyway.\n\nYour idea certainly sounds cleaner.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-29T18:15:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34281",
    "user": "mabshoff"
}
```

Replying to [comment:4 mhansen]:
> I don't agree with William's positive review on this for some design reasons.  First off, it is only useful from the notebook as it just spits out HTML while all other cases of show work fine from the command-line.  Tacking random things and keywords onto show is not a maintainable solution especially since the new functionality is completely orthogonal to what's already there.
> 
> Instead this should be some function in a module for creating HTML output of objects.

Ok, let's take this discussion to sage-devel. I might reverse this patch since Jaap oberved a doctest failure that seems impossible to happen. Another reason to reverse this is that we do not want to ship a show with this option if we are going to break it anyway.

Your idea certainly sounds cleaner.

Cheers,

Michael



---

archive/issue_comments_034282.json:
```json
{
    "body": "Attachment [trac_4575-taketwo.patch](tarball://root/attachments/some-uuid/ticket4575/trac_4575-taketwo.patch) by mhansen created at 2008-11-29 18:39:36",
    "created_at": "2008-11-29T18:39:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34282",
    "user": "mhansen"
}
```

Attachment [trac_4575-taketwo.patch](tarball://root/attachments/some-uuid/ticket4575/trac_4575-taketwo.patch) by mhansen created at 2008-11-29 18:39:36



---

archive/issue_comments_034283.json:
```json
{
    "body": "I've attached a patch which implements my idea.  I added a comment about html.nested_list, Since the user would have to read the docstring to the previous keyword anyway.",
    "created_at": "2008-11-29T18:41:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34283",
    "user": "mhansen"
}
```

I've attached a patch which implements my idea.  I added a comment about html.nested_list, Since the user would have to read the docstring to the previous keyword anyway.



---

archive/issue_comments_034284.json:
```json
{
    "body": "I'm ok with revoking my positive review.  I like Mike's suggestion better.",
    "created_at": "2008-11-29T19:02:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34284",
    "user": "was"
}
```

I'm ok with revoking my positive review.  I like Mike's suggestion better.



---

archive/issue_comments_034285.json:
```json
{
    "body": "Ok, can we then get a review on Mike's patch? Since it applies on to of Wilfried's patch we should attempt to get it into 3.2.1.rc1.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-29T21:14:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34285",
    "user": "mabshoff"
}
```

Ok, can we then get a review on Mike's patch? Since it applies on to of Wilfried's patch we should attempt to get it into 3.2.1.rc1.

Cheers,

Michael



---

archive/issue_comments_034286.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2008-11-30T05:42:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34286",
    "user": "mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_034287.json:
```json
{
    "body": "Due to the problems with extra mbox{} popping up reported by Jaap, John and also me on some boxen I will revert this patch in 3.2.1.rc1. See also \n\nhttp://groups.google.com/group/sage-devel/t/3a6575cb49cd61a8\n\nReopened. Hopefully Mike Hansen's approach will be merged in 3.2.2.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-30T05:42:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34287",
    "user": "mabshoff"
}
```

Due to the problems with extra mbox{} popping up reported by Jaap, John and also me on some boxen I will revert this patch in 3.2.1.rc1. See also 

http://groups.google.com/group/sage-devel/t/3a6575cb49cd61a8

Reopened. Hopefully Mike Hansen's approach will be merged in 3.2.2.

Cheers,

Michael



---

archive/issue_comments_034288.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2008-11-30T05:42:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34288",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_034289.json:
```json
{
    "body": "\n```\nsage -t  \"devel/sage/sage/misc/functional.py\"               \n********************************************************************** \nFile \"/home/jaap/work/downloads/sage-3.2.1.alpha2/devel/sage/sage/misc/functiona l.py\", line 891: \n     sage: show([(i, j, i == j) for i in [0..1] for j in [0..1]], table_form = True) \nExpected: \n     <html> \n     <div class=\"notruncate\"> \n     <table class=\"table_form\"> \n     <tbody> \n     <tr class =\"row-a\"> \n     <td><span class=\"math\">0</span></td> \n     <td><span class=\"math\">0</span></td> \n     <td><span class=\"math\">\\mbox{\\rm True}</span></td> \n     </tr> \n     <tr class =\"row-b\"> \n     <td><span class=\"math\">0</span></td> \n     <td><span class=\"math\">1</span></td> \n     <td><span class=\"math\">\\mbox{\\rm False}</span></td> \n     </tr> \n     <tr class =\"row-a\"> \n     <td><span class=\"math\">1</span></td> \n     <td><span class=\"math\">0</span></td> \n     <td><span class=\"math\">\\mbox{\\rm False}</span></td> \n     </tr> \n     <tr class =\"row-b\"> \n     <td><span class=\"math\">1</span></td> \n     <td><span class=\"math\">1</span></td> \n     <td><span class=\"math\">\\mbox{\\rm True}</span></td> \n     </tr> \n     </tbody> \n     </table> \n     </div> \n     </html> \nGot: \n     <html> \n     <div class=\"notruncate\"> \n     <table class=\"table_form\"> \n     <tbody> \n     <tr class =\"row-a\"> \n     <td><span class=\"math\">0</span></td> \n     <td><span class=\"math\">0</span></td> \n     <td><span class=\"math\">True</span></td> \n     </tr> \n     <tr class =\"row-b\"> \n     <td><span class=\"math\">0</span></td> \n     <td><span class=\"math\">1</span></td> \n     <td><span class=\"math\">False</span></td> \n     </tr> \n     <tr class =\"row-a\"> \n     <td><span class=\"math\">1</span></td> \n     <td><span class=\"math\">0</span></td> \n     <td><span class=\"math\">False</span></td> \n     </tr> \n     <tr class =\"row-b\"> \n     <td><span class=\"math\">1</span></td> \n     <td><span class=\"math\">1</span></td> \n     <td><span class=\"math\">True</span></td> \n     </tr> \n     </tbody> \n     </table> \n     </div> \n     </html> \n********************************************************************** \n1 items had failures: \n    1 of   5 in __main__.example_53 \n***Test Failed*** 1 failures. \nFor whitespace errors, see the file /home/jaap/downloads/sage-3.2.1.alpha2/tmp/.doctest_functional.py \n         [11.5 s] \nexit code: 1024 \n```\n",
    "created_at": "2008-11-30T05:44:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34289",
    "user": "mabshoff"
}
```


```
sage -t  "devel/sage/sage/misc/functional.py"               
********************************************************************** 
File "/home/jaap/work/downloads/sage-3.2.1.alpha2/devel/sage/sage/misc/functiona l.py", line 891: 
     sage: show([(i, j, i == j) for i in [0..1] for j in [0..1]], table_form = True) 
Expected: 
     <html> 
     <div class="notruncate"> 
     <table class="table_form"> 
     <tbody> 
     <tr class ="row-a"> 
     <td><span class="math">0</span></td> 
     <td><span class="math">0</span></td> 
     <td><span class="math">\mbox{\rm True}</span></td> 
     </tr> 
     <tr class ="row-b"> 
     <td><span class="math">0</span></td> 
     <td><span class="math">1</span></td> 
     <td><span class="math">\mbox{\rm False}</span></td> 
     </tr> 
     <tr class ="row-a"> 
     <td><span class="math">1</span></td> 
     <td><span class="math">0</span></td> 
     <td><span class="math">\mbox{\rm False}</span></td> 
     </tr> 
     <tr class ="row-b"> 
     <td><span class="math">1</span></td> 
     <td><span class="math">1</span></td> 
     <td><span class="math">\mbox{\rm True}</span></td> 
     </tr> 
     </tbody> 
     </table> 
     </div> 
     </html> 
Got: 
     <html> 
     <div class="notruncate"> 
     <table class="table_form"> 
     <tbody> 
     <tr class ="row-a"> 
     <td><span class="math">0</span></td> 
     <td><span class="math">0</span></td> 
     <td><span class="math">True</span></td> 
     </tr> 
     <tr class ="row-b"> 
     <td><span class="math">0</span></td> 
     <td><span class="math">1</span></td> 
     <td><span class="math">False</span></td> 
     </tr> 
     <tr class ="row-a"> 
     <td><span class="math">1</span></td> 
     <td><span class="math">0</span></td> 
     <td><span class="math">False</span></td> 
     </tr> 
     <tr class ="row-b"> 
     <td><span class="math">1</span></td> 
     <td><span class="math">1</span></td> 
     <td><span class="math">True</span></td> 
     </tr> 
     </tbody> 
     </table> 
     </div> 
     </html> 
********************************************************************** 
1 items had failures: 
    1 of   5 in __main__.example_53 
***Test Failed*** 1 failures. 
For whitespace errors, see the file /home/jaap/downloads/sage-3.2.1.alpha2/tmp/.doctest_functional.py 
         [11.5 s] 
exit code: 1024 
```




---

archive/issue_comments_034290.json:
```json
{
    "body": "Replying to [comment:4 mhansen]:\n> I don't agree with William's positive review on this for some design reasons.  First off, it is only useful from the notebook as it just spits out HTML while all other cases of show work fine from the command-line.\n\nI agree, It should also do something useful on the command-line.\n\n> Tacking random things and keywords onto show is not a maintainable solution especially since the new functionality is completely orthogonal to what's already there.\n\n> Instead this should be some function in a module for creating HTML output of objects.\n\nThis is probably cleaner implementation wise, but I don't think html.nested_list()\nis a good userinterface. Why should the user of the notebook need to know the\nimplementation detail that the output is produced using HTML? And the output of the\nfunction is not really html anyway, but html + latex.\n\nIt is also inconsistent, since\n\nsage: html(sin(x)/x)\n\nproduces acii art, and not html + jsmath.\n\nThere are already at least five functions that produce jsmath output in the notebook,\nwhich all behave differently:\n\n**show():**\n    Produces latex in display mode.\n    And works with graphic objects of course.\n\n**view():**\n    Produces latex in inline mode (which is hard to read in the notebook).\n    This has many options that only work on the commandline and with xdvi.\n    For graphic objects it returns a string representation.\n\n**typeset():**\n    Same behaviour as view() but has no options.\n\n**pretty_print():**\n    produces latex in inline mode.\n\n    If used on the graphics objects, it shows it like show().\n    But it doesn't accept any options, as show() does.\n\n**jsmath():**\n    produces latex in display mode.\n    For graphic objects it returns a string representation,\n    but inside latex math-mode.\n\n    The docstring says that there is a option mode\n    which changes between display and inline mode.\n\n    Unfortunately this only works in doctest mode.\n    In the notebook I get:\n\n```\n    sage: jsmath(x^2, 'inline')\n    Traceback (click to the left for traceback)\n    ...\n    TypeError: __call__() takes exactly 2 arguments (3 given)\n```\n\nIs there a deeper reason why Sage has all these functions? Or have\nthey just accumulated over the years? A few of these should probably\nbe deprecated.\n\nIn my opinion show() is the best of these, because also x.show() works,\nso it is consistent. It's short and easy to remember.\nIt just needs better documentation.\n\nWould a mode flag for show() like the one for jsmath() be okay? Then\nit could be extended in the future without adding additional keywords.\n\nGrettings,\nWilfried",
    "created_at": "2008-12-03T20:27:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34290",
    "user": "whuss"
}
```

Replying to [comment:4 mhansen]:
> I don't agree with William's positive review on this for some design reasons.  First off, it is only useful from the notebook as it just spits out HTML while all other cases of show work fine from the command-line.

I agree, It should also do something useful on the command-line.

> Tacking random things and keywords onto show is not a maintainable solution especially since the new functionality is completely orthogonal to what's already there.

> Instead this should be some function in a module for creating HTML output of objects.

This is probably cleaner implementation wise, but I don't think html.nested_list()
is a good userinterface. Why should the user of the notebook need to know the
implementation detail that the output is produced using HTML? And the output of the
function is not really html anyway, but html + latex.

It is also inconsistent, since

sage: html(sin(x)/x)

produces acii art, and not html + jsmath.

There are already at least five functions that produce jsmath output in the notebook,
which all behave differently:

**show():**
    Produces latex in display mode.
    And works with graphic objects of course.

**view():**
    Produces latex in inline mode (which is hard to read in the notebook).
    This has many options that only work on the commandline and with xdvi.
    For graphic objects it returns a string representation.

**typeset():**
    Same behaviour as view() but has no options.

**pretty_print():**
    produces latex in inline mode.

    If used on the graphics objects, it shows it like show().
    But it doesn't accept any options, as show() does.

**jsmath():**
    produces latex in display mode.
    For graphic objects it returns a string representation,
    but inside latex math-mode.

    The docstring says that there is a option mode
    which changes between display and inline mode.

    Unfortunately this only works in doctest mode.
    In the notebook I get:

```
    sage: jsmath(x^2, 'inline')
    Traceback (click to the left for traceback)
    ...
    TypeError: __call__() takes exactly 2 arguments (3 given)
```

Is there a deeper reason why Sage has all these functions? Or have
they just accumulated over the years? A few of these should probably
be deprecated.

In my opinion show() is the best of these, because also x.show() works,
so it is consistent. It's short and easy to remember.
It just needs better documentation.

Would a mode flag for show() like the one for jsmath() be okay? Then
it could be extended in the future without adding additional keywords.

Grettings,
Wilfried



---

archive/issue_comments_034291.json:
```json
{
    "body": "Wilfried,\n\nplease post the summary you made above to sage-devel so we can have some design discussion.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-03T22:12:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34291",
    "user": "mabshoff"
}
```

Wilfried,

please post the summary you made above to sage-devel so we can have some design discussion.

Cheers,

Michael



---

archive/issue_comments_034292.json:
```json
{
    "body": "What is the status of this?  I'm needing it pretty often, and end up writing my own every time:\n\n\n```\ndef html_table(data):\n    html(\"<table border=1>\")\n    for row in gg:\n        html(\"<tr>\")\n        for cell in row:\n            html(\"<td>\")\n            show(cell)\n            html(\"</td>\")\n        html(\"</tr>\")\n    html(\"</table>\")\n```\n\n\n(it looks nicer if you have #5836 applied)",
    "created_at": "2009-04-20T18:53:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34292",
    "user": "jason"
}
```

What is the status of this?  I'm needing it pretty often, and end up writing my own every time:


```
def html_table(data):
    html("<table border=1>")
    for row in gg:
        html("<tr>")
        for cell in row:
            html("<td>")
            show(cell)
            html("</td>")
        html("</tr>")
    html("</table>")
```


(it looks nicer if you have #5836 applied)



---

archive/issue_comments_034293.json:
```json
{
    "body": "Note that since #5836 fixes images to show exactly where the call to show() happens, I think it would be great if the fix on this ticket called show(thing in cell) instead of latex(thing in cell).  For text, show outputs latex, so I think it will just expand what you can do (i.e., put graphics in tables and have it show those pictures).",
    "created_at": "2009-04-20T19:57:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34293",
    "user": "jason"
}
```

Note that since #5836 fixes images to show exactly where the call to show() happens, I think it would be great if the fix on this ticket called show(thing in cell) instead of latex(thing in cell).  For text, show outputs latex, so I think it will just expand what you can do (i.e., put graphics in tables and have it show those pictures).



---

archive/issue_comments_034294.json:
```json
{
    "body": "More comments:\n\n* It would be simpler to have the row classes use itertools.cycle, instead of the modular arithmetic (smaller code size, anyway, and standard python tools)\n* It would be fantastic to be able to easily specify styles, like borders, background colors, heading rows, etc.\n\nand again, the call to latex should be replaced with a call to show() after #5836 is applied.",
    "created_at": "2009-04-20T20:02:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34294",
    "user": "jason"
}
```

More comments:

* It would be simpler to have the row classes use itertools.cycle, instead of the modular arithmetic (smaller code size, anyway, and standard python tools)
* It would be fantastic to be able to easily specify styles, like borders, background colors, heading rows, etc.

and again, the call to latex should be replaced with a call to show() after #5836 is applied.



---

archive/issue_comments_034295.json:
```json
{
    "body": "contains all previous patches",
    "created_at": "2009-04-21T14:19:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34295",
    "user": "whuss"
}
```

contains all previous patches



---

archive/issue_comments_034296.json:
```json
{
    "body": "Attachment [table.patch](tarball://root/attachments/some-uuid/ticket4575/table.patch) by whuss created at 2009-04-21 14:31:39\n\nReplying to [comment:15 jason]:\n> More comments:\n> \n>  * It would be simpler to have the row classes use itertools.cycle, instead of the modular arithmetic (smaller code size, anyway, and standard python tools)\n>  * It would be fantastic to be able to easily specify styles, like borders, background colors, heading rows, etc.\n> \n> and again, the call to latex should be replaced with a call to show() after #5836 is applied.\n\nI attached a new patch, which needs on #5836 to be applied. The command is now called html.table(). itertools.cycle is used, there is a option to use the first row as a heading,\nstrings are put into the table cells unmodified and also graphic objects are placed into\nthe table correctly.\n\nIt was not possible to just use show() unmodified because this results in nested notebook\ncells which render the notebook unusable.",
    "created_at": "2009-04-21T14:31:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34296",
    "user": "whuss"
}
```

Attachment [table.patch](tarball://root/attachments/some-uuid/ticket4575/table.patch) by whuss created at 2009-04-21 14:31:39

Replying to [comment:15 jason]:
> More comments:
> 
>  * It would be simpler to have the row classes use itertools.cycle, instead of the modular arithmetic (smaller code size, anyway, and standard python tools)
>  * It would be fantastic to be able to easily specify styles, like borders, background colors, heading rows, etc.
> 
> and again, the call to latex should be replaced with a call to show() after #5836 is applied.

I attached a new patch, which needs on #5836 to be applied. The command is now called html.table(). itertools.cycle is used, there is a option to use the first row as a heading,
strings are put into the table cells unmodified and also graphic objects are placed into
the table correctly.

It was not possible to just use show() unmodified because this results in nested notebook
cells which render the notebook unusable.



---

archive/issue_comments_034297.json:
```json
{
    "body": "was: this last patch changes show so that show(..., linkmode=True) *returns* a string, rather than just prints a string.  How do you feel about it?\n\nI think it makes things cleaner to do things like the patch does.  There ought to be some way of programmatically getting the output that show would have printed so you can do something with it, like wrap it in td tags as in the patch.",
    "created_at": "2009-04-22T11:03:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34297",
    "user": "jason"
}
```

was: this last patch changes show so that show(..., linkmode=True) *returns* a string, rather than just prints a string.  How do you feel about it?

I think it makes things cleaner to do things like the patch does.  There ought to be some way of programmatically getting the output that show would have printed so you can do something with it, like wrap it in td tags as in the patch.



---

archive/issue_comments_034298.json:
```json
{
    "body": "This is a great piece of functionality.  I'm sure I'll use it a lot.\n\nI'm bothered a bit that the cells are automatically \"shown\" (instead of just printed).  I think I would have called it show.table() and just made it check to make sure we were running in the notebook.  But I also see that this discussion has been had above.  Oh well.  I'm willing to concede the naming for a positive review so that this gets in.\n\nI give this a positive review.  However, we should wait for a couple of days to see if William has something to say about the changes to show().  If he hasn't weighed in on the issue after a while, change this to positive review.",
    "created_at": "2009-05-30T06:55:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34298",
    "user": "jason"
}
```

This is a great piece of functionality.  I'm sure I'll use it a lot.

I'm bothered a bit that the cells are automatically "shown" (instead of just printed).  I think I would have called it show.table() and just made it check to make sure we were running in the notebook.  But I also see that this discussion has been had above.  Oh well.  I'm willing to concede the naming for a positive review so that this gets in.

I give this a positive review.  However, we should wait for a couple of days to see if William has something to say about the changes to show().  If he hasn't weighed in on the issue after a while, change this to positive review.



---

archive/issue_comments_034299.json:
```json
{
    "body": "apply on top of previous patch",
    "created_at": "2009-05-30T07:06:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34299",
    "user": "jason"
}
```

apply on top of previous patch



---

archive/issue_comments_034300.json:
```json
{
    "body": "Attachment [trac_4575-referee.patch](tarball://root/attachments/some-uuid/ticket4575/trac_4575-referee.patch) by jason created at 2009-05-30 07:06:47\n\nThe referee patch contains slight doctest fixes so that doctests pass (there were some issues with the latex spacing).",
    "created_at": "2009-05-30T07:06:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34300",
    "user": "jason"
}
```

Attachment [trac_4575-referee.patch](tarball://root/attachments/some-uuid/ticket4575/trac_4575-referee.patch) by jason created at 2009-05-30 07:06:47

The referee patch contains slight doctest fixes so that doctests pass (there were some issues with the latex spacing).



---

archive/issue_comments_034301.json:
```json
{
    "body": "I'm ok with the api addition to show.",
    "created_at": "2009-05-30T13:39:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34301",
    "user": "was"
}
```

I'm ok with the api addition to show.



---

archive/issue_comments_034302.json:
```json
{
    "body": "Merged in 4.0.1.alpha0.",
    "created_at": "2009-06-01T06:26:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34302",
    "user": "mhansen"
}
```

Merged in 4.0.1.alpha0.



---

archive/issue_comments_034303.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-01T06:26:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34303",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_034304.json:
```json
{
    "body": "Replying to [ticket:4575 whuss]:\n> The attached patch adds the option table_form to the show() command.\n> \n> If table_form = True, nested lists are shown in the notebook as nicely\n> formatted html tables.\nCan someone upload a screenshot that shows an example of a nicely formatted HTML table. Code sample would be good as well, if relevant. I plan to showcase this ticket in the release tour, and having a visual is worth a thousand words.",
    "created_at": "2009-06-04T14:26:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34304",
    "user": "mvngu"
}
```

Replying to [ticket:4575 whuss]:
> The attached patch adds the option table_form to the show() command.
> 
> If table_form = True, nested lists are shown in the notebook as nicely
> formatted html tables.
Can someone upload a screenshot that shows an example of a nicely formatted HTML table. Code sample would be good as well, if relevant. I plan to showcase this ticket in the release tour, and having a visual is worth a thousand words.



---

archive/issue_comments_034305.json:
```json
{
    "body": "Attachment [html_table.png](tarball://root/attachments/some-uuid/ticket4575/html_table.png) by whuss created at 2009-06-04 14:54:50",
    "created_at": "2009-06-04T14:54:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34305",
    "user": "whuss"
}
```

Attachment [html_table.png](tarball://root/attachments/some-uuid/ticket4575/html_table.png) by whuss created at 2009-06-04 14:54:50



---

archive/issue_comments_034306.json:
```json
{
    "body": "Attachment [html_table1.png](tarball://root/attachments/some-uuid/ticket4575/html_table1.png) by whuss created at 2009-06-04 14:58:35\n\nReplying to [comment:22 mvngu]:\n> Can someone upload a screenshot that shows an example of a nicely formatted HTML table. Code sample would be good as well, if relevant. I plan to showcase this ticket in the release tour, and having a visual is worth a thousand words.\n\nThe first picture is produced by:\n\n\n```\nsage: functions = [sin(x), cos(x), tan(x), acos(x)]\nsage: t = [[f, taylor(f, x, 0, 10)] for f in functions]\nsage: html.table([[\"Function\", \"Series\"]] + t, header = True)\n```\n\n\nIt is also possible to put graphic objects into the table:\n\n\n```\nsage: f = 1/x*sin(x)\nsage: t = [[\"Function\", \"Plot\"],[f, plot(f, x, -4*pi, 4*pi)]]\nsage: html.table(t, header = True)\n```\n\n\nI hope this helps.",
    "created_at": "2009-06-04T14:58:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34306",
    "user": "whuss"
}
```

Attachment [html_table1.png](tarball://root/attachments/some-uuid/ticket4575/html_table1.png) by whuss created at 2009-06-04 14:58:35

Replying to [comment:22 mvngu]:
> Can someone upload a screenshot that shows an example of a nicely formatted HTML table. Code sample would be good as well, if relevant. I plan to showcase this ticket in the release tour, and having a visual is worth a thousand words.

The first picture is produced by:


```
sage: functions = [sin(x), cos(x), tan(x), acos(x)]
sage: t = [[f, taylor(f, x, 0, 10)] for f in functions]
sage: html.table([["Function", "Series"]] + t, header = True)
```


It is also possible to put graphic objects into the table:


```
sage: f = 1/x*sin(x)
sage: t = [["Function", "Plot"],[f, plot(f, x, -4*pi, 4*pi)]]
sage: html.table(t, header = True)
```


I hope this helps.



---

archive/issue_comments_034307.json:
```json
{
    "body": "Replying to [comment:23 whuss]:\n> The first picture is produced by:\n<SNIP>\n> It is also possible to put graphic objects into the table:\n<SNIP>\n> I hope this helps.\nHoly bitbucket! Those images look drop-dead gorgeous! Thanks, Wilfried.",
    "created_at": "2009-06-04T15:05:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34307",
    "user": "mvngu"
}
```

Replying to [comment:23 whuss]:
> The first picture is produced by:
<SNIP>
> It is also possible to put graphic objects into the table:
<SNIP>
> I hope this helps.
Holy bitbucket! Those images look drop-dead gorgeous! Thanks, Wilfried.



---

archive/issue_comments_034308.json:
```json
{
    "body": "Also, you can try \n\n\n```\nhtml.table([[\"Graph\", \"Vertices\", \"Edges\"]] + [(g.plot(), g.order(), g.size()) for g in graphs(3)], header=True)\n```\n\n\n(sorry, I don't have the patch applied right now, so I can't post a screenshot.  It'd be nice if alpha.sagenb.org was updated...)",
    "created_at": "2009-06-04T19:30:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34308",
    "user": "jason"
}
```

Also, you can try 


```
html.table([["Graph", "Vertices", "Edges"]] + [(g.plot(), g.order(), g.size()) for g in graphs(3)], header=True)
```


(sorry, I don't have the patch applied right now, so I can't post a screenshot.  It'd be nice if alpha.sagenb.org was updated...)



---

archive/issue_comments_034309.json:
```json
{
    "body": "See #6433 for a related issue.",
    "created_at": "2009-06-27T17:27:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4575",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4575#issuecomment-34309",
    "user": "jhpalmieri"
}
```

See #6433 for a related issue.
