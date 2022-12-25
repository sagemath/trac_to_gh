# Issue 7298: use html5 video tag for animations

archive/issues_007298.json:
```json
{
    "body": "Assignee: whuss\n\nCC:  mhampton @nilesjohnson @novoselt\n\nKeywords: animation, video\n\nThe attached patch adds support for creating Ogg Theora videos from\nanimation objects.\n\nThe resulting video files are embedded into the notebook using the\nhtml5 video tag.\n\nThe show method of animations now works more like the one of\nGraphics objects. Animations can now be embeddend in html fragments,\nfor example using html.table().\n\nBy default animations are still created as animated gifs. To get\na Theora video from an animation \"a\" use:\n\n\n```\na.show(format = 'ogv')\n```\n\n\nDepends on libtheora and libogg spkg's (Trac: #7297).\n\nIssue created by migration from https://trac.sagemath.org/ticket/7298\n\n",
    "created_at": "2009-10-25T16:00:45Z",
    "labels": [
        "component: graphics",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "use html5 video tag for animations",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7298",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```
Assignee: whuss

CC:  mhampton @nilesjohnson @novoselt

Keywords: animation, video

The attached patch adds support for creating Ogg Theora videos from
animation objects.

The resulting video files are embedded into the notebook using the
html5 video tag.

The show method of animations now works more like the one of
Graphics objects. Animations can now be embeddend in html fragments,
for example using html.table().

By default animations are still created as animated gifs. To get
a Theora video from an animation "a" use:


```
a.show(format = 'ogv')
```


Depends on libtheora and libogg spkg's (Trac: #7297).

Issue created by migration from https://trac.sagemath.org/ticket/7298





---

archive/issue_comments_060640.json:
```json
{
    "body": "Attachment [ogv.patch](tarball://root/attachments/some-uuid/ticket7298/ogv.patch) by whuss created at 2009-10-25 16:01:03",
    "created_at": "2009-10-25T16:01:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60640",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Attachment [ogv.patch](tarball://root/attachments/some-uuid/ticket7298/ogv.patch) by whuss created at 2009-10-25 16:01:03



---

archive/issue_comments_060641.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-25T16:01:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60641",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_060642.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2009-10-25T16:01:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60642",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_060643.json:
```json
{
    "body": "Changing assignee from whuss to @jasongrout.",
    "created_at": "2010-02-27T21:02:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60643",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from whuss to @jasongrout.



---

archive/issue_comments_060644.json:
```json
{
    "body": "Changing assignee from @jasongrout to whuss.",
    "created_at": "2010-02-27T21:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60644",
    "user": "https://github.com/jasongrout"
}
```

Changing assignee from @jasongrout to whuss.



---

archive/issue_comments_060645.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-01T08:23:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60645",
    "user": "https://trac.sagemath.org/admin/accounts/users/pang"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060646.json:
```json
{
    "body": "The \"iterations\" optional argument does not work, but I don't think it's needed, as html5 has video controls. I'd suggest to either remove this argument, or change the documentation of 'ogv' from:\n\n-  ``iterations`` - integer (default: 0); number of\n   iterations of animation. If 0, loop forever.\n\nto:\n\n-  ``iterations`` - this argument is ignored, but kept for\n   compatibility with the 'gif' function\n           \nOtherwise, everything's fine. The issue above is absolutely minor, so I'm giving a positive review.",
    "created_at": "2010-05-01T08:23:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60646",
    "user": "https://trac.sagemath.org/admin/accounts/users/pang"
}
```

The "iterations" optional argument does not work, but I don't think it's needed, as html5 has video controls. I'd suggest to either remove this argument, or change the documentation of 'ogv' from:

-  ``iterations`` - integer (default: 0); number of
   iterations of animation. If 0, loop forever.

to:

-  ``iterations`` - this argument is ignored, but kept for
   compatibility with the 'gif' function
           
Otherwise, everything's fine. The issue above is absolutely minor, so I'm giving a positive review.



---

archive/issue_comments_060647.json:
```json
{
    "body": "I've updated the Author(s) and Reviewer(s) fields with full names.  Please correct them, if I'm wrong.",
    "created_at": "2010-07-20T10:08:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60647",
    "user": "https://github.com/qed777"
}
```

I've updated the Author(s) and Reviewer(s) fields with full names.  Please correct them, if I'm wrong.



---

archive/issue_comments_060648.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-20T10:08:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60648",
    "user": "https://github.com/qed777"
}
```

Resolution: fixed



---

archive/issue_comments_060649.json:
```json
{
    "body": "By the way,\n\n* Mercurial patches for Sage should include the ticket number in the first line of the commit string.\n* The patch filename should include the ticket number.  A common form is `trac_7298-add_ogv_format.patch`.",
    "created_at": "2010-07-20T10:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60649",
    "user": "https://github.com/qed777"
}
```

By the way,

* Mercurial patches for Sage should include the ticket number in the first line of the commit string.
* The patch filename should include the ticket number.  A common form is `trac_7298-add_ogv_format.patch`.



---

archive/issue_comments_060650.json:
```json
{
    "body": "Changing status from closed to needs_work.",
    "created_at": "2010-07-21T00:19:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60650",
    "user": "https://github.com/qed777"
}
```

Changing status from closed to needs_work.



---

archive/issue_comments_060651.json:
```json
{
    "body": "I'm getting a docbuild warning from `sage/plot/animate.py`:\n\n```\n:0: (WARNING/2) Literal block expected; none found.\n```\n\nI think the problem is that the `ogv` method's docstring ends with\n\n```\n        .. note::\n           If libtheora is not installed, you will get an error\n           message like this::\n```\n\nCould someone please fix this?  For now, I'm removing [attachment:ogv.patch] from 4.5.2.alpha0.",
    "created_at": "2010-07-21T00:19:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60651",
    "user": "https://github.com/qed777"
}
```

I'm getting a docbuild warning from `sage/plot/animate.py`:

```
:0: (WARNING/2) Literal block expected; none found.
```

I think the problem is that the `ogv` method's docstring ends with

```
        .. note::
           If libtheora is not installed, you will get an error
           message like this::
