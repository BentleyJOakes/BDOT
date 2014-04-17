// Copyright 2011 The MathWorks, Inc.


function local_onload() {
    var docObj = window.document;
    var alink =  docObj.getElementById("linkToText_plain");
    if (alink) {
        alink.href = "matlab:rtwprivate('editUrlTextFile','" + alink.href + "')";
    }
    alink = docObj.getElementById("linkToCS");
    if (alink) {
        alink.href = "matlab:rtwprivate('rtw_view_code_configset_from_report','" + alink.href + "');";
    }
}
