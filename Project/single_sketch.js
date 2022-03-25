//var x;
//var y;
var pos;
var prev;

function setup() {
  createCanvas(400, 400);
  //x = 200;
  //y = 200;
  background(51);
  pos = createVector(200,200);
  prev = pos.copy();
  console.log(pos);
}

function draw() {
  
  strokeWeight(2);
  stroke(255);
  //point(pos.x, pos.y);
  line(pos.x, pos.y, prev.x, prev.y);
  prev.set(pos);
  var step = p5.Vector.random2D(); //unit vector


  var r = random(100);
  if(r<1){
    step.mult(random(25,100));
  }else{
    step.setMag(2);
  }


  pos.add(step);

}
