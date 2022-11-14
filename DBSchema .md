
 I think these are all of the relevant tables for ticket queries (and possibly some extra ones).

 * system
  * name text (pk)
  * value text
 * permission
  * username text (pk)
  * action text (pk)
 * auth_cookie
  * cookie text (pk)
  * name text (pk)
  * ipnr text (pk)
  * time integer
 * session
  * sid text (pk)
  * authenticated integer (pk)
  * last_visit integer
  * session_authenticated_idx (index)
  * session_last_visit_idx (index)
 * session_attribute
  * sid text (pk)
  * authenticated integer (pk)
  * name text (pk)
  * value text
 * attachment
  * type text (pk)
  * id text (pk)
  * filename text (pk)
  * size integer
  * time integer
  * description text
  * author text
  * ipnr text
 * wiki
  * name text (pk)
  * version integer (pk)
  * time integer
  * author text
  * ipnr text
  * text text
  * comment text
  * readonly integer
  * wiki_time_idx (index)
 * revision
  * repos integer (pk)
  * rev text (pk)
  * time integer
  * author text
  * message text
  * revision_time_idx (index)
 * repository
  * id integer(pk)
  * name text (pk)
  * value text
 * node_change
  * repos integer (pk)
  * rev text (pk)
  * path text (pk)
  * node_type text
  * change_type text (pk)
  * base_path text
  * base_rev text
  * node_change_rev_idx (index)
 * ticket
  * id integer (pk)
  * type text
  * time integer
  * changetime integer
  * component text
  * severity text
  * priority text
  * owner text
  * reporter text
  * cc text
  * version text
  * milestone text
  * status text
  * resolution text
  * summary text
  * description text
  * keywords text
  * ticket_pkey (index)
  * ticket_status_idx (index)
  * ticket_time_idx (index)
 * ticket_change
  * ticket integer (pk)
  * time integer (pk)
  * author text
  * field text (pk)
  * oldvalue text
  * newvalue text
  * ticket_change_time_idx (index)
  * ticket_change_ticket_idx (index)
 * ticket_custom
  * ticket integer (pk)
  * name text (pk)
  * value text
 * enum
  * type text (pk)
  * name text (pk)
  * value text
 * component
  * name text (pk)
  * owner text
  * description text
 * milestone
  * name text (pk)
  * due integer
  * completed integer
  * description text
 * version
  * name text (pk)
  * time integer
  * description text
 * report
  * id integer (pk)
  * author text
  * title text
  * query text
  * description