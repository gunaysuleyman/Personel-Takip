// static/js/date_format.js
document.addEventListener('DOMContentLoaded', function() {
    var dateInput = document.querySelector('input[name="date"]');

    dateInput.addEventListener('input', function(e) {
        var value = e.target.value;
        if (/^\d{2}$/.test(value)) {
            e.target.value = value + '.';
        } else if (/^\d{2}\/\d{2}$/.test(value)) {
            e.target.value = value + '.';
        }
    });
});

document.addEventListener('DOMContentLoaded', function() {
    var dateInput = document.querySelector('input[name="date"]');

    // Date formatting while typing
    dateInput.addEventListener('input', function(e) {
        var value = e.target.value;
        if (/^\d{2}$/.test(value)) {
            e.target.value = value + '.';
        } else if (/^\d{2}\/\d{2}$/.test(value)) {
            e.target.value = value + '.';
        }
    });

    // Setting today's date on calendar icon click
    var calendarIcon = document.getElementById('calendar-icon');
    calendarIcon.addEventListener('click', function() {
        // console.log('clicked');
        var today = new Date();
        var dd = String(today.getDate()).padStart(2, '0');
        var mm = String(today.getMonth() + 1).padStart(2, '0'); // January is 0!
        var yyyy = today.getFullYear();
        var formatted_date = dd + '.' + mm + '.' + yyyy;
        // console.log(formatted_date);
        dateInput.value = formatted_date;
    });
});