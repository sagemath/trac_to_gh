# Issue 9428: Internationalize the Sage Notebook

Issue created by migration from Trac.

Original creator: timdumol

Original creation time: 2010-07-05 09:37:24

Assignee: jason, was

CC:  ddrake aquino.luizclaudio@gmail.com robert.marik

This patch internationalizes the Sage Notebook and adds a localization to Brazilian Portuguese.


---

Comment by timdumol created at 2010-07-05 09:39:35

Changing type from defect to enhancement.


---

Comment by timdumol created at 2010-07-05 09:45:33

i18n the notebook and adds a l20n to pt_BR


---

Comment by timdumol created at 2010-07-05 09:46:00

Changing status from new to needs_review.


---

Attachment


---

Attachment

Rebase on SageNB 0.8.1. Replaces previous patch.


---

Comment by timdumol created at 2010-07-05 14:31:26

Good idea. I will make the loading lazy, although the languages loaded will stay in memory, since there are multiple users using the notebook, who may each require a different language.


---

Comment by timdumol created at 2010-07-05 14:54:13

Defers language loading until requested.


---

Attachment

A package with this patch (tentatively SageNB 0.9) based on SageNB 0.8.1 is avaialable at http://sage.math.washington.edu/home/timdumol/sagenb-0.9.spkg


---

Comment by timdumol created at 2010-07-06 09:34:02

