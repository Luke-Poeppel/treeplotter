require("./Treant.min.js"); 
var tree_data = require("./tree.json");

console.log("Parsing JSON data & Creating Tree...")

var tree = JSON.parse(tree_data);

var chart_config = {
    chart: {
        container: "#mytree",
        
        connectors: {
            type: "curve"
        },
        node: {
            HTMLclass: "nodeExample1"
        }
    },
    nodeStructure: tree["nodeStructure"]
}

new Treant(chart_config);