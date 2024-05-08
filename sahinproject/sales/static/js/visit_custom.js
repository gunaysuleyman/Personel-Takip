(function($) {
    $(document).ready(function() {
        // Customer alanını dinle
        $('#id_customer').change(function() {
            var customerId = $(this).val();
            // Müşteri seçildi mi kontrol et
            if (customerId) {
                $.ajax({
                    url: '/admin/get_customer_data/', // Müşteri verilerini getirecek view URL'si
                    data: {
                        'customer_id': customerId
                    },
                    dataType: 'json',
                    success: function(data) {
                        // AJAX isteği başarılı oldu, il ve ilçe alanlarını doldur
                        $('#id_il').val(data.il);
                        $('#id_ilce').val(data.ilce);
                    }
                });
            }
        });
    });
})(django.jQuery);
