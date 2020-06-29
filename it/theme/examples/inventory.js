$(document).ready(function () {
  // http://handsontable.com/demo/renderers.html

  var data = [
    [1001, "Test result spreadsheet", "XLS", "File-server", "-", false],
    [1002, "A public database", "CSV", "Data warehouse", "http://opendata.admin.ch/", true],
  ];
  
  var container = document.getElementById('handsontable');
  var hot = new Handsontable(container,
  {
    data: data,
    minSpareRows: 1,
    colHeaders: ["Identifier", "Title", "Format(s)", "Internal Location", "External URL", "Anonymized?"],
    contextMenu: true
  });
  
  Handsontable.Dom.addEvent(document.body, 'click', function (e) {

    var element = e.target || e.srcElement;

    if (element.nodeName == "BUTTON" && element.name == 'dump') {
      var name = element.getAttribute('data-dump');
      var instance = element.getAttribute('data-instance');
      var hot = window[instance];
      console.log('data of ' + name, hot.getData());
    }

  });

});