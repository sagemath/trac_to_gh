# Issue 7441: notebook: make it possible to upload from the url of a published worksheet

archive/issues_007441.json:
```json
{
    "body": "Assignee: boothby\n\n```\n>> I go to \"upload\", and try to upload a worksheet from url in a public\n>> notebook --- so it's an https://... I guess that's why it fails (the\n>> page itself is a published worksheet, so password is not required, but\n>> I guess the upload can't pull a worksheet from an https url).\n>\n> Upload from a URL can't upload from a published worksheet that is\n> published as http or https, actually.  It never occurred to me to\n> implement that.  It's meant for uploading sws files, which might be\n> sitting on the web somewhere.     Uploading from the URL of a\n> published worksheet is an interesting idea.\n>\n\n+1 to this.  More than once, I've tried it, and found out again and\nagain that it didn't work.\n\n -- Jason\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/7441\n\n",
    "created_at": "2009-11-12T06:40:03Z",
    "labels": [
        "component: notebook",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "notebook: make it possible to upload from the url of a published worksheet",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7441",
    "user": "https://github.com/williamstein"
}
```
Assignee: boothby

```
>> I go to "upload", and try to upload a worksheet from url in a public
>> notebook --- so it's an https://... I guess that's why it fails (the
>> page itself is a published worksheet, so password is not required, but
>> I guess the upload can't pull a worksheet from an https url).
>
> Upload from a URL can't upload from a published worksheet that is
> published as http or https, actually.  It never occurred to me to
> implement that.  It's meant for uploading sws files, which might be
> sitting on the web somewhere.     Uploading from the URL of a
> published worksheet is an interesting idea.
>

+1 to this.  More than once, I've tried it, and found out again and
again that it didn't work.

 -- Jason
```

Issue created by migration from https://trac.sagemath.org/ticket/7441





---

archive/issue_comments_062526.json:
```json
{
    "body": "Let me add another +1 to this. It would make it much easier when teaching -- I write up a worksheet for an assignment, publish it, and then tell the students the URL. They log into their accounts, hit upload, paste in the URL, and they have the worksheet. As it stands, either I or my students needs to manually save the worksheet file somewhere and do something with it.\n\nAs a quick and dirty hack, I see that published worksheets have something like this in their html source:\n\n<li><a href=\"download/blargle floomp.sws\">Download.</a></li>\n\n...so maybe, when given a url that does not end in .sws, the upload mechanism could just suck in the html source, look for the first hyperlink tag that resembles the above, and use that URL? I'm thinking a regex of `<a href=\"download/.*\\.sws\">` or similar.\n\nSome kind of magic incantation in the html would also allow people to use random web pages as upload sources; imagine taking the URL of a blog post and putting into the upload box, and it automagically finds a .sws file to download. This could be the html version of the \"embed a .sws file into a pdf\" idea that has been discussed before.",
    "created_at": "2010-03-02T09:31:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7441#issuecomment-62526",
    "user": "https://github.com/dandrake"
}
```

Let me add another +1 to this. It would make it much easier when teaching -- I write up a worksheet for an assignment, publish it, and then tell the students the URL. They log into their accounts, hit upload, paste in the URL, and they have the worksheet. As it stands, either I or my students needs to manually save the worksheet file somewhere and do something with it.

As a quick and dirty hack, I see that published worksheets have something like this in their html source:

<li><a href="download/blargle floomp.sws">Download.</a></li>

...so maybe, when given a url that does not end in .sws, the upload mechanism could just suck in the html source, look for the first hyperlink tag that resembles the above, and use that URL? I'm thinking a regex of `<a href="download/.*\.sws">` or similar.

Some kind of magic incantation in the html would also allow people to use random web pages as upload sources; imagine taking the URL of a blog post and putting into the upload box, and it automagically finds a .sws file to download. This could be the html version of the "embed a .sws file into a pdf" idea that has been discussed before.



---

archive/issue_comments_062527.json:
```json
{
    "body": "Well, that's my \"don't forget to use preview\" lesson for today...\n\nReplying to [comment:1 ddrake]:\n> published worksheets have something like this in their html source:\n\n\nI meant to follow that with:\n\n```\n<li><a href=\"download/blargle floomp.sws\">Download.</a></li>\n```",
    "created_at": "2010-03-02T09:34:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7441#issuecomment-62527",
    "user": "https://github.com/dandrake"
}
```

Well, that's my "don't forget to use preview" lesson for today...

Replying to [comment:1 ddrake]:
> published worksheets have something like this in their html source:


I meant to follow that with:

```
<li><a href="download/blargle floomp.sws">Download.</a></li>
```



---

archive/issue_comments_062528.json:
```json
{
    "body": "I think we can implement the \"magic incantation\" with something very simple, just like RSS autodiscovery. In the `<head>` of any HTML document that wishes to advertise a link to a related Sage worksheet, just put:\n\n```\n<link rel=\"alternate\" type=\"application/sage\" title=\"the title of the worksheet\"\n      href=\"http://url.to.worksheet.sws\">\n```\nThe \"application/sage\" mimics what the notebook server gives when downloading a worksheet from the \"Download\" link on a published worksheet. I don't know if that's a proper MIME type.\n\nMore info: http://www.rssboard.org/rss-autodiscovery and http://www.w3schools.com/tags/tag_link.asp. The rel=\"alternate\" specifies that the link is to an alternate version of the content, which is exactly what we want.\n\nWe just need to put that link into published worksheets, and then get the \"upload worksheet from URL\" stuff to look for that link.\n\nRSS autodiscovery is well-established and works very well, so using the same mechanism for our own purposes seems like a good idea, and is very easy for anyone to use on any web page.",
    "created_at": "2010-03-26T01:50:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7441#issuecomment-62528",
    "user": "https://github.com/dandrake"
}
```

I think we can implement the "magic incantation" with something very simple, just like RSS autodiscovery. In the `<head>` of any HTML document that wishes to advertise a link to a related Sage worksheet, just put:

```
<link rel="alternate" type="application/sage" title="the title of the worksheet"
      href="http://url.to.worksheet.sws">
```
The "application/sage" mimics what the notebook server gives when downloading a worksheet from the "Download" link on a published worksheet. I don't know if that's a proper MIME type.

More info: http://www.rssboard.org/rss-autodiscovery and http://www.w3schools.com/tags/tag_link.asp. The rel="alternate" specifies that the link is to an alternate version of the content, which is exactly what we want.

We just need to put that link into published worksheets, and then get the "upload worksheet from URL" stuff to look for that link.

RSS autodiscovery is well-established and works very well, so using the same mechanism for our own purposes seems like a good idea, and is very easy for anyone to use on any web page.



---

archive/issue_comments_062529.json:
```json
{
    "body": "add <link rel=\"alternate\"... stuff to published worksheets",
    "created_at": "2010-05-20T02:37:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7441#issuecomment-62529",
    "user": "https://github.com/dandrake"
}
```

add <link rel="alternate"... stuff to published worksheets



---

archive/issue_comments_062530.json:
```json
{
    "body": "Attachment [trac_7441_link_rel.patch](tarball://root/attachments/some-uuid/ticket7441/trac_7441_link_rel.patch) by @dandrake created at 2010-05-20 02:37:51\n\nadd support to \"upload a worksheet\" page for parsing <link rel=\"alternate\"... links",
    "created_at": "2010-05-20T02:37:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7441#issuecomment-62530",
    "user": "https://github.com/dandrake"
}
```

Attachment [trac_7441_link_rel.patch](tarball://root/attachments/some-uuid/ticket7441/trac_7441_link_rel.patch) by @dandrake created at 2010-05-20 02:37:51

add support to "upload a worksheet" page for parsing <link rel="alternate"... links



---

archive/issue_comments_062531.json:
```json
{
    "body": "Attachment [trac_7441_upload.patch](tarball://root/attachments/some-uuid/ticket7441/trac_7441_upload.patch) by @dandrake created at 2010-05-20 02:43:09\n\nThese two patches are a mostly-working implementation of these ideas. The \"link_rel\" patch simply adds the appropriate link into the head of published worksheets; the \"upload\" patch adds support to the \"upload a worksheet\" stuff so that it parses and downloads associated worksheets.\n\nRight now, however, it runs into a strange error that I don't understand. Try applying these patches, publishing a worksheet, and then using the worksheet's public URL in the upload box. You'll get a strange twisted error, the user's session will get messed up, but if you log back in, you'll see that the worksheet did get imported.\n\n(It's likely that it won't work at all with https URLs; we'll work on that later.)\n\nAny ideas?",
    "created_at": "2010-05-20T02:43:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7441#issuecomment-62531",
    "user": "https://github.com/dandrake"
}
```

Attachment [trac_7441_upload.patch](tarball://root/attachments/some-uuid/ticket7441/trac_7441_upload.patch) by @dandrake created at 2010-05-20 02:43:09

These two patches are a mostly-working implementation of these ideas. The "link_rel" patch simply adds the appropriate link into the head of published worksheets; the "upload" patch adds support to the "upload a worksheet" stuff so that it parses and downloads associated worksheets.

Right now, however, it runs into a strange error that I don't understand. Try applying these patches, publishing a worksheet, and then using the worksheet's public URL in the upload box. You'll get a strange twisted error, the user's session will get messed up, but if you log back in, you'll see that the worksheet did get imported.

(It's likely that it won't work at all with https URLs; we'll work on that later.)

Any ideas?



---

archive/issue_comments_062532.json:
```json
{
    "body": "#9875 turns out to be a dup of this request.\n\nIt's not clear to me that the current patch deal with #9875, though.  Dan, does the second patch also parse OLD published worksheets, and links in the form `http://www.sagenb.org/home/pub/2423` (that is, the directory)?  I assume that the first patch only will make it easier to upload html links on worksheets published *after* this patch is incorporated, not older published worksheets.\n\nOnce you clarify that, we can probably close #9875 as a dup.",
    "created_at": "2011-01-18T14:28:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7441#issuecomment-62532",
    "user": "https://github.com/kcrisman"
}
```

#9875 turns out to be a dup of this request.

It's not clear to me that the current patch deal with #9875, though.  Dan, does the second patch also parse OLD published worksheets, and links in the form `http://www.sagenb.org/home/pub/2423` (that is, the directory)?  I assume that the first patch only will make it easier to upload html links on worksheets published *after* this patch is incorporated, not older published worksheets.

Once you clarify that, we can probably close #9875 as a dup.



---

archive/issue_comments_062533.json:
```json
{
    "body": "Changing status from new to needs_work.",
    "created_at": "2011-01-18T14:28:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7441#issuecomment-62533",
    "user": "https://github.com/kcrisman"
}
```

Changing status from new to needs_work.



---

archive/issue_comments_062534.json:
```json
{
    "body": "Replying to [comment:5 kcrisman]:\n>  Dan, does the second patch also parse OLD published worksheets, and links in the form `http://www.sagenb.org/home/pub/2423` (that is, the directory)?  I assume that the first patch only will make it easier to upload html links on worksheets published *after* this patch is incorporated, not older published worksheets.\n\n\nThat's correct. My intent here is to only affect worksheets published *after* these patches are put in. Users can always republish a worksheet to get the new stuff included in the published version.",
    "created_at": "2011-01-19T05:15:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7441#issuecomment-62534",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:5 kcrisman]:
>  Dan, does the second patch also parse OLD published worksheets, and links in the form `http://www.sagenb.org/home/pub/2423` (that is, the directory)?  I assume that the first patch only will make it easier to upload html links on worksheets published *after* this patch is incorporated, not older published worksheets.


That's correct. My intent here is to only affect worksheets published *after* these patches are put in. Users can always republish a worksheet to get the new stuff included in the published version.



---

archive/issue_comments_062535.json:
```json
{
    "body": "Also, note that with the notebook rewrite, the bits that affect `twist.py` will have to be rewritten for the new Flask version of the notebook.",
    "created_at": "2011-01-19T05:18:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7441#issuecomment-62535",
    "user": "https://github.com/dandrake"
}
```

Also, note that with the notebook rewrite, the bits that affect `twist.py` will have to be rewritten for the new Flask version of the notebook.



---

archive/issue_comments_062536.json:
```json
{
    "body": "Is this resolved by [this github PR](https://github.com/sagemath/sagenb/pull/56)?",
    "created_at": "2012-07-06T00:12:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7441#issuecomment-62536",
    "user": "https://github.com/kcrisman"
}
```

Is this resolved by [this github PR](https://github.com/sagemath/sagenb/pull/56)?



---

archive/issue_events_017643.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7441",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7441#event-17643"
}
```



---

archive/issue_events_017644.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7441",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7441#event-17644"
}
```



---

archive/issue_events_017645.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7441",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7441#event-17645"
}
```



---

archive/issue_events_017646.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7441",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7441#event-17646"
}
```



---

archive/issue_events_017647.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7441",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7441#event-17647"
}
```



---

archive/issue_events_017648.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7441",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7441#event-17648"
}
```



---

archive/issue_events_017649.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7441",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7441#event-17649"
}
```



---

archive/issue_events_017650.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2014-09-17T02:46:24Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7441",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7441#event-17650"
}
```



---

archive/issue_events_017651.json:
```json
{
    "actor": "https://github.com/kcrisman",
    "created_at": "2014-09-17T02:46:24Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7441",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7441#event-17651"
}
```



---

archive/issue_comments_062537.json:
```json
{
    "body": "Changing status from needs_work to positive_review.",
    "created_at": "2014-09-17T02:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7441#issuecomment-62537",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_work to positive_review.



---

archive/issue_comments_062538.json:
```json
{
    "body": "I can confirm this works now!",
    "created_at": "2014-09-17T02:46:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7441#issuecomment-62538",
    "user": "https://github.com/kcrisman"
}
```

I can confirm this works now!



---

archive/issue_comments_062539.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-09-18T18:00:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7441",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7441#issuecomment-62539",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_017652.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-09-18T18:00:23Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7441",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7441#event-17652"
}
```
