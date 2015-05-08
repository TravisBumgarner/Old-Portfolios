/*Future Improvements:
1. gameSpeed and paddleSize are user prompted with difficulty levels. 
                    2. gameOver screen
3. Create menu where user can select modes
3.1 Easy, Medium, Hard, Insane (Controls inverted or something)
4. Quick Game Intro. 
5. Select Input method: Arrow keys or mouse
6. Random goodies appear that you can click on (Extra balls, more points, slow the ball down for a certain number of movements, etc);
7. Photoshop objects
8. Make levels?
                    9. Different angles for the ball.
*/

//User Generated Settings
var gameSpeed = 1;
var paddleSize = 30;

//Global Variables
background(133, 133, 133);
var counter = 0;
var x = random(100,300);
var y = random(100,300);
var xDirectionMod=1;
var yDirectionMod=1;

//Paddle Movement
var paddleMovement=function(){
    strokeWeight(5);
    var paddleTop =    line(mouseX+paddleSize,10,mouseX-paddleSize,10);
    var paddleLeft =   line(10,mouseY+paddleSize,10,mouseY-paddleSize);
    var paddleRight =  line(390,mouseY+paddleSize,390,mouseY-paddleSize);
    var paddleBot =    line(mouseX+paddleSize,390,mouseX-paddleSize,390);
};

//Function to change true to false and vice versa. Additionally modifies the angle of the ball when it hits the wall. 
if(round(random(0,1))===0){var randomDirectionX=true;}else{randomDirectionX=false;}
if(round(random(0,1))===0){var randomDirectionY=true;}else{randomDirectionY=false;}
var directionX = randomDirectionX; 
var directionY = randomDirectionY;
var directionChange = function(toChange){
    xDirectionMod = random(0.5,1.5);
    yDirectionMod = random(0.5,1.5);
    if(toChange){return false;}
    else if(!toChange){return true;}
};

//You Lose Display
var youLose = function(){
    background(0,0,0);
    textSize(50);
    fill(255, 0, 0);
    textAlign(CENTER,CENTER);
    text("You lose.\n Score: " + counter, 200,200);
};

//Movement of ball when it hits the wall.
var ballsToTheWall = function(){    
    if(x >= 380 || x <= 20 || y >= 380 || y <= 20){

         gameSpeed+=0.05; //Increases game speed by 0.05 per wall hit.
         if(x >= 380 || x <= 20){
            if(y>=mouseY-paddleSize&&y<=mouseY+paddleSize){
                directionX = directionChange(directionX);
                counter++; ///Adds one to the game counter per wall hit.
                return;
            }
            else{youLose();}
         }
         else if(y >= 380 || y <= 20){
            if(x>=mouseX-paddleSize&x<=mouseX+paddleSize){
                directionY = directionChange(directionY);
                counter++; ///Adds one to the game counter per wall hit.
                return;
            }
            else{youLose();}
         }
    } 
};

//Movement of ball in central area.
var moveBall = function(){
        
    if(!directionX){x=x+gameSpeed*xDirectionMod;}
    else if(directionX){x=x-gameSpeed*xDirectionMod;}
    
    if(!directionY){y=y+gameSpeed*yDirectionMod;}
    else if(directionY){y=y-gameSpeed*yDirectionMod;}
};

var draw = function() {
    text(random(false,true),50,50);
    strokeWeight(10);
    fill(133, 133, 133);
    rect(0,0,400,400);
    paddleMovement();
    ballsToTheWall(); //Checks if ball has arrived to the wall.
    moveBall(); //Incrementally Moves ball in X and Y directions.
    stroke(1);
    fill(0, 0, 0);
    ellipse(x,y,20,20);
    textAlign(CENTER,CENTER);
    text("Score: " + counter,200,350);
};