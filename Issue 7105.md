# Issue 7105: change search_doc and search_src so the links are opened in a new tab/window

archive/issues_007105.json:
```json
{
    "body": "Assignee: boothby\n\nOne way would be to add target=\"_new\" right before href=\"...\". \n\nThe justification for this change is that currently after looking at the docs one hits the backbutton which results in a corrupted view of the worksheet (for now). \n\nIssue created by migration from https://trac.sagemath.org/ticket/7105\n\n",
    "created_at": "2009-10-04T05:36:58Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.7",
    "title": "change search_doc and search_src so the links are opened in a new tab/window",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7105",
    "user": "@williamstein"
}
```
Assignee: boothby

One way would be to add target="_new" right before href="...". 

The justification for this change is that currently after looking at the docs one hits the backbutton which results in a corrupted view of the worksheet (for now). 

Issue created by migration from https://trac.sagemath.org/ticket/7105





---

archive/issue_comments_058813.json:
```json
{
    "body": "I think another way would be to save the search results to a file -- `format_search_as_html` may already put things in the right format -- and open that file using \n\n```\n  from sage.misc.viewer import browser\n  import os\n  url = .. file name ...\n  os.system(browser() + \" \" + url)\n```\n",
    "created_at": "2009-10-04T16:14:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7105#issuecomment-58813",
    "user": "@jhpalmieri"
}
```

I think another way would be to save the search results to a file -- `format_search_as_html` may already put things in the right format -- and open that file using 

```
  from sage.misc.viewer import browser
  import os
  url = .. file name ...
  os.system(browser() + " " + url)
