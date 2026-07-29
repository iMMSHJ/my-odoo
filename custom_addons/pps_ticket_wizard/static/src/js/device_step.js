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
        fetch('/support/new/device/info', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({jsonrpc: '2.0', method: 'call', params: {asset_id: assetId}}),
        })
        .then(function (r) { return r.json(); })
        .then(function (data) {
            var result = data.result || {};
            document.getElementById('pps_info_location').textContent = result.location || '-';
            document.getElementById('pps_info_sla').textContent = result.sla_name || '-';
            document.getElementById('pps_info_response').textContent = result.sla_response || '-';
            document.getElementById('pps_info_onsite').textContent = result.sla_onsite || '-';
            infoBox.style.display = 'block';
        });
    });
});
