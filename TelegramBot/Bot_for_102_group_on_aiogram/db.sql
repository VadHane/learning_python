create table users(
    id_user integer primary key,
    name_user varchar(255),
    is_admin boolean
);

create table links(
    primary_name varchar(255) primary key,
    link varchar(500),
    description_link varchar(255)
);

insert into users(id_user, name_user, is_admin)
values
    ('643559378', 'Вадім', true),
    ('586050730', 'Юля', false);


