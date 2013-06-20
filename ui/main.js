
function test(){
    var g = $('span').mathquill('latex')
    var h=g.replace(/\\/g ,"@");
    console.log(g+'::'+h);
    document.title = "msgToPython:::" + h;
}

function jsCallback(msg) {
    document.getElementById("out").innerHTML = msg;
}


$('body').on('keydown',function(e){
    test();
});