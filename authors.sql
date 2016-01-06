SELECT xmlelement(
    name "wp:author",
        xmlforest (
          id as "wp:author_id",
          username as "wp:author_login",
          email as "wp:author_email",
          first_name as "wp:display_name",
          first_name as "wp:first_name",
          last_name as "wp:last_name"
          )
        )
FROM auth_user ORDER BY id;
