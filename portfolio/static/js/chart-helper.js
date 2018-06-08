const ChartHelper = (function() {
    color1 = "#233347";
    color2 = "#618DC7";
    color3 = "#A4B7D0";
    color4 = "#383F47";
    color5 = "#486994";

    let allColors = [color1, color2, color3, color4, color5];

    let chartVisible = new Map();
    let chartData = new Map();

    let randomColors = function(numColors) {
        let colors = [];
        for (let i = 0; i < numColors; i++) {
            colors.push(allColors[Math.floor(Math.random() * allColors.length)])
        }
        console.log(colors);
        return colors;
    }

    let registerChart = function(chartId, data) {
        if (!chartVisible.has(chartId)) {
            chartVisible.set(chartId, false);
            chartData.set(chartId, data);
        } else {
            return 'Error: chart id is already registered.'
        }
    }

    let chartAnimate = function(pageTop, pageBottom) {
        for (chartId of chartVisible.keys()) {
            const chartCanvas = $('#' + chartId);
            if (!chartVisible.get(chartId) && chartCanvas.position().top < pageBottom) {
                chartVisible.set(chartId, true)
                new Chart(document.getElementById(chartId), chartData.get(chartId));
            }
        }
    }

    return {
        randomColors: randomColors,
        registerChart: registerChart,
        chartAnimate: chartAnimate,
    }
})();
