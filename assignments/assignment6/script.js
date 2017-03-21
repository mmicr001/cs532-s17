var w=960,h=500;
var svg=d3.select("#chart")
.append("svg")
.attr("width",w).attr("height",h);
svg
.append("text")
.text("hello world!").attr("x",200).attr("y",200);