class Boid{

    constructor(){
        this.position = createVector(random(width) , random(height));
        this.velocity = p5.Vector.random2D();
        this.velocity.setMag(random(2, 4));
        this.acceleration = createVector();
        this.maxForce = 1;
        this.maxSpeed =4;
        //this.randomVelocity = 0.01
        this.r = 1.2;
        this.obstacle = new Obstacle();
    }

    edges(){
        if(this.position.x>width){
            this.position.x = 0

        }else if(this.position.x <0){
            this.position.x = width;
        }

        if(this.position.y>height){
            this.position.y = 0;

        }else if(this.position.y <0){
            this.position.y = height;
        }
    }

    align(boids){
        let radius =50;

        let avg = createVector();
        let total = 0;

        for(let other of boids){
            let d = dist(
                this.position.x, 
                this.position.y, 
                other.position.x, 
                other.position.y
            );
            if(d<radius && other != this){
                avg.add(other.velocity); //adding up all velocities
                total++;
            }
        }
        if(total>0){
            avg.div(total);
            //steer force
            avg.setMag(this.maxSpeed);
            avg.sub(this.velocity);//vector
            avg.limit(this.maxForce);
            
        }
        return avg;
    }

    cohesion(boids){
        let radius =50;

        let avg = createVector();
        let total = 0;

        for(let other of boids){
            let d = dist(
                this.position.x, 
                this.position.y, 
                other.position.x, 
                other.position.y
            );
            if(d<radius && other != this){
                avg.add(other.position); //adding up all velocities
                total++;
            }
        }
        if(total>0){
            avg.div(total);
            avg.sub(this.position);
            avg.setMag(this.maxSpeed);
            avg.sub(this.velocity);
            avg.limit(this.maxForce);
            
        }
        return avg;
    }

    repulsion(boids){
        let radius =50;
        let rad_obstacle = 80;

        let avg = createVector();
        let total = 0;

        for(let other of boids){
            let d = dist(
                this.position.x, 
                this.position.y, 
                other.position.x, 
                other.position.y
            );
            if(d<radius && other != this){
                let diff = p5.Vector.sub(this.position, other.position);
                diff.div(d);
                avg.add(diff); //adding up all velocities
                total++;
            }
        }
        if(total>0){
            avg.div(total);
            avg.setMag(this.maxSpeed);
            avg.sub(this.velocity);
            avg.limit(this.maxForce);
            
        }

        // handler for obstacle

        if(this.obstacle.present === true){
            let dObstacle = dist(
                this.position.x, 
                this.position.y, 
                this.obstacle.position.x, 
                this.obstacle.position.y
            );

            if(dObstacle<rad_obstacle){
                    let diff = p5.Vector.sub(this.position, this.obstacle.position);
                    diff.div(dObstacle);
                    avg.add(diff); //adding up all velocities
                    total++;
             
                }

       

                
        }

        
        return avg;
    }

    

    flock(boids){
        
        let alignment = this.align(boids); //c3
        let cohesion = this.cohesion(boids); //c1
        let repulsion = this.repulsion(boids); //c2
        //let r = createVector(); //c4

        repulsion.mult(repuslionSlider.value());
        cohesion.mult(cohesionSlider.value());
        alignment.mult(alignSlider.value());
        //r.mult(randomSlider.value());


        this.acceleration.add(repulsion);
        this.acceleration.add(alignment);
        this.acceleration.add(cohesion);
        //this.acceleration.add(r);
    }


    update(){
        this.position.add(this.velocity); //just like we add v1 + V2 + v3...
        this.velocity.add(this.acceleration);
        this.velocity.limit(this.maxSpeed);
        this.acceleration.mult(0);
    }

 

    show(){
        strokeWeight(8);
        stroke(255);
        let theta = this.velocity.heading() + radians(90);
        push();
        translate(this.position.x, this.position.y);
        rotate(theta);
        beginShape();
        vertex(0, -this.r * 2);
        vertex(-this.r, this.r * 2);
        vertex(this.r, this.r * 2);
        endShape(CLOSE);
        pop();
        //point(this.position.x, this.position.y);
    }

}


