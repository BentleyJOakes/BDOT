//Copyright 2010-2011 The MathWorks, Inc.

function rtwannotate_do(xmlDoc) {
    var rtwCode = document.getElementById("RTWcode");
    // style
    var style = xmlDoc.getElementsByTagName("style");
    if (style) {
      for (i=0;i<style.length;++i) {
        var cssCode = style[i].firstChild.nodeValue;
        var styleElement = document.createElement("style");
        styleElement.type = "text/css";
        if (styleElement.styleSheet) {
          styleElement.styleSheet.cssText = cssCode;
        } else {
          styleElement.appendChild(document.createTextNode(cssCode));
        }
        document.getElementsByTagName("head")[0].appendChild(styleElement);
      }
    }
    // summary
    var summary = xmlDoc.getElementsByTagName("summary")[0];
    if (summary) {
      var summaryAnnotation = summary.getElementsByTagName("annotation")[0];
      if (summaryAnnotation) {
        var span = document.createElement("span");
        span.innerHTML = summaryAnnotation.firstChild.nodeValue;
        rtwCode.parentNode.insertBefore(span,rtwCode);
      }
    }
    // line
    var data = xmlDoc.getElementsByTagName("line");
    var annotationsTable = new Array();
    var defaultAnnotation;
    for (i=0;i<data.length;++i) {
      var id = data[i].getAttribute("id");
      if (id == "default") {
        defaultAnnotation = data[i].getElementsByTagName("annotation")[0];
      } else {
        annotationsTable[parseInt(id)] = data[i].getElementsByTagName("annotation");
      }
    }
    var lines = rtwCode.childNodes;
    for (i=0;i<lines.length;++i) {
      var annotations = annotationsTable[i+1];
      if (annotations && annotations.length > 0) {  
        // first annotation
        var span = document.createElement("span");
        span.innerHTML = annotations[0].firstChild.nodeValue;
        lines[i].insertBefore(span,lines[i].firstChild);
        // more annotations
        for (j=1;j<annotations.length;++j) {
          span = document.createElement("span");
          span.innerHTML = annotations[j].firstChild.nodeValue + "<br />";
          // how to handle nl?
          lines[i].appendChild(span);
        }
      } else if (defaultAnnotation) {
        // default annotation
        var newElement = document.createElement("span");
        newElement.innerHTML = defaultAnnotation.firstChild.nodeValue;
        lines[i].insertBefore(newElement,lines[i].firstChild);
      }
    }
}

function rtwannotate_other(filename) {
    var span = document.createElement("span");
    span.innerHTML = "<SPAN>  Warning: Code coverage data is not loaded due to a web browser compatibility issue.</SPAN>";
    var rtwCode = document.getElementById("RTWcode");
    rtwCode.parentNode.insertBefore(span,rtwCode);
}

function rtwannotate_IE(filename) {
    var xmlDoc;
    if (navigator.appName == "Microsoft Internet Explorer") {
        // Internet Explorer 5/6 
        try {
            xmlDoc = new ActiveXObject("Microsoft.XMLDOM");
            xmlDoc.async = true;
            xmlDoc.onreadystatechange = function() {
                if (xmlDoc.readyState == 4) rtwannotate_do(xmlDoc);
            }
            xmlDoc.load(filename);
        } catch(e) {
            rtwannotate_other(filename)
        }
    } else {
        rtwannotate_other(filename);
    }
}

function rtwannotate(filename) {
    if (window.XMLHttpRequest) {
        try {
            var xhttp=new XMLHttpRequest();
            xhttp.onreadystatechange = function() {
                if (this.readyState == 4) rtwannotate_do(this.responseXML);
            }
            xhttp.open("GET",filename);
            xhttp.send("");
        } catch(e) {
            if (navigator.appName === "Netscape" &&  e.code === 1012) {
                // file not found: ignore
            } else {
                rtwannotate_IE(filename);
            }
        }
    } else {
        rtwannotate_IE(filename);
    }
}

