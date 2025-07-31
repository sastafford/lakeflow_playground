import dlt

dlt.create_streaming_table("silver_person")

dlt.create_auto_cdc_from_snapshot_flow(
 target="silver_person",
 source="person_snapshot",
 keys=["id"],
 stored_as_scd_type=2
)