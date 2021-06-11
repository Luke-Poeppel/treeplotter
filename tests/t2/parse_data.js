console.log("Parsing JSON data & Creating Tree...");

require("./Treant.min.js"); 
var tree_data = require("./tree.json");
var chart_config_data_raw = require("./chart_config.json"); 

var tree = JSON.parse(tree_data);
var chart_config_data = JSON.parse(chart_config_data_raw); 

// var nodeStructureObjDict = tree["nodeStructure"];
// var mmm = [chart_config_data, nodeStructureObjDict];
// var chart_config = {
//   chart: chart_config_data
// }

var chart_config = {
  chart: chart_config_data,
  nodeStructure: tree["nodeStructure"]
}

new Treant(chart_config);