function hid_div(){
    if ($('#pubForm').length > 0 ){
        $('#pubForm').hide();
    }

    if ($('#disggreReson').length> 0){
        $('#disggreReson').hide();
    }
}

/* 显示和隐藏不同意申请理由的输入框 */
$(document).ready(function(){
    if ($('#disggreReson').length > 0){
        $("#show_div").click(function() {
            $("#disggreReson").toggle();
        });
    };

    if ($('#remindStuChoice').length > 0){
        $("#show_div").click(function() {
            $("#remindStuChoice").toggle();
        });
    };

    if ($('#pubForm').length > 0){
        $("#showPubForm").click(function() {
            $("#pubForm").toggle();
        });
    };

});

function pub_ann(){
    var ann = $('#group_ann').val();
    console.log(ann.trim())
    if (ann.trim() == ''){
        alert('不能为空！');
        return false;
    }
};


$('.captcha').css({
    'cursor': 'pointer'
})

//验证码刷新
$('.captcha').click(function(){
    $.getJSON("/captcha/refresh/",
        function(result){
            $('.captcha').attr('src', result['image_url']);
            $('#id_captcha_0').val(result['key']);
        });
 });
