# Issue 9428: Internationalize the Sage Notebook

archive/issues_009428.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  ddrake aquino.luizclaudio@gmail.com robert.marik\n\nThis patch internationalizes the Sage Notebook and adds a localization to Brazilian Portuguese.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9428\n\n",
    "created_at": "2010-07-05T09:37:24Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "title": "Internationalize the Sage Notebook",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9428",
    "user": "timdumol"
}
```
Assignee: jason, was

CC:  ddrake aquino.luizclaudio@gmail.com robert.marik

This patch internationalizes the Sage Notebook and adds a localization to Brazilian Portuguese.

Issue created by migration from https://trac.sagemath.org/ticket/9428





---

archive/issue_comments_089952.json:
```json
{
    "body": "Changing type from defect to enhancement.",
    "created_at": "2010-07-05T09:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89952",
    "user": "timdumol"
}
```

Changing type from defect to enhancement.



---

archive/issue_comments_089953.json:
```json
{
    "body": "i18n the notebook and adds a l20n to pt_BR",
    "created_at": "2010-07-05T09:45:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89953",
    "user": "timdumol"
}
```

i18n the notebook and adds a l20n to pt_BR



---

archive/issue_comments_089954.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-05T09:46:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89954",
    "user": "timdumol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_089955.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-07-05T09:46:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89955",
    "user": "timdumol"
}
```

Attachment



---

archive/issue_comments_089956.json:
```json
{
    "body": "Attachment\n\nRebase on SageNB 0.8.1. Replaces previous patch.",
    "created_at": "2010-07-05T12:43:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89956",
    "user": "timdumol"
}
```

Attachment

Rebase on SageNB 0.8.1. Replaces previous patch.



---

archive/issue_comments_089957.json:
```json
{
    "body": "Good idea. I will make the loading lazy, although the languages loaded will stay in memory, since there are multiple users using the notebook, who may each require a different language.",
    "created_at": "2010-07-05T14:31:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89957",
    "user": "timdumol"
}
```

Good idea. I will make the loading lazy, although the languages loaded will stay in memory, since there are multiple users using the notebook, who may each require a different language.



---

archive/issue_comments_089958.json:
```json
{
    "body": "Defers language loading until requested.",
    "created_at": "2010-07-05T14:54:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89958",
    "user": "timdumol"
}
```

Defers language loading until requested.



---

archive/issue_comments_089959.json:
```json
{
    "body": "Attachment\n\nA package with this patch (tentatively SageNB 0.9) based on SageNB 0.8.1 is avaialable at http://sage.math.washington.edu/home/timdumol/sagenb-0.9.spkg",
    "created_at": "2010-07-05T15:24:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89959",
    "user": "timdumol"
}
```

Attachment

A package with this patch (tentatively SageNB 0.9) based on SageNB 0.8.1 is avaialable at http://sage.math.washington.edu/home/timdumol/sagenb-0.9.spkg



---

archive/issue_comments_089960.json:
```json
{
    "body": "Since the package is based on SageNB 0.8.1 (#9430), you'll need to apply the main sage library patch to at #7379 (run hg_sage.apply('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7379/trac-7379-decorator-defaults.patch'), then restart sage with sage -br).\n\nI have moved the translation of the description strings and group strings to the html generation function so as to be able to dynamically change the language.\n\nThe new package (at the same url) removes conf_lcma.py.",
    "created_at": "2010-07-06T09:34:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89960",
    "user": "timdumol"
}
```