```

Could someone please fix this?  For now, I'm removing [attachment:ogv.patch] from 4.5.2.alpha0.



---

archive/issue_comments_060652.json:
```json
{
    "body": "only apply this patch",
    "created_at": "2010-07-21T07:20:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60652",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

only apply this patch



---

archive/issue_comments_060653.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-07-21T07:21:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60653",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060654.json:
```json
{
    "body": "Attachment [trac-7298-ogv.patch](tarball://root/attachments/some-uuid/ticket7298/trac-7298-ogv.patch) by whuss created at 2010-07-21 07:21:50\n\nReplying to [comment:7 mpatel]:\n> I'm getting a docbuild warning from `sage/plot/animate.py`:\n> {{{\n> :0: (WARNING/2) Literal block expected; none found.\n> }}}\n> I think the problem is that the `ogv` method's docstring ends with\n> {{{\n>         .. note::\n>            If libtheora is not installed, you will get an error\n>            message like this::\n> }}}\n> Could someone please fix this?  For now, I'm removing [attachment:ogv.patch] from 4.5.2.alpha0.\n\nI added the error message to the documentation in the new patch [attachment:trac-7298-ogv.patch].",
    "created_at": "2010-07-21T07:21:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60654",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Attachment [trac-7298-ogv.patch](tarball://root/attachments/some-uuid/ticket7298/trac-7298-ogv.patch) by whuss created at 2010-07-21 07:21:50

Replying to [comment:7 mpatel]:
> I'm getting a docbuild warning from `sage/plot/animate.py`:
> {{{
> :0: (WARNING/2) Literal block expected; none found.
> }}}
> I think the problem is that the `ogv` method's docstring ends with
> {{{
>         .. note::
>            If libtheora is not installed, you will get an error
>            message like this::
> }}}
> Could someone please fix this?  For now, I'm removing [attachment:ogv.patch] from 4.5.2.alpha0.

I added the error message to the documentation in the new patch [attachment:trac-7298-ogv.patch].



---

archive/issue_comments_060655.json:
```json
{
    "body": "Hi,\n\nI'd really like to use this, but I'm having trouble from the start . . . \n\n\n```\nsage: a = animate([sin(x + float(k)) for k in srange(0,2*pi,0.7)], xmin=0, xmax=2*pi, figsize=[2,1])\nsage: a.ogv()\nError: libtheora does not appear to be installed. Saving an\nanimation to a Ogg Theora file or displaying an animation requires the\nlibtheora spkg, so please install it and try again.\n\nsage: install_package('libtheora')\nTraceback (most recent call last):\nValueError: Package is already installed. Try install_package('libtheora',force=True)\n```\n\n\nI did install both `libogg` and `libtheora` using `install_package` in sage 4.5.2",
    "created_at": "2010-09-07T20:19:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60655",
    "user": "https://github.com/nilesjohnson"
}
```

Hi,

I'd really like to use this, but I'm having trouble from the start . . . 


```
sage: a = animate([sin(x + float(k)) for k in srange(0,2*pi,0.7)], xmin=0, xmax=2*pi, figsize=[2,1])
sage: a.ogv()
Error: libtheora does not appear to be installed. Saving an
animation to a Ogg Theora file or displaying an animation requires the
libtheora spkg, so please install it and try again.

sage: install_package('libtheora')
Traceback (most recent call last):
ValueError: Package is already installed. Try install_package('libtheora',force=True)
```


I did install both `libogg` and `libtheora` using `install_package` in sage 4.5.2



---

archive/issue_comments_060656.json:
```json
{
    "body": "Replying to [comment:9 niles]:\n> Hi,\n> \n> I'd really like to use this, but I'm having trouble from the start . . . \n> \n> {{{\n> sage: a = animate([sin(x + float(k)) for k in srange(0,2*pi,0.7)], xmin=0, xmax=2*pi, figsize=[2,1])\n> sage: a.ogv()\n> Error: libtheora does not appear to be installed. Saving an\n> animation to a Ogg Theora file or displaying an animation requires the\n> libtheora spkg, so please install it and try again.\n> \n> sage: install_package('libtheora')\n> Traceback (most recent call last):\n> ValueError: Package is already installed. Try install_package('libtheora',force=True)\n> }}}\n> \n> I did install both `libogg` and `libtheora` using `install_package` in sage 4.5.2\n\nIf the two packages are installed correctly the 'png2theora' command line utility should\nbe in $SAGE_ROOT/local/bin.\n\nAnd\n\n```\nsage: !png2theora --help\n```\n\nshould give some output.",
    "created_at": "2010-09-08T08:20:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60656",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Replying to [comment:9 niles]:
> Hi,
> 
> I'd really like to use this, but I'm having trouble from the start . . . 
> 
> {{{
> sage: a = animate([sin(x + float(k)) for k in srange(0,2*pi,0.7)], xmin=0, xmax=2*pi, figsize=[2,1])
> sage: a.ogv()
> Error: libtheora does not appear to be installed. Saving an
> animation to a Ogg Theora file or displaying an animation requires the
> libtheora spkg, so please install it and try again.
> 
> sage: install_package('libtheora')
> Traceback (most recent call last):
> ValueError: Package is already installed. Try install_package('libtheora',force=True)
> }}}
> 
> I did install both `libogg` and `libtheora` using `install_package` in sage 4.5.2

If the two packages are installed correctly the 'png2theora' command line utility should
be in $SAGE_ROOT/local/bin.

And

```
sage: !png2theora --help
```

should give some output.



---

archive/issue_comments_060657.json:
```json
{
    "body": "Replying to [comment:10 whuss]:\n\nThanks for the reply; it seems that these are installed though:\n\n> If the two packages are installed correctly the 'png2theora' command line utility should\n> be in $SAGE_ROOT/local/bin.\n\nindeed:\n\n```\n$ which png2theora\n/Applications/sage/local/bin/png2theora\n```\n\n\n> \n> And\n>\n\n```\nsage: !png2theora --help\n```\n\n> should give some output.\n\n\n```\nsage: !png2theora --help\npng2theora 1.1\nUsage: png2theora [options] <input>\n\nThe input argument uses C printf format to represent a list of files,\n  i.e. file-%06d.png to look for files file000001.png to file9999999.png \n...\n```\n\n\nOther things I could check?",
    "created_at": "2010-09-08T11:42:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60657",
    "user": "https://github.com/nilesjohnson"
}
```

Replying to [comment:10 whuss]:

Thanks for the reply; it seems that these are installed though:

> If the two packages are installed correctly the 'png2theora' command line utility should
> be in $SAGE_ROOT/local/bin.

indeed:

```
$ which png2theora
/Applications/sage/local/bin/png2theora
```


> 
> And
>

```
sage: !png2theora --help
```

> should give some output.


```
sage: !png2theora --help
png2theora 1.1
Usage: png2theora [options] <input>

The input argument uses C printf format to represent a list of files,
  i.e. file-%06d.png to look for files file000001.png to file9999999.png 
...
```


Other things I could check?



---

archive/issue_comments_060658.json:
```json
{
    "body": "Replying to [comment:11 niles]:\n> Other things I could check?\n\nI don't know what the problem is. The code just creates a bunch of png files with the frames of\nthe animation and then calls 'png2theora' to convert it an ogv file.\n\nThe relevant code is at the lines 405-415 of sage/plot/animate.py. You can try to remove the\ntry/except block to see the real error message of check_call.",
    "created_at": "2010-09-08T13:30:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60658",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Replying to [comment:11 niles]:
> Other things I could check?

I don't know what the problem is. The code just creates a bunch of png files with the frames of
the animation and then calls 'png2theora' to convert it an ogv file.

The relevant code is at the lines 405-415 of sage/plot/animate.py. You can try to remove the
try/except block to see the real error message of check_call.



---

archive/issue_comments_060659.json:
```json
{
    "body": "Replying to [comment:12 whuss]:\n> Replying to [comment:11 niles]:\n> > Other things I could check?\n> \n> I don't know what the problem is. The code just creates a bunch of png files with the frames of\n> the animation and then calls 'png2theora' to convert it an ogv file.\n> \n> The relevant code is at the lines 405-415 of sage/plot/animate.py. You can try to remove the\n> try/except block to see the real error message of check_call.\n\nThanks; the problem seems to be that, for me, `check_call` needs to be called with a list of inputs -- giving the command as a single string fails for some reason (`png2theora` returns its usage message, so probably it is not receiving the arguments in the expected format):\n\n\n```\nsage: check_call([\"png2theora\", '-o \"tmp2.ogv\"', '%08d.png'])\n9 frames, 202x106\nCompressing....                                          \n./00000000.png\n./00000001.png\n./00000002.png\n./00000003.png\n./00000004.png\n./00000005.png\n./00000006.png\n./00000007.png\n./00000008.png\n   \ndone.\n\n0\n```\n\n\nbut \n\n```\nsage: check_call([\"png2theora\", '-o \"tmp2.ogv\" %08d.png'])\npng2theora 1.1\nUsage: png2theora [options] <input>\n...\n```\n\n\nand \n\n```\nsage: check_call('png2theora -o \"tmp3.ogv\" %08d.png')\n---------------------------------------------------------------------------\nOSError                                   Traceback (most recent call last)\n...\nOSError: [Errno 2] No such file or directory\n```\n\n\nThe last command is a simplified version of what appears in `sage/plot/animate.py` . . . does it really work for other people here?  And if so, why?",
    "created_at": "2010-09-08T15:35:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60659",
    "user": "https://github.com/nilesjohnson"
}
```

Replying to [comment:12 whuss]:
> Replying to [comment:11 niles]:
> > Other things I could check?
> 
> I don't know what the problem is. The code just creates a bunch of png files with the frames of
> the animation and then calls 'png2theora' to convert it an ogv file.
> 
> The relevant code is at the lines 405-415 of sage/plot/animate.py. You can try to remove the
> try/except block to see the real error message of check_call.

Thanks; the problem seems to be that, for me, `check_call` needs to be called with a list of inputs -- giving the command as a single string fails for some reason (`png2theora` returns its usage message, so probably it is not receiving the arguments in the expected format):


```
sage: check_call(["png2theora", '-o "tmp2.ogv"', '%08d.png'])
9 frames, 202x106
Compressing....                                          
./00000000.png
./00000001.png
./00000002.png
./00000003.png
./00000004.png
./00000005.png
./00000006.png
./00000007.png
./00000008.png
   
done.

0
```


but 

```
sage: check_call(["png2theora", '-o "tmp2.ogv" %08d.png'])
png2theora 1.1
Usage: png2theora [options] <input>
...
```


and 

```
sage: check_call('png2theora -o "tmp3.ogv" %08d.png')
---------------------------------------------------------------------------
OSError                                   Traceback (most recent call last)
...
OSError: [Errno 2] No such file or directory
```


The last command is a simplified version of what appears in `sage/plot/animate.py` . . . does it really work for other people here?  And if so, why?



---

archive/issue_comments_060660.json:
```json
{
    "body": "Apply trac-7298-ogv.patch\n\n(This comment is for [Patch Buildbot](http://wiki.sagemath.org/buildbot))",
    "created_at": "2010-12-04T16:44:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60660",
    "user": "https://github.com/nilesjohnson"
}
```

Apply trac-7298-ogv.patch

(This comment is for [Patch Buildbot](http://wiki.sagemath.org/buildbot))



---

archive/issue_comments_060661.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-12-04T17:49:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60661",
    "user": "https://github.com/nilesjohnson"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_060662.json:
```json
{
    "body": "Replying to [comment:13 niles]:\n> Replying to [comment:12 whuss]:\n> > Replying to [comment:11 niles]:\n\n> Thanks; the problem seems to be that, for me, `check_call` needs to be called with a list of inputs -- giving the command as a single string fails for some reason (`png2theora` returns its usage message, so probably it is not receiving the arguments in the expected format):\n> \n\n```\n sage: check_call([\"png2theora\", '-o \"tmp2.ogv\"', '%08d.png'])\n 9 frames, 202x106\n Compressing....                                          \n ./00000000.png\n ./00000001.png\n ./00000002.png\n ./00000003.png\n ./00000004.png\n ./00000005.png\n ./00000006.png\n ./00000007.png\n ./00000008.png\n    \n done.\n \n 0\n }}}\n> \n> but \n{{{\n sage: check_call([\"png2theora\", '-o \"tmp2.ogv\" %08d.png'])\n png2theora 1.1\n Usage: png2theora [options] <input>\n ...\n }}}\n> \n> and \n{{{\n sage: check_call('png2theora -o \"tmp3.ogv\" %08d.png')\n ---------------------------------------------------------------------------\n OSError                                   Traceback (most recent call last)\n ...\n OSError: [Errno 2] No such file or directory\n }}}\n> \n> The last command is a simplified version of what appears in `sage/plot/animate.py` . . . does it really work for other people here?  And if so, why?\n\n\nThis seems to be the offending code:\n\n{{{\n405\t        cmd = 'cd \"%s\"; sage-native-execute png2theora -o \"%s\" -f %s  %%08d.png 2> /dev/null'%(d, savefile, int(100/delay))\n406\t        from subprocess import check_call, CalledProcessError\n407\t        try: \n408\t            check_call(cmd, shell=True) \n}}}\n\nI'm switching this to \"needs work\", since I think ``cmd`` needs to be a list of strings rather than a single string (see above).",
    "created_at": "2010-12-04T17:49:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60662",
    "user": "https://github.com/nilesjohnson"
}
```

Replying to [comment:13 niles]:
> Replying to [comment:12 whuss]:
> > Replying to [comment:11 niles]:

> Thanks; the problem seems to be that, for me, `check_call` needs to be called with a list of inputs -- giving the command as a single string fails for some reason (`png2theora` returns its usage message, so probably it is not receiving the arguments in the expected format):
> 

```
 sage: check_call(["png2theora", '-o "tmp2.ogv"', '%08d.png'])
 9 frames, 202x106
 Compressing....                                          
 ./00000000.png
 ./00000001.png
 ./00000002.png
 ./00000003.png
 ./00000004.png
 ./00000005.png
 ./00000006.png
 ./00000007.png
 ./00000008.png
    
 done.
 
 0
 }}}
> 
> but 
{{{
 sage: check_call(["png2theora", '-o "tmp2.ogv" %08d.png'])
 png2theora 1.1
 Usage: png2theora [options] <input>
 ...
 }}}
> 
> and 
{{{
 sage: check_call('png2theora -o "tmp3.ogv" %08d.png')
 ---------------------------------------------------------------------------
 OSError                                   Traceback (most recent call last)
 ...
 OSError: [Errno 2] No such file or directory
 }}}
> 
> The last command is a simplified version of what appears in `sage/plot/animate.py` . . . does it really work for other people here?  And if so, why?


This seems to be the offending code:

{{{
405	        cmd = 'cd "%s"; sage-native-execute png2theora -o "%s" -f %s  %%08d.png 2> /dev/null'%(d, savefile, int(100/delay))
406	        from subprocess import check_call, CalledProcessError
407	        try: 
408	            check_call(cmd, shell=True) 
}}}

I'm switching this to "needs work", since I think ``cmd`` needs to be a list of strings rather than a single string (see above).



---

archive/issue_comments_060663.json:
```json
{
    "body": "I tried working on this again, but now I'm having trouble installing the `libtheora` spkg with sage 4.6.  For what it's worth, installing `libogg` went fine.  Is this a known issue?\n\nThe last lines of the failing install (before the timing and other end messages) are:\n\n\n```\n...\nmake[2]: Nothing to be done for `install-data-am'.\nmake[2]: Nothing to be done for `install-exec-am'.\n/bin/sh ./mkinstalldirs /Applications/sage/local/lib/pkgconfig\n /usr/bin/install -c -m 644 theora.pc /Applications/sage/local/lib/pkgconfig/theora.pc\n /usr/bin/install -c -m 644 theoradec.pc /Applications/sage/local/lib/pkgconfig/theoradec.pc\n /usr/bin/install -c -m 644 theoraenc.pc /Applications/sage/local/lib/pkgconfig/theoraenc.pc\ncp: examples/.libs/png2theora: No such file or directory\n```\n",
    "created_at": "2011-01-10T21:41:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60663",
    "user": "https://github.com/nilesjohnson"
}
```

I tried working on this again, but now I'm having trouble installing the `libtheora` spkg with sage 4.6.  For what it's worth, installing `libogg` went fine.  Is this a known issue?

The last lines of the failing install (before the timing and other end messages) are:


```
...
make[2]: Nothing to be done for `install-data-am'.
make[2]: Nothing to be done for `install-exec-am'.
/bin/sh ./mkinstalldirs /Applications/sage/local/lib/pkgconfig
 /usr/bin/install -c -m 644 theora.pc /Applications/sage/local/lib/pkgconfig/theora.pc
 /usr/bin/install -c -m 644 theoradec.pc /Applications/sage/local/lib/pkgconfig/theoradec.pc
 /usr/bin/install -c -m 644 theoraenc.pc /Applications/sage/local/lib/pkgconfig/theoraenc.pc
