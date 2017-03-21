var w=960,h=500,flag=0;
var svg=d3.select("#chart").append("svg").attr("width",w).attr("height",h);
var myRect=svg
.append( "rect").attr({x:100,y:100,width:100,height:100})
.style("fill","steelblue");
myRect.on("click",function() {
flag=1-flag;
myRect.style("fill", flag?"darkorange":"steelblue");
})