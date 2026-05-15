$(document).ready(function() {
    $('.select-buscador').each(function() {
        var $esteSelect = $(this);
        $esteSelect.select2({
            theme: 'bootstrap-5',
            placeholder: $esteSelect.find('option:first').text(),
            allowClear: true,
            dropdownParent: $esteSelect.parent()
        });
    });

    $('.select-paralelo-lineas').each(function() {
        var $esteSelect = $(this);
        $esteSelect.select2({
            theme: 'bootstrap-5',
            placeholder: 'Buscar de paralelo...',
            allowClear: true,
            dropdownParent: $esteSelect.parent(),
            templateResult: formatResult,
            templateSelection: formatSelection
        });
    });

    function formatResult(state) {
        if (!state.id) return state.text;
        
        var partes = state.text.split('|');
        
        if (partes.length === 2) {
            var $html = $(
                '<div style="line-height: 1.3; text-align: left;">' +
                    '<strong style="color: #212529; font-size: 0.95rem;">' + partes[0] + '</strong>' +
                    '<div style="font-size: 0.82em; color: #6c757d; margin-top: 2px;">' + partes[1] + '</div>' +
                '</div>'
            );
            return $html;
        }
        return state.text;
    }

    function formatSelection(state) {
        if (!state.id) return state.text;
        return state.text.replace('|', ' — ');
    }
});