function loadJSXG(path)
{
    var selection = document.getElementById("selection");
    path = "file:///home/graebe/git/SD/code/Geo-18/Intergeo/";
    fname = path + selection.options[selection.selectedIndex].value.toString();

    $('debug').innerHTML = fname+'<br>';
    board = JXG.JSXGraph.loadBoardFromFile('jxgbox', fname , 'Intergeo');
}
