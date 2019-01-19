//原生js
window.onload = function () {
	var ni_rank_name = document.getElementById('ni-rank-name').getElementsByTagName('a');
	var ni_rank_day = document.getElementById('ni-rank-day');
	var ni_rank_week = document.getElementById('ni-rank-week');
	var all_news_tag = document.getElementById('all-news-tag');

	ni_rank_name[0].onmouseover = function () {
		ni_rank_day.style.display = 'block';
		ni_rank_week.style.display = 'none';
		all_news_tag.style.display = "none"
	}

	ni_rank_name[1].onmouseover = function () {
		ni_rank_day.style.display = 'none';
		ni_rank_week.style.display = 'block';
		all_news_tag.style.display = 'none';
	}

	ni_rank_name[2].onmouseover = function () {
		ni_rank_day.style.display = 'none';
		ni_rank_week.style.display = 'none';
		all_news_tag.style.display = 'block';
	}
}