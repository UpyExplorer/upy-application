# Environment Variables

## Summary

An environment variable is a variable that exists in the context of your project, that is, it only exists on my computer.

### Variable Creation

To create environment variables in your project, simply follow the file template,
available in the root of the project called `.env-default`.

Instructions:

- Copy the `.env-default` file.
- Renames the copy from `.env-default-copy` to `.env`.
- Edit the `.env` file with the necessary information.

### Variable List

| NOME                          | Tipo    | Valor Exemplo                                   |
| ----------------------------  | ------- | ------------------------------------------------|
| DJANGO_DEBUG                  | Integer | 1                                               |
| DJANGO_ENV                    | String  | test - development - production                 |
| DJANGO_APP                    | String  | python manage.py runserver                      |
| DJANGO_SETTINGS_MODULE        | String  | app.settings.development                        |
| DJANGO_DATABASE_URL           | String  | mysql+pymysql://USER:PASSWORD@HOST:PORT/NAME    |
| DJANGO_SECRET_KEY             | String  | key                                             |
| DJANGO_HOST                   | String  | 0.0.0.0                                         |
| DJANGO_PORT                   | Integer | 8080                                            |
| DJANGO_EMAIL_HOST             | String  | smtp.email.com                                  |
| DJANGO_EMAIL_HOST_USER        | String  | no-reply@email.com                              |
| DJANGO_DEFAULT_FROM_EMAIL     | String  | no-reply@email.com                              |
| DJANGO_EMAIL_HOST_PASSWORD    | String  | password                                        |
| DJANGO_EMAIL_PORT             | Integer | 465                                             |
| DJANGO_ALLOWED_HOSTS          | String  | localhost                                       |
| DISABLE_COLLECTSTATIC         | Integer | 1                                               |
| REDIS_TLS_URL                 | String  | rediss://:123@host.com:00000                    |
| REDIS_URL                     | String  | rediss://:123@host.com:00000                    |
