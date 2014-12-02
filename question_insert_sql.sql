INSERT IGNORE into Test.sof_questions
(post_id, accepted_answer_id, creation_date,score,view_count,owner_user_id,body,title,tags,answer_count, comment_count,favourite_count,body_annotation, title_annotation)
SELECT post_id, accepted_answer_id, creation_date,score,view_count,owner_user_id,body,title,tags,answer_count, comment_count, favourite_count,body_annotation, title_annotation
FROM Test.sof_posts WHERE post_type_id =1 and tags like '%xml%' and post_id > 4370185
LIMIT 300000;