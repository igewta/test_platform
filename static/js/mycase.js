var CaseInit = function (caseId) {

    function getcaseinfo(){
        // 调用接口信息接口
        $.post("/cases/cases_info/", {'caseid':caseId}, function (resp) {
            if(resp.success === "true"){
                result = resp.data;

                document.getElementById("req_name").value = result.name;
                document.getElementById("req_url").value = result.url;
                document.getElementById("req_header").value = result.headers;
                document.getElementById("req_parameter").value = result.params;
                document.getElementById("assert_text").value = result.assertText;

                if (result.reqMethod === "post"){
                    document.getElementById("post").setAttribute("checked", "")
                }

                if (result.reqType === "json"){
                    document.getElementById("json").setAttribute("checked", "")
                }

                ProjectInit('project_name', 'module_name', result.project_name, result.module_name);
            }else{
                window.alert(resp.message);
            }

        });
    }
    // 调用getProjectList函数
    getcaseinfo(); 

};
    