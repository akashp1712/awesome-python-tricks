$(document).ready(function(){

    loadTheData();

    function loadTheData() {

        var itemName = 'extend';
        var codeData = pythonData['data'][itemName];
        $("#code").html(codeData['text']);

        highlightCode();
        updateDocumentation();

        function updateDocumentation(itemName) {
            var elem = [];
            elem[0] = "<h2 id='doc-title'>" + codeData['name'] + '</h2>';
            elem[1] = '<div>' + codeData['desc'] + '</div>';

            var text = elem.join('');

            $('#documentation').html(text);
        }

        function highlightCode() {
            $('pre code').each(function(i, e) {hljs.highlightBlock(e);});
        }
    }
});