cp: examples/.libs/png2theora: No such file or directory
```




---

archive/issue_comments_060664.json:
```json
{
    "body": "Replying to [comment:17 niles]:\n> I tried working on this again, but now I'm having trouble installing the `libtheora` spkg with sage 4.6.  For what it's worth, installing `libogg` went fine.  Is this a known issue?\n\nI just tried to install libtheora on sage-4.6.2 (Debian 64bit), and it worked without problems.\n\n> The last lines of the failing install (before the timing and other end messages) are:\n> \n> {{{\n> ...\n> make[2]: Nothing to be done for `install-data-am'.\n> make[2]: Nothing to be done for `install-exec-am'.\n> /bin/sh ./mkinstalldirs /Applications/sage/local/lib/pkgconfig\n>  /usr/bin/install -c -m 644 theora.pc /Applications/sage/local/lib/pkgconfig/theora.pc\n>  /usr/bin/install -c -m 644 theoradec.pc /Applications/sage/local/lib/pkgconfig/theoradec.pc\n>  /usr/bin/install -c -m 644 theoraenc.pc /Applications/sage/local/lib/pkgconfig/theoraenc.pc\n> cp: examples/.libs/png2theora: No such file or directory\n> }}}\n\npng2theora is one of the example programs included in libtheora and it is used by this patch\nto generate the ogv videos. This line means that it failed to build. Besides libtheora itself\nits only dependency is libpng. Did you get the line\n\n\n```\nchecking for PNG... yes\n```\n\n\nin the configure log?\nWhich platform are you using?",
    "created_at": "2011-03-07T11:27:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60664",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Replying to [comment:17 niles]:
> I tried working on this again, but now I'm having trouble installing the `libtheora` spkg with sage 4.6.  For what it's worth, installing `libogg` went fine.  Is this a known issue?

I just tried to install libtheora on sage-4.6.2 (Debian 64bit), and it worked without problems.

> The last lines of the failing install (before the timing and other end messages) are:
> 
> {{{
> ...
> make[2]: Nothing to be done for `install-data-am'.
> make[2]: Nothing to be done for `install-exec-am'.
> /bin/sh ./mkinstalldirs /Applications/sage/local/lib/pkgconfig
>  /usr/bin/install -c -m 644 theora.pc /Applications/sage/local/lib/pkgconfig/theora.pc
>  /usr/bin/install -c -m 644 theoradec.pc /Applications/sage/local/lib/pkgconfig/theoradec.pc
>  /usr/bin/install -c -m 644 theoraenc.pc /Applications/sage/local/lib/pkgconfig/theoraenc.pc
> cp: examples/.libs/png2theora: No such file or directory
> }}}

png2theora is one of the example programs included in libtheora and it is used by this patch
to generate the ogv videos. This line means that it failed to build. Besides libtheora itself
its only dependency is libpng. Did you get the line


```
checking for PNG... yes
```


in the configure log?
Which platform are you using?



---

archive/issue_comments_060665.json:
```json
{
    "body": "Replying to [comment:18 whuss]:\n> \n\n```\n checking for PNG... yes\n }}}\n\nAh, I got \n{{{\nchecking for PNG... no\n}}}\n\nI'm using Mac OS 10.6.6.  Since I made my last post above, I have downloaded libtheora directly from their website and compiled png2theora successfully outside of Sage.  I just retried installing from within Sage, and it still cannot find libpng, and still fails to build png2theora . . .\n\nSo the fix probably has to do with telling Sage how to accurately find libpng; is that right?",
    "created_at": "2011-03-07T13:05:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60665",
    "user": "https://github.com/nilesjohnson"
}
```

Replying to [comment:18 whuss]:
> 

```
 checking for PNG... yes
 }}}

Ah, I got 
{{{
checking for PNG... no
}}}

I'm using Mac OS 10.6.6.  Since I made my last post above, I have downloaded libtheora directly from their website and compiled png2theora successfully outside of Sage.  I just retried installing from within Sage, and it still cannot find libpng, and still fails to build png2theora . . .

So the fix probably has to do with telling Sage how to accurately find libpng; is that right?



---

archive/issue_comments_060666.json:
```json
{
    "body": "Replying to [comment:19 niles]:\n> Replying to [comment:18 whuss]:\n> > \n> {{{\n>  checking for PNG... yes\n>  }}}\n> \n> Ah, I got \n> {{{\n> checking for PNG... no\n> }}}\n> \n> I'm using Mac OS 10.6.6.  Since I made my last post above, I have downloaded libtheora directly from their website and compiled png2theora successfully outside of Sage.  I just retried installing from within Sage, and it still cannot find libpng, and still fails to build png2theora . . .\n> \n> So the fix probably has to do with telling Sage how to accurately find libpng; is that right?\n\nYes. I have never developed on Mac OS, so I don't really know how to fix it. This is the autoconf\ncheck, used by libtheora to test for libpng:\n\n\n```\ndnl check for libpng\nHAVE_PNG=no\nif test \"x$HAVE_PKG_CONFIG\" = \"xyes\"\nthen\n  PKG_CHECK_MODULES(PNG, libpng, HAVE_PNG=yes, HAVE_PNG=no)\nfi\nAC_SUBST(PNG_CFLAGS)\nAC_SUBST(PNG_LIBS)\n```\n\n\nIt is very simple, and since the original source builds for you, this should also work on Mac OS.\n\nMaybe one could hard code the variables PNG_CFLAGS and PNG_LIBS in spkg-install, but there should be a better solution.",
    "created_at": "2011-03-07T14:33:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60666",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Replying to [comment:19 niles]:
> Replying to [comment:18 whuss]:
> > 
> {{{
>  checking for PNG... yes
>  }}}
> 
> Ah, I got 
> {{{
> checking for PNG... no
> }}}
> 
> I'm using Mac OS 10.6.6.  Since I made my last post above, I have downloaded libtheora directly from their website and compiled png2theora successfully outside of Sage.  I just retried installing from within Sage, and it still cannot find libpng, and still fails to build png2theora . . .
> 
> So the fix probably has to do with telling Sage how to accurately find libpng; is that right?

Yes. I have never developed on Mac OS, so I don't really know how to fix it. This is the autoconf
check, used by libtheora to test for libpng:


```
dnl check for libpng
HAVE_PNG=no
if test "x$HAVE_PKG_CONFIG" = "xyes"
then
  PKG_CHECK_MODULES(PNG, libpng, HAVE_PNG=yes, HAVE_PNG=no)
fi
AC_SUBST(PNG_CFLAGS)
AC_SUBST(PNG_LIBS)
```


It is very simple, and since the original source builds for you, this should also work on Mac OS.

Maybe one could hard code the variables PNG_CFLAGS and PNG_LIBS in spkg-install, but there should be a better solution.



---

archive/issue_comments_060667.json:
```json
{
    "body": "I believe that we ship libpng, so it's weird that it didn't find it.\n\nI know in matplotlib, though, on OSX, we look for libpng12.  It seems that a long time ago, we kept picking up the wrong libpng on OSX, so now we look for libpng12.  I believe the problem has been fixed since then, but the \"fix\" for matplotlib is still in the spkg.",
    "created_at": "2011-03-07T16:10:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60667",
    "user": "https://github.com/jasongrout"
}
```

I believe that we ship libpng, so it's weird that it didn't find it.

I know in matplotlib, though, on OSX, we look for libpng12.  It seems that a long time ago, we kept picking up the wrong libpng on OSX, so now we look for libpng12.  I believe the problem has been fixed since then, but the "fix" for matplotlib is still in the spkg.



---

archive/issue_comments_060668.json:
```json
{
    "body": "Replying to [comment:21 jason]:\n> I believe that we ship libpng, so it's weird that it didn't find it.\n> \n> I know in matplotlib, though, on OSX, we look for libpng12.  It seems that a long time ago, we kept picking up the wrong libpng on OSX, so now we look for libpng12.  I believe the problem has been fixed since then, but the \"fix\" for matplotlib is still in the spkg.\n\nI created a new spkg for libtheora, which checks for libpng12.\n\n[http://www.math.tugraz.at/~huss/spkg/libtheora-1.1.1.p1.spkg](http://www.math.tugraz.at/~huss/spkg/libtheora-1.1.1.p1.spkg)\n\nIt still works for me. Could someone test it on OSX?",
    "created_at": "2011-03-07T17:11:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60668",
    "user": "https://trac.sagemath.org/admin/accounts/users/whuss"
}
```

Replying to [comment:21 jason]:
> I believe that we ship libpng, so it's weird that it didn't find it.
> 
> I know in matplotlib, though, on OSX, we look for libpng12.  It seems that a long time ago, we kept picking up the wrong libpng on OSX, so now we look for libpng12.  I believe the problem has been fixed since then, but the "fix" for matplotlib is still in the spkg.

I created a new spkg for libtheora, which checks for libpng12.

