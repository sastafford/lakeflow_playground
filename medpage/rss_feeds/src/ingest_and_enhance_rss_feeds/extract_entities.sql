CREATE OR REPLACE TABLE usa.osint.gold_rss AS
SELECT
  *,
  ai_extract(content, array('person', 'organization', 'location', 'disease', 'drug', 'treatment')) AS entities
FROM
  usa.osint.silver_rss;
