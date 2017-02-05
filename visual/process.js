//var csv is the CSV file with headers
function csvJSON(csv) {
  var lines = csv.split("\n");
  var result = [];
  for (var i = 0; i < lines.length; i++) {
    if (lines[i] == "") continue;
      var obj = [];
      var currentline = lines[i].split(",");
      for(var j = 0; j < currentline.length-1; j++) {
          obj.push(parseFloat(currentline[j]));
      }
      result.push(obj);
  }

  return result; //JavaScript object
  //return JSON.stringify(result); //JSON
}

function Data() {
  // Following member variables are initialized within getDbConnection().
  this.probability = null
  this.vocab = null
  this.inv_vocab = null
  this.raw_prob = null
  this.text_data = null
}

Data.prototype.loadText = function(filename) {
  var data_ob = this;
  var rawFile = new XMLHttpRequest();
  rawFile.open("GET", filename, false);
  rawFile.onreadystatechange = function ()
  {
    if(rawFile.readyState === 4) {
      if(rawFile.status === 200 || rawFile.status == 0) {
        var allText = rawFile.responseText;
        allText = allText.replace(/<unk>/g, "^")
        allText = allText.replace(/\n/g, "")
        allText = allText.replace(/\s+/g, ' ').trim()
        data_ob.text_data = allText.substring(0,100);
      }
    }
  }
  rawFile.send(null);
}

Data.prototype.loadVocab = function(filename) {
  var data_ob = this;
  var rawFile = new XMLHttpRequest();
  rawFile.open("GET", filename, false);
  rawFile.onreadystatechange = function ()
  {
    if(rawFile.readyState === 4) {
      if(rawFile.status === 200 || rawFile.status == 0) {
        var allText = rawFile.responseText;
        data_ob.vocab = JSON.parse(allText);
        data_ob.inv_vocab = _.invert(data_ob.vocab);
      }
    }
  }
  rawFile.send(null);
}

Data.prototype.loadProbability = function(filename) {
  var data_ob = this;
  var rawFile = new XMLHttpRequest();
  rawFile.open("GET", filename, false);
  rawFile.onreadystatechange = function ()
  {
    if(rawFile.readyState === 4) {
      if(rawFile.status === 200 || rawFile.status == 0) {
        var allText = rawFile.responseText;
        data_ob.raw_prob = csvJSON(allText);
      }
    }
  }
  rawFile.send(null);
}

Data.prototype.process = function() {
  this.probability = [];
  for (var i = 0; i < 50; i++) {
    var epoch_prob = []
    for (var j = 0; j < 100; j++) {

      epoch_prob.push(this.build_prob(this.raw_prob[i*100 + j]));
    }
    this.probability.push(epoch_prob);
  }
}

Data.prototype.build_prob = function(probability) {
  var distro = {
    "name": "distribution",
    "children": []
  }
  for (var i = 0; i < probability.length; i++) {
    distro["children"].push({
      "name": this.inv_vocab[i],
      "size": probability[i]
    });
  }
  return distro;
}

Data.prototype.common = function(prob_file) {
  this.loadText("text.txt");
  this.loadVocab("vocab_text.json");
  this.loadProbability(prob_file);
  this.process();
}
