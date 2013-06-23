
function test(){
    var arr=[];
    $('.mathquill-editable').each(
    function( index ) {
        var g = $(this).mathquill('latex')
        var h=g.replace(/\\/g ,"@");
        console.log(g+'::'+h);
        arr.push(h);
    })
    document.title = "msgToPython:::" + arr;
}

function jsCallback(msg) {
    document.getElementById("out").innerHTML = msg;
}


$('body').on('keyup',function(e){
    console.log($('textarea').val());
    test();
});