```




---

archive/issue_comments_058814.json:
```json
{
    "body": "Possibly good idea.  I did something like this with \"help(foo)\", where it creates a link to a page that opens in a new browser.",
    "created_at": "2009-10-04T19:05:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7105#issuecomment-58814",
    "user": "@williamstein"
}
```

Possibly good idea.  I did something like this with "help(foo)", where it creates a link to a page that opens in a new browser.



---

archive/issue_comments_058815.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2011-03-25T22:53:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7105#issuecomment-58815",
    "user": "@jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_058816.json:
```json
{
    "body": "Here's a patch.",
    "created_at": "2011-03-25T22:53:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7105#issuecomment-58816",
    "user": "@jhpalmieri"
}
```

Here's a patch.



---

archive/issue_comments_058817.json:
```json
{
    "body": "Attachment [trac_7105-search.patch](tarball://root/attachments/some-uuid/ticket7105/trac_7105-search.patch) by @jhpalmieri created at 2011-03-25 22:54:10",
    "created_at": "2011-03-25T22:54:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7105#issuecomment-58817",
    "user": "@jhpalmieri"
}
```

Attachment [trac_7105-search.patch](tarball://root/attachments/some-uuid/ticket7105/trac_7105-search.patch) by @jhpalmieri created at 2011-03-25 22:54:10



---

archive/issue_comments_058818.json:
```json
{
    "body": "By the way, according to [this link](http://thedesignspace.net/MT2archives/000316.html), `target=\"_blank\"` is preferable to `target=\"_new\"`.  This fits with my experience, also.",
    "created_at": "2011-03-25T22:55:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7105#issuecomment-58818",
    "user": "@jhpalmieri"
}
```

By the way, according to [this link](http://thedesignspace.net/MT2archives/000316.html), `target="_blank"` is preferable to `target="_new"`.  This fits with my experience, also.



---

archive/issue_comments_058819.json:
```json
{
    "body": "Oh, this is a great idea.  I'll try to review it soon if no one else does.",
    "created_at": "2011-03-28T18:38:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7105#issuecomment-58819",
    "user": "@kcrisman"
}
```

Oh, this is a great idea.  I'll try to review it soon if no one else does.



---

archive/issue_comments_058820.json:
```json
{
    "body": "It only took a year and half to implement.  Since the main part of the patch is the addition of 16 characters (the rest is modification to doctests), that's about one character per month...",
    "created_at": "2011-03-28T18:45:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7105#issuecomment-58820",
    "user": "@jhpalmieri"
}
```

It only took a year and half to implement.  Since the main part of the patch is the addition of 16 characters (the rest is modification to doctests), that's about one character per month...



---

archive/issue_comments_058821.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-03-29T20:03:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7105#issuecomment-58821",
    "user": "@kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_058822.json:
```json
{
    "body": "Okay, this looks okay and works.  Definitely an improvement - I had never used the search much in the notebook because it just gave a list of files.\n\nI have to say, I really don't like that it gives you the file.  Getting the whole plot/plot.py isn't very useful!  I mean, you can do a text search, but the command-line experience is much better than that.",
    "created_at": "2011-03-29T20:03:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7105#issuecomment-58822",
    "user": "@kcrisman"
}
```

Okay, this looks okay and works.  Definitely an improvement - I had never used the search much in the notebook because it just gave a list of files.

I have to say, I really don't like that it gives you the file.  Getting the whole plot/plot.py isn't very useful!  I mean, you can do a text search, but the command-line experience is much better than that.



---

archive/issue_comments_058823.json:
```json
{
    "body": "Replying to [comment:7 kcrisman]:\n> I have to say, I really don't like that it gives you the file.  Getting the whole plot/plot.py isn't very useful!  I mean, you can do a text search, but the command-line experience is much better than that.\n\nI'm trying to think of what else we could do.  If you do \"search_src\", it opens up the source code, but there are no tags or any other way to navigate the resulting page.  Maybe we could highlight the search terms somehow?  This probably requires some javascript, about which I know basically nothing.  If you do \"search_doc\", it opens up the html documentation, which has tags, and maybe we could jump to the tag nearest the first instance of the search terms.  Another option for search_doc would be to defer to Sphinx's search, which highlights code and jumps to some instance (not necessarily the first, maybe the best match?).",
    "created_at": "2011-03-29T20:59:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7105#issuecomment-58823",
    "user": "@jhpalmieri"
}
```

Replying to [comment:7 kcrisman]:
> I have to say, I really don't like that it gives you the file.  Getting the whole plot/plot.py isn't very useful!  I mean, you can do a text search, but the command-line experience is much better than that.

I'm trying to think of what else we could do.  If you do "search_src", it opens up the source code, but there are no tags or any other way to navigate the resulting page.  Maybe we could highlight the search terms somehow?  This probably requires some javascript, about which I know basically nothing.  If you do "search_doc", it opens up the html documentation, which has tags, and maybe we could jump to the tag nearest the first instance of the search terms.  Another option for search_doc would be to defer to Sphinx's search, which highlights code and jumps to some instance (not necessarily the first, maybe the best match?).



---

archive/issue_comments_058824.json:
```json
{
    "body": "I don't know why it can't literally return the output of search_src in the command line. Maybe because that's piped into less?\n\nWell, in any case this is another ticket. No point turning this into the next ticket to nowhere.",
    "created_at": "2011-03-29T21:11:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7105#issuecomment-58824",
    "user": "@kcrisman"
}
```

I don't know why it can't literally return the output of search_src in the command line. Maybe because that's piped into less?

Well, in any case this is another ticket. No point turning this into the next ticket to nowhere.



---

archive/issue_comments_058825.json:
```json
{
    "body": "Replying to [comment:9 kcrisman]:\n> I don't know why it can't literally return the output of search_src in the command line. Maybe because that's piped into less?\n\nNo, the command `_format_search_as_html` deliberately ignores multiple matches in the same file, along with the line numbers and the line containing each match -- it just uses the file name.  The extra information is there, but it's discarded.  I wonder if there's a good way to present it.  Figure out a way to use javascript to open up a Python file to a specified line, and then give one link for each matching line?  Also keep the current version as a more compact option?\n\n> Well, in any case this is another ticket. No point turning this into the next ticket to nowhere.\n\nI agree, I'm just brainstorming.",
    "created_at": "2011-03-29T21:37:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7105#issuecomment-58825",
    "user": "@jhpalmieri"
}
```

Replying to [comment:9 kcrisman]:
> I don't know why it can't literally return the output of search_src in the command line. Maybe because that's piped into less?

No, the command `_format_search_as_html` deliberately ignores multiple matches in the same file, along with the line numbers and the line containing each match -- it just uses the file name.  The extra information is there, but it's discarded.  I wonder if there's a good way to present it.  Figure out a way to use javascript to open up a Python file to a specified line, and then give one link for each matching line?  Also keep the current version as a more compact option?

> Well, in any case this is another ticket. No point turning this into the next ticket to nowhere.

I agree, I'm just brainstorming.



---

archive/issue_comments_058826.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-04-13T07:42:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7105",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7105#issuecomment-58826",
    "user": "@jdemeyer"
}
```

Resolution: fixed
