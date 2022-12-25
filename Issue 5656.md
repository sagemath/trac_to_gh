# Issue 5656: add hint to lift() function to docstring of groebner_basis()

archive/issues_005656.json:
```json
{
    "body": "Assignee: @malb\n\nKeywords: docstring, doc, Groebner basis\n\nOn [sage-support]:\n> > On Tuesday 31 March 2009, Florian wrote:\n> > Hello everyone,\n> > \n> > I've been trying to figure out whether the following \n> > functionality is implemented, but so far I could not. I was \n> > hoping that anyone would know if it existed and in that case \n> > what the syntax is.\n> > \n> > Suppose you computed the reduced Groebner Basis G of an ideal \n> > I= (f1,...,fn) in some polynomial ring R, and suppose that \n> > that Groebner Basis turned out to be G=(1). Is there a \n> > function that finds some, maybe even all, combinations of \n> > coefficients h1,...,hn such that h1*f1+...+hn*fn=1?\n> > \n> > This is basically a byproduct of e.g. the Buchberger \n> > Algorithm. The question is whether this information can be \n> > accessed.\n\nMartin answers ... and William Stein replies:\n> Martin, since this is a frequently asked question, do you think\n> something about this should be added to the groebner_basis \n> docstring?  The groebner_basis docstring is 3 pages right now, so \n> this shouldn't be too far down there.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5656\n\n",
    "created_at": "2009-04-01T11:25:00Z",
    "labels": [
        "component: commutative algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0.1",
    "title": "add hint to lift() function to docstring of groebner_basis()",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5656",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

Keywords: docstring, doc, Groebner basis

On [sage-support]:
> > On Tuesday 31 March 2009, Florian wrote:
> > Hello everyone,
> > 
> > I've been trying to figure out whether the following 
> > functionality is implemented, but so far I could not. I was 
> > hoping that anyone would know if it existed and in that case 
> > what the syntax is.
> > 
> > Suppose you computed the reduced Groebner Basis G of an ideal 
> > I= (f1,...,fn) in some polynomial ring R, and suppose that 
> > that Groebner Basis turned out to be G=(1). Is there a 
> > function that finds some, maybe even all, combinations of 
> > coefficients h1,...,hn such that h1*f1+...+hn*fn=1?
> > 
> > This is basically a byproduct of e.g. the Buchberger 
> > Algorithm. The question is whether this information can be 
> > accessed.

Martin answers ... and William Stein replies:
> Martin, since this is a frequently asked question, do you think
> something about this should be added to the groebner_basis 
> docstring?  The groebner_basis docstring is 3 pages right now, so 
> this shouldn't be too far down there.

Issue created by migration from https://trac.sagemath.org/ticket/5656





---

archive/issue_comments_044144.json:
```json
{
    "body": "Attachment [gb_lift.patch](tarball://root/attachments/some-uuid/ticket5656/gb_lift.patch) by @malb created at 2009-05-12 01:55:46",
    "created_at": "2009-05-12T01:55:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5656#issuecomment-44144",
    "user": "https://github.com/malb"
}
```

Attachment [gb_lift.patch](tarball://root/attachments/some-uuid/ticket5656/gb_lift.patch) by @malb created at 2009-05-12 01:55:46



---

archive/issue_comments_044145.json:
```json
{
    "body": "Attachment [trac_5656-gb_lift-revised.patch](tarball://root/attachments/some-uuid/ticket5656/trac_5656-gb_lift-revised.patch) by @burcin created at 2009-06-04 13:50:50\n\nrevision of Martin's patch",
    "created_at": "2009-06-04T13:50:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5656#issuecomment-44145",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_5656-gb_lift-revised.patch](tarball://root/attachments/some-uuid/ticket5656/trac_5656-gb_lift-revised.patch) by @burcin created at 2009-06-04 13:50:50

revision of Martin's patch



---

archive/issue_comments_044146.json:
```json
{
    "body": "I posted a revised version of Martin's patch, attachment:trac_5656-gb_lift-revised.patch, the changes are:\n\n* fix places where !`` was used for math instead of `\n* provide a link to the .lift() method\n* remove the long lines in the INPUT section",
    "created_at": "2009-06-04T13:58:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5656#issuecomment-44146",
    "user": "https://github.com/burcin"
}
```

I posted a revised version of Martin's patch, attachment:trac_5656-gb_lift-revised.patch, the changes are:

* fix places where !`` was used for math instead of `
* provide a link to the .lift() method
* remove the long lines in the INPUT section



---

archive/issue_comments_044147.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-06-04T18:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5656#issuecomment-44147",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_005899.json:
```json
{
    "actor": "@mwhansen",
    "created_at": "2009-06-04T18:28:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5656",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5656#event-5899"
}
```



---

archive/issue_comments_044148.json:
```json
{
    "body": "Merged trac_5656-gb_lift-revised.patch in 4.0.1.rc1.",
    "created_at": "2009-06-04T18:28:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5656",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5656#issuecomment-44148",
    "user": "https://github.com/mwhansen"
}
```

Merged trac_5656-gb_lift-revised.patch in 4.0.1.rc1.
