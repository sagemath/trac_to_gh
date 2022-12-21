# Issue 3552: sage notebook -- worksheet.py -- bring coverage up to 100%

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-07-05 17:53:08

Assignee: boothby

Bring the doctest coverage for worksheet.py up to 100%. Currently (in 3.0.3) coverage is at 3% with most functions totally undocumented:


```
was`@`sage:~/d/sage/server/notebook$ sage -coverage worksheet.py
----------------------------------------------------------------------
worksheet.py
SCORE worksheet.py: 3% (6 of 193)
Missing documentation:
         * initialized_sage(server, ulimit)
         * init_sage_prestart(server, ulimit)
         * one_prestarted_sage(server, ulimit)
         * worksheet_filename(name, owner)
         * __init__(self, name, dirname, notebook, system, owner, docbrowser=False, pretty_print=False)
         * __cmp__(self, other)
         * __repr__(self)
         * __len__(self)
         * docbrowser(self)
         * conf(self)
         * collaborators(self)
         * set_collaborators(self, v)
         * viewers(self)
         * delete_notebook_specific_data(self)
         * name(self)
         * set_name(self, name)
         * set_filename_without_owner(self, nm)
         * set_filename(self, filename)
         * filename(self)
         * directory(self)
         * data_directory(self)
         * attached_data_files(self)
         * cells_directory(self)
         * notebook(self)
         * DIR(self)
         * system(self)
         * set_system(self, system='sage')
         * pretty_print(self)
         * set_pretty_print(self, check='false')
         * is_published(self)
         * worksheet_that_was_published(self)
         * publisher(self)
         * is_publisher(self, username)
         * has_published_version(self)
         * set_published_version(self, filename)
         * published_version(self)
         * set_worksheet_that_was_published(self, W)
         * rate(self, x, comment, username)
         * is_rater(self, username)
         * ratings(self)
         * html_ratings_info(self)
         * rating(self)
         * everyone_has_deleted_this_worksheet(self)
         * user_view(self, user)
         * set_user_view(self, user, x)
         * user_view_is(self, user, x)
         * is_archived(self, user)
         * is_active(self, user)
         * is_trashed(self, user)
         * move_to_archive(self, user)
         * set_active(self, user)
         * move_to_trash(self, user)
         * move_out_of_trash(self, user)
         * delete_cells_directory(self)
         * owner(self)
         * is_owner(self, username)
         * set_owner(self, owner)
         * user_is_only_viewer(self, user)
         * user_is_viewer(self, user)
         * user_is_collaborator(self, user)
         * add_viewer(self, user)
         * add_collaborator(self, user)
         * save(self)
         * save_snapshot(self, user, E=None)
         * get_snapshot_text_filename(self, name)
         * user_autosave_interval(self, username)
         * autosave(self, username)
         * revert_to_snapshot(self, name)
         * _saved_by_info(self, x)
         * snapshot_data(self)
         * uncache_snapshot_data(self)
         * revert_to_last_saved_state(self)
         * snapshot_directory(self)
         * __getstate__(self)
         * __setstate__(self, state)
         * html(self, include_title=True, do_print=False, confirm_before_leave=False, read_only=False)
         * truncated_name(self, max=30)
         * html_title(self, username='guest')
         * is_doc_worksheet(self)
         * set_is_doc_worksheet(self, value)
         * html_save_discard_buttons(self)
         * html_share_publish_buttons(self, select=None)
         * cls(x)
         * html_data_options_list(self)
         * html_file_menu(self)
         * html_menu(self)
         * html_worksheet_body(self, do_print, publish=False)
         * javascript_for_being_active_worksheet(self)
         * javascript_for_jsmath_rendering(self)
         * last_edited(self)
         * last_to_edit(self)
         * record_edit(self, user)
         * time_since_last_edited(self)
         * html_time_since_last_edited(self)
         * html_time_last_edited(self)
         * cell_id_list(self)
         * compute_cell_id_list(self)
         * clear(self)
         * set_not_computing(self)
         * quit(self)
         * next_block_id(self)
         * initialize_sage(self)
         * eval_asap_no_output(self, cmd, username=None)
         * start_next_comp(self)
         * clear_queue(self)
         * worksheet_command(self, cmd)
         * time_idle(self)
         * last_compute_walltime(self)
         * _record_that_we_are_computing(self, username=None)
         * ping(self, username)
         * queue(self)
         * queue_id_list(self)
         * _enqueue_auto(self)
         * _enqueue_auto_cells(self)
         * set_cell_counter(self)
         * _new_text_cell(self, plain_text, id=None)
         * next_hidden_id(self)
         * _new_cell(self, id=None, hidden=False, input='')
         * append(self, L)
         * __getitem__(self, n)
         * get_cell_with_id(self, id)
         * synchronize(self, s)
         * synchro(self)
         * is_last_id_and_previous_is_nonempty(self, id)
         * best_completion(self, s, word)
         * completions_html(self, id, s, cols=3)
         * preparse_input(self, input, C)
         * preparse_introspection_input(self, input, C, introspect)
         * preparse_nonswitched_input(self, input)
         * ')
         * _strip_synchro_from_start_of_output(self, s)
         * _process_output(self, s)
         * postprocess_output(self, out, C)
         * _get_last_identifier(self, s)
         * preparse(self, s)
         * attached_files(self)
         * attach(self, filename)
         * detach(self, filename)
         * _normalized_filenames(self, L)
         * load_path(self)
         * hunt_file(self, filename)
         * _load_file(self, filename, files_seen_so_far, this_file)
         * _save_objects(self, s)
         * do_sage_extensions_preparsing(self, s, files_seen_so_far=[], this_file='')
         * _eval_cmd(self, system, cmd, dir)
         * cython_import(self, cmd, C)
         * attached_html(self)
         * show_all(self)
         * hide_all(self)
         * foo(x)
         * first_word(s)
         * format_completions_as_html(cell_id, completions)
         * extract_name(text)
         * extract_system(text)
         * convert_seconds_to_meaningful_time_span(t)
         * convert_time_to_string(t)
         * _get_next(s, quote='"')


Missing doctests:
         * filename_without_owner(self)
         * satisfies_search(self, search)
         * plain_text(self, prompts=False, banner=True)
         * input_text(self)
         * edit_text(self)
         * reset_interact_state(self)
         * edit_save(self, text, ignore_ids=False)
         * javascript_confirm_before_leave(self)
         * warn_about_other_person_editing(self,username, threshold)
         * cell_list(self)
         * append_new_cell(self)
         * new_cell_before(self, id, input="")
         * new_cell_after(self, id, input="")
         * delete_cell_with_id(self, id)
         * computing(self)
         * compute_process_has_been_started(self)
         * sage(self)
         * restart_sage(self)
         * quit_if_idle(self, timeout)
         * enqueue(self, C, username=None, next=False)
         * delete_cell_input_files(self)
         * check_cell(self, id)
         * load_any_changed_attached_files(self, s)
         * check_for_system_switching(self, s, C)
         * extract_text_before_first_compute_cell(text)
         * extract_first_compute_cell(text)
         * after_first_word(s)
         * dictify(s)
         * next_available_id(v)
         * split_search_string_into_keywords(s)

```



---

Comment by was created at 2008-07-05 18:49:42

document top; optimize opening new worksheets


---

Attachment


---

Comment by was created at 2008-07-05 21:23:38

this brings coverage up to 35% and fixes some bugs.


---

Attachment


---

Attachment


---

Comment by mabshoff created at 2008-07-05 22:27:45

Also positive review on sage-3552-part3.patch.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-05 22:51:09

This seems to depend on #3550.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-05 23:31:47

Merge in Sage 3.0.4.alpha2


---

Comment by mabshoff created at 2008-07-05 23:31:47

Resolution: fixed
