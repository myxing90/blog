$(function () {
    var pw_old = $('#id_password_old');
    var pw_new = $('#id_password_new');
    var pw_yz = $('#id_password_new_yz');
    var submit = $('.submit');
    var PW_ERROR_INFO = $('#PW_ERROR_INFO');

    pw_new.blur(function () {
        // $('.password_new_info').remove();
        if (pw_new.val().length < 4 && pw_new.val().length >= 1) {
            pw_new.after('<p class="password_new_info pw_yz">密码长度小于4位</p>');
            // pw_yz.attr("disabled", 'disabled')
        }
        // else {
        //     pw_yz.removeAttr('disabled')
        // }
    });

    pw_yz.bind('blur keyup', (function () {
        $('.password_yz_info').remove();
        if (pw_new.val() !== pw_yz.val() && pw_yz.val().length >= 1) {
            pw_yz.after('<p class="password_yz_info pw_yz">两次密码不一致</p>');
        };
    }));

    if (PW_ERROR_INFO.text() == '原密码错误') {
        pw_old.after('<p class="password_old_info pw_yz">原密码错误，请重试！</p>');
    };

    if (PW_ERROR_INFO.text() == '密码修改成功') {
        alert('密码修改成功！');
        window.location.href = "/useradmin/";
    };
})