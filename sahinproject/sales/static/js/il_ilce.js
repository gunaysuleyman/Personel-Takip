document.addEventListener('DOMContentLoaded', function() {
    var ilSelect = document.getElementById('id_il');
    var ilceSelect = document.getElementById('id_ilce');

    ilSelect.addEventListener('change', function() {
        var ilId = this.value;
        ilceSelect.innerHTML = '';  // Önceki ilçe seçeneklerini temizle

        if (ilId) {
            fetch(`/get_ilceler/?il_id=${ilId}`)
            .then(response => response.json())
            .then(data => {
                data.forEach(ilce => {
                    var option = document.createElement('option');
                    option.textContent = ilce.ad;
                    option.value = ilce.id;
                    ilceSelect.appendChild(option);
                });
            });
        }
    });
});
