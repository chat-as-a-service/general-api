CREATE TABLE organization (
    id bigserial PRIMARY KEY,
    name varchar(255) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    created_by varchar(255) NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    updated_by varchar(255) NOT NULL
);

CREATE TABLE account (
    id bigserial PRIMARY KEY,
    email varchar(255) NOT NULL,
    password text NOT NULL,
    first_name varchar(255) NOT NULL,
    last_name varchar(255) NOT NULL,
    organization_id bigint,
    created_at timestamp with time zone NOT NULL,
    created_by varchar(255) NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    updated_by varchar(255) NOT NULL
);
CREATE INDEX idx_account_organization_id ON account(organization_id);

CREATE TABLE application (
    id bigserial PRIMARY KEY,
    uuid uuid NOT NULL DEFAULT gen_random_uuid(),
    name varchar(255) NOT NULL,
    organization_id bigint NOT NULL,
    master_api_token varchar(255) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    created_by varchar(255) NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    updated_by varchar(255) NOT NULL
);
CREATE INDEX idx_application_organization_id ON application(organization_id);
CREATE INDEX idx_application_organization_master_api_token ON application(master_api_token);

CREATE TABLE "user" (
    id bigserial PRIMARY KEY,
    application_id bigint NOT NULL,
    username varchar(255) NOT NULL,
    nickname varchar(255) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    created_by varchar(255) NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    updated_by varchar(255) NOT NULL,
    UNIQUE (application_id, username)
);
CREATE INDEX idx_user_application_id ON "user"(application_id);

CREATE TABLE channel (
    id bigserial PRIMARY KEY,
    uuid uuid NOT NULL unique DEFAULT gen_random_uuid(),
    application_id bigint NOT NULL,
    name varchar(255) NOT NULL,
    max_members INT NOT NULL,
    created_at timestamp with time zone NOT NULL,
    created_by varchar(255) NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    updated_by varchar(255) NOT NULL
);
CREATE INDEX idx_channel_application_id ON channel(application_id);

CREATE TABLE channel_users (
    id bigserial PRIMARY KEY,
    user_id bigint NOT NULL,
    channel_id bigint NOT NULL,
    created_at timestamp with time zone NOT NULL,
    created_by varchar(255) NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    updated_by varchar(255) NOT NULL
);
CREATE INDEX idx_channel_users_user_id ON channel_users(user_id);
CREATE INDEX idx_channel_users_channel_id ON channel_users(channel_id);

CREATE TABLE message (
    id bigserial PRIMARY KEY,
    uuid uuid NOT NULL DEFAULT gen_random_uuid(),
    user_id bigint NOT NULL,
    channel_id bigint NOT NULL,
    message varchar(3000) NOT NULL,
    created_at timestamp with time zone NOT NULL,
    created_by varchar(255) NOT NULL,
    updated_at timestamp with time zone NOT NULL,
    updated_by varchar(255) NOT NULL
);
CREATE INDEX idx_message_user_id ON message(user_id);
CREATE INDEX idx_message_channel_id ON message(channel_id);
CREATE INDEX idx_message_created_at ON message(created_at);
