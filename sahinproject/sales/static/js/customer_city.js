// jQuery ile
$('#id_customer').change(function() {
    var customerId = $(this).val();
    $.ajax({
        url: '/get_customer_info/' + customerId + '/',
        data: {
            'customer_id': customerId
        },
        dataType: 'json',
        success: function(data) {
            console.log(data);
            $('#id_il').val(data.il_id);
            $('#id_ilce').val(data.ilce_id);
        }
    });
});

// // Pure JavaScript ile
// document.getElementById('id_customer').addEventListener('change', function() {
//     var customerId = this.value;
//     var xhr = new XMLHttpRequest();
//     xhr.open('GET', '/get_customer_info/?customer_id=' + customerId, true);
//     xhr.onload = function() {
//         if (xhr.status === 200) {
//             var data = JSON.parse(xhr.responseText);
//             document.getElementById('id_il').value = data.il_id;
//             document.getElementById('id_ilce').value = data.ilce_id;
//         }
//     };
//     xhr.send();
// });
