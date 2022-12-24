# Issue 9655: Add an example ploting spherical harmonics to spherical_plot3d's docstring

archive/issues_009655.json:
```json
{
    "body": "Assignee: olazo\n\nKeywords: spherical,harmonics\n\nPloting Spherical Harmonics is one of the most useful ways to use spherical_plot3d. Adding an example of that would be nice.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9655\n\n",
    "created_at": "2010-08-01T01:43:52Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.6.1",
    "title": "Add an example ploting spherical harmonics to spherical_plot3d's docstring",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9655",
    "user": "olazo"
}
```
Assignee: olazo

Keywords: spherical,harmonics

Ploting Spherical Harmonics is one of the most useful ways to use spherical_plot3d. Adding an example of that would be nice.

Issue created by migration from https://trac.sagemath.org/ticket/9655





---

archive/issue_comments_093704.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-10-28T00:45:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9655#issuecomment-93704",
    "user": "olazo"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_093705.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2010-10-28T00:46:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9655#issuecomment-93705",
    "user": "olazo"
}
```

Changing priority from major to minor.



---

archive/issue_comments_093706.json:
```json
{
    "body": "Attachment [trac-9655_spherical-harmonic-example.patch](tarball://root/attachments/some-uuid/ticket9655/trac-9655_spherical-harmonic-example.patch) by mvngu created at 2010-11-02 09:07:36",
    "created_at": "2010-11-02T09:07:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9655#issuecomment-93706",
    "user": "mvngu"
}
```

Attachment [trac-9655_spherical-harmonic-example.patch](tarball://root/attachments/some-uuid/ticket9655/trac-9655_spherical-harmonic-example.patch) by mvngu created at 2010-11-02 09:07:36



---

archive/issue_comments_093707.json:
```json
{
    "body": "Attachment [trac-9655_reviewer.patch](tarball://root/attachments/some-uuid/ticket9655/trac-9655_reviewer.patch) by mvngu created at 2010-11-02 09:13:38\n\nHere are some issues with olazo's patch:\n\n* The \"User\" should be filled with your real name and preferred contact email address. I have fixed this in my update of olazo's patch; see [attachment:trac-9655_spherical-harmonic-example.patch].\n* The code in olazo's patch does not conform to Python coding conventions. In particular, see [PEP 8](http://www.python.org/dev/peps/pep-0008/). This is fixed in my reviewer patch; see [attachment:trac-9655_reviewer.patch]. Someone other than me needs to review that. If my patch gets a positive review, the whole ticket gets a positive review.",
    "created_at": "2010-11-02T09:13:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9655#issuecomment-93707",
    "user": "mvngu"
}
```

Attachment [trac-9655_reviewer.patch](tarball://root/attachments/some-uuid/ticket9655/trac-9655_reviewer.patch) by mvngu created at 2010-11-02 09:13:38

Here are some issues with olazo's patch:

* The "User" should be filled with your real name and preferred contact email address. I have fixed this in my update of olazo's patch; see [attachment:trac-9655_spherical-harmonic-example.patch].
* The code in olazo's patch does not conform to Python coding conventions. In particular, see [PEP 8](http://www.python.org/dev/peps/pep-0008/). This is fixed in my reviewer patch; see [attachment:trac-9655_reviewer.patch]. Someone other than me needs to review that. If my patch gets a positive review, the whole ticket gets a positive review.



---

archive/issue_comments_093708.json:
```json
{
    "body": "Replying to [comment:3 mvngu]:\n> Here are some issues with olazo's patch:\n> \n>  * The \"User\" should be filled with your real name and preferred contact email address. I have fixed this in my update of olazo's patch; see [attachment:trac-9655_spherical-harmonic-example.patch].\n\nThis is the first patch I produced using mecurial queues. At some point I recieved a warning about User not being defined, but how do I set it up? I mean other than directly editing the .patch\n\n>  * The code in olazo's patch does not conform to Python coding conventions. In particular, see [PEP 8](http://www.python.org/dev/peps/pep-0008/). This is fixed in my reviewer patch; see [attachment:trac-9655_reviewer.patch]. Someone other than me needs to review that. If my patch gets a positive review, the whole ticket gets a positive review.\n\nI was unaware of such conventions...",
    "created_at": "2010-11-02T21:41:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9655#issuecomment-93708",
    "user": "olazo"
}
```

Replying to [comment:3 mvngu]:
> Here are some issues with olazo's patch:
> 
>  * The "User" should be filled with your real name and preferred contact email address. I have fixed this in my update of olazo's patch; see [attachment:trac-9655_spherical-harmonic-example.patch].

This is the first patch I produced using mecurial queues. At some point I recieved a warning about User not being defined, but how do I set it up? I mean other than directly editing the .patch

>  * The code in olazo's patch does not conform to Python coding conventions. In particular, see [PEP 8](http://www.python.org/dev/peps/pep-0008/). This is fixed in my reviewer patch; see [attachment:trac-9655_reviewer.patch]. Someone other than me needs to review that. If my patch gets a positive review, the whole ticket gets a positive review.

I was unaware of such conventions...



---

archive/issue_comments_093709.json:
```json
{
    "body": "Replying to [comment:5 olazo]:\n> At some point I recieved a warning about User not being defined, but how do I set it up? I mean other than directly editing the .patch\n\nYou should use the Mercurial configuration file `~/.hgrc`. Here's a template for your `~/.hgrc` file:\n\n\n```sh\n[ui]\neditor = /usr/bin/vim\nusername = Carl Friedrich Gauss <cfgauss@uni-goettingen.de>\n\n[extensions]\n# Enable the Mercurial queues extension.\nhgext.mq =\n# Enable the record, qrecord and crecord extensions for cherry picking.\nhgext.record =\n\n[diff]\n# Format diff output using Git style.\ngit = True\n# Prevent qrefresh from updating timestamps. If you're keeping your patch\n# queue under revision control, it can be quite annoying when every qrefresh\n# updates the timestamps in your patch. The following prevents this from\n# happening.\nnodates = 1\n```\n\n\nChange your username accordingly.\n\n\n\n\n\n> I was unaware of such conventions...\n\nSee [this page](http://www.sagemath.org/doc/developer/conventions.html) of the [Developer's Guide](http://www.sagemath.org/doc/developer/index.html) for more details about coding conventions used by the Sage library.",
    "created_at": "2010-11-03T07:20:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9655#issuecomment-93709",
    "user": "mvngu"
}
```

Replying to [comment:5 olazo]:
> At some point I recieved a warning about User not being defined, but how do I set it up? I mean other than directly editing the .patch

You should use the Mercurial configuration file `~/.hgrc`. Here's a template for your `~/.hgrc` file:


```sh
[ui]
editor = /usr/bin/vim
username = Carl Friedrich Gauss <cfgauss@uni-goettingen.de>

