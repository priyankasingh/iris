INSERT IGNORE into sof_answers
(post_id,parent_id,creation_date, score, body, title,owner_user_id, tags, comment_count, body_annotation, title_annotation)
select t1.post_id, t1.parent_id, t1.creation_date, t1.score, t1.body, t2.title, t1.owner_user_id, t2.tags, t1.comment_count, t1.body_annotation, t2.title_annotation
from Test.sof_posts t1, Test.sof_questions t2
Where t1.parent_id = t2.post_id and t1.post_id > 15776855
LIMIT 1100000;