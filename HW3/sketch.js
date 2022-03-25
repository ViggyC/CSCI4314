const flock = [];
const object = [];

let alignSlider, cohesionSlider, repuslionSlider, randomSlider;

function setup(){
    createCanvas(800,640);
    
    cohesionSlider = createSlider(0,5,1,0.01);
    repuslionSlider = createSlider(0,5,1,0.01);
    alignSlider = createSlider(0,5,1,0.01);
    randomSlider = createSlider(0,5,1,0.01);

    for (let i=0; i<1; i++){
        object.push(new Obstacle());
    }
    for (let i=0; i<400; i++){
        flock.push(new Boid());
    }

    valueDisplayer = createP()
    valueDisplayer.position(10,height+50)

    valueDisplayer1 = createP()
    valueDisplayer1.position(150,height+50)

    valueDisplayer2 = createP()
    valueDisplayer2.position(300,height+50)

    valueDisplayer3 = createP()
    valueDisplayer3.position(430,height+50)
   

    
}

function draw(){
    background(51);
    for (let boid of flock){
        boid.edges();
        boid.flock(flock);
        boid.update();
        boid.show();
    }
    for (let o of object){
        o.show();
    }
    valueDisplayer.html('Attraction(c1)'+cohesionSlider.value())
    valueDisplayer1.html('Repulsion(c2)'+repuslionSlider.value())
    valueDisplayer2.html('Align(c3)'+alignSlider.value())
    valueDisplayer3.html('Random(c4)'+randomSlider.value())
  
}