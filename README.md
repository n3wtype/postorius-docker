# postorius-docker

The purpose of this Dockerfile is to build postorius container that could be used with mailman3.

## Usage

This docker containter could be used in cooperation with mailman3-docker image [github](https://github.com/n3wtype/mailman3-docker) [dockerhub](https://hub.docker.com/r/newtype87/mailman3-docker/) and with [compose](https://github.com/n3wtype/mailman3-compose).

As part of RUN command admin user is beeing auto-created with password specified by **POSTORIUS_ADMIN_PASS** env variable. If admin user already its password is beeing update to reflect current vlaue of **POSTORIUS_ADMIN_PASS** provided.

## Expected env variables

**MAILMAN_REST_API_URL** - url pointing to mailman3 REST API endpoint (default: http://mailman-core:8001)
**MAILMAN_REST_API_USER** - user used to authenticate to mailman3 API endpoint (default: restadmin)
**MAILMAN_REST_API_PASSWORD** - password used to authenticate to mailman3 API endpoint (default: restpass)

**POSTORIUS_SMTP_HOST** - address of smtp server which is relaying messgaes send by postorius (default: none, must be provided)
**POSTORIUS_SMTP_PORT** - tcp port used to connect to relay smtp server (default: 25)
**POSTORIUS_SMTP_FROM** - email address used in smtp from field for messages genearted by postorius (default: none, must be provided)
**POSTORIUS_SMTP_USE_TLS** - TRUE/FALSE (default: FALSE)
**POSTORIUS_SMTP_USE_SSL** - TRUE/FALSE (default: FALSE)i

**POSTORIUS_ADMIN_PASS** - password for postorius admin user (default: postoriuspass)



