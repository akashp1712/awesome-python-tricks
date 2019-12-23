$(document).ready(function(){

    loadTheData();

    function loadTheData() {

        var data = pythonData['data'];
        var keys = Object.keys(data);
        var itemKey = keys[randomNumber(0, keys.length)];
        console.log(randomNumber(0, keys.length));
        var codeData = data[itemKey];

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

    function randomNumber(min, max) {
        // generating number between min and max with rounding
        return (Math.random() * (max - min) + min) << 0;
    }

});

