
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
    console.log(msg);
    var list=msg.split(",");
    $(".out").each(
    function( index ) {
        $(this).text(list[index]);
    })
}

function toggleMenu(){
    console.log('test');
    $('nav').toggleClass('on');
}


$('.mathquill-editable').on('keyup',function(e){
    console.log('element:'+this);
    test();
});