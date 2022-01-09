$(function () {
    //设置富文本
    // tinymce.init({
    //     selector: '',
    //     height: 400,
    //     plugins: "quickbars emoticons",
    //     inline: false,
    //     toolbar: true,
    //     menubar: true,
    //     quickbars_selection_toolbar: 'bold italic | link h2 h3 blockquote',
    //     quickbars_insert_toolbar: 'quickimage quicktable',
    //
    // });
    tinymce.init({
    //选择class为content的标签作为编辑器
    selector: '.mytextarea',
    //方向从左到右
    directionality: 'ltr',
    //语言选择中文
    language: 'zh_CN',
    //高度为400
    height: 400,
    width: '100%',
    //工具栏上面的补丁按钮
    plugins: [
        'advlist autolink link image lists charmap print preview hr anchor pagebreak spellchecker',
        'searchreplace wordcount visualblocks visualchars code fullscreen insertdatetime media nonbreaking',
        'save table contextmenu directionality template paste textcolor',
        'codesample imageupload',
        'code paste',
    ],
    //工具栏的补丁按钮
    toolbar: 'insertfile undo redo styleselect \
     bold italic imageupload fontsizeselect forecolor backcolor emoticons \
     alignleft aligncenter alignright alignjustify \
     bullist numlist outdent indent \
     link image  \
     print preview media fullpage  \
     codesample fullscreen ',
    //字体大小
    fontsize_formats: '10pt 12pt 14pt 18pt 24pt 36pt',
    //按tab不换行
    nonbreaking_force_tab: true,
    imageupload_url: "submit-image",
    paste_data_images: true,
});
    //验证手机号码
    $('#InputPhone').blur(function () {
        let phone = $(this).val();
        let span_ele = $(this).next('span');
        if (phone.length == 11) {
            span_ele.text('');
            $.get('/user/checkphone', {phone: phone}, function (data) {
                // {#console.log(data);#}
                if (data.code != 200) {
                    span_ele.css({"color": "#ff0011", "font-size": "12px"});
                    span_ele.text(data.msg);
                }
            }
        )
        } else {
            span_ele.css({"color": "#ff0011", "font-size": "12px"});
            span_ele.text('手机格式错误');
        }

    });
    $('.right1').hide();
    $('.right1').eq(0).show();
    $("#left p").first().css({'background-color': 'rgba(30, 150, 196, 0.94)'});
    //切换右侧div
    $("#left p").each(function (i) {
        $(this).click(function () {
            $("#left p").css({'background-color': 'rgba(30, 150, 196, 0.94)'});
            $(this).css({'background-color': 'skyblue', 'box-shadow': '5px 5px 5px deepskyblue'});
            $('.right1').hide();
            $('.right1').eq(i).show();
        });
    });

})