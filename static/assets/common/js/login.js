/**
 * Created by Administrator on 2017/7/20.
 */
/**
 * Created by Administrator on 2017/7/20.
 */
$(".register").click(function (e) {
    var e = e||window.event;
    $(".register-main").show();
    $(".login-main").hide();
    e.preventDefault();
    e.stopPropagation();
});
$(".back-login").click(function (e) {
    var e = e||window.event;
    $(".register-main").hide();
    $(".forget-main").hide();
    $(".login-main").show();
    createCode(".verification-code");
    e.preventDefault();
    e.stopPropagation();
});
$(".forget").click(function (e) {
    var e = e||window.event;
    $(".login-main").hide();
    $(".forget-main").show();
    createCode(".verification-code");
    e.preventDefault();
    e.stopPropagation();
});
$(".unitname").click(function (e) {
    $(".unit-list").hide();
    var e = e||window.event;
    $(this).next(".unit-list").show();
    e.preventDefault();
    e.stopPropagation();
});
$(document).bind('click',function(){
    $(".unit-list").hide();
});
function createCode(id) {
    var code = "";
    var codeLength = 4;//验证码的长度
    var checkCode = $(id);
    var selectChar = new Array(0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m');
    for(var i=0;i<codeLength;i++) {
        var charIndex = Math.floor(Math.random()*62);
        code +=selectChar[charIndex];
    }
    if(checkCode) {
        checkCode.text(code)
    }
}
$(function () {
    createCode(".verification-code");
});
$(".other-code").click(function (e) {
    var e = e||window.event;
    createCode(".verification-code");
    e.preventDefault();
    e.stopPropagation();
})
function alertPrompt(text){
    var temp='<div class="tip" style="display: block;">'+
                '<div class="tiptop"><span>提示信息</span></div>'+
                '<div class="tipinfo">'+
                '<div class="tipright">'+
                '<p id="alerttext">'+text+'</p>'+
                '</div>'+
                '</div>'+
                '<div class="tipbtn">'+
                '<input name="" class="sure" value="确定" type="button">'+
                '</div>'+
                '</div>'+
                '<div class="alert-modal-bgcolor fade in"></div>'
    $(document.body).append(temp);
    $(".tipbtn .sure").unbind("click").bind("click",function () {
        $(".tip").remove()
        $(".alert-modal-bgcolor").remove()
    })
};