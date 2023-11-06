import dlt

# This is just a placeholder
dlt.apply_changes(
    target=current_table_name,
    source=change_table_name,
    keys=keys,
    sequence_by=sequence_by,
    apply_as_deletes=apply_as_deletes,
    except_column_list=except_column_list,
)