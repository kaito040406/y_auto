onload = function () {
  var input_data = [];
  this.document.getElementById("file").onclick = function () {
    var fileInput = document.getElementById("file");
    var fileReader = new FileReader();
    fileInput.onchange = function () {
      let file = fileInput.files[0];
      fileReader.readAsText(file);
    };
    fileReader.onload = function () {
      i = 0;
      fileReader.result.split("\n").forEach(function (line) {
        var line_data = line.split(",");
        input_data[i] = line_data;
        i = i + 1;
      });
    };
  };

  document.getElementById("start_button").onclick = function () {
    var result = confirm("実行しますか？");
    if (result) {
      if (input_data.length != 0) {
        pysub();
      } else {
        alert("CSVデータを読み込んでください");
      }
    } else {
      alert("キャンセルされました");
    }
  };

  async function pysub() {
    var check = await eel.start(input_data)();
  }
};
