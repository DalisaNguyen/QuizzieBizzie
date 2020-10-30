// Copyright (c) 2020 by Raymond G McCord (https://codepen.io/slow_izzm/pen/GzQeoL)

// Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
// documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, 
// copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
// and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

// The above copyright notice and this permission notice shall be included in all copies or 
// substantial portions of the Software.

// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE 
// WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT 
// HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
// ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


let confettiColor = [],
    confetti = [];

function setup() {
    createCanvas(windowWidth * 0.98, windowHeight * 0.90);
    confettiColor = [color('#00aeef'), color('#ec008c'), color('#72c8b6')];
    for (let i = 0; i < 100; i++) {
        confetti[i] = new Confetti(random(0, width), random(-height, 0), random(-1, 1));
    }
}

function draw() {
    clear();
    background(220, 1);

    for (let i = 0; i < confetti.length / 2; i++) {
        confetti[i].confettiDisplay();

        if (confetti[i].y > height) {
            confetti[i] = new Confetti(random(0, width), random(-height, 0), random(-1, 1));
        }
    }

    for (let i = int(confetti.length / 2); i < confetti.length; i++) {
        confetti[i].confettiDisplay();

        if (confetti[i].y > height) {
            confetti[i] = new Confetti(random(0, width), random(-height, 0), random(-1, 1));
        }
    }
}

function windowResized() {
    resizeCanvas(windowWidth * 0.98, windowHeight * 0.90);
}

class Confetti {
    constructor(_x, _y, _s) {
        this.x = _x;
        this.y = _y;
        this.speed = _s;
        this.time = random(0, 100);
        this.color = random(confettiColor);
        this.amp = random(2, 30);
        this.phase = random(0.5, 2);
        this.size = random(width / 25, height / 50);
    }

    confettiDisplay() {
        fill(this.color);
        //blendMode(SCREEN);
        noStroke();
        push();
        translate(this.x, this.y);
        translate(this.amp * sin(this.time * this.phase), this.speed * cos(2 * this.time * this.phase));
        rotate(this.time);
        rectMode(CENTER);
        scale(cos(this.time / 4), sin(this.time / 4));
        rect(0, 0, this.size, this.size / 2);
        pop();

        this.time = this.time + 0.1;

        this.speed += 1 / 200;

        this.y += this.speed;
    }
}