[http://www.math.tugraz.at/~huss/spkg/libtheora-1.1.1.p1.spkg](http://www.math.tugraz.at/~huss/spkg/libtheora-1.1.1.p1.spkg)

It still works for me. Could someone test it on OSX?



---

archive/issue_comments_060669.json:
```json
{
    "body": "log file of failing install in Mac 10.6",
    "created_at": "2011-03-07T19:06:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60669",
    "user": "https://github.com/nilesjohnson"
}
```

log file of failing install in Mac 10.6



---

archive/issue_comments_060670.json:
```json
{
    "body": "Attachment [libtheora_Mac-10.6.log](tarball://root/attachments/some-uuid/ticket7298/libtheora_Mac-10.6.log) by @nilesjohnson created at 2011-03-07 19:08:54\n\nReplying to [comment:22 whuss]:\n> It still works for me. Could someone test it on OSX?\n> \n\nI'm afraid it's still failing for me--PNG is still not found.  Here is the complete [attachment:libtheora_Mac-10.6.log log file].",
    "created_at": "2011-03-07T19:08:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60670",
    "user": "https://github.com/nilesjohnson"
}
```

Attachment [libtheora_Mac-10.6.log](tarball://root/attachments/some-uuid/ticket7298/libtheora_Mac-10.6.log) by @nilesjohnson created at 2011-03-07 19:08:54

Replying to [comment:22 whuss]:
> It still works for me. Could someone test it on OSX?
> 

I'm afraid it's still failing for me--PNG is still not found.  Here is the complete [attachment:libtheora_Mac-10.6.log log file].



---

archive/issue_comments_060671.json:
```json
{
    "body": "I don't know autoconf.  What exactly does ` PKG_CHECK_MODULES(PNG, libpng, HAVE_PNG=yes, HAVE_PNG=no)` do?  I think it's looking in `$SAGE_ROOT/local/lib/pkgconfig`, and you should have a libpng12.pc and a libpng.pc file in there.  How exactly does PKG_CHECK_MODULES determine if libpng is installed?",
    "created_at": "2011-03-07T21:06:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60671",
    "user": "https://github.com/jasongrout"
}
```

I don't know autoconf.  What exactly does ` PKG_CHECK_MODULES(PNG, libpng, HAVE_PNG=yes, HAVE_PNG=no)` do?  I think it's looking in `$SAGE_ROOT/local/lib/pkgconfig`, and you should have a libpng12.pc and a libpng.pc file in there.  How exactly does PKG_CHECK_MODULES determine if libpng is installed?



---

archive/issue_comments_060672.json:
```json
{
    "body": "Replying to [comment:24 jason]:\n> I don't know autoconf.  What exactly does ` PKG_CHECK_MODULES(PNG, libpng, HAVE_PNG=yes, HAVE_PNG=no)` do?  I think it's looking in `$SAGE_ROOT/local/lib/pkgconfig`, and you should have a libpng12.pc and a libpng.pc file in there.  How exactly does PKG_CHECK_MODULES determine if libpng is installed?\n\nwell, I don't know any of this :)  But I do indeed have libpng12.pc and libpng.pc in `$SAGE_ROOT/local/lib/pkgconfig`",
    "created_at": "2011-03-07T21:36:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60672",
    "user": "https://github.com/nilesjohnson"
}
```

Replying to [comment:24 jason]:
> I don't know autoconf.  What exactly does ` PKG_CHECK_MODULES(PNG, libpng, HAVE_PNG=yes, HAVE_PNG=no)` do?  I think it's looking in `$SAGE_ROOT/local/lib/pkgconfig`, and you should have a libpng12.pc and a libpng.pc file in there.  How exactly does PKG_CHECK_MODULES determine if libpng is installed?

well, I don't know any of this :)  But I do indeed have libpng12.pc and libpng.pc in `$SAGE_ROOT/local/lib/pkgconfig`



---

archive/issue_comments_060673.json:
```json
{
    "body": "I tried installing on my mac, and I'm having a different problem.  First I did `sage -i libogg`, and this seems to have worked.  When I run `sage -i libtheora` or when I download and install the new spkg listed by whuss, I get these errors in the log file:\n\n```\nchecking for Vorbis... no\n*** Could not run Vorbis test program, checking why...\n*** The test program failed to compile or link. See the file config.log for the\n*** exact error that occured. This usually means Vorbis was incorrectly installed\n*** or that you have moved Vorbis since it was installed.\n```\n\nand\n\n```\n*** The sdl-config script installed by SDL could not be found\n*** If SDL was installed in PREFIX, make sure PREFIX/bin is in\n*** your path, or set the SDL_CONFIG environment variable to the\n*** full path to sdl-config.\nconfigure: WARNING: *** Unable to find SDL -- Not compiling example players ***\n```\n\nIt doesn't even check whether png is installed.",
    "created_at": "2011-03-07T21:37:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60673",
    "user": "https://github.com/jhpalmieri"
}
```

I tried installing on my mac, and I'm having a different problem.  First I did `sage -i libogg`, and this seems to have worked.  When I run `sage -i libtheora` or when I download and install the new spkg listed by whuss, I get these errors in the log file:

```
checking for Vorbis... no
*** Could not run Vorbis test program, checking why...
*** The test program failed to compile or link. See the file config.log for the
*** exact error that occured. This usually means Vorbis was incorrectly installed
*** or that you have moved Vorbis since it was installed.
```

and

```
*** The sdl-config script installed by SDL could not be found
*** If SDL was installed in PREFIX, make sure PREFIX/bin is in
*** your path, or set the SDL_CONFIG environment variable to the
*** full path to sdl-config.
configure: WARNING: *** Unable to find SDL -- Not compiling example players ***
```

It doesn't even check whether png is installed.



---

archive/issue_comments_060674.json:
```json
{
    "body": "I also notice that in config.log it says\n\n```\nHAVE_PKG_CONFIG=''\n```\n\nWould that explain why it was skipping the png test?",
    "created_at": "2011-03-07T21:50:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60674",
    "user": "https://github.com/jhpalmieri"
}
```

I also notice that in config.log it says

```
HAVE_PKG_CONFIG=''
```

Would that explain why it was skipping the png test?



---

archive/issue_comments_060675.json:
```json
{
    "body": "I think this patch is largely superseded by #11170, which provides an `ffmpeg` option for creating animations; by installing ffmpeg, you can create videos in Theora format, which makes the spkgs and patch here unnecessary. Also, ffmpeg supports far more formats, which makes it a more flexible solution.\n\nPerhaps the focus here should be on changing the notebook so that animations are automatically displayed, much like images and animated GIFs are now. I would love to be able to create Theora or WebM videos with the `animate()` command and have them automatically displayed.",
    "created_at": "2011-05-02T07:23:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60675",
    "user": "https://github.com/dandrake"
}
```

I think this patch is largely superseded by #11170, which provides an `ffmpeg` option for creating animations; by installing ffmpeg, you can create videos in Theora format, which makes the spkgs and patch here unnecessary. Also, ffmpeg supports far more formats, which makes it a more flexible solution.

Perhaps the focus here should be on changing the notebook so that animations are automatically displayed, much like images and animated GIFs are now. I would love to be able to create Theora or WebM videos with the `animate()` command and have them automatically displayed.



---

archive/issue_comments_060676.json:
```json
{
    "body": "Replying to [comment:28 ddrake]:\n> I think this patch is largely superseded by #11170, which provides an `ffmpeg` option for creating animations; by installing ffmpeg, you can create videos in Theora format, which makes the spkgs and patch here unnecessary. Also, ffmpeg supports far more formats, which makes it a more flexible solution.\n\nThere is perhaps also the subtlety of patent and license issues -- there seem to be more severe limitations on the ways ffmpeg can be distributed, while png2theora is licensed under a relatively free BSD-style license . . . thus png2theora could conceivably be included with sage at some point, while ffmpeg is harder to imagine.\n\nIn any case, the patch at #11170 is quite useful, and doesn't suffer from the Mac-specific problems mentioned above.",
    "created_at": "2011-05-02T15:02:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60676",
    "user": "https://github.com/nilesjohnson"
}
```

Replying to [comment:28 ddrake]:
> I think this patch is largely superseded by #11170, which provides an `ffmpeg` option for creating animations; by installing ffmpeg, you can create videos in Theora format, which makes the spkgs and patch here unnecessary. Also, ffmpeg supports far more formats, which makes it a more flexible solution.

There is perhaps also the subtlety of patent and license issues -- there seem to be more severe limitations on the ways ffmpeg can be distributed, while png2theora is licensed under a relatively free BSD-style license . . . thus png2theora could conceivably be included with sage at some point, while ffmpeg is harder to imagine.

In any case, the patch at #11170 is quite useful, and doesn't suffer from the Mac-specific problems mentioned above.



---

archive/issue_comments_060677.json:
```json
{
    "body": "Replying to [comment:29 niles]:\n> There is perhaps also the subtlety of patent and license issues -- there seem to be more severe limitations on the ways ffmpeg can be distributed\n\nCan you clarify this? I've seen this claim elsewhere, but I'm not sure what it means.  On the [ffmpeg web page](http://www.ffmpeg.org/) it says that it is distributed under LGPL or GPL, depending on what components are being used, and this wouldn't put any extra restrictions on us.  I guess the very last question on [this page](http://www.ffmpeg.org/legal.html) might be an issue, but it's not very clear to me.",
    "created_at": "2011-05-02T16:16:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60677",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:29 niles]:
> There is perhaps also the subtlety of patent and license issues -- there seem to be more severe limitations on the ways ffmpeg can be distributed

Can you clarify this? I've seen this claim elsewhere, but I'm not sure what it means.  On the [ffmpeg web page](http://www.ffmpeg.org/) it says that it is distributed under LGPL or GPL, depending on what components are being used, and this wouldn't put any extra restrictions on us.  I guess the very last question on [this page](http://www.ffmpeg.org/legal.html) might be an issue, but it's not very clear to me.



---

archive/issue_comments_060678.json:
```json
{
    "body": "Replying to [comment:30 jhpalmieri]:\n> Replying to [comment:29 niles]:\n\n> Can you clarify this? \n\nUnfortunately no, I don't really understand the issues involved here.  I just wanted to note that there do seem to be legal issues.\n\nBut you are right that ffmpeg itself seems intended to be free.  The question (I think) is whether it infringes unintentionally on some patents (notably mpeg), but it may be that the answer to this question has implications only for commercial products.  That question (whether or not mpeg patent infringement by ffmpeg might have real consequences for sage) would have to be sorted out before ffmpeg could be included.",
    "created_at": "2011-05-02T20:51:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60678",
    "user": "https://github.com/nilesjohnson"
}
```

Replying to [comment:30 jhpalmieri]:
> Replying to [comment:29 niles]:

> Can you clarify this? 

Unfortunately no, I don't really understand the issues involved here.  I just wanted to note that there do seem to be legal issues.

But you are right that ffmpeg itself seems intended to be free.  The question (I think) is whether it infringes unintentionally on some patents (notably mpeg), but it may be that the answer to this question has implications only for commercial products.  That question (whether or not mpeg patent infringement by ffmpeg might have real consequences for sage) would have to be sorted out before ffmpeg could be included.



---

archive/issue_comments_060679.json:
```json
{
    "body": "Replying to [comment:28 ddrake]:\n> Perhaps the focus here should be on changing the notebook so that animations are automatically displayed, much like images and animated GIFs are now. I would love to be able to create Theora or WebM videos with the `animate()` command and have them automatically displayed.\n\nSee #16533 for a branch which does add the video tag, backed by ffmpeg. It also restores animation embedding in general, which appears to be broken at the moment, and it adds support for APNG as well.",
    "created_at": "2014-06-26T07:48:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60679",
    "user": "https://github.com/gagern"
}
```

Replying to [comment:28 ddrake]:
> Perhaps the focus here should be on changing the notebook so that animations are automatically displayed, much like images and animated GIFs are now. I would love to be able to create Theora or WebM videos with the `animate()` command and have them automatically displayed.

See #16533 for a branch which does add the video tag, backed by ffmpeg. It also restores animation embedding in general, which appears to be broken at the moment, and it adds support for APNG as well.



---

archive/issue_comments_060680.json:
```json
{
    "body": "I hope I'm not stepping on anybodies toes by commandeering this ticket here to carry my branch. And I hope I'm doing it the right way.\n\nThat branch is my <video> tag implementation, building on code from #16533. Once that is accepted, the modification to add the video tag is pretty small, and mostly involves some mime type fiddling.\n\nI kept the table embedding stuff in there, since Wilfried Huss had it in his patch, and it seemed like a good idea but probably not worth a ticket all by itself.\n----\nNew commits:",
    "created_at": "2014-06-27T18:57:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60680",
    "user": "https://github.com/gagern"
}
```

I hope I'm not stepping on anybodies toes by commandeering this ticket here to carry my branch. And I hope I'm doing it the right way.

That branch is my <video> tag implementation, building on code from #16533. Once that is accepted, the modification to add the video tag is pretty small, and mostly involves some mime type fiddling.

I kept the table embedding stuff in there, since Wilfried Huss had it in his patch, and it seemed like a good idea but probably not worth a ticket all by itself.
----
New commits:



---

archive/issue_comments_060681.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-06-27T18:57:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60681",
    "user": "https://github.com/gagern"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060682.json:
```json
{
    "body": "Replying to [comment:37 gagern]:\n> I hope I'm not stepping on anybodies toes by commandeering this ticket here to carry my branch. And I hope I'm doing it the right way.\n\nWell, it's been 3 years since the last activity here, I'm just happy that someone is paying attention to it again :)",
    "created_at": "2014-06-27T20:19:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60682",
    "user": "https://github.com/nilesjohnson"
}
```

Replying to [comment:37 gagern]:
> I hope I'm not stepping on anybodies toes by commandeering this ticket here to carry my branch. And I hope I'm doing it the right way.

Well, it's been 3 years since the last activity here, I'm just happy that someone is paying attention to it again :)



---

archive/issue_comments_060683.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2014-07-11T21:25:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60683",
    "user": "https://github.com/gagern"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_060684.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2014-07-12T15:41:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60684",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_060685.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2014-07-12T15:48:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60685",
    "user": "https://github.com/gagern"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060686.json:
```json
{
    "body": "OK, I rebased this on my recent work on various other tickets, culminating in #16645. [\u200bThese are the changes](http://git.sagemath.org/sage.git/diff/?h=u/gagern/ticket/7298&id2=bb7307f0649cfa90916f74c102d1d09a424b759a) that need reviewing in this ticket here.",
    "created_at": "2014-07-12T15:48:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60686",
    "user": "https://github.com/gagern"
}
```

OK, I rebased this on my recent work on various other tickets, culminating in #16645. [​These are the changes](http://git.sagemath.org/sage.git/diff/?h=u/gagern/ticket/7298&id2=bb7307f0649cfa90916f74c102d1d09a424b759a) that need reviewing in this ticket here.



---

archive/issue_comments_060687.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-07-15T13:20:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60687",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_060688.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-09-02T21:17:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60688",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_060689.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2014-12-16T22:32:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60689",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_060690.json:
```json
{
    "body": "Changing description to reflect what this is currently about.",
    "created_at": "2015-01-06T19:26:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60690",
    "user": "https://github.com/gagern"
}
```

Changing description to reflect what this is currently about.



---

archive/issue_comments_060691.json:
```json
{
    "body": "The recent changes from #17234 interfere heavily with my work here.\n\nI'm working on a rebase just now (which is somewhat annoying, considering that this ticket is waiting for review for 9 months now, and this is the third time I have to rebase it). But in some points I'm not certain how to integrate my goals with what #17234 did. For video, there are different formats to choose from, no single format will satisfy everybody, so I needed some flexibility there. On the other hand, almost all the different formats are the result of passing some PNG frames through ffmpeg, providing a suitable file name for the output, and then writing a HTML tag to embed that file. So all I need to know about a video format is a file name extension which ffmpeg will recognize and a mime type which the browser will recognize. I can even obtain one of these from the other using `mimetypes.guess_extension` resp. `mimetypes.guess_type`.\n\nNow #17234 introduced the rich output type catalog, using yet another way to name types, and as far as I can see at the moment without hookups to either file name extensions or mime types. But what seems worse to me is that this catalog is an  explicit list of allowed types, with no obvious room for extension at runtime.\n\n* Should I restrict users to e.g. Theora and WebM as video formats?\n* Should I add some `OutputAnyVideo` class to catch all cases?\n* Should I dynamically create new classes, one for every user-requested format?\n* How about support for more than one format, should we introduce a type which generates a bunch of common video formats (e.g. again Theora and WebM) to plug them into a single `<video>` tag so the browser can pick what he likes best, at the cost of increased conversion time?\n\nJudging from e.g. the handling of LaTeX output, it looks as if I could simply generate HTML and have that recognized by the notebooks. I hope that's the case. I'll have to look whether embedding animations into tables still makes sense, but I hope it does.",
    "created_at": "2015-03-12T00:57:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60691",
    "user": "https://github.com/gagern"
}
```

The recent changes from #17234 interfere heavily with my work here.

I'm working on a rebase just now (which is somewhat annoying, considering that this ticket is waiting for review for 9 months now, and this is the third time I have to rebase it). But in some points I'm not certain how to integrate my goals with what #17234 did. For video, there are different formats to choose from, no single format will satisfy everybody, so I needed some flexibility there. On the other hand, almost all the different formats are the result of passing some PNG frames through ffmpeg, providing a suitable file name for the output, and then writing a HTML tag to embed that file. So all I need to know about a video format is a file name extension which ffmpeg will recognize and a mime type which the browser will recognize. I can even obtain one of these from the other using `mimetypes.guess_extension` resp. `mimetypes.guess_type`.

Now #17234 introduced the rich output type catalog, using yet another way to name types, and as far as I can see at the moment without hookups to either file name extensions or mime types. But what seems worse to me is that this catalog is an  explicit list of allowed types, with no obvious room for extension at runtime.

* Should I restrict users to e.g. Theora and WebM as video formats?
* Should I add some `OutputAnyVideo` class to catch all cases?
* Should I dynamically create new classes, one for every user-requested format?
* How about support for more than one format, should we introduce a type which generates a bunch of common video formats (e.g. again Theora and WebM) to plug them into a single `<video>` tag so the browser can pick what he likes best, at the cost of increased conversion time?

Judging from e.g. the handling of LaTeX output, it looks as if I could simply generate HTML and have that recognized by the notebooks. I hope that's the case. I'll have to look whether embedding animations into tables still makes sense, but I hope it does.



---

archive/issue_comments_060692.json:
```json
{
    "body": "I saw that the 2d animations are currently not in shaped and opened #17783, I didn't find your ticket.\n\nThe display backend (SageNB, IPython notebook, ...) declares which types it can display, and Sage then returns one (or None) of the supported types from `_rich_repr_`. There is no need for mime types (they are a bad fit for this problem anyways, whats the mime type for a sequence-of-pngs animation?). That is the only sane way to support multiple display backends, separation of concerns.",
    "created_at": "2015-03-12T09:11:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60692",
    "user": "https://github.com/vbraun"
}
```

I saw that the 2d animations are currently not in shaped and opened #17783, I didn't find your ticket.

The display backend (SageNB, IPython notebook, ...) declares which types it can display, and Sage then returns one (or None) of the supported types from `_rich_repr_`. There is no need for mime types (they are a bad fit for this problem anyways, whats the mime type for a sequence-of-pngs animation?). That is the only sane way to support multiple display backends, separation of concerns.



---

archive/issue_comments_060693.json:
```json
{
    "body": "I think the whole premise of \"showing animations in a certain format\" is misguided. Users care either about\n* actually seeing the animation play, or\n* saving an animation in a particular format to be used elsewhere.\nBut \"showing in a particular format\" is just bad UX, you are designing around technical abilities instead of what a user might want. This could also be said about the `viewer=...` argument for 3-d plots, but there we really don't have a truly good option so we need to give the user a way to choose between the devil and the deep sea. But GIF/APNG/Webm animations presumably all look the same to a human, so there is no point to expose those details when showing an animation.",
    "created_at": "2015-03-12T20:00:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60693",
    "user": "https://github.com/vbraun"
}
```

I think the whole premise of "showing animations in a certain format" is misguided. Users care either about
* actually seeing the animation play, or
* saving an animation in a particular format to be used elsewhere.
But "showing in a particular format" is just bad UX, you are designing around technical abilities instead of what a user might want. This could also be said about the `viewer=...` argument for 3-d plots, but there we really don't have a truly good option so we need to give the user a way to choose between the devil and the deep sea. But GIF/APNG/Webm animations presumably all look the same to a human, so there is no point to expose those details when showing an animation.



---

archive/issue_comments_060694.json:
```json
{
    "body": "Replying to [comment:50 vbraun]:\n> GIF/APNG/Webm animations presumably all look the same to a human\n\nI *very strongly* disagree. Animations involving gradients, e.g. from 3D scenes, tend to look *horrible* in 255 color GIF. Animations with few frames and lots of change in between (like e.g. the first example from the animate docs) look *horrible* as video, due to heavy compression artifacts.\n\nAPNG looks as good as things can get, since we create everything else from a bunch of PNG frames and this is a lossless method. But for lengthy animations it might simply be too big to be feasible to transfer this. After all, my APNG assembler makes no effort to compress things using clever frame disposal combinations. It simply concatenates files, more or less.\n\nDo I need to bundle up a few examples to support these claims, or will you accept my word or your own observations for this?\n\n> Users care either about [\u2026] saving an animation in a particular format to be used elsewhere.\n\nThe easiest way to do this, in my book, is have the animation show up in my notebook, then right-click and save to file. That works for cloud sessions as well as for local sessions as well as for sessions using some notebook server in my LAN. And I can always look at the animation first, make sure it looks the way I want it to, *then* save it to a local file once I'm satisfied. So the distinction between \u201cview\u201d and \u201csave\u201d is not as sharp as you claim.",
    "created_at": "2015-03-12T20:50:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60694",
    "user": "https://github.com/gagern"
}
```

Replying to [comment:50 vbraun]:
> GIF/APNG/Webm animations presumably all look the same to a human

I *very strongly* disagree. Animations involving gradients, e.g. from 3D scenes, tend to look *horrible* in 255 color GIF. Animations with few frames and lots of change in between (like e.g. the first example from the animate docs) look *horrible* as video, due to heavy compression artifacts.

APNG looks as good as things can get, since we create everything else from a bunch of PNG frames and this is a lossless method. But for lengthy animations it might simply be too big to be feasible to transfer this. After all, my APNG assembler makes no effort to compress things using clever frame disposal combinations. It simply concatenates files, more or less.

Do I need to bundle up a few examples to support these claims, or will you accept my word or your own observations for this?

> Users care either about […] saving an animation in a particular format to be used elsewhere.

The easiest way to do this, in my book, is have the animation show up in my notebook, then right-click and save to file. That works for cloud sessions as well as for local sessions as well as for sessions using some notebook server in my LAN. And I can always look at the animation first, make sure it looks the way I want it to, *then* save it to a local file once I'm satisfied. So the distinction between “view” and “save” is not as sharp as you claim.



---

archive/issue_comments_060695.json:
```json
{
    "body": "The IPython notebook doesn't support GIF/Webm and the browser probably not APNG, so what is this rightclick-save going to do? Nothing. Maybe save a single frame from the canvas where some javascript is paying the animation. Does not work.",
    "created_at": "2015-03-12T20:55:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60695",
    "user": "https://github.com/vbraun"
}
```

The IPython notebook doesn't support GIF/Webm and the browser probably not APNG, so what is this rightclick-save going to do? Nothing. Maybe save a single frame from the canvas where some javascript is paying the animation. Does not work.



---

archive/issue_comments_060696.json:
```json
{
    "body": "Distinguishing between lossy / lossless compression for graphics is reasonable, and doesn't require the user to know what webm&apng is. This is similar to preferring vector or raster graphics for 2-d plots. In #17234 I introduced a preference system for rich output, e.g.\n\n```\nsage: %display graphics vector\nsage: plot(sin)\n```\n\nwill prefer vector graphics formats when displaying the plot. This should probably be extended to cover lossy vs. lossless.",
    "created_at": "2015-03-12T21:04:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60696",
    "user": "https://github.com/vbraun"
}
```

Distinguishing between lossy / lossless compression for graphics is reasonable, and doesn't require the user to know what webm&apng is. This is similar to preferring vector or raster graphics for 2-d plots. In #17234 I introduced a preference system for rich output, e.g.

```
sage: %display graphics vector
sage: plot(sin)
```

will prefer vector graphics formats when displaying the plot. This should probably be extended to cover lossy vs. lossless.



---

archive/issue_comments_060697.json:
```json
{
    "body": "Replying to [comment:52 vbraun]:\n> The IPython notebook doesn't support GIF/Webm\n\nIPython is not the only notebook. I'm happy to use SageNB in almost all of my daily work, and have been happily using my own video-enabled branch on several occasions as well. If IPython doesn't support these, that's just one more reason to stick with SageNB for now, and hope that IPython learns to play along eventually.\n\n> and the browser probably not APNG\n\nMy Firefox supports APNG just fine, thank you very much. \n\n> so what is this rightclick-save going to do? Nothing. [\u2026] Does not work.\n\nI tell you this *is* working, since I *am* doing this, on a fairly regular basis. (I very much hope you won't claim that this is just me pressing the space bar for heat-induced Ctrl.)",
    "created_at": "2015-03-12T21:05:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60697",
    "user": "https://github.com/gagern"
}
```

Replying to [comment:52 vbraun]:
> The IPython notebook doesn't support GIF/Webm

IPython is not the only notebook. I'm happy to use SageNB in almost all of my daily work, and have been happily using my own video-enabled branch on several occasions as well. If IPython doesn't support these, that's just one more reason to stick with SageNB for now, and hope that IPython learns to play along eventually.

> and the browser probably not APNG

My Firefox supports APNG just fine, thank you very much. 

> so what is this rightclick-save going to do? Nothing. […] Does not work.

I tell you this *is* working, since I *am* doing this, on a fairly regular basis. (I very much hope you won't claim that this is just me pressing the space bar for heat-induced Ctrl.)



---

archive/issue_comments_060698.json:
```json
{
    "body": "Replying to [comment:54 gagern]:\n> I very much hope you won't claim that this is just me pressing the space bar for heat-induced Ctrl.\n\nYou are calling show() to save a file. Do I need to say more? ;)\n\nWhat any notebook *should* do is automatically download the file after you call save(), or at least show a download link. The fact that the saved file only lingers around on the remote server is yet another usability WTF. But thats a different ticket.",
    "created_at": "2015-03-12T21:19:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60698",
    "user": "https://github.com/vbraun"
}
```

Replying to [comment:54 gagern]:
> I very much hope you won't claim that this is just me pressing the space bar for heat-induced Ctrl.

You are calling show() to save a file. Do I need to say more? ;)

What any notebook *should* do is automatically download the file after you call save(), or at least show a download link. The fact that the saved file only lingers around on the remote server is yet another usability WTF. But thats a different ticket.



---

archive/issue_comments_060699.json:
```json
{
    "body": "Replying to [comment:53 vbraun]:\n> Distinguishing between lossy / lossless compression for graphics is reasonable, and doesn't require the user to know what webm&apng is.\n\nDistinguishing between the color-reduction losses of GIF and the frequency-domain compression losses of WebM and Theora does, in my opinion, indeed require some knowledge of formats. Sure, I won't mind if a polyfill-supported APNG becomes the lossless and shiny default, so that only the tech-savvy people ever have to make such a distinction.\n\nI'd say that on the one hand, noone should be forced to make any format decision for elementary work (small 2D animations with few colors), but those who have the knowledge to choose a format should also have the power to get things displayed in their format of choice. I don't want to force anybody to save stuff to a file and open it in a different application just because showing it in line would offer too many choices.\n\nBy the way, how are chances that every browser-based notebook will reliably detect whether the browser supports WebM, Theora, or perhaps even something else which FFmpeg already supports but Sage does not know about?\n\nI'd go a step further: there are many ways the animation composition might be tweaked. For ffmpeg videos you might control a million settings, bit rate probably the most important one. For GIF via ImageMagick there are a number of steps one can perform to achieve smaller and better files, reduction to a global color table foremost among these. I'd like to one day offer all of this power to the user, so he can pass ffmpeg command line switches or enable ImageMagick optimizations, whether he's saving to disk or viewing in browser. If you don't believe in \u201cright click to save\u201d, then you can still consider the \u201cview in browser\u201d as a preview to what will be saved to disk.\n\nWith the changes I had here, passing `**kwds` from `show` through `save` all the way to the format-specific methods, where additional options could be introduced as needed. Now if you claim that the user shouldn't even have control over whether the animation goes through FFmpeg or through ImageMagick, that approach doesn't make that much sense any more. I want to keep my power to choose.",
    "created_at": "2015-03-12T21:20:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60699",
    "user": "https://github.com/gagern"
}
```

Replying to [comment:53 vbraun]:
> Distinguishing between lossy / lossless compression for graphics is reasonable, and doesn't require the user to know what webm&apng is.

Distinguishing between the color-reduction losses of GIF and the frequency-domain compression losses of WebM and Theora does, in my opinion, indeed require some knowledge of formats. Sure, I won't mind if a polyfill-supported APNG becomes the lossless and shiny default, so that only the tech-savvy people ever have to make such a distinction.

I'd say that on the one hand, noone should be forced to make any format decision for elementary work (small 2D animations with few colors), but those who have the knowledge to choose a format should also have the power to get things displayed in their format of choice. I don't want to force anybody to save stuff to a file and open it in a different application just because showing it in line would offer too many choices.

By the way, how are chances that every browser-based notebook will reliably detect whether the browser supports WebM, Theora, or perhaps even something else which FFmpeg already supports but Sage does not know about?

I'd go a step further: there are many ways the animation composition might be tweaked. For ffmpeg videos you might control a million settings, bit rate probably the most important one. For GIF via ImageMagick there are a number of steps one can perform to achieve smaller and better files, reduction to a global color table foremost among these. I'd like to one day offer all of this power to the user, so he can pass ffmpeg command line switches or enable ImageMagick optimizations, whether he's saving to disk or viewing in browser. If you don't believe in “right click to save”, then you can still consider the “view in browser” as a preview to what will be saved to disk.

With the changes I had here, passing `**kwds` from `show` through `save` all the way to the format-specific methods, where additional options could be introduced as needed. Now if you claim that the user shouldn't even have control over whether the animation goes through FFmpeg or through ImageMagick, that approach doesn't make that much sense any more. I want to keep my power to choose.



---

archive/issue_comments_060700.json:
```json
{
    "body": "Replying to [comment:55 vbraun]:\n> What any notebook *should* do is automatically download the file after you call save()\n\nNo, I might be post-processing things remotely, from within the Sage session.\n\n> or at least show a download link. The fact that the saved file only lingers around on the remote server is yet another usability WTF. But thats a different ticket.\n\nSounds good, what ticket number is it?\n\nCan we please also have an option `preview` to the method `save` so it will show an inlined preview of the file you've just saved and can download via the link? In that case, I'll simply switch to writing `save` instead of `show` and will be just as happy as I am now, since it does give show me the file inline, give me full control over the format, and lets me save via right-click or that link. I don't care about the name of the method, I care about what it does.\n\nIn case you want to continue this discussion on IRC, I'll try to stay around in #sagemath for a bit.",
    "created_at": "2015-03-12T21:36:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60700",
    "user": "https://github.com/gagern"
}
```

Replying to [comment:55 vbraun]:
> What any notebook *should* do is automatically download the file after you call save()

No, I might be post-processing things remotely, from within the Sage session.

> or at least show a download link. The fact that the saved file only lingers around on the remote server is yet another usability WTF. But thats a different ticket.

Sounds good, what ticket number is it?

Can we please also have an option `preview` to the method `save` so it will show an inlined preview of the file you've just saved and can download via the link? In that case, I'll simply switch to writing `save` instead of `show` and will be just as happy as I am now, since it does give show me the file inline, give me full control over the format, and lets me save via right-click or that link. I don't care about the name of the method, I care about what it does.

In case you want to continue this discussion on IRC, I'll try to stay around in #sagemath for a bit.



---

archive/issue_comments_060701.json:
```json
{
    "body": "Replying to [comment:57 gagern]:\n> Can we please also have an option `preview` to the method `save` so it will show an inlined preview of the file you've just saved\n\nSo instead of calling show() to save you want to call save() to show the animation? ;-)",
    "created_at": "2015-03-12T22:57:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60701",
    "user": "https://github.com/vbraun"
}
```

Replying to [comment:57 gagern]:
> Can we please also have an option `preview` to the method `save` so it will show an inlined preview of the file you've just saved

So instead of calling show() to save you want to call save() to show the animation? ;-)



---

archive/issue_comments_060702.json:
```json
{
    "body": "Guess I missed you... maybe some time this weekend?\n\nI created #17942 for `save()`-ing",
    "created_at": "2015-03-12T23:42:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60702",
    "user": "https://github.com/vbraun"
}
```

Guess I missed you... maybe some time this weekend?

I created #17942 for `save()`-ing



---

archive/issue_comments_060703.json:
```json
{
    "body": "does not apply (and confuses the patchbot, see sage-devel)",
    "created_at": "2015-03-24T20:54:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60703",
    "user": "https://github.com/fchapoton"
}
```

does not apply (and confuses the patchbot, see sage-devel)



---

archive/issue_comments_060704.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-03-24T20:54:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60704",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_060705.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2015-04-18T19:14:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60705",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_060706.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2015-04-18T19:32:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60706",
    "user": "https://github.com/gagern"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_060707.json:
```json
{
    "body": "Yet another rebase. Perhaps it can be merged for Sage 6.7?\n\nRight now, I support videos if the user explicitely requests a given format. When no format is specified, animated GIF remains the only option. I know Volker doesn't like it if people *have* to specify such low level stuff like file formats. And I wouldn't mind some sane automatic choices based on requests of a higher level, e.g. requests for full-color output or whatever. But getting that to work is far from trivial, so I'd ask you to postpone any fancy automatic format detection to a follow-up ticket, so that we can get the basic support in without getting lost in the details of fancy automatisms.\n\nRight now, I don't support APNG as a format for `show` yet. #16650 should take care of that once this here gets merged. There might be some controversy ahead that way, so again I consider it best to get this bit here in before expanding on it.\n\nRight now, I only support Sage Notebook, since that is all I use when creating animations. While I could test small examples using command line or the IPython notebook, I'm not using either on a regular basis, so I might be missing important aspects of how they operate. I'd prefer to merge this support for what I know, and postpone support for other backends. I have some ideas there, but I'd be asking more input from users of said backends, which could possibly delay things somewhat.\n\nSo please try to review this change with the scope I chose, keeping in mind that this is but the first step in a direction aiming for more high-level requests, more consistent support for various formats, and more support from various backends other than the Sage notebook. Feel free to create follow-up tickets if you want to start a discussion for one of these subsequent steps. If this gets merged early in the 6.7 cycle, we might get some of the other things in as well.",
    "created_at": "2015-04-18T19:32:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60707",
    "user": "https://github.com/gagern"
}
```

Yet another rebase. Perhaps it can be merged for Sage 6.7?

Right now, I support videos if the user explicitely requests a given format. When no format is specified, animated GIF remains the only option. I know Volker doesn't like it if people *have* to specify such low level stuff like file formats. And I wouldn't mind some sane automatic choices based on requests of a higher level, e.g. requests for full-color output or whatever. But getting that to work is far from trivial, so I'd ask you to postpone any fancy automatic format detection to a follow-up ticket, so that we can get the basic support in without getting lost in the details of fancy automatisms.

Right now, I don't support APNG as a format for `show` yet. #16650 should take care of that once this here gets merged. There might be some controversy ahead that way, so again I consider it best to get this bit here in before expanding on it.

Right now, I only support Sage Notebook, since that is all I use when creating animations. While I could test small examples using command line or the IPython notebook, I'm not using either on a regular basis, so I might be missing important aspects of how they operate. I'd prefer to merge this support for what I know, and postpone support for other backends. I have some ideas there, but I'd be asking more input from users of said backends, which could possibly delay things somewhat.

So please try to review this change with the scope I chose, keeping in mind that this is but the first step in a direction aiming for more high-level requests, more consistent support for various formats, and more support from various backends other than the Sage notebook. Feel free to create follow-up tickets if you want to start a discussion for one of these subsequent steps. If this gets merged early in the 6.7 cycle, we might get some of the other things in as well.



---

archive/issue_comments_060708.json:
```json
{
    "body": "I don't mind it if the initial ticket only supports SageNB. But OutputVideoAny is just a slap in the face of any attempt at sanity. The whole point of the rich output model is to separate different output types. The rich output container must not contain anything but the data. No mime types, no file extensions. The type is unique to the output. By lumping it into a single OutputAllVideoThatSageNBunderstands you destroy any hope of ever supporting other notebooks without reverting your branch.",
    "created_at": "2015-04-18T23:28:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60708",
    "user": "https://github.com/vbraun"
}
```

I don't mind it if the initial ticket only supports SageNB. But OutputVideoAny is just a slap in the face of any attempt at sanity. The whole point of the rich output model is to separate different output types. The rich output container must not contain anything but the data. No mime types, no file extensions. The type is unique to the output. By lumping it into a single OutputAllVideoThatSageNBunderstands you destroy any hope of ever supporting other notebooks without reverting your branch.



---

archive/issue_comments_060709.json:
```json
{
    "body": "Replying to [comment:63 vbraun]:\n> But OutputVideoAny is just a slap in the face of any attempt at sanity. The whole point of the rich output model is to separate different output types.\n\nI can understand some of your concerns. To me, a supported output type is a promise. For most simple output types the promise is \u201cif you give me a file of said type, I'll display it to the user\u201d. But with video, it's not as simple. It's not the backend which decides what video formats are supported, but instead it's the browser or the system setup. So the promise I associate with `OutputVideoAny` is \u201cif you give me a file of said type, I'll present it to a user in such a way that it either plays or the user gets notified about what went wrong\u201d. Which in a browser context means \u201cI'll create a HTML5 `<video>` tag for it\u201d.\n\nDue to this nature, `OutputVideoAny` should never be used to auto-guess supported formats. It doesn't mean \u201cthis client supports any video format\u201d, but instead \u201cthis client can present any video format to the user, but that presentation might be in the form or an error message\u201d. So the machinery shouldn't use it to throw arbitrary formats at the back end, but as a means to throw explicitly requested formats at it.\n\nI wouldn't mind having specific formats. For video, a full file format description consists of a container format, a video codec format, and possibly a bunch of other constraints as well. So we'd have `OutputVideoWebMVP8` and `OutputVideoWebMVP9` and `OutputVideoOggTheora` and `OutputVideoAviH264` and `OutputVideoFlashH264` and `OutputVideoMp4H264` and `OutputVideoQuicktimeH264` and probably a hundred other combinations. (We could parse the list of formats FFmpeg supports.) And in my opinion, each of these would indicate a promise to actually support the given type. So we'd have to somehow detect support. Or state that such a type being listed with the supported types does not imply it's actually supported. I have no idea on how to do auto-detection, and having a bunch of maybe supported formats feels no different to my `OutputVideoAny`.\n\nSo do you have any suggestions of how to handle this situation in a better way? I understand your criticism from an idealistic point of view, but on the pragmatic side, unless one can do active format support detection, all formats are essentially the same to the backend, and a single representation for all of them avoids useless overhead.\n\n> The rich output container must not contain anything but the data. No mime types, no file extensions. The type is unique to the output. By lumping it into a single OutputAllVideoThatSageNBunderstands you destroy any hope of ever supporting other notebooks without reverting your branch.\n\nIt's not \u201coutput all video that Sage NB understands\u201d. It's more like \u201coutput all video which can possibly be handled by a `<video>` tag\u201d, combined with \u201coutput all video which gets opened by launching up the user's default media player\u201d. For the `<video>` tag you need the MIME type. For the media player, you need the correct file extension. But if you consider the `<video>` element as the deliverable of the output, then the mime type is very much part of the data needed to assemble that.\n\nOne more comment: if there is one thing I can't stand about computer programs, it's if these try to be more clever than the user. The user should be in charge, and if the user says \u201cI want to view this animation in that format\u201d, the code should not second-guess that decision, should not forbid the operation just because the named format isn't in a list of known formats, or support by the browser or media player can't be verified up front. Please leave the users in charge of their application, not the other way round!",
    "created_at": "2015-04-19T09:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60709",
    "user": "https://github.com/gagern"
}
```

Replying to [comment:63 vbraun]:
> But OutputVideoAny is just a slap in the face of any attempt at sanity. The whole point of the rich output model is to separate different output types.

I can understand some of your concerns. To me, a supported output type is a promise. For most simple output types the promise is “if you give me a file of said type, I'll display it to the user”. But with video, it's not as simple. It's not the backend which decides what video formats are supported, but instead it's the browser or the system setup. So the promise I associate with `OutputVideoAny` is “if you give me a file of said type, I'll present it to a user in such a way that it either plays or the user gets notified about what went wrong”. Which in a browser context means “I'll create a HTML5 `<video>` tag for it”.

Due to this nature, `OutputVideoAny` should never be used to auto-guess supported formats. It doesn't mean “this client supports any video format”, but instead “this client can present any video format to the user, but that presentation might be in the form or an error message”. So the machinery shouldn't use it to throw arbitrary formats at the back end, but as a means to throw explicitly requested formats at it.

I wouldn't mind having specific formats. For video, a full file format description consists of a container format, a video codec format, and possibly a bunch of other constraints as well. So we'd have `OutputVideoWebMVP8` and `OutputVideoWebMVP9` and `OutputVideoOggTheora` and `OutputVideoAviH264` and `OutputVideoFlashH264` and `OutputVideoMp4H264` and `OutputVideoQuicktimeH264` and probably a hundred other combinations. (We could parse the list of formats FFmpeg supports.) And in my opinion, each of these would indicate a promise to actually support the given type. So we'd have to somehow detect support. Or state that such a type being listed with the supported types does not imply it's actually supported. I have no idea on how to do auto-detection, and having a bunch of maybe supported formats feels no different to my `OutputVideoAny`.

So do you have any suggestions of how to handle this situation in a better way? I understand your criticism from an idealistic point of view, but on the pragmatic side, unless one can do active format support detection, all formats are essentially the same to the backend, and a single representation for all of them avoids useless overhead.

> The rich output container must not contain anything but the data. No mime types, no file extensions. The type is unique to the output. By lumping it into a single OutputAllVideoThatSageNBunderstands you destroy any hope of ever supporting other notebooks without reverting your branch.

It's not “output all video that Sage NB understands”. It's more like “output all video which can possibly be handled by a `<video>` tag”, combined with “output all video which gets opened by launching up the user's default media player”. For the `<video>` tag you need the MIME type. For the media player, you need the correct file extension. But if you consider the `<video>` element as the deliverable of the output, then the mime type is very much part of the data needed to assemble that.

One more comment: if there is one thing I can't stand about computer programs, it's if these try to be more clever than the user. The user should be in charge, and if the user says “I want to view this animation in that format”, the code should not second-guess that decision, should not forbid the operation just because the named format isn't in a list of known formats, or support by the browser or media player can't be verified up front. Please leave the users in charge of their application, not the other way round!



---

archive/issue_comments_060710.json:
```json
{
    "body": "Supported means that we have code for trying to display that particular output type. There is not necessarily a guarantee that it'll work, you might be missing an external dependency (e.g. java). But if its unsupported then it can't possibly work because there is no code to do something with it. \n\nAt the same time you don't have to make a different output type for each sub-type, its ok to lump together formats that are likely to be supported at the same time (e.g. because they are common in some type of container). For example, there is no OutputImagePdf for each pdf version. But formats with a different mime type, say, aren't going to always be supported by the same player. In that sense their taxonomy is similar to mime types (but not exactly the same, e.g. support for multi-file output, jmol, ...) Just use your judgement. Is every video player going to be able to play animated gifs? I don't think so -> different output types.\n\nOn top of my head, I would suggest the following:\n* OutputVideoAnimatedGif\n* OutputVideoAnimatedPNG\n* OutputVideoWebm\n* OutputVideoMp4\n* OutputVideoFlash\n* OutputVideoQuicktime",
    "created_at": "2015-04-19T12:47:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60710",
    "user": "https://github.com/vbraun"
}
```

Supported means that we have code for trying to display that particular output type. There is not necessarily a guarantee that it'll work, you might be missing an external dependency (e.g. java). But if its unsupported then it can't possibly work because there is no code to do something with it. 

At the same time you don't have to make a different output type for each sub-type, its ok to lump together formats that are likely to be supported at the same time (e.g. because they are common in some type of container). For example, there is no OutputImagePdf for each pdf version. But formats with a different mime type, say, aren't going to always be supported by the same player. In that sense their taxonomy is similar to mime types (but not exactly the same, e.g. support for multi-file output, jmol, ...) Just use your judgement. Is every video player going to be able to play animated gifs? I don't think so -> different output types.

On top of my head, I would suggest the following:
* OutputVideoAnimatedGif
* OutputVideoAnimatedPNG
* OutputVideoWebm
* OutputVideoMp4
* OutputVideoFlash
* OutputVideoQuicktime



---

archive/issue_comments_060711.json:
```json
{
    "body": "I fully agree with the Animated PNG format, that should be a type on its own. The OutputImageGif alreads includes animated GIF, according to its docstring. Should this be changed? Should the browser-based backends declare support for [WebM](http://caniuse.com/#feat=webm), [Ogg](http://caniuse.com/#feat=ogv) and [MPEG4](http://caniuse.com/#feat=mpeg4), even though the browser might be lacking support for either? Is there any way how a backend could, at some later time, indicate that indeed it does support a given video format?",
    "created_at": "2015-04-20T05:57:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60711",
    "user": "https://github.com/gagern"
}
```

I fully agree with the Animated PNG format, that should be a type on its own. The OutputImageGif alreads includes animated GIF, according to its docstring. Should this be changed? Should the browser-based backends declare support for [WebM](http://caniuse.com/#feat=webm), [Ogg](http://caniuse.com/#feat=ogv) and [MPEG4](http://caniuse.com/#feat=mpeg4), even though the browser might be lacking support for either? Is there any way how a backend could, at some later time, indicate that indeed it does support a given video format?



---

archive/issue_comments_060712.json:
```json
{
    "body": "I would prefer to make animated gif its own output type since many stand-alone image viewers will not show the animation. I just hadn't thought through the case of animations when I wrote it.\n\nIdeally, browser-based backends would have some browser detection and then only return the actually supported output types. Though right now this is not implemented. Lacking that, you should return everything that a modern browser would support.",
    "created_at": "2015-04-20T12:58:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60712",
    "user": "https://github.com/vbraun"
}
```

I would prefer to make animated gif its own output type since many stand-alone image viewers will not show the animation. I just hadn't thought through the case of animations when I wrote it.

Ideally, browser-based backends would have some browser detection and then only return the actually supported output types. Though right now this is not implemented. Lacking that, you should return everything that a modern browser would support.



---

archive/issue_comments_060713.json:
```json
{
    "body": "Is Internet Explorer 11 a modern browser, even though it lacks WebM support? If you are tempted to answer this \u201cno\u201d and instead opt for MPEG-4 AVC as the codec with best cross-browser support, then please keep in mind that use of that codec might make the resulting content patent-encumbered, so I would very much like to keep at least one free alternative around. So for pragmatic reasons I'd declare recent releases of Chrome and Firefox as the only modern browsers here, and thus pretend that all web browsers support all three formats mentioned above. Or in other words, I'll go with the fact that the formats *might* be supported, which is all my `OutputVideoAny` approach did in any case. I'll adapt the code along these lines soon.",
    "created_at": "2015-04-20T15:25:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60713",
    "user": "https://github.com/gagern"
}
```

Is Internet Explorer 11 a modern browser, even though it lacks WebM support? If you are tempted to answer this “no” and instead opt for MPEG-4 AVC as the codec with best cross-browser support, then please keep in mind that use of that codec might make the resulting content patent-encumbered, so I would very much like to keep at least one free alternative around. So for pragmatic reasons I'd declare recent releases of Chrome and Firefox as the only modern browsers here, and thus pretend that all web browsers support all three formats mentioned above. Or in other words, I'll go with the fact that the formats *might* be supported, which is all my `OutputVideoAny` approach did in any case. I'll adapt the code along these lines soon.



---

archive/issue_comments_060714.json:
```json
{
    "body": "Fine with me. I'm not saying that it should behave differently than your `OutputVideoAny`, I'm just asking you to make it possible for other backends to rely on the output types.",
    "created_at": "2015-04-20T18:18:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60714",
    "user": "https://github.com/vbraun"
}
```

Fine with me. I'm not saying that it should behave differently than your `OutputVideoAny`, I'm just asking you to make it possible for other backends to rely on the output types.



---

archive/issue_comments_060715.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-04-21T15:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60715",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_060716.json:
```json
{
    "body": "Thanks, looks much better.\n\nI still dislike that HTML 5 tag attributes are attached to the rich output types, that makes no sense outside of a browser. The settings in question:\n* autoplay: Pointless, you ran `animation.show()` so obviously you want to see the animation\n* controls: Who would ever want no video controls? Hard to imagine any use case for that on a scientific data visualization platform.\n* loop: Seems desirable\nSo IMHO we should only have a `loop=True` optional keyword argument on the video output types, and no attrs={} dictionary.",
    "created_at": "2015-04-22T00:49:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60716",
    "user": "https://github.com/vbraun"
}
```

Thanks, looks much better.

I still dislike that HTML 5 tag attributes are attached to the rich output types, that makes no sense outside of a browser. The settings in question:
* autoplay: Pointless, you ran `animation.show()` so obviously you want to see the animation
* controls: Who would ever want no video controls? Hard to imagine any use case for that on a scientific data visualization platform.
* loop: Seems desirable
So IMHO we should only have a `loop=True` optional keyword argument on the video output types, and no attrs={} dictionary.



---

archive/issue_comments_060717.json:
```json
{
    "body": "Replying to [comment:71 vbraun]:\n> Thanks, looks much better.\n\nGlad you say so. I'm still a bit concerned by the fact that a format supported by backend and FFmpeg still won't be supported only because it's not in our list.\n\nI'm slightly worried by the fact that we save the video to some temporary file, only to copy it to the current working directory in a subsequent step, where SageNB can pick it up. This feels kind of wasteful. As far as I see, the temporary file used for the rich output never gets deleted (if this is wrong, where is the code doing that), which means a long-running SageNB process will accumulate temporary files without association to notebook cells, and might exhaust some tempfs due to this. Should this be a separate ticket?\n\n> I still dislike that HTML 5 tag attributes are attached to the rich output types, that makes no sense outside of a browser.\n\nWell, most of the attributes map to other players as well. To support that claim, take e.g. `xine` which has `-Z` to suppress autoplay, `--hide-gui` and `--no-gui` to disable controls, and `--loop` or perhaps `--loop=repeat` to loop. So while the names of the attributes were taken from HTML5, the semantics can be found elsewhere as well.\n\nThe main problem is that each viewer has a different set of command line arguments to represent these options, and as long as we open stuff through `xdg-open` (which I consider the most likely approach for `BackendIPythonCommandline` on Linux), we have little chance of actually supporting any of this outside the browser in the near future.\n\n> The settings in question:\n> * autoplay: Pointless, you ran `animation.show()` so obviously you want to see the animation\n\nUse case: Creating the animation takes five minutes, so you work in some other window while Sage gets its act together. When you switch back you want to be able to view the animation from the beginning using a single click. Or perhaps you have a loop creating several animations, and want to show them one after the other. Controlling when an animation starts may be particularly important in an environment where you have an audience, and some effect visible in the animation which you don't want to divulge prematurely.\n\n> * controls: Who would ever want no video controls? Hard to imagine any use case for that on a scientific data visualization platform.\n\nI guess you are right there. I guess the main reason to have that in HTML is when you have your own controls written in JavaScript. Not something we need to worry about.\n\n> * loop: Seems desirable\n\nMapping `loop` to e.g. the IPython command line backend sounds like it's going to be really tricky, but I think we simply have to live with the fact that some backends won't support some of the features.\n\n> So IMHO we should only have a `loop=True` optional keyword argument on the video output types, and no attrs={} dictionary.\n\nIf I could convince you with the `autoplay` use cases, should I add two keyword arguments? I guess so.",
    "created_at": "2015-04-22T06:46:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60717",
    "user": "https://github.com/gagern"
}
```

Replying to [comment:71 vbraun]:
> Thanks, looks much better.

Glad you say so. I'm still a bit concerned by the fact that a format supported by backend and FFmpeg still won't be supported only because it's not in our list.

I'm slightly worried by the fact that we save the video to some temporary file, only to copy it to the current working directory in a subsequent step, where SageNB can pick it up. This feels kind of wasteful. As far as I see, the temporary file used for the rich output never gets deleted (if this is wrong, where is the code doing that), which means a long-running SageNB process will accumulate temporary files without association to notebook cells, and might exhaust some tempfs due to this. Should this be a separate ticket?

> I still dislike that HTML 5 tag attributes are attached to the rich output types, that makes no sense outside of a browser.

Well, most of the attributes map to other players as well. To support that claim, take e.g. `xine` which has `-Z` to suppress autoplay, `--hide-gui` and `--no-gui` to disable controls, and `--loop` or perhaps `--loop=repeat` to loop. So while the names of the attributes were taken from HTML5, the semantics can be found elsewhere as well.

The main problem is that each viewer has a different set of command line arguments to represent these options, and as long as we open stuff through `xdg-open` (which I consider the most likely approach for `BackendIPythonCommandline` on Linux), we have little chance of actually supporting any of this outside the browser in the near future.

> The settings in question:
> * autoplay: Pointless, you ran `animation.show()` so obviously you want to see the animation

Use case: Creating the animation takes five minutes, so you work in some other window while Sage gets its act together. When you switch back you want to be able to view the animation from the beginning using a single click. Or perhaps you have a loop creating several animations, and want to show them one after the other. Controlling when an animation starts may be particularly important in an environment where you have an audience, and some effect visible in the animation which you don't want to divulge prematurely.

> * controls: Who would ever want no video controls? Hard to imagine any use case for that on a scientific data visualization platform.

I guess you are right there. I guess the main reason to have that in HTML is when you have your own controls written in JavaScript. Not something we need to worry about.

> * loop: Seems desirable

Mapping `loop` to e.g. the IPython command line backend sounds like it's going to be really tricky, but I think we simply have to live with the fact that some backends won't support some of the features.

> So IMHO we should only have a `loop=True` optional keyword argument on the video output types, and no attrs={} dictionary.

If I could convince you with the `autoplay` use cases, should I add two keyword arguments? I guess so.



---

archive/issue_comments_060718.json:
```json
{
    "body": "Temporary files are always a kludge, which is why the OutputBuffer is designed around in-memory buffers. In general there is no guarantee that the compute kernel and the notebook server share a common file system. Like all temporary files, they are eventually deleted by the separate sage-cleaner process.\n\nThere is a technical solution to not playing stuff in hidden browser tabs: http://caniuse.com/#feat=pagevisibility. No need to force the user to do it by hand.\n\nIf you want to show multiple animations one after the other then you really want a single animation with the frames concatenated. Presumably you can add animation objects... \n\nIf you don't want the audience to see the animation then don't evaluate the cell that shows the animation. Thats about equally disruptive in a presentation as having to click on something to play the animation. If the UI has a special \"slides\" mode (like the IPython notebook) then it should handle <video> in a way that does not disrupt the flow, you should only ever need forward/backward button on the presentation remote control.",
    "created_at": "2015-04-22T13:27:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60718",
    "user": "https://github.com/vbraun"
}
```

Temporary files are always a kludge, which is why the OutputBuffer is designed around in-memory buffers. In general there is no guarantee that the compute kernel and the notebook server share a common file system. Like all temporary files, they are eventually deleted by the separate sage-cleaner process.

There is a technical solution to not playing stuff in hidden browser tabs: http://caniuse.com/#feat=pagevisibility. No need to force the user to do it by hand.

If you want to show multiple animations one after the other then you really want a single animation with the frames concatenated. Presumably you can add animation objects... 

If you don't want the audience to see the animation then don't evaluate the cell that shows the animation. Thats about equally disruptive in a presentation as having to click on something to play the animation. If the UI has a special "slides" mode (like the IPython notebook) then it should handle <video> in a way that does not disrupt the flow, you should only ever need forward/backward button on the presentation remote control.



---

archive/issue_comments_060719.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2015-08-26T07:52:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60719",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_060720.json:
```json
{
    "body": "Rebased, and incorporated latest review comments in that [last commit](http://git.sagemath.org/sage.git/commit/?id=ea5dfe2f6b0ac9468962540e9afb7be33f869233). Is this ready for merge now?\n\nPerhaps in the long run we should have something like a `prepare` method for animation objects, which creates the video file without showing it, and on which one can call `show` or `save` later on, with minimal cost. But I'll leave that idea for later.",
    "created_at": "2015-08-26T07:56:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60720",
    "user": "https://github.com/gagern"
}
```

Rebased, and incorporated latest review comments in that [last commit](http://git.sagemath.org/sage.git/commit/?id=ea5dfe2f6b0ac9468962540e9afb7be33f869233). Is this ready for merge now?

Perhaps in the long run we should have something like a `prepare` method for animation objects, which creates the video file without showing it, and on which one can call `show` or `save` later on, with minimal cost. But I'll leave that idea for later.



---

archive/issue_comments_060721.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-08-26T13:41:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60721",
    "user": "https://github.com/vbraun"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_060722.json:
```json
{
    "body": "Thanks for the review. Now I can build on this for #16650.",
    "created_at": "2015-08-26T15:12:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7298",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7298#issuecomment-60722",
    "user": "https://github.com/gagern"
}
```

Thanks for the review. Now I can build on this for #16650.
