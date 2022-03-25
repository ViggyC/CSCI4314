class Obstacle{

    constructor(){
        this.position = createVector(800/2 , 640/2);
        this.present = true;
        this.display = true;
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