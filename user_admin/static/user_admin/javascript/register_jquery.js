
$(document).ready(function () {
    //注册函数
    var id_username = $("#id_username");
    var id_password = $("#id_password");
    var id_password_yz = $("#id_password_yz");
    var id_email = $("#id_email");
    var submit = $(".submit");

    //检查用户名
    id_username.blur(function () {
        $('.name_tip').remove();
        if (id_username.val().length < 3) {
            id_username.after('<p class="name_tip tip">用户名长度小于3位</p>');
            // submit.attr("disabled",true);
        }
        else {
            var input_name = id_username.val();
            $.ajax({
                url: '/ajax_check_username/',
                type: 'POST',
                data: { username: input_name },
                success: function (arg) {
                    if (arg === input_name) {
                        id_username.after('<p class="name_tip tip">用户名已存在</p>');
                    }
                }
            })
        }

    });

    //检查密码
    id_password.blur(function () {
        $('.password_tip').remove();
        if (id_password.val().length < 4) {
            id_password.after('<p class="password_tip tip">密码长度小于4位</p>');
        }

    });

    //第二次核对密码
    id_password_yz.blur(function () {
        $('.password_yz_tip').remove();
        if (id_password_yz.val() !== id_password.val()) {
            id_password_yz.after('<p class="password_yz_tip tip">两次密码不一致</p>');
        }
    });
});

