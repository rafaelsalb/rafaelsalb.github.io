let canvas;
let bars = [];
let idx = 1;
let bar_width = 0;
let bar_height = 0;
let run = false;
let end = false;
let iterations = 0;
let loops = 0;


function start()
{
    canvas = createCanvas(Utils.elementWidth(parent_div), 600);
    canvas.parent("canvas");
    let amt_bars = parseInt(document.getElementById("length").value);
    bar_width = width / amt_bars;
    bar_height = height / amt_bars;
    bars = [];
    iterations = 0;
    loops = 0;
    idx = 0;

    for (let i = 1; i <= amt_bars; ++i) {
        bars.push(lerp(1, amt_bars, i / amt_bars));
    }

    let _case = document.getElementById("case").value;

    switch (_case) {
        case "random":
            bars = fisher_yates(bars);
            break;
        case "worst":
            bars = bars.reverse();
            break;
        case "best":
            break;
    }

    run = true;
    end = false;
    loop();
    stop_timer();
    start_timer();
    document.getElementById("average-case").innerText += amt_bars * amt_bars + " iterations.";
}

function is_sorted()
{
    return bars.reduce((n, item) => n !== false && item >= n && item)
}

function fisher_yates(array)
{
    for (let i = array.length - 1; i > 0; --i) {
        let j = int(random(0, i))
        let temp = array[i];
        array[i] = array[j];
        array[j] = temp;
    }

    return array;
}

function setup()
{
    parent_div = document.getElementById("canvas");
    frameRate(600);
    noStroke();
    console.log(Utils.elementWidth(parent_div));
    canvas = createCanvas(Utils.elementWidth(parent_div), 600);
    canvas.parent("canvas");
    noLoop();
}

function draw()
{
    background(0);
    fill(255);

    if (run) {
        document.getElementById("iterations").innerText = ++iterations;
        
        for(let i = 0; i < bars.length; ++i) {
            rect(i * bar_width, height - bars[i] * bar_height, bar_width, bars[i] * bar_height);
        }

        if (bars[idx-1] > bars[idx]) {
            let temp = bars[idx];
            bars[idx] = bars[idx-1];
            bars[idx-1] = temp;
        }

        if (idx == bars.length - 1 - loops) {
            idx = 0;
            loops++;
        }
        ++idx;
        if (end) {
            noLoop();
            stop_timer();
        }
        if (is_sorted()) {
            end = true;
        }
    }
}