Since the package is based on SageNB 0.8.1 (#9430), you'll need to apply the main sage library patch to at #7379 (run hg_sage.apply('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7379/trac-7379-decorator-defaults.patch'), then restart sage with sage -br).

I have moved the translation of the description strings and group strings to the html generation function so as to be able to dynamically change the language.

The new package (at the same url) removes conf_lcma.py.


---

Comment by timdumol created at 2010-08-17 16:55:47

Replaces all others. Adds a few more strings to translation, and implements dummy _() functions, as described in comments.


---

Attachment

Added a couple more strings to translation. Replaces all others.


---

Comment by timdumol created at 2010-08-19 14:39:44

New test package at http://sage.math.washington.edu/home/timdumol/sagenb-0.8.2-dev-i18n.spkg fixing all noted issues.


---

Comment by robert.marik created at 2010-08-24 07:19:38

Hi, thank you for this great work. I have several comments:

I installed sagenb-0.8.2-dev-i18n.spkg and started Sage. I got error caused by empty locale directory. However, this has been fixed after installing portugese and czech translations. Is this behavior intented?

I have seen that some strings have been changed from the version announced in [sage-notebook mailing list](http://groups.google.cz/group/sage-notebook/browse_thread/thread/9b7b6aee9e331962), but I was not able to find the sagenb.pot with strings for translations.

If anyone is interested, I have one feature request related to the strings "XX minutes ago". It is [requested](http://groups.google.cz/group/sage-notebook/msg/1eae0947a08c16a5?) in the sage-notebook in the thread linked above. Could this be fixed? Many thanks.

btw: How to review this trac? I have seen [devel comments](http://nb.sagemath.org/dev.html). Is it reasonable to run doctests for sagenb tickets?


---

Attachment

Replaces previous patches. Added the requested "XX <time> ago" fix. Updated the sagenb.po file with the latest strings to be translated. Added sagenb/locale to the package data list.


---

Comment by timdumol created at 2010-08-26 11:52:38

Hi,

There is a new package version at the same url: http://sage.math.washington.edu/home/timdumol/sagenb-0.8.2-dev-i18n.spkg

The error regarding the missing locale directory was a bug. The new patch fixes this, and addresses your issue regarding "XX <time units> ago".

The new translations are found in `sagenb.po`.


---

Comment by robert.marik created at 2010-08-27 21:32:50

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

Comment by robert.marik created at 2010-08-28 18:49:15

I observed that if I click in worksheet to Undo button, the Last Edited field does not contain the name of the author, but the word "ago". Switching languages does not change the string in the field Last Edited. The string is always in the notebook default language.

Do you have the same behavior? Do you know how to fix this? I think that there should be no strings for translation in the function _saved_by_info, since the whole phrase is translated in the function snapshot_data. Is this right?

If you prepare new version, could you add the directory cs_CZ and the file from 
http://user.mendelu.cz/marik/sage/sagenb.po ?

I tested extensivelly the last version of the sagenb package and everything works fine, with one exception in Last Edited field described above.

It seems that the welcome page and registration process must be in the default language of the notebook right now. Could this be improved in some later versions?

Still trying to make selenium tests work in order to finish review of this ticket... 

Many thanks for working on i18n!


---

Comment by robert.marik created at 2010-09-08 08:58:00

Changing status from needs_review to needs_work.


---

Comment by robert.marik created at 2010-09-08 08:58:00

The "last edited" field in the "Undo" part of the notebook is always in the default notebook language and does not change when changing account settings.

The other things work. Excellent! Is is easy to fix this last issue? Many thanks.


---

Comment by timdumol created at 2010-09-10 02:23:33

The last part shouldn't be too difficult to fix. I've added your localization.


---

Attachment

Replaces all previous. Really fixed the undo problem.


---

Comment by timdumol created at 2010-09-10 04:07:16

Changing status from needs_work to needs_review.


---

Comment by timdumol created at 2010-09-10 04:07:16

The latest version of the pkg is up at http://sage.math.washington.edu/home/timdumol/sagenb-0.8.2-dev-i18n.spkg. I've included your sagenb.po, and the above patch. Please be advised that there is a new string to be translated ("%s ago").


---

Comment by timdumol created at 2010-09-11 02:54:41

Replaces all others. Fixed a bug in the fix.


---

Attachment

New package version here: http://sage.math.washington.edu/home/timdumol/sagenb-0.8.2-dev-i18n.spkg fixing the bug in Undo.


---

Comment by timdumol created at 2010-09-11 14:53:13

Another package version at the same url fixing a minor doctest error.


---

Comment by timdumol created at 2010-09-11 14:56:51

Fixed a failing doctest.


---

Comment by robert.marik created at 2010-09-11 18:38:54

Changing status from needs_review to positive_review.


---

Attachment

Looks fine for me, instals fine, works fine, no problems found when using it for a longer time and for many various things.

All doctests (sage -t -sagenb) passed. 

Very very important patch, thank you.

I am not able to check the Brazilian Portugese, but despite this fact I give a positive review! 

Many thanks for this work.


---

Comment by LuizAquino created at 2010-09-14 19:14:19

Changing status from positive_review to needs_work.


---

Comment by LuizAquino created at 2010-09-14 19:14:19

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

Attachment

Fixes the issues pointed out by LuizAquino. Updates pt_BR.


---

Comment by timdumol created at 2010-09-15 16:27:03

Thank you for pointing out these issues. I have posted a new patch, and a new package at the same url (http://sage.math.washington.edu/home/timdumol/sagenb-0.8.2-dev-i18n.spkg) addressing these issues.

robert.marik, it seems that some strings re: the notebook settings are left untranslated (Doc pool size, Type of challenge, etc.) in the cs_CZ locale.


---

Comment by robert.marik created at 2010-09-15 16:56:43

Replying to [comment:20 timdumol]:

> robert.marik, it seems that some strings re: the notebook settings are left untranslated (Doc pool size, Type of challenge, etc.) in the cs_CZ locale.

Yes, I think that only admin (skilled person) can see these strings and he (she) is more familiar with the English terminology than the localized names. This should avoid some uncertainties. Do you accept this point of view?

Is the new package ready for review?


---

Comment by LuizAquino created at 2010-09-15 19:06:27

Replying to [comment:20 timdumol]:
> Thank you for pointing out these issues. I have posted a new patch, and a new package at the same url (http://sage.math.washington.edu/home/timdumol/sagenb-0.8.2-dev-i18n.spkg) addressing these issues.
> 

Thank you for solve those issues!

But, it seems we have another new ones:

- When we click on the link "New Worksheet" at the "Home" page, the
new worksheet is created with a title in the default language and not in the user one. So, if the default language is "en_US" and the user one is "pt_BR", then when we click on "Nova Planilha" (New Worksheet) the worksheet will have the title "Untitled" and not "Sem título".

- When we plot a surface (using the function plot3d), the text "Get Image" (at the side of the plot window) and "To save this image (...)" (that appears when we click on "Get Image") are in English no matter what is the user language or default language.


---

Comment by LuizAquino created at 2010-09-15 19:26:30

Replying to [comment:21 robert.marik]:

> Yes, I think that only admin (skilled person) can see these strings and he (she) is more familiar with the English terminology than the localized names.

Even for a "skilled person", I think is more comfortable to use a software in your native language.

And you're assuming that a "skilled person" is someone that knows English, but it isn't necessarily true.


---

Attachment

Fixes more issues pointed out by LuizAquino.


---

Comment by timdumol created at 2010-09-16 11:33:40

I have attache a new patch, and uploaded a new package at once again the same url (http://sage.math.washington.edu/home/timdumol/sagenb-0.8.2-dev-i18n.spkg) solving the new issues. Sorry for all the bugs! I did not notice the other gettext instances.

I personally prefer using software in English, but I happen to be somewhat weak in my native language (Filipino). Also, translating the particular phrases left untranslated by Robert would be incredibly verbose in my native language, but this may not be the case in Czech.


---

Comment by LuizAquino created at 2010-09-16 14:24:57

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

Comment by robert.marik created at 2010-09-16 18:35:42

Replying to [comment:25 LuizAquino]:
> 
> Robert Marik, could you update the cs_CZ localization files to translate the new strings?

I merged my po file with the pot file from the last sagenb spg and translated untranslated string. Added also translations for "Click to rename this worksheet"  and "Select an attached file". The file with Czech translations is at http://user.mendelu.cz/marik/sage/sagenb.po 

I think that the pot file distributed in spkg package is not up-to-date but running pybabel gives error on my installation (Debian Lenny)


```
marik`@`um-bc107:/opt/sage/spkg/build/sagenb-0.8.2-dev-i18n/src/sagenb/sagenb$ pybabel extract -F ./babel.cfg . -o output.pot
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

Comment by LuizAquino created at 2010-09-16 19:25:25

Here is an updated .pot file:

https://sites.google.com/site/lcmaquino/sage/sagenb.pot?attredirects=0&d=1

I can generate it running pybabel on Ubuntu 10.04 without problem.

But, we have to take care about the .js files. In the new version of the package we are translating the .js files using the dictionary "translations" (defined in "data/sage/js/localization.js"), so we can't extract these strings using pybabel because it looks for "gettext()", "ngetttext()" and "_()" functions. Maybe we can implement a dummy "_()" function, as we did before.


---

Comment by LuizAquino created at 2010-09-30 17:53:19

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
}}} 

#sagenb/data/sage/js/localization.js, line 5

There is a open comment tag "{#", but there isn't a close comment tag "#}". So, I typed "#}" in the line 7.

I notice that you forgot to put the strings "Problem inserting new input cell before current input cell." and "Problem inserting new text cell before current input cell." in the files localization.js and translated-messages.js.

After install, I notice that the date below the title of a worksheet (at the worksheet page) appears as "None". To solve it, I changed the file:

#sagenb/notebook/worksheet.js

line 4166: I commented this line.

line 4168 (solve an 'exceptions.UnicodeEncodeError' in Czech and the text "None" below the title of a worksheet):

From:
{{{
time.strftime(month+' %d, %Y %I:%M %p', time.localtime(float(t)))
}}}
To:
{{{
return month + time.strftime(' %d, %Y %I:%M %p', time.localtime(float(t)))
}}}

After all, it seems that the issues pointed in above comment 26 are solved! :)

I updated the pt_BR localization files (translating the name of months) and the .pot file. Please add this to the next package:

http://sites.google.com/site/lcmaquino/sage/sagenb_pt_BR.tar.gz?attredirects=0&d=1

https://sites.google.com/site/lcmaquino/sage/sagenb.pot?attredirects=0&d=1

By the way, please remove the file "sagenb/notebook/conf_lcma.py" (as you did before).

I think we're ready to ask for another localization files! What do you think?


---

Comment by timdumol created at 2010-10-01 22:46:15

Adds Luiz Aquino's fixes and .m/po/t files.


---

Comment by timdumol created at 2010-10-02 00:36:48

Changing status from needs_work to needs_review.


---

Attachment

Sorry, I forgot to post here that I had updated the spkg. Here's a new spkg (http://sage.math.washington.edu/home/timdumol/sagenb-0.8.2-dev-i18n.spkg) and patch implementing your changes.

Since you approve of my changes, and your changes count as a reviewer patch, shall we mark this positive review?


---

Comment by LuizAquino created at 2010-10-02 13:53:24

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

Comment by LuizAquino created at 2010-10-02 13:58:29

By the way, please add the .pot file to the next package. I think it should be in "sagenb-0.8.2_dev_i18n-py2.6.egg/sagenb/locale" directory.


---

Comment by LuizAquino created at 2010-10-02 14:02:55

> Since you approve of my changes, and your changes count as a reviewer patch, shall we mark this positive review?

Unfortunately we can't mark this as "positive review" yet. But we're very close to do so! :)


---

Comment by robert.marik created at 2010-11-07 05:54:56

Replying to [comment:32 LuizAquino]:
> Unfortunately we can't mark this as "positive review" yet. But we're very close to do so! :)

Where is the problem? Can I help to finish this useful ticket?


---

Comment by LuizAquino created at 2010-11-07 20:16:05

Replying to [comment:33 robert.marik]:
> 
> Where is the problem? Can I help to finish this useful ticket?
> 

We should implement the solutions pointed in comments 28 and 30 and update the package. But, where you read "sagenb/notebook/worksheet.js", please understand "sagenb/notebook/worksheet.py".


---

Comment by kini created at 2012-06-23 09:09:30

Changing status from needs_review to positive_review.


---

Comment by kini created at 2012-06-23 09:09:30

This ticket has been superseded by #11471.


---

Comment by jdemeyer created at 2012-09-05 07:15:38

Resolution: duplicate