Since the package is based on SageNB 0.8.1 (#9430), you'll need to apply the main sage library patch to at #7379 (run hg_sage.apply('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7379/trac-7379-decorator-defaults.patch'), then restart sage with sage -br).

I have moved the translation of the description strings and group strings to the html generation function so as to be able to dynamically change the language.

The new package (at the same url) removes conf_lcma.py.



---

archive/issue_comments_089961.json:
```json
{
    "body": "Replaces all others. Adds a few more strings to translation, and implements dummy _() functions, as described in comments.",
    "created_at": "2010-08-17T16:55:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89961",
    "user": "timdumol"
}
```

Replaces all others. Adds a few more strings to translation, and implements dummy _() functions, as described in comments.



---

archive/issue_comments_089962.json:
```json
{
    "body": "Attachment\n\nAdded a couple more strings to translation. Replaces all others.",
    "created_at": "2010-08-19T11:24:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89962",
    "user": "timdumol"
}
```

Attachment

Added a couple more strings to translation. Replaces all others.



---

archive/issue_comments_089963.json:
```json
{
    "body": "New test package at http://sage.math.washington.edu/home/timdumol/sagenb-0.8.2-dev-i18n.spkg fixing all noted issues.",
    "created_at": "2010-08-19T14:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89963",
    "user": "timdumol"
}
```

New test package at http://sage.math.washington.edu/home/timdumol/sagenb-0.8.2-dev-i18n.spkg fixing all noted issues.



---

archive/issue_comments_089964.json:
```json
{
    "body": "Hi, thank you for this great work. I have several comments:\n\nI installed sagenb-0.8.2-dev-i18n.spkg and started Sage. I got error caused by empty locale directory. However, this has been fixed after installing portugese and czech translations. Is this behavior intented?\n\nI have seen that some strings have been changed from the version announced in [sage-notebook mailing list](http://groups.google.cz/group/sage-notebook/browse_thread/thread/9b7b6aee9e331962), but I was not able to find the sagenb.pot with strings for translations.\n\nIf anyone is interested, I have one feature request related to the strings \"XX minutes ago\". It is [requested](http://groups.google.cz/group/sage-notebook/msg/1eae0947a08c16a5?) in the sage-notebook in the thread linked above. Could this be fixed? Many thanks.\n\nbtw: How to review this trac? I have seen [devel comments](http://nb.sagemath.org/dev.html). Is it reasonable to run doctests for sagenb tickets?",
    "created_at": "2010-08-24T07:19:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89964",
    "user": "robert.marik"
}
```

Hi, thank you for this great work. I have several comments:

I installed sagenb-0.8.2-dev-i18n.spkg and started Sage. I got error caused by empty locale directory. However, this has been fixed after installing portugese and czech translations. Is this behavior intented?

I have seen that some strings have been changed from the version announced in [sage-notebook mailing list](http://groups.google.cz/group/sage-notebook/browse_thread/thread/9b7b6aee9e331962), but I was not able to find the sagenb.pot with strings for translations.

If anyone is interested, I have one feature request related to the strings "XX minutes ago". It is [requested](http://groups.google.cz/group/sage-notebook/msg/1eae0947a08c16a5?) in the sage-notebook in the thread linked above. Could this be fixed? Many thanks.

btw: How to review this trac? I have seen [devel comments](http://nb.sagemath.org/dev.html). Is it reasonable to run doctests for sagenb tickets?



---

archive/issue_comments_089965.json:
```json
{
    "body": "Attachment\n\nReplaces previous patches. Added the requested \"XX <time> ago\" fix. Updated the sagenb.po file with the latest strings to be translated. Added sagenb/locale to the package data list.",
    "created_at": "2010-08-26T09:23:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89965",
    "user": "timdumol"
}
```

Attachment

Replaces previous patches. Added the requested "XX <time> ago" fix. Updated the sagenb.po file with the latest strings to be translated. Added sagenb/locale to the package data list.



---

archive/issue_comments_089966.json:
```json
{
    "body": "Hi,\n\nThere is a new package version at the same url: http://sage.math.washington.edu/home/timdumol/sagenb-0.8.2-dev-i18n.spkg\n\nThe error regarding the missing locale directory was a bug. The new patch fixes this, and addresses your issue regarding \"XX <time units> ago\".\n\nThe new translations are found in `sagenb.po`.",
    "created_at": "2010-08-26T11:52:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89966",
    "user": "timdumol"
}
```

Hi,

There is a new package version at the same url: http://sage.math.washington.edu/home/timdumol/sagenb-0.8.2-dev-i18n.spkg

The error regarding the missing locale directory was a bug. The new patch fixes this, and addresses your issue regarding "XX <time units> ago".

The new translations are found in `sagenb.po`.



---

archive/issue_comments_089967.json:
```json
{
    "body": "Hi, thank you for the patch\n\n1. Installs fine, works as expected\n\n2. sage -t -sagenb passed\n\n3. I was not able to configure selenium tests, got errors like \"unable to start browser\". Do I need to run these tests to give a positive review to this ticket?\n\n4. It seems that the issue \"XX <time units> ago\" has not been resolved. The workseet.py still contains\n\n```\n    def _saved_by_info(self, x, username=None):\n        try:\n            u = self.__saved_by_info[x]\n            return ' '+_('ago by %s', username)%u\n        except (KeyError,AttributeError):\n            return ' '+_('ago', username)\n```\n\nand I do not have possibility to put internationalized text on the front of the number, like \n\"pred 10 sekundami\". But no matter, can be resolved later on a ticket which adds Czech translation which is also finished.",
    "created_at": "2010-08-27T21:32:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89967",
    "user": "robert.marik"
}
```

Hi, thank you for the patch

1. Installs fine, works as expected

2. sage -t -sagenb passed

3. I was not able to configure selenium tests, got errors like "unable to start browser". Do I need to run these tests to give a positive review to this ticket?

4. It seems that the issue "XX <time units> ago" has not been resolved. The workseet.py still contains

```
    def _saved_by_info(self, x, username=None):
        try:
            u = self.__saved_by_info[x]
            return ' '+_('ago by %s', username)%u
        except (KeyError,AttributeError):
            return ' '+_('ago', username)
```

and I do not have possibility to put internationalized text on the front of the number, like 
"pred 10 sekundami". But no matter, can be resolved later on a ticket which adds Czech translation which is also finished.



---

archive/issue_comments_089968.json:
```json
{
    "body": "I observed that if I click in worksheet to Undo button, the Last Edited field does not contain the name of the author, but the word \"ago\". Switching languages does not change the string in the field Last Edited. The string is always in the notebook default language.\n\nDo you have the same behavior? Do you know how to fix this? I think that there should be no strings for translation in the function _saved_by_info, since the whole phrase is translated in the function snapshot_data. Is this right?\n\nIf you prepare new version, could you add the directory cs_CZ and the file from \nhttp://user.mendelu.cz/marik/sage/sagenb.po ?\n\nI tested extensivelly the last version of the sagenb package and everything works fine, with one exception in Last Edited field described above.\n\nIt seems that the welcome page and registration process must be in the default language of the notebook right now. Could this be improved in some later versions?\n\nStill trying to make selenium tests work in order to finish review of this ticket... \n\nMany thanks for working on i18n!",
    "created_at": "2010-08-28T18:49:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89968",
    "user": "robert.marik"
}
```

I observed that if I click in worksheet to Undo button, the Last Edited field does not contain the name of the author, but the word "ago". Switching languages does not change the string in the field Last Edited. The string is always in the notebook default language.

Do you have the same behavior? Do you know how to fix this? I think that there should be no strings for translation in the function _saved_by_info, since the whole phrase is translated in the function snapshot_data. Is this right?

If you prepare new version, could you add the directory cs_CZ and the file from 
http://user.mendelu.cz/marik/sage/sagenb.po ?

I tested extensivelly the last version of the sagenb package and everything works fine, with one exception in Last Edited field described above.

It seems that the welcome page and registration process must be in the default language of the notebook right now. Could this be improved in some later versions?

Still trying to make selenium tests work in order to finish review of this ticket... 

Many thanks for working on i18n!



---

archive/issue_comments_089969.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-09-08T08:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89969",
    "user": "robert.marik"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_089970.json:
```json
{
    "body": "The \"last edited\" field in the \"Undo\" part of the notebook is always in the default notebook language and does not change when changing account settings.\n\nThe other things work. Excellent! Is is easy to fix this last issue? Many thanks.",
    "created_at": "2010-09-08T08:58:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89970",
    "user": "robert.marik"
}
```

The "last edited" field in the "Undo" part of the notebook is always in the default notebook language and does not change when changing account settings.

The other things work. Excellent! Is is easy to fix this last issue? Many thanks.



---

archive/issue_comments_089971.json:
```json
{
    "body": "The last part shouldn't be too difficult to fix. I've added your localization.",
    "created_at": "2010-09-10T02:23:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89971",
    "user": "timdumol"
}
```

The last part shouldn't be too difficult to fix. I've added your localization.



---

archive/issue_comments_089972.json:
```json
{
    "body": "Attachment\n\nReplaces all previous. Really fixed the undo problem.",
    "created_at": "2010-09-10T03:55:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89972",
    "user": "timdumol"
}
```

Attachment

Replaces all previous. Really fixed the undo problem.



---

archive/issue_comments_089973.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-09-10T04:07:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89973",
    "user": "timdumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089974.json:
```json
{
    "body": "The latest version of the pkg is up at http://sage.math.washington.edu/home/timdumol/sagenb-0.8.2-dev-i18n.spkg. I've included your sagenb.po, and the above patch. Please be advised that there is a new string to be translated (\"%s ago\").",
    "created_at": "2010-09-10T04:07:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89974",
    "user": "timdumol"
}
```

The latest version of the pkg is up at http://sage.math.washington.edu/home/timdumol/sagenb-0.8.2-dev-i18n.spkg. I've included your sagenb.po, and the above patch. Please be advised that there is a new string to be translated ("%s ago").



---

archive/issue_comments_089975.json:
```json
{
    "body": "Replaces all others. Fixed a bug in the fix.",
    "created_at": "2010-09-11T02:54:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89975",
    "user": "timdumol"
}
```

Replaces all others. Fixed a bug in the fix.



---

archive/issue_comments_089976.json:
```json
{
    "body": "Attachment\n\nNew package version here: http://sage.math.washington.edu/home/timdumol/sagenb-0.8.2-dev-i18n.spkg fixing the bug in Undo.",
    "created_at": "2010-09-11T05:27:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89976",
    "user": "timdumol"
}
```

Attachment

New package version here: http://sage.math.washington.edu/home/timdumol/sagenb-0.8.2-dev-i18n.spkg fixing the bug in Undo.



---

archive/issue_comments_089977.json:
```json
{
    "body": "Another package version at the same url fixing a minor doctest error.",
    "created_at": "2010-09-11T14:53:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89977",
    "user": "timdumol"
}
```

Another package version at the same url fixing a minor doctest error.



---

archive/issue_comments_089978.json:
```json
{
    "body": "Fixed a failing doctest.",
    "created_at": "2010-09-11T14:56:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89978",
    "user": "timdumol"
}
```

Fixed a failing doctest.



---

archive/issue_comments_089979.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-09-11T18:38:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89979",
    "user": "robert.marik"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_089980.json:
```json
{
    "body": "Attachment\n\nLooks fine for me, instals fine, works fine, no problems found when using it for a longer time and for many various things.\n\nAll doctests (sage -t -sagenb) passed. \n\nVery very important patch, thank you.\n\nI am not able to check the Brazilian Portugese, but despite this fact I give a positive review! \n\nMany thanks for this work.",
    "created_at": "2010-09-11T18:38:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89980",
    "user": "robert.marik"
}
```

Attachment

Looks fine for me, instals fine, works fine, no problems found when using it for a longer time and for many various things.

All doctests (sage -t -sagenb) passed. 

Very very important patch, thank you.

I am not able to check the Brazilian Portugese, but despite this fact I give a positive review! 

Many thanks for this work.



---

archive/issue_comments_089981.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-09-14T19:14:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89981",
    "user": "LuizAquino"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_089982.json:
```json
{
    "body": "I observed the follow issues:\n\n- When we create a new user the language for them is the default one (as\nwe expected). But when we go to the page \"Settings > Account Setting\" of\nthis user we see \"en_US\" as the user language and not the default one,\nbeside the pages are actually in the default one.\n\n- The language for the JavaScript code is in the default one and not in\nthe user one. For example, if the default language is \"en_US\" and the\nuser language is \"pt_BR\", then when we click on the link \"Esvaziar\nLixeira\" (Empty Trash) at the page \"Lixeira\" (Trash) the message appears\nin English and not in Portuguese.\n\n- When we change the default language the language for the JavaScript\ncode is still the old one. We need to restart the Notebook to update the\nlanguage for the JavaScript code. By the way, I think that the language\nfor the JavaScript should be the same as the user.\n\n- When we set a \"simple\" challenge for account registration the question\nin the registration process is in the default language as we expected,\nbut we have to give the answer in English. For example, if the default\nlanguage is \"pt_BR\" and we answer the question \"Quanto \u00e9 2 mais\n3?\" (What is 2 plus 3?) with \"cinco\" (five) we get an error. But, if we\nanswer that question with \"five\", we don't get an error. So, the\nquestion is in Portuguese but we have to give the answer in English.\n\n- The messages in the \"Last Edited\" column at the pages \"Home\" and\n\"Published\" are wrong. Each message is in two languages: the first half\nis in the default language and the second half is in the user language.\n\nI updated the pt_br locale files. I made some corrections and I translated the new strings. Please, add this to the next sagenb package:\n\nhttp://sites.google.com/site/lcmaquino/sage/sagenb_pt_BR.tar.gz?attredirects=0&d=1",
    "created_at": "2010-09-14T19:14:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89982",
    "user": "LuizAquino"
}
```

I observed the follow issues:

- When we create a new user the language for them is the default one (as
we expected). But when we go to the page "Settings > Account Setting" of
this user we see "en_US" as the user language and not the default one,
beside the pages are actually in the default one.

- The language for the JavaScript code is in the default one and not in
the user one. For example, if the default language is "en_US" and the
user language is "pt_BR", then when we click on the link "Esvaziar
Lixeira" (Empty Trash) at the page "Lixeira" (Trash) the message appears
in English and not in Portuguese.

- When we change the default language the language for the JavaScript
code is still the old one. We need to restart the Notebook to update the
language for the JavaScript code. By the way, I think that the language
for the JavaScript should be the same as the user.

- When we set a "simple" challenge for account registration the question
in the registration process is in the default language as we expected,
but we have to give the answer in English. For example, if the default
language is "pt_BR" and we answer the question "Quanto é 2 mais
3?" (What is 2 plus 3?) with "cinco" (five) we get an error. But, if we
answer that question with "five", we don't get an error. So, the
question is in Portuguese but we have to give the answer in English.

- The messages in the "Last Edited" column at the pages "Home" and
"Published" are wrong. Each message is in two languages: the first half
is in the default language and the second half is in the user language.

I updated the pt_br locale files. I made some corrections and I translated the new strings. Please, add this to the next sagenb package:

http://sites.google.com/site/lcmaquino/sage/sagenb_pt_BR.tar.gz?attredirects=0&d=1



---

archive/issue_comments_089983.json:
```json
{
    "body": "Attachment\n\nFixes the issues pointed out by LuizAquino. Updates pt_BR.",
    "created_at": "2010-09-15T16:19:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89983",
    "user": "timdumol"
}
```

Attachment

Fixes the issues pointed out by LuizAquino. Updates pt_BR.



---

archive/issue_comments_089984.json:
```json
{
    "body": "Thank you for pointing out these issues. I have posted a new patch, and a new package at the same url (http://sage.math.washington.edu/home/timdumol/sagenb-0.8.2-dev-i18n.spkg) addressing these issues.\n\nrobert.marik, it seems that some strings re: the notebook settings are left untranslated (Doc pool size, Type of challenge, etc.) in the cs_CZ locale.",
    "created_at": "2010-09-15T16:27:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89984",
    "user": "timdumol"
}
```

Thank you for pointing out these issues. I have posted a new patch, and a new package at the same url (http://sage.math.washington.edu/home/timdumol/sagenb-0.8.2-dev-i18n.spkg) addressing these issues.

robert.marik, it seems that some strings re: the notebook settings are left untranslated (Doc pool size, Type of challenge, etc.) in the cs_CZ locale.



---

archive/issue_comments_089985.json:
```json
{
    "body": "Replying to [comment:20 timdumol]:\n\n> robert.marik, it seems that some strings re: the notebook settings are left untranslated (Doc pool size, Type of challenge, etc.) in the cs_CZ locale.\n\nYes, I think that only admin (skilled person) can see these strings and he (she) is more familiar with the English terminology than the localized names. This should avoid some uncertainties. Do you accept this point of view?\n\nIs the new package ready for review?",
    "created_at": "2010-09-15T16:56:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89985",
    "user": "robert.marik"
}
```

Replying to [comment:20 timdumol]:

> robert.marik, it seems that some strings re: the notebook settings are left untranslated (Doc pool size, Type of challenge, etc.) in the cs_CZ locale.

Yes, I think that only admin (skilled person) can see these strings and he (she) is more familiar with the English terminology than the localized names. This should avoid some uncertainties. Do you accept this point of view?

Is the new package ready for review?



---

archive/issue_comments_089986.json:
```json
{
    "body": "Replying to [comment:20 timdumol]:\n> Thank you for pointing out these issues. I have posted a new patch, and a new package at the same url (http://sage.math.washington.edu/home/timdumol/sagenb-0.8.2-dev-i18n.spkg) addressing these issues.\n> \n\nThank you for solve those issues!\n\nBut, it seems we have another new ones:\n\n- When we click on the link \"New Worksheet\" at the \"Home\" page, the\nnew worksheet is created with a title in the default language and not in the user one. So, if the default language is \"en_US\" and the user one is \"pt_BR\", then when we click on \"Nova Planilha\" (New Worksheet) the worksheet will have the title \"Untitled\" and not \"Sem t\u00edtulo\".\n\n- When we plot a surface (using the function plot3d), the text \"Get Image\" (at the side of the plot window) and \"To save this image (...)\" (that appears when we click on \"Get Image\") are in English no matter what is the user language or default language.",
    "created_at": "2010-09-15T19:06:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89986",
    "user": "LuizAquino"
}
```

Replying to [comment:20 timdumol]:
> Thank you for pointing out these issues. I have posted a new patch, and a new package at the same url (http://sage.math.washington.edu/home/timdumol/sagenb-0.8.2-dev-i18n.spkg) addressing these issues.
> 

Thank you for solve those issues!

But, it seems we have another new ones:

- When we click on the link "New Worksheet" at the "Home" page, the
new worksheet is created with a title in the default language and not in the user one. So, if the default language is "en_US" and the user one is "pt_BR", then when we click on "Nova Planilha" (New Worksheet) the worksheet will have the title "Untitled" and not "Sem título".

- When we plot a surface (using the function plot3d), the text "Get Image" (at the side of the plot window) and "To save this image (...)" (that appears when we click on "Get Image") are in English no matter what is the user language or default language.



---

archive/issue_comments_089987.json:
```json
{
    "body": "Replying to [comment:21 robert.marik]:\n\n> Yes, I think that only admin (skilled person) can see these strings and he (she) is more familiar with the English terminology than the localized names.\n\nEven for a \"skilled person\", I think is more comfortable to use a software in your native language.\n\nAnd you're assuming that a \"skilled person\" is someone that knows English, but it isn't necessarily true.",
    "created_at": "2010-09-15T19:26:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89987",
    "user": "LuizAquino"
}
```

Replying to [comment:21 robert.marik]:

> Yes, I think that only admin (skilled person) can see these strings and he (she) is more familiar with the English terminology than the localized names.

Even for a "skilled person", I think is more comfortable to use a software in your native language.

And you're assuming that a "skilled person" is someone that knows English, but it isn't necessarily true.



---

archive/issue_comments_089988.json:
```json
{
    "body": "Attachment\n\nFixes more issues pointed out by LuizAquino.",
    "created_at": "2010-09-16T11:10:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89988",
    "user": "timdumol"
}
```

Attachment

Fixes more issues pointed out by LuizAquino.



---

archive/issue_comments_089989.json:
```json
{
    "body": "I have attache a new patch, and uploaded a new package at once again the same url (http://sage.math.washington.edu/home/timdumol/sagenb-0.8.2-dev-i18n.spkg) solving the new issues. Sorry for all the bugs! I did not notice the other gettext instances.\n\nI personally prefer using software in English, but I happen to be somewhat weak in my native language (Filipino). Also, translating the particular phrases left untranslated by Robert would be incredibly verbose in my native language, but this may not be the case in Czech.",
    "created_at": "2010-09-16T11:33:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89989",
    "user": "timdumol"
}
```

I have attache a new patch, and uploaded a new package at once again the same url (http://sage.math.washington.edu/home/timdumol/sagenb-0.8.2-dev-i18n.spkg) solving the new issues. Sorry for all the bugs! I did not notice the other gettext instances.

I personally prefer using software in English, but I happen to be somewhat weak in my native language (Filipino). Also, translating the particular phrases left untranslated by Robert would be incredibly verbose in my native language, but this may not be the case in Czech.



---

archive/issue_comments_089990.json:
```json
{
    "body": "Replying to [comment:24 timdumol]:\n> I have attache a new patch, and uploaded a new package at once again the same url (http://sage.math.washington.edu/home/timdumol/sagenb-0.8.2-dev-i18n.spkg) solving the new issues. Sorry for all the bugs! I did not notice the other gettext instances.\n>\n\nYou're making a great job, Tim Dumol! All the last issues are solved.\n\nBut, unfortunately I realize more three (minor) issues:\n\n- The text \"evaluate\" below the first cell in a worksheet is in the default language and not in the user one.\n\n- We have two more strings to translate:\n\n* data/sage/html/notebook/base.html, line 71: \"Click to rename this worksheet\"\n\n* data/sage/html/notebook/base.html, line 112 -> \"Select an attached file\"\n\nWe are not using the function gettext() in these strings.\n\n- It's not a big deal, but the date below the title of a worksheet (at the worksheet page) is in English.\n\nI updated the pt_BR localization files. Please add this to the next package:\n\nhttp://sites.google.com/site/lcmaquino/sage/sagenb_pt_BR.tar.gz?attredirects=0&d=1\n\nRobert Marik, could you update the cs_CZ localization files to translate the new strings?\n\nI think that after solve these issues we are ready to ask for another localization files! I hope that sage will be available in a lot of languages very soon!",
    "created_at": "2010-09-16T14:24:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89990",
    "user": "LuizAquino"
}
```

Replying to [comment:24 timdumol]:
> I have attache a new patch, and uploaded a new package at once again the same url (http://sage.math.washington.edu/home/timdumol/sagenb-0.8.2-dev-i18n.spkg) solving the new issues. Sorry for all the bugs! I did not notice the other gettext instances.
>

You're making a great job, Tim Dumol! All the last issues are solved.

But, unfortunately I realize more three (minor) issues:

- The text "evaluate" below the first cell in a worksheet is in the default language and not in the user one.

- We have two more strings to translate:

* data/sage/html/notebook/base.html, line 71: "Click to rename this worksheet"

* data/sage/html/notebook/base.html, line 112 -> "Select an attached file"

We are not using the function gettext() in these strings.

- It's not a big deal, but the date below the title of a worksheet (at the worksheet page) is in English.

I updated the pt_BR localization files. Please add this to the next package:

http://sites.google.com/site/lcmaquino/sage/sagenb_pt_BR.tar.gz?attredirects=0&d=1

Robert Marik, could you update the cs_CZ localization files to translate the new strings?

I think that after solve these issues we are ready to ask for another localization files! I hope that sage will be available in a lot of languages very soon!



---

archive/issue_comments_089991.json:
```json
{
    "body": "Replying to [comment:25 LuizAquino]:\n> \n> Robert Marik, could you update the cs_CZ localization files to translate the new strings?\n\nI merged my po file with the pot file from the last sagenb spg and translated untranslated string. Added also translations for \"Click to rename this worksheet\"  and \"Select an attached file\". The file with Czech translations is at http://user.mendelu.cz/marik/sage/sagenb.po \n\nI think that the pot file distributed in spkg package is not up-to-date but running pybabel gives error on my installation (Debian Lenny)\n\n\n```\nmarik@um-bc107:/opt/sage/spkg/build/sagenb-0.8.2-dev-i18n/src/sagenb/sagenb$ pybabel extract -F ./babel.cfg . -o output.pot\nextracting messages from data/sage/html/base.html (encoding=\"utf-8\")\nTraceback (most recent call last):\n  File \"/usr/bin/pybabel\", line 8, in <module>\n    load_entry_point('Babel==0.9.1', 'console_scripts', 'pybabel')()\n  File \"/var/lib/python-support/python2.5/babel/messages/frontend.py\", line 1072, in main\n    return CommandLineInterface().run(sys.argv)\n  File \"/var/lib/python-support/python2.5/babel/messages/frontend.py\", line 645, in run\n    return getattr(self, cmdname)(args[1:])\n  File \"/var/lib/python-support/python2.5/babel/messages/frontend.py\", line 879, in extract\n    for filename, lineno, message, comments in extracted:\n  File \"/var/lib/python-support/python2.5/babel/messages/extract.py\", line 153, in extract_from_dir\n    options=options):\n  File \"/var/lib/python-support/python2.5/babel/messages/extract.py\", line 179, in extract_from_file\n    return list(extract(method, fileobj, keywords, comment_tags, options))\n  File \"/var/lib/python-support/python2.5/babel/messages/extract.py\", line 238, in extract\n    if func is None:\nUnboundLocalError: local variable 'func' referenced before assignment\n\n\n```\n",
    "created_at": "2010-09-16T18:35:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89991",
    "user": "robert.marik"
}
```

Replying to [comment:25 LuizAquino]:
> 
> Robert Marik, could you update the cs_CZ localization files to translate the new strings?

I merged my po file with the pot file from the last sagenb spg and translated untranslated string. Added also translations for "Click to rename this worksheet"  and "Select an attached file". The file with Czech translations is at http://user.mendelu.cz/marik/sage/sagenb.po 

I think that the pot file distributed in spkg package is not up-to-date but running pybabel gives error on my installation (Debian Lenny)


```
marik@um-bc107:/opt/sage/spkg/build/sagenb-0.8.2-dev-i18n/src/sagenb/sagenb$ pybabel extract -F ./babel.cfg . -o output.pot
extracting messages from data/sage/html/base.html (encoding="utf-8")
Traceback (most recent call last):
  File "/usr/bin/pybabel", line 8, in <module>
    load_entry_point('Babel==0.9.1', 'console_scripts', 'pybabel')()
  File "/var/lib/python-support/python2.5/babel/messages/frontend.py", line 1072, in main
    return CommandLineInterface().run(sys.argv)
  File "/var/lib/python-support/python2.5/babel/messages/frontend.py", line 645, in run
    return getattr(self, cmdname)(args[1:])
  File "/var/lib/python-support/python2.5/babel/messages/frontend.py", line 879, in extract
    for filename, lineno, message, comments in extracted:
  File "/var/lib/python-support/python2.5/babel/messages/extract.py", line 153, in extract_from_dir
    options=options):
  File "/var/lib/python-support/python2.5/babel/messages/extract.py", line 179, in extract_from_file
    return list(extract(method, fileobj, keywords, comment_tags, options))
  File "/var/lib/python-support/python2.5/babel/messages/extract.py", line 238, in extract
    if func is None:
UnboundLocalError: local variable 'func' referenced before assignment


```




---

archive/issue_comments_089992.json:
```json
{
    "body": "Here is an updated .pot file:\n\nhttps://sites.google.com/site/lcmaquino/sage/sagenb.pot?attredirects=0&d=1\n\nI can generate it running pybabel on Ubuntu 10.04 without problem.\n\nBut, we have to take care about the .js files. In the new version of the package we are translating the .js files using the dictionary \"translations\" (defined in \"data/sage/js/localization.js\"), so we can't extract these strings using pybabel because it looks for \"gettext()\", \"ngetttext()\" and \"_()\" functions. Maybe we can implement a dummy \"_()\" function, as we did before.",
    "created_at": "2010-09-16T19:25:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89992",
    "user": "LuizAquino"
}
```

Here is an updated .pot file:

https://sites.google.com/site/lcmaquino/sage/sagenb.pot?attredirects=0&d=1

I can generate it running pybabel on Ubuntu 10.04 without problem.

But, we have to take care about the .js files. In the new version of the package we are translating the .js files using the dictionary "translations" (defined in "data/sage/js/localization.js"), so we can't extract these strings using pybabel because it looks for "gettext()", "ngetttext()" and "_()" functions. Maybe we can implement a dummy "_()" function, as we did before.



---

archive/issue_comments_089993.json:
```json
{
    "body": "Hi Tim,\n\nIt seems you updated the package. I tried to install it and I got some errors. To solve them, I changed the files:\n\n#sagenb/notebook/template.py, line 142\n\nFrom: \n\n```\nenv.filters['_'] = lambda x: return x\n```\n\nTo:\n\n```\nenv.filters['_'] = lambda x: x\n```\n \n\n#sagenb/data/sage/js/localization.js, line 5\n\nThere is a open comment tag \"{#\", but there isn't a close comment tag \"#}\". So, I typed \"#}\" in the line 7.\n\nI notice that you forgot to put the strings \"Problem inserting new input cell before current input cell.\" and \"Problem inserting new text cell before current input cell.\" in the files localization.js and translated-messages.js.\n\nAfter install, I notice that the date below the title of a worksheet (at the worksheet page) appears as \"None\". To solve it, I changed the file:\n\n#sagenb/notebook/worksheet.js\n\nline 4166: I commented this line.\n\nline 4168 (solve an 'exceptions.UnicodeEncodeError' in Czech and the text \"None\" below the title of a worksheet):\n\nFrom:\n\n```\ntime.strftime(month+' %d, %Y %I:%M %p', time.localtime(float(t)))\n```\n\nTo:\n\n```\nreturn month + time.strftime(' %d, %Y %I:%M %p', time.localtime(float(t)))\n```\n\n\nAfter all, it seems that the issues pointed in above comment 26 are solved! :)\n\nI updated the pt_BR localization files (translating the name of months) and the .pot file. Please add this to the next package:\n\nhttp://sites.google.com/site/lcmaquino/sage/sagenb_pt_BR.tar.gz?attredirects=0&d=1\n\nhttps://sites.google.com/site/lcmaquino/sage/sagenb.pot?attredirects=0&d=1\n\nBy the way, please remove the file \"sagenb/notebook/conf_lcma.py\" (as you did before).\n\nI think we're ready to ask for another localization files! What do you think?",
    "created_at": "2010-09-30T17:53:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89993",
    "user": "LuizAquino"
}
```

Hi Tim,

It seems you updated the package. I tried to install it and I got some errors. To solve them, I changed the files:

#sagenb/notebook/template.py, line 142

From: 

```
env.filters['_'] = lambda x: return x
```

To:

```
env.filters['_'] = lambda x: x
```
 

#sagenb/data/sage/js/localization.js, line 5

There is a open comment tag "{#", but there isn't a close comment tag "#}". So, I typed "#}" in the line 7.

I notice that you forgot to put the strings "Problem inserting new input cell before current input cell." and "Problem inserting new text cell before current input cell." in the files localization.js and translated-messages.js.

After install, I notice that the date below the title of a worksheet (at the worksheet page) appears as "None". To solve it, I changed the file:

#sagenb/notebook/worksheet.js

line 4166: I commented this line.

line 4168 (solve an 'exceptions.UnicodeEncodeError' in Czech and the text "None" below the title of a worksheet):

From:

```
time.strftime(month+' %d, %Y %I:%M %p', time.localtime(float(t)))
```

To:

```
return month + time.strftime(' %d, %Y %I:%M %p', time.localtime(float(t)))
```


After all, it seems that the issues pointed in above comment 26 are solved! :)

I updated the pt_BR localization files (translating the name of months) and the .pot file. Please add this to the next package:

http://sites.google.com/site/lcmaquino/sage/sagenb_pt_BR.tar.gz?attredirects=0&d=1

https://sites.google.com/site/lcmaquino/sage/sagenb.pot?attredirects=0&d=1

By the way, please remove the file "sagenb/notebook/conf_lcma.py" (as you did before).

I think we're ready to ask for another localization files! What do you think?



---

archive/issue_comments_089994.json:
```json
{
    "body": "Adds Luiz Aquino's fixes and .m/po/t files.",
    "created_at": "2010-10-01T22:46:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89994",
    "user": "timdumol"
}
```

Adds Luiz Aquino's fixes and .m/po/t files.



---

archive/issue_comments_089995.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-10-02T00:36:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89995",
    "user": "timdumol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_089996.json:
```json
{
    "body": "Attachment\n\nSorry, I forgot to post here that I had updated the spkg. Here's a new spkg (http://sage.math.washington.edu/home/timdumol/sagenb-0.8.2-dev-i18n.spkg) and patch implementing your changes.\n\nSince you approve of my changes, and your changes count as a reviewer patch, shall we mark this positive review?",
    "created_at": "2010-10-02T00:36:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89996",
    "user": "timdumol"
}
```

Attachment

Sorry, I forgot to post here that I had updated the spkg. Here's a new spkg (http://sage.math.washington.edu/home/timdumol/sagenb-0.8.2-dev-i18n.spkg) and patch implementing your changes.

Since you approve of my changes, and your changes count as a reviewer patch, shall we mark this positive review?



---

archive/issue_comments_089997.json:
```json
{
    "body": "It installed ok. But, you didn't comment (or remove) the line 4166 in \"sagenb/notebook/worksheet.js\". Without this change, I got an error when I tried to save a new worksheet. The last messages about this error were:\n\n\n```\n\t  File \"/home/lcaquino/Instaladores/sage/sage/local/lib/python2.6/site-packages/sagenb-0.8.2_dev_i18n-py2.6.egg/sagenb/notebook/twist.py\", line 864, in render\n\t    self.worksheet.save_snapshot(self.username)\n\t  File \"/home/lcaquino/Instaladores/sage/sage/local/lib/python2.6/site-packages/sagenb-0.8.2_dev_i18n-py2.6.egg/sagenb/notebook/worksheet.py\", line 1964, in save_snapshot\n\t    self.limit_snapshots()\n\t  File \"/home/lcaquino/Instaladores/sage/sage/local/lib/python2.6/site-packages/sagenb-0.8.2_dev_i18n-py2.6.egg/sagenb/notebook/worksheet.py\", line 2060, in limit_snapshots\n\t    amnesty = int(calendar.timegm(time.strptime(\"01 May 2009\", \"%d %b %Y\")))\n\t  File \"/home/lcaquino/Instaladores/sage/sage/local/lib/python/_strptime.py\", line 454, in _strptime_time\n\t    return _strptime(data_string, format)[0]\n\t  File \"/home/lcaquino/Instaladores/sage/sage/local/lib/python/_strptime.py\", line 325, in _strptime\n\t    (data_string, format))\n\texceptions.ValueError: time data '01 May 2009' does not match format '%d %b %Y'\n```\n\n\nBy the way, you forgot to put the strings in the files \"localization.js\" and \"translated-messages.js\" as pointed above.\n\nWhen we finish the work with this package, how do you think to instruct another user to add new localization files? Do you think to ask them to send to you the localization files and then you add it to the package?",
    "created_at": "2010-10-02T13:53:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89997",
    "user": "LuizAquino"
}
```

It installed ok. But, you didn't comment (or remove) the line 4166 in "sagenb/notebook/worksheet.js". Without this change, I got an error when I tried to save a new worksheet. The last messages about this error were:


```
	  File "/home/lcaquino/Instaladores/sage/sage/local/lib/python2.6/site-packages/sagenb-0.8.2_dev_i18n-py2.6.egg/sagenb/notebook/twist.py", line 864, in render
	    self.worksheet.save_snapshot(self.username)
	  File "/home/lcaquino/Instaladores/sage/sage/local/lib/python2.6/site-packages/sagenb-0.8.2_dev_i18n-py2.6.egg/sagenb/notebook/worksheet.py", line 1964, in save_snapshot
	    self.limit_snapshots()
	  File "/home/lcaquino/Instaladores/sage/sage/local/lib/python2.6/site-packages/sagenb-0.8.2_dev_i18n-py2.6.egg/sagenb/notebook/worksheet.py", line 2060, in limit_snapshots
	    amnesty = int(calendar.timegm(time.strptime("01 May 2009", "%d %b %Y")))
	  File "/home/lcaquino/Instaladores/sage/sage/local/lib/python/_strptime.py", line 454, in _strptime_time
	    return _strptime(data_string, format)[0]
	  File "/home/lcaquino/Instaladores/sage/sage/local/lib/python/_strptime.py", line 325, in _strptime
	    (data_string, format))
	exceptions.ValueError: time data '01 May 2009' does not match format '%d %b %Y'
```


By the way, you forgot to put the strings in the files "localization.js" and "translated-messages.js" as pointed above.

When we finish the work with this package, how do you think to instruct another user to add new localization files? Do you think to ask them to send to you the localization files and then you add it to the package?



---

archive/issue_comments_089998.json:
```json
{
    "body": "By the way, please add the .pot file to the next package. I think it should be in \"sagenb-0.8.2_dev_i18n-py2.6.egg/sagenb/locale\" directory.",
    "created_at": "2010-10-02T13:58:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89998",
    "user": "LuizAquino"
}
```

By the way, please add the .pot file to the next package. I think it should be in "sagenb-0.8.2_dev_i18n-py2.6.egg/sagenb/locale" directory.



---

archive/issue_comments_089999.json:
```json
{
    "body": "> Since you approve of my changes, and your changes count as a reviewer patch, shall we mark this positive review?\n\nUnfortunately we can't mark this as \"positive review\" yet. But we're very close to do so! :)",
    "created_at": "2010-10-02T14:02:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-89999",
    "user": "LuizAquino"
}
```

> Since you approve of my changes, and your changes count as a reviewer patch, shall we mark this positive review?

Unfortunately we can't mark this as "positive review" yet. But we're very close to do so! :)



---

archive/issue_comments_090000.json:
```json
{
    "body": "Replying to [comment:32 LuizAquino]:\n> Unfortunately we can't mark this as \"positive review\" yet. But we're very close to do so! :)\n\nWhere is the problem? Can I help to finish this useful ticket?",
    "created_at": "2010-11-07T05:54:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-90000",
    "user": "robert.marik"
}
```

Replying to [comment:32 LuizAquino]:
> Unfortunately we can't mark this as "positive review" yet. But we're very close to do so! :)

Where is the problem? Can I help to finish this useful ticket?



---

archive/issue_comments_090001.json:
```json
{
    "body": "Replying to [comment:33 robert.marik]:\n> \n> Where is the problem? Can I help to finish this useful ticket?\n> \n\nWe should implement the solutions pointed in comments 28 and 30 and update the package. But, where you read \"sagenb/notebook/worksheet.js\", please understand \"sagenb/notebook/worksheet.py\".",
    "created_at": "2010-11-07T20:16:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-90001",
    "user": "LuizAquino"
}
```

Replying to [comment:33 robert.marik]:
> 
> Where is the problem? Can I help to finish this useful ticket?
> 

We should implement the solutions pointed in comments 28 and 30 and update the package. But, where you read "sagenb/notebook/worksheet.js", please understand "sagenb/notebook/worksheet.py".



---

archive/issue_comments_090002.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-06-23T09:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-90002",
    "user": "kini"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_090003.json:
```json
{
    "body": "This ticket has been superseded by #11471.",
    "created_at": "2012-06-23T09:09:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-90003",
    "user": "kini"
}
```

This ticket has been superseded by #11471.



---

archive/issue_comments_090004.json:
```json
{
    "body": "Resolution: duplicate",
    "created_at": "2012-09-05T07:15:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9428",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9428#issuecomment-90004",
    "user": "jdemeyer"
}
```

Resolution: duplicate
