import praw

r = praw.Reddit(user_agent='example')
submission = r.get_subreddit('programming').get_top(limit=10)
for i in submission:
        print i
        
CREATE  TABLE IF NOT EXISTS `Test`.`red_posts` (
  `id` INT NOT NULL AUTO_INCREMENT ,
  `post_id` VARCHAR(25) NULL ,
  `title` VARCHAR(500) NULL ,
  `body` LONGTEXT NULL ,
  `author` VARCHAR(50) NULL ,
  `up_vote` INT NULL ,
  `down_vote` INT NULL ,
  `score` INT NULL ,
  `permalink` VARCHAR(500) NULL ,
  `url` VARCHAR(500) NULL ,
  `creation_date` INT(11) NULL ,
  `subreddit` VARCHAR(50) NULL ,
  PRIMARY KEY (`id`) ,
  UNIQUE INDEX `post_id_UNIQUE` (`post_id` ASC) )
ENGINE = InnoDB