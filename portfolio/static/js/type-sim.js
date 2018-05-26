let TypeSimulation = function(el, typeText, lead, end, period) {
    this.typeText = shuffleArray(typeText);
    this.typeText.push(end);

    this.element = el;
    this.loopNum = 0;
    this.period = parseInt(period, 10) || 2000;
    this.lead = lead;
    this.txt = '';
    this.tick();
    this.isDeleting = false;
};

TypeSimulation.prototype.tick = function() {
    let i = this.loopNum;
    let fullTxt = this.lead + this.typeText[i];

    if (this.isDeleting) {
        this.txt = fullTxt.substring(0, this.txt.length - 1);
    } else {
        this.txt = fullTxt.substring(0, this.txt.length + 1);
    }

    this.element.innerHTML = '<span class="wrap">' + this.txt + '</span>';

    let delta = 200 - Math.random() * 100;

    if (this.isDeleting) { delta /= 2; }

    if (!this.isDeleting && this.txt === fullTxt) {
        delta = this.period;
        this.isDeleting = this.loopNum != this.typeText.length - 1;
    } else if (this.isDeleting && this.txt === '') {
        this.isDeleting = false;
        this.loopNum++;
        delta = 500;
    }

    let that = this;
    if (this.loopNum < this.typeText.length) {
        setTimeout(() => {
            that.tick();
        }, delta);
    }
};

let startTyping = function() {
    let ids = ["header-text"];

    for (id of ids) {
        let element = document.getElementById(id);
        let typeText = element.dataset.text;
        let period = element.dataset.interval;
        let lead = element.dataset.lead;
        let end = element.dataset.end;
        if (typeText) {
          new TypeSimulation(element, JSON.parse(typeText), lead, end, period);
        }

        // INJECT CSS
        let css = document.createElement("style");
        css.type = "text/css";
        css.innerHTML = "#" + id + " > .wrap { border-right: 0.08em solid #fff}";
        document.body.appendChild(css);
    }
}

function shuffleArray(array) {
    for (let i = array.length - 1; i > 0; i--) {
        let j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]];
    }
    return array;
}
