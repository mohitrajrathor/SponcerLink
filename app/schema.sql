DROP TABLE IF EXISTS "sponcers";
DROP TABLE IF EXISTS "industries";
DROP TABLE IF EXISTS "campaigns";
DROP TABLE IF EXISTS "ad_requests";
DROP TABLE IF EXISTS "admins";
DROP TABLE IF EXISTS "admin_actions";
DROP TABLE IF EXISTS "influencers";
DROP TABLE IF EXISTS "social_accounts";
DROP TABLE IF EXISTS "sponcership_requests";
DROP TABLE IF EXISTS "niche_categories";




CREATE TABLE IF NOT EXISTS "sponcers" (
	"sponcer_id" INTEGER NOT NULL UNIQUE,
	"username" TEXT NOT NULL,
	"name" TEXT NOT NULL,
	"password" TEXT NOT NULL,
	"join_time" TEXT NOT NULL,
	"sp_company" INTEGER NOT NULL DEFAULT false,
	"industry_id" INTEGER,
	"email" TEXT NOT NULL,
	"ph_num" INTEGER NOT NULL,
	"address" TEXT NOT NULL,
	"website" TEXT,
	"balance" REAL NOT NULL DEFAULT 0,
	PRIMARY KEY("sponcer_id"),
	FOREIGN KEY ("industry_id") REFERENCES "industries"("industry_id")
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS "industries" (
	"industry_id" INTEGER NOT NULL UNIQUE,
	"name" TEXT NOT NULL,
	"description" TEXT NOT NULL,
	"created_time" TEXT NOT NULL,
	PRIMARY KEY("industry_id")	
);

CREATE TABLE IF NOT EXISTS "campaigns" (
	"camp_id" INTEGER NOT NULL UNIQUE,
	"title" TEXT NOT NULL,
	"description" TEXT NOT NULL,
	"niche_category" INTEGER NOT NULL,
	"budget" REAL NOT NULL,
	"start_date" TEXT NOT NULL,
	"end_date" TEXT NOT NULL,
	"sponcer_id" INTEGER NOT NULL,
	"created_time" TEXT NOT NULL,
	"update_time" TEXT NOT NULL,
	"privacy_type" TEXT NOT NULL DEFAULT 'public',
	"category_id" INTEGER,
	PRIMARY KEY("camp_id"),
	FOREIGN KEY ("sponcer_id") REFERENCES "sponcers"("sponcer_id")
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS "ad_requests" (
	"request_id" INTEGER NOT NULL UNIQUE,
	"sponcer_id" INTEGER NOT NULL,
	"influencer_id" INTEGER NOT NULL,
	"title" TEXT NOT NULL,
	"description" TEXT NOT NULL,
	-- date from which ad should start showing.
	"start_date" TEXT NOT NULL,
	-- ad showing till this date.
	"end_date" TEXT NOT NULL,
	"budget" REAL NOT NULL,
	"status" TEXT NOT NULL,
	"created_time" TEXT NOT NULL,
	"updated_time" TEXT NOT NULL,
	"camp_id" INTEGER NOT NULL,
	PRIMARY KEY("request_id"),
	FOREIGN KEY ("sponcer_id") REFERENCES "sponcers"("sponcer_id")
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS "admins" (
	"admin_id" INTEGER NOT NULL UNIQUE,
	"username" TEXT NOT NULL,
	"email" TEXT NOT NULL,
	"password" TEXT NOT NULL,
	"created_time" TEXT NOT NULL,
	"updated_time" TEXT NOT NULL,
	PRIMARY KEY("admin_id"),
	FOREIGN KEY ("admin_id") REFERENCES "admin_actions"("admin_id")
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS "admin_actions" (
	"action_id" INTEGER NOT NULL UNIQUE,
	"user_id" INTEGER NOT NULL,
	-- can be influencer or sponcer
	"type" TEXT NOT NULL,
	-- can be "warned" or "fully-restricted"
	"flag_type" TEXT NOT NULL,
	-- id of admin who did the action

	"admin_id" INTEGER NOT NULL,
	"reason" TEXT,
	"time" TEXT NOT NULL,
	PRIMARY KEY("action_id"),
	FOREIGN KEY ("user_id") REFERENCES "sponcers"("sponcer_id")
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS "influencers" (
	"influencer_id" INTEGER NOT NULL UNIQUE,
	"name" TEXT NOT NULL,
	"email" TEXT NOT NULL,
	"ph_num" INTEGER NOT NULL,
	"password" TEXT NOT NULL,
	"bio" TEXT,
	"niche_category" TEXT NOT NULL,
	"balance" REAL NOT NULL DEFAULT 0,
	"created_time" TEXT NOT NULL,
	"updated_time" TEXT NOT NULL,
	"category_id" INTEGER NOT NULL,
	PRIMARY KEY("influencer_id"),
	FOREIGN KEY ("influencer_id") REFERENCES "ad_requests"("influencer_id")
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS "social_accounts" (
	"account_id" INTEGER NOT NULL UNIQUE,
	"platform_id" INTEGER NOT NULL UNIQUE,
	"handle_url" TEXT NOT NULL UNIQUE,
	"followers_count" INTEGER NOT NULL,
	"created_time" TEXT NOT NULL,
	"updated_time" TEXT NOT NULL,
	"influencer_id" INTEGER NOT NULL UNIQUE,
	PRIMARY KEY("account_id"),
	FOREIGN KEY ("influencer_id") REFERENCES "influencers"("influencer_id")
	ON UPDATE NO ACTION ON DELETE NO ACTION
);

CREATE TABLE IF NOT EXISTS "sponcership_requests" (
	"sp_req_id" INTEGER NOT NULL UNIQUE,
	"influencer_id" INTEGER NOT NULL,
	"camp_id" INTEGER NOT NULL,
	"title" TEXT NOT NULL,
	"description" TEXT NOT NULL,
	"ask_price" REAL NOT NULL,
	"start_date" TEXT NOT NULL,
	"end_date" TEXT NOT NULL,
	"status" TEXT NOT NULL,
	"created_time" TEXT NOT NULL,
	"updated_time" TEXT NOT NULL,
	PRIMARY KEY("sp_req_id"),
	FOREIGN KEY ("influencer_id") REFERENCES "influencers"("influencer_id")
	ON UPDATE NO ACTION ON DELETE NO ACTION
);
