CREATE TABLE public.video_project (
    id bigint NOT NULL,
    created_by character varying(255),
    created_date date,
    last_modified_by character varying(255),
    last_modified_date date,
    title character varying(255),
    status character varying(255)
    organization_uuid
);

CREATE TABLE public.video_project_group ( => layer
    id bigint NOT NULL,
    created_by character varying(255),
    created_date date,
    last_modified_by character varying(255),
    last_modified_date date,
    name character varying(255),
    project_id bigint NOT NULL,
    "position" integer
);

CREATE TABLE public.video_project_item (
    id bigint NOT NULL,
    created_by character varying(255),
    created_date date,
    last_modified_by character varying(255),
    last_modified_date date,
    end_timestamp bigint,
    src character varying(255),
    start_timestamp bigint,
    group_id bigint NOT NULL,
    item_type character varying(255)
    offset
);

CREATE TABLE public.video_project_item_thumbnail (
    id bigint NOT NULL,
    created_by character varying(255),
    created_date date,
    last_modified_by character varying(255),
    last_modified_date date,
    "position" bigint,
    src character varying(255),
    item_id bigint NOT NULL
);

ALTER TABLE ONLY public.video_project_group
    ADD CONSTRAINT video_project_group_pkey PRIMARY KEY (id);

ALTER TABLE ONLY public.video_project_item
    ADD CONSTRAINT video_project_item_pkey PRIMARY KEY (id);

ALTER TABLE ONLY public.video_project_item_thumbnail
    ADD CONSTRAINT video_project_item_thumbnail_pkey PRIMARY KEY (id);

ALTER TABLE ONLY public.video_project
    ADD CONSTRAINT video_project_pkey PRIMARY KEY (id);


ALTER TABLE ONLY public.video_project_item
    ADD CONSTRAINT item_group_fk FOREIGN KEY (group_id) REFERENCES public.video_project_group(id);

ALTER TABLE ONLY public.video_project_group
    ADD CONSTRAINT group_project_fk FOREIGN KEY (project_id) REFERENCES public.video_project(id);

ALTER TABLE ONLY public.video_project_item_thumbnail
    ADD CONSTRAINT thumbnail_item_fk FOREIGN KEY (item_id) REFERENCES public.video_project_item(id);