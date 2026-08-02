document.addEventListener('DOMContentLoaded', function () {
    var select = document.getElementById('pps_asset_select');
    if (!select) return;

    select.addEventListener('change', function () {
        var assetId = select.value;
        var infoBox = document.getElementById('pps_asset_info');
        if (!assetId) {
            infoBox.style.display = 'none';
            return;
        }
        // Data is already rendered server-side into hidden divs (no AJAX,
        // to avoid a race condition with session writes — see DOC-038 §8.4).
        var source = document.getElementById('pps_asset_data_' + assetId);
        if (source) {
            document.getElementById('pps_info_location').textContent = source.dataset.location || '-';
            document.getElementById('pps_info_sla').textContent = source.dataset.slaName || '-';
            document.getElementById('pps_info_response').textContent = source.dataset.slaResponse || '-';
            document.getElementById('pps_info_onsite').textContent = source.dataset.slaOnsite || '-';
            infoBox.style.display = 'block';
        }
    });
});
