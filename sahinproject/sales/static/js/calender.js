$(document).ready(function () {
    $('#calendar-icon').click(function () {
        var today = new Date();
        var dd = String(today.getDate()).padStart(2, '0');
        var mm = String(today.getMonth() + 1).padStart(2, '0'); //January is 0!
        var yyyy = today.getFullYear();
        var formatted_date = yyyy + '-' + mm + '-' + dd;
        $('#id_date').val(formatted_date);
    });
});
