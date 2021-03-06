ALTER TABLE webapps_rating_descriptors
    DROP COLUMN `has_generic_alcohol_ref`,
    DROP COLUMN `has_generic_blood_gore`,
    DROP COLUMN `has_generic_blood`,
    DROP COLUMN `has_generic_crude_humor`,
    DROP COLUMN `has_generic_drug_ref`,
    DROP COLUMN `has_generic_fantasy_violence`,
    DROP COLUMN `has_generic_intense_violence`,
    DROP COLUMN `has_generic_mild_blood`,
    DROP COLUMN `has_generic_mild_fantasy_violence`,
    DROP COLUMN `has_generic_mild_lang`,
    DROP COLUMN `has_generic_mild_violence`,
    DROP COLUMN `has_generic_nudity`,
    DROP COLUMN `has_generic_partial_nudity`,
    DROP COLUMN `has_generic_real_gambling`,
    DROP COLUMN `has_generic_sex_themes`,
    DROP COLUMN `has_generic_sim_gambling`,
    DROP COLUMN `has_generic_strong_lang`,
    DROP COLUMN `has_generic_strong_sex_content`,
    DROP COLUMN `has_generic_suggestive`,

    ADD COLUMN `has_generic_discrimination` bool NOT NULL,
    ADD COLUMN `has_generic_drugs` bool NOT NULL,
    ADD COLUMN `has_generic_gambling` bool NOT NULL,
    ADD COLUMN `has_generic_no_descs` bool NOT NULL,
    ADD COLUMN `has_generic_online` bool NOT NULL,
    ADD COLUMN `has_generic_scary` bool NOT NULL,
    ADD COLUMN `has_generic_violence` bool NOT NULL,

    ADD COLUMN `has_pegi_digital_purchases` bool NOT NULL,
    ADD COLUMN `has_pegi_shares_info` bool NOT NULL,
    ADD COLUMN `has_pegi_shares_location` bool NOT NULL,
    ADD COLUMN `has_pegi_users_interact` bool NOT NULL,

    CHANGE `has_esrb_alcohol` `has_esrb_alcohol_ref` bool NOT NULL;
