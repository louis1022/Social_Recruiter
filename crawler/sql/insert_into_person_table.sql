truncate social_recruiter.app_person;

insert into social_recruiter.app_person 
(
  user_id,
  screen_name,
  location,
  url,
  description,
  friends_count,
  followers_count,
  listed_count,
  favourites_count,
  statuses_count,
  created_at
)

select 
  user_id,
  screen_name,
  location,
  url,
  description,
  friends_count,
  followers_count,
  listed_count,
  favourites_count,
  statuses_count,
  created_at
from twitter_db.user_info;
