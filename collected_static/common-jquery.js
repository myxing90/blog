//	右下角功能按钮（回到顶部，反馈）
$(document).ready(function () {
	var go_top = $(".go-top");
	var feedback = $(".feedback");
	var feedback_box = $('.feedback-box');
	var feedback_button = $("#feedback-button")

	go_top.mousemove(function () {
		go_top.html('回到<br>顶部');
		go_top.css({
			'background-image': '',
			'background-color': '#188eee',
			'color': '#fff',
		});
	});

	go_top.mouseout(function () {
		go_top.text('');
		go_top.css({
			'background-color': '',
			'background-image': 'url(../../static/mysite/images/icon/top.png)',
		});
	});

	$(window).scroll(function () { 				//bom 操作，当浏览器窗口滑动的时候。
		var feedback_top = feedback.offset().top
		if (feedback_top < 600) {
			go_top.hide();
		} else {
			go_top.show();
		}
	});

	go_top.click(function () {
		$('body,html').animate({
			scrollTop: '0'
		}, 'fast');
	});

	feedback_box_handel();

	function feedback_box_handel() {
		feedback.bind({
			mouseover: function () {
				feedback.html('我要<br>反馈');
				feedback.css({
					'background-image': '',
					'background-color': '#188eee',
					'color': '#fff'
				});
			},
			mouseout: function () {
				feedback.text('');
				feedback.css({
					'background-color': '',
					'background-image': 'url(../../static/mysite/images/icon/feedback.png)'
				});
			}
		});

		feedback.click(function () {
			if (feedback_box.css('display') === 'none') {
				// alert(feedback_box.css('display'));
				feedback.unbind("mouseover mouseout");
				feedback.html('点击<br>关闭')
			} else {
				// alert(feedback_box.css('display'))
				feedback.bind({
					mouseover: function () {
						feedback.html('我要<br>反馈');
						feedback.css({
							'background-image': '',
							'background-color': '#188eee',
							'color': '#fff'
						});
					},
					mouseout: function () {
						feedback.text('');
						feedback.css({
							'background-color': '',
							'background-image': 'url(../../static/mysite/images/icon/feedback.png)'
						});
					}
				});
			};
			feedback_box.toggle("normal")
		});
	};

	feedback_button.click(function () {
		var feedback_content = $('#problem');
		var feedback_contact = $('#contact');
		$.ajax({
			url: '/ajax_feedback/',
			type: 'POST',
			data: {
				feedback_content: feedback_content.val(),
				feedback_contact: feedback_contact.val()
			},
			success: function (msg) {
				if (msg === 'True') {
					alert('您的反馈提交成功，谢谢！');
					feedback_content.val('');
					feedback_contact.val('');
					// feedback_box.hide('normal');
				} else {
					alert('请输入要反馈的内容或者关闭反馈框');
				}
			}
		});
	});
});