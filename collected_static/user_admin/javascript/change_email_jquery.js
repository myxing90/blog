$(function () {
    var old_email = $('#old-email')
    var new_email = $('#new-email')
    var yzm = $('#yzm')
    var email_button = $('.email-button')
    var email_submit = $('#email-submit')
    var input_info = $('.input-info')

    old_email.blur(function () {
        $.ajax({
            url: '/ajax_check_old_email/',
            type: 'POST',
            data: { old_email: old_email.val() },
            success: function (arg) {
                if (arg === 'True' && old_email.val().length >= 5) {
                    input_info.first().text('旧邮箱验证成功');
                    return true;
                }
                else {
                    if (arg === 'False' && old_email.val().length >= 1) {
                        input_info.first().text('旧邮箱验证错误，请从新输入');
                        return false;
                    }
                };
            }
        });
    });

    email_button.click(function () {
        var email_re = /\w[-\w+\.]*@([A-Za-z0-9]+\.)+[a-zA-Z]{1,3}/
        if (email_re.test(new_email.val())) {
            input_info.text('');
            $.ajax({
                url: '/ajax_send_yzm/',
                type: 'POST',
                data: { new_email: new_email.val() },
                success: function (arg) {
                    if (arg === 'True') {
                        input_info.eq(2).text('验证码已发送，1小时有效');
                        return true;
                    };
                }
            });
        }
        else {
            input_info.eq(1).text('请输入正确的邮箱格式!');
            return false;
            alert('请输入正确的邮箱格式!');
        };
    });

    email_submit.click(function () {
        alert('ok');
    })
})
