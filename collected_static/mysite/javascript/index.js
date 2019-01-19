//原生js
window.onload = function () {
	var ppt = document.getElementById('ppt');
	var ppt_num = document.getElementById('ppt-num').getElementsByTagName('li');
	var ppt_img = document.getElementById('ppt-img');
	var now = 0;
	for (var i = 0; i < ppt_num.length; i++) {
		ppt_num[i].index = i;
		ppt_num[i].onclick = function () {
			now = this.index;
			for (var i = 0; i < ppt_num.length; i++) {
				ppt_num[i].className = '';
			}
			ppt_num[now].className = 'active';
			if (now == 0) { startMove(ppt_img, { left: -320 * now }, 1.2); }
			else { startMove(ppt_img, { left: -320 * now }, 4); }
		}
	}

	function next() {
		now++;
		if (now == ppt_num.length) {
			now = 0;
		}
		for (var i = 0; i < ppt_num.length; i++) {
			ppt_num[i].className = '';
		}
		ppt_num[now].className = 'active';
		if (now == 0) { startMove(ppt_img, { left: -320 * now }, 1.2); }
		else { startMove(ppt_img, { left: -320 * now }, 4); }
	}

	var timer = setInterval(next, 5000);
	ppt.onmouseover = function () {
		clearInterval(timer);
	}
	ppt.onmouseout = function () {
		timer = setInterval(next, 5000);
	}
}

function getStyle(obj, name) {
	if (obj.currentStyle) {
		return obj.currentStyle[name];
	}
	else {
		return getComputedStyle(obj, false)[name];
	}
}

function startMove(obj, json, speed_ctrl, fnEnd) {
	clearInterval(obj.timer);
	obj.timer = setInterval(function () {
		var bStop = true;		//假设：所有值都已经到了

		for (var attr in json) {
			var cur = 0;

			if (attr == 'opacity') {
				cur = Math.round(parseFloat(getStyle(obj, attr)) * 100);
			}
			else {
				cur = parseInt(getStyle(obj, attr));
			}

			var speed = (json[attr] - cur) / speed_ctrl;
			speed = speed > 0 ? Math.ceil(speed) : Math.floor(speed);

			if (cur != json[attr])
				bStop = false;

			if (attr == 'opacity') {
				obj.style.filter = 'alpha(opacity:' + (cur + speed) + ')';
				obj.style.opacity = (cur + speed) / 100;
			}
			else {
				obj.style[attr] = cur + speed + 'px';
			}
		}

		if (bStop) {
			clearInterval(obj.timer);

			if (fnEnd) fnEnd();
		}
	}, 30);
}