[extensions]
# Enable the Mercurial queues extension.
hgext.mq =
# Enable the record, qrecord and crecord extensions for cherry picking.
hgext.record =

[diff]
# Format diff output using Git style.
git = True
# Prevent qrefresh from updating timestamps. If you're keeping your patch
# queue under revision control, it can be quite annoying when every qrefresh
# updates the timestamps in your patch. The following prevents this from
# happening.
nodates = 1
```


Change your username accordingly.





> I was unaware of such conventions...

See [this page](http://www.sagemath.org/doc/developer/conventions.html) of the [Developer's Guide](http://www.sagemath.org/doc/developer/index.html) for more details about coding conventions used by the Sage library.



---

archive/issue_comments_093710.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-11-03T15:57:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9655#issuecomment-93710",
    "user": "@haikona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_093711.json:
```json
{
    "body": "This is the first patch I've ever reviewed, so a second look by someone else might not be a bad idea.",
    "created_at": "2010-11-03T16:05:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9655#issuecomment-93711",
    "user": "@haikona"
}
```

This is the first patch I've ever reviewed, so a second look by someone else might not be a bad idea.



---

archive/issue_comments_093712.json:
```json
{
    "body": "Replying to [comment:8 spice]:\n> This is the first patch I've ever reviewed, so a second look by someone else might not be a bad idea.\n\nPlease put down your real name in the field \"Reviewer(s):\".",
    "created_at": "2010-11-04T04:33:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9655#issuecomment-93712",
    "user": "mvngu"
}
```

Replying to [comment:8 spice]:
> This is the first patch I've ever reviewed, so a second look by someone else might not be a bad idea.

Please put down your real name in the field "Reviewer(s):".



---

archive/issue_comments_093713.json:
```json
{
    "body": "Done.\n\nThanks Minh.",
    "created_at": "2010-11-04T17:40:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9655#issuecomment-93713",
    "user": "@haikona"
}
```

Done.

Thanks Minh.



---

archive/issue_comments_093714.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-11-10T22:19:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9655",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9655#issuecomment-93714",
    "user": "@jdemeyer"
}
```

Resolution: fixed
