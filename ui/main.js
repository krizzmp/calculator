
function test(){
    var arr=[];
    $('.mathquill-editable').each(
    function( index ) {
        var g = $(this).mathquill('latex')
        var h=g.replace(/\\/g ,"@");
        //console.log(g+'::'+h);
        arr.push(h);
    })
    var str='';
    for(var i=0;i<arr.length-1;i++){
        str+=arr[i]+';;;';
        console.log(str);
    }
    str+=arr[arr.length-1];
    document.title = "msgToPython:::" + str;
}

function jsCallback(msg) {
    //console.log(msg);
    var list=msg.split(",");
    $(".out").each(
    function( index ) {
        $(this).mathquill('latex',list[index]);
    })
}

function toggleMenu(){
    //console.log('test');
    $('nav').toggleClass('on');
}
function newline(t){
    k=$("<div class='mathLine'></div>");
    f1=$("<span class='mathquill-editable'></span>");
    f2=$("<span class='out mathquill-embedded-latex'></span>");
    $(t).parent().after(k);
    k1=$('<span class=""></span>').appendTo(k).mathquill('editable');
    $('<span class="out"></span>').appendTo(k).mathquill();
    k1.children('.textarea').children('textarea').focus();

}

$(document).on('keyup','.mathquill-editable',function(e){
    //console.log('element:'+this);
    test();
    if(e.keyCode=="13"){
        //console.log('jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj');
        newline(this);
    }
});