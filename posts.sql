SELECT xmlelement(
    name item,
        xmlforest (
            title as "title",
            'http://kreuzundquer-ev.de/blog/' || to_char(date, 'YYYY') || '/' || to_char(date, 'MM') || '/' || to_char(date, 'DD') || '/' || slug as "link",
            date as "pubDate",
            (SELECT username FROM auth_user u WHERE u.id = p.author_id) as "dc:creator",
            'http://kreuzundquer-ev.de/?p=' || p.id  as "guid",
            '' as "description",
            -- '<![CDATA[' || body_html || ']]>' as "content:encoded",
            body_html as "content:encoded",
            -- '<![CDATA[' || excerpt || ']]>' as "excerpt:encoded",
            excerpt as "excerpt:encoded",
            p.id as "wp:post_id",
            date as "wp:post_date",
            date as "wp:post_date_gmt",
            'open' as "wp:comment_status",
            'open' as "wp:ping_status",
            slug as "wp:post_name",
            'publish' as "wp:status",
            '0' as "wp:post_parent",
            '0' as "wp:menu_order",
            'post' as "wp:post_type",
            '' as "wp:post_password",
            '0' as "wp:is_sick"
        ),
        xmlagg(
            xmlelement(
                name "wp:comment",
                xmlforest(
                    c.id as "wp:comment_id",
                    c.user_name as "wp:comment_author",
                    c.user_email as "wp:comment_author_email",
                    c.ip_address as "wp:comment_author_IP",
                    c.submit_date as "wp:comment_date",
                    c.submit_date as "wp:comment_date_gmt",
                    c.comment as "wp:comment_content",
                    c.id / c.id as "wp:comment_approved", -- '1'
                    c.id - c.id as "wp:comment_parent" -- '0'
                    --'' as "wp:comment_type",
                    --c.user_id as "wp:comment_user_id"
                )
            )
        )
    )
FROM blog_entry p
  LEFT JOIN django_comments c ON c.object_pk::numeric = p.id
--WHERE p.date BETWEEN '2010-01-01' AND '2011-01-01'
GROUP BY p.id
ORDER BY p.id;
