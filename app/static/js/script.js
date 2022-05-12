var icon = document.getElementById("icon1"),
  count = 3;
icon.onclick = function() {
  count += 1;
 document.getElementById("span1").innerHTML = `${count}`
};


var jcon = document.getElementById("icon2"),
  count = 2;
jcon.onclick = function() {
  count += 1;
 document.getElementById("span2").innerHTML = `${count}`
};