# Issue 7441: notebook: make it possible to upload from the url of a published worksheet

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-11-12 06:40:03

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



---

Comment by ddrake created at 2010-03-02 09:31:32

Let me add another +1 to this. It would make it much easier when teaching -- I write up a worksheet for an assignment, publish it, and then tell the students the URL. They log into their accounts, hit upload, paste in the URL, and they have the worksheet. As it stands, either I or my students needs to manually save the worksheet file somewhere and do something with it.

As a quick and dirty hack, I see that published worksheets have something like this in their html source:

<li><a href="download/blargle floomp.sws">Download.</a></li>

...so maybe, when given a url that does not end in .sws, the upload mechanism could just suck in the html source, look for the first hyperlink tag that resembles the above, and use that URL? I'm thinking a regex of `<a href="download/.*\.sws">` or similar.

Some kind of magic incantation in the html would also allow people to use random web pages as upload sources; imagine taking the URL of a blog post and putting into the upload box, and it automagically finds a .sws file to download. This could be the html version of the "embed a .sws file into a pdf" idea that has been discussed before.


---

Comment by ddrake created at 2010-03-02 09:34:11

Well, that's my "don't forget to use preview" lesson for today...

Replying to [comment:1 ddrake]:
> published worksheets have something like this in their html source:

I meant to follow that with:


```
<li><a href="download/blargle floomp.sws">Download.</a></li>
```



---

Comment by ddrake created at 2010-03-26 01:50:43

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

Comment by ddrake created at 2010-05-20 02:37:07

add <link rel="alternate"... stuff to published worksheets


---

Attachment

add support to "upload a worksheet" page for parsing <link rel="alternate"... links


---

Attachment

These two patches are a mostly-working implementation of these ideas. The "link_rel" patch simply adds the appropriate link into the head of published worksheets; the "upload" patch adds support to the "upload a worksheet" stuff so that it parses and downloads associated worksheets.

Right now, however, it runs into a strange error that I don't understand. Try applying these patches, publishing a worksheet, and then using the worksheet's public URL in the upload box. You'll get a strange twisted error, the user's session will get messed up, but if you log back in, you'll see that the worksheet did get imported.

(It's likely that it won't work at all with https URLs; we'll work on that later.)

Any ideas?


---

Comment by kcrisman created at 2011-01-18 14:28:19

#9875 turns out to be a dup of this request.

It's not clear to me that the current patch deal with #9875, though.  Dan, does the second patch also parse OLD published worksheets, and links in the form `http://www.sagenb.org/home/pub/2423` (that is, the directory)?  I assume that the first patch only will make it easier to upload html links on worksheets published *after* this patch is incorporated, not older published worksheets.

Once you clarify that, we can probably close #9875 as a dup.


---

Comment by kcrisman created at 2011-01-18 14:28:19

Changing status from new to needs_work.


---

Comment by ddrake created at 2011-01-19 05:15:11

Replying to [comment:5 kcrisman]:
>  Dan, does the second patch also parse OLD published worksheets, and links in the form `http://www.sagenb.org/home/pub/2423` (that is, the directory)?  I assume that the first patch only will make it easier to upload html links on worksheets published *after* this patch is incorporated, not older published worksheets.

That's correct. My intent here is to only affect worksheets published *after* these patches are put in. Users can always republish a worksheet to get the new stuff included in the published version.


---

Comment by ddrake created at 2011-01-19 05:18:48

Also, note that with the notebook rewrite, the bits that affect `twist.py` will have to be rewritten for the new Flask version of the notebook.


---

Comment by kcrisman created at 2012-07-06 00:12:02

Is this resolved by [this github PR](https://github.com/sagemath/sagenb/pull/56)?


---

Comment by kcrisman created at 2014-09-17 02:46:24

Changing status from needs_work to positive_review.


---

Comment by kcrisman created at 2014-09-17 02:46:24

I can confirm this works now!


---

Comment by vbraun created at 2014-09-18 18:00:23

Resolution: fixed
