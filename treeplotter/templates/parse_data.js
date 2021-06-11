console.log("Parsing JSON data & Creating Tree...");

require("./Treant.min.js"); 
var tree_data = require("./tree.json");
// var chart_config_data_raw = require("./chart_config.json"); 

var tree = JSON.parse(tree_data);

// var chart_config_data = JSON.parse(chart_config_data_raw); 
// var chart_config = {
//   chart_config_data,
//   nodeStructure: tree["nodeStructure"]
// }
var chart_config = {
  chart: {
      container: "#treeplotter",
      
      connectors: {
          type: 'curve'
      },
      node: {
          HTMLclass: "treeNode"
      }
  },
  nodeStructure: tree["nodeStructure"]
}

new Treant(chart_config);