var canvas;

function setup()
{
    canvas = createCanvas(400, 400);
    canvas.position(0, 0);
    canvas.style('z-index', '-1');
}

function draw()
{
    background(0);
    circle(width/2, height/2, 20);
}