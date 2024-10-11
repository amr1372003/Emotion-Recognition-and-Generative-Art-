let particles = [];
let num = 200;
let noise_scale = 0.01 / 2;

let mood = "default"; // Default mood
let previousMood = mood;

function setup() {
    createCanvas(windowWidth, windowHeight);
    num = random(200, 500);
    
    for (let x = 0; x < num; x++) {
        particles.push(createVector(random(width), random(height)));
    }

    // Fetch mood periodically
    setInterval(fetchMood, 5000);
}

function draw() {
    background(0, 10);
    
    for (let i = 0; i < num; i++) {
        let p = particles[i];
        
        setMoodColor(p, mood);
        
        point(p.x, p.y);
        let n = noise(p.x * noise_scale, p.y * noise_scale, frameCount * 2 * noise_scale);
        let a = TAU * n;
        p.x += cos(a);
        p.y += sin(a);

        // Wrap particles around canvas edges
        if (p.x < 0) p.x = width;
        if (p.x > width) p.x = 0;
        if (p.y < 0) p.y = height;
        if (p.y > height) p.y = 0;
    }
}

function setMoodColor(p, mood) {
    let r, g, b, alpha;
    switch (mood) {
        case "happy":
            r = 255; // Full red
            g = map(p.x, 0, width, 200, 255); // Vary green
            b = 0; // No blue
            break;
        case "sad":
            r = 0; // No red
            g = 0; // No green
            b = map(p.x, 0, width, 200, 255); // Vary blue
            break;
        case "angry":
            r = map(p.x, 0, width, 200, 255); // Vary red
            g = 0; // No green
            b = 0; // No blue
            break;
        default:
            r = map(p.x, 0, width, 100, 200); // Vary gray
            g = map(p.x, 0, width, 100, 200); // Vary gray
            b = map(p.x, 0, width, 100, 200); // Vary gray
            break;
    }
    
    alpha = map(dist(width / 2, height / 2, p.x, p.y), 0, 350, 400, 0);
    
    stroke(r, g, b);
    fill(r, g, b, alpha);
}

function fetchMood() {
    fetch('http://localhost:5000/get_mood')
        .then(response => response.json())
        .then(data => {
            mood = data.mood;
        })
        .catch(err => console.error('Error fetching mood:', err));
}
