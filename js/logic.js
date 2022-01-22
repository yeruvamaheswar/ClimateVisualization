d3.json("https://pkgstore.datahub.io/core/sea-level-rise/epa-sea-level_json/data/ac016d75688136c47a04ac70298e42ec/epa-sea-level_json.json").then(function (response) {
    //console.log(response);
    var sea_level = [];
    var years = [];
    var x_axis = [];
    for (let i = 0; i < response.length; i++) {
        sea_level.push(response[i]["CSIRO Adjusted Sea Level"]);
        years.push(response[i].Year);
        x_axis.push(i + 1);


    };

    var trace1 = {
        x: years,
        y: sea_level,
        mode: 'lines+markers',
        connectgaps: true
    };

    

    var data = [trace1];

    var layout = {
        title: "Sea level rise",
        showlegend: false
    };

    Plotly.newPlot('myDiv', data, layout);
});

d3.json("https://pkgstore.datahub.io/core/glacier-mass-balance/glaciers_json/data/6270342ca6134dadf8f94221be683bc6/glaciers_json.json").then(function (response) {
    console.log(response);
    var mass_ice = [];
    var years = [];
    var x_axis = [];
    for (let i = 0; i < response.length; i++) {
        mass_ice.push(response[i]["Mean cumulative mass balance"]);
        years.push(response[i].Year);
        x_axis.push(i + 1);


    };

    var trace1 = {
        x: years,
        y:  mass_ice,
        mode: 'lines+markers',
        connectgaps: true
    };

    var data = [trace1];

    var layout = {
        title: "Average cumulative mass balance of reference Glaciers worldwide ",
        showlegend: false
    };

    Plotly.newPlot('myDoc', data, layout);
});

// make some waves.
var ocean = document.getElementById("ocean"),
    waveWidth = 10,
    waveCount = Math.floor(window.innerWidth/waveWidth),
    docFrag = document.createDocumentFragment();

for(var i = 0; i < waveCount; i++){
  var wave = document.createElement("div");
  wave.className += " wave";
  docFrag.appendChild(wave);
  wave.style.left = i * waveWidth + "px";
  wave.style.webkitAnimationDelay = (i/100) + "s";
}

ocean.appendChild(docFrag);


