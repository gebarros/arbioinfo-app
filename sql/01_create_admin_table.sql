drop table if exists admin;
create table admin (
  id integer primary key autoincrement,
  user text not null,
  pass text not null
)
