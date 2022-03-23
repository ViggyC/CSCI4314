class Obstacle{

    constructor(){
        this.position = createVector(640/2 , 640/2);
        this.present = false;

    }

    show(){
        strokeWeight(50);
        stroke(255);
        stroke('red');
        if (this.present)
            point(this.position.x, this.position.y);
    }
}