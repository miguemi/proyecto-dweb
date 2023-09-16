$(function () {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {"data": "name"},
            {"data": null},
        ],
        columnDefs: [
            {
                targets: [2],
                orderable: false,
                class: 'text-center',
                render: function (data, type, row) {
                    return `<a href="/category/edit/${row.id}" class="btn btn-warning btn-xs btn-flat"><i class="fas fa-edit"></i></a> 
                            <a href="/category/delete/${row.id}" class="btn btn-danger btn-xs btn-flat"><i class="fas fa-trash-alt"></i></a>`;
                }
            },
        ],
        initComplete: function (settings, json) {
        }
    });
});