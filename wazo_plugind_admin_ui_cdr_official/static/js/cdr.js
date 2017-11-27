$(document).ready(function () {
  let table_config = {
    select: true,
    columns: [
      {data: 'start'},
      {data: 'source_extension'},
      {data: 'source_name'},
      {data: 'destination_extension'},
      {data: 'destination_name'},
      {data: 'duration'},
      {data: 'answered'},
    ],
    columnDefs: [
      {targets: 0}
    ]
  };

  let Table = create_table_serverside(table_config);
  Table.buttons(0, null).containers().appendTo('body');
});
