--	<item>
--		<title>_4</title>
--		<link>http://192.168.99.100:8080/?attachment_id=1582</link>
--		<pubDate>Sat, 28 Nov 2015 02:55:29 +0000</pubDate>
--		<dc:creator><![CDATA[stefan]]></dc:creator>
--		<guid isPermaLink="false">http://192.168.99.100:8080/wp-content/uploads/2015/11/4.jpg</guid>
--		<description></description>
--		<content:encoded><![CDATA[]]></content:encoded>
--		<excerpt:encoded><![CDATA[]]></excerpt:encoded>
--		<wp:post_id>1582</wp:post_id>
--		<wp:post_date>2015-11-28 03:55:29</wp:post_date>
--		<wp:post_date_gmt>2015-11-28 02:55:29</wp:post_date_gmt>
--		<wp:comment_status>open</wp:comment_status>
--		<wp:ping_status>closed</wp:ping_status>
--		<wp:post_name>_4</wp:post_name>
--		<wp:status>inherit</wp:status>
--		<wp:post_parent>0</wp:post_parent>
--		<wp:menu_order>0</wp:menu_order>
--		<wp:post_type>attachment</wp:post_type>
--		<wp:post_password></wp:post_password>
--		<wp:is_sticky>0</wp:is_sticky>
--		<wp:attachment_url>http://192.168.99.100:8080/wp-content/uploads/2015/11/4.jpg</wp:attachment_url>
--		<wp:postmeta>
--			<wp:meta_key>_wp_attached_file</wp:meta_key>
--			<wp:meta_value><![CDATA[2015/11/4.jpg]]></wp:meta_value>
--		</wp:postmeta>
--		<wp:postmeta>
--			<wp:meta_key>_wp_attachment_metadata</wp:meta_key>
--			<wp:meta_value><![CDATA[a:5:{s:5:"width";i:692;s:6:"height";i:461;s:4:"file";s:13:"2015/11/4.jpg";s:5:"sizes";a:3:{s:9:"thumbnail";a:4:{s:4:"file";s:13:"4-150x150.jpg";s:5:"width";i:150;s:6:"height";i:150;s:9:"mime-type";s:10:"image/jpeg";}s:6:"medium";a:4:{s:4:"file";s:13:"4-300x200.jpg";s:5:"width";i:300;s:6:"height";i:200;s:9:"mime-type";s:10:"image/jpeg";}s:14:"post-thumbnail";a:4:{s:4:"file";s:13:"4-604x270.jpg";s:5:"width";i:604;s:6:"height";i:270;s:9:"mime-type";s:10:"image/jpeg";}}s:10:"image_meta";a:11:{s:8:"aperture";i:0;s:6:"credit";s:0:"";s:6:"camera";s:0:"";s:7:"caption";s:0:"";s:17:"created_timestamp";i:0;s:9:"copyright";s:0:"";s:12:"focal_length";i:0;s:3:"iso";i:0;s:13:"shutter_speed";i:0;s:5:"title";s:0:"";s:11:"orientation";i:0;}}]]></wp:meta_value>
--		</wp:postmeta>
--	</item>

SELECT xmlelement(
    name item,
        xmlforest (
            slug as "title",
            'http://192.168.99.100:8080/?attachment_id=' || 10000 + id as "link",
            uploaded as "pubDate",
            'stefan' as "dc:creator",
            'http://kreuzundquer-ev.de/static/uploads/' || to_char(p.uploaded, 'YYYY') || '/' || to_char(p.uploaded, 'MM') || '/' || 10000 + p.id || '.jpg'  as "guid",
            '' as "description",
            '' as "content:encoded",
            '' as "excerpt:encoded",
            10000 + p.id as "wp:post_id",
            uploaded as "wp:post_date",
            uploaded as "wp:post_date_gmt",
            'open' as "wp:comment_status",
            'open' as "wp:ping_status",
            slug as "wp:post_name",
            'inherit' as "wp:status",
            '0' as "wp:post_parent",
            '0' as "wp:menu_order",
            'attachment' as "wp:post_type",
            '' as "wp:post_password",
            '0' as "wp:is_sick",
            'http://kreuzundquer-ev.de/static/uploads/' || to_char(p.uploaded, 'YYYY') || '/' || to_char(p.uploaded, 'MM') || '/' || 10000 + p.id || '.jpg'  as "wp:attachment_url"
        )
    )
FROM media_photos p
ORDER BY p.id;
