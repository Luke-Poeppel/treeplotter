console.log("Parsing JSON data & Creating Tree...");

require("./Treant.min.js"); 
var tree_data = require("./tree.json");
var chart_config_data_raw = require("./chart_config.json"); 

var tree = JSON.parse(tree_data);
var chart_config_data = JSON.parse(chart_config_data_raw); 

nodeStructureObjDict = tree["nodeStructure"];
var chart_config = [chart_config_data, nodeStructureObjDict];

new Treant(chart_config);