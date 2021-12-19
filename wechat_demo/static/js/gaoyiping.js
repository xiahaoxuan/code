/*
 *  Author: gaoyiping(iam@gaoyiping.com)
 */
// if(navigator.userAgent.match(/(iPhone|iPod|iPad|Windows Phone|Android|ios)/i)){window.location.href="/mobile/"}

function minute2timepicker(minute) {
	if (minute >= 0 && minute <= 1440) {
		var h, m;
		var h = Math.floor(minute / 60);
		if (h < 10) h = "0" + h;
		var m = minute % 60;
		if (m < 10) m = "0" + m;
		return h+":"+m;
	}
	return "00:00";
}