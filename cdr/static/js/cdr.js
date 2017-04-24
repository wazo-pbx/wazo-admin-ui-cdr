$(document).ready(function() {
  var table_config = {
    columns: [
      { data: 'start' },
      { data: 'source_extension' },
      { data: 'source_name' },
      { data: 'destination_extension' },
      { data: 'destination_name' },
      { data: 'duration' },
      { data: 'answered' },
    ]
  };
  create_table_serverside(table_config);
});
