class Obstacle{

    constructor(xpos, ypos){
        this.xpos = 800/2
        this.ypos = 640/2
        this.position = createVector(this.xpos ,this.ypos);
        this.present = true;
        this.display = true;
    }

    move(){
        var step = p5.Vector.random2D(); //unit vector
        var r = random(100);
        if(r<1){
            step.mult(random(5,20));
        }else{
            step.setMag(2);
        }
        this.position.add(step)
    }

    show(){
        strokeWeight(35);
        stroke(255);
        stroke('red');
        if (this.display){
            point(this.position.x, this.position.y);
   
        }      
    }
}