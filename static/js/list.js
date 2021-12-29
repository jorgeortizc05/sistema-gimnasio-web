$(function () {
    $('#data').DataTable({
        responsive: true,
        dom: 'B<"clear">lfrtip',
        buttons: ['copyHtml5',
            'excelHtml5',
            'csvHtml5',
            'pdfHtml5',
            'print'],
        language: {
            "url": "//cdn.datatables.net/plug-ins/9dcbecd42ad/i18n/Spanish.json"
        }
    });
    $('.btnTest').on('click', () => {
        $.ajax({
            url: urlTypePeopleList,
            type: 'POST',
            data: {id: 15},
            dataType: 'json'
        }).done((data) => {
            console.table(data)
        }).fail((jqXHR, textStatus, errorThrown) => {
            console.log("No hay datos de ese tipo de persona");
            console.log(textStatus + ": " + errorThrown);
        }).always((data) => {

        });
    });
});