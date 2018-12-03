//显示用例信息
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
                document.getElementById("assert_text").value = result.result;

                if (result.reqMethod === "post"){
                    document.getElementById("post").setAttribute("checked", "")
                }

                if (result.reqType === "json"){
                    document.getElementById("json").setAttribute("checked", "")
                }

                ProjectInit('project_name', 'module_name', result.project_id, result.module_id);
            }else{
                window.alert(resp.message);
            }

        });
    }
    // 调用getProjectList函数
    getcaseinfo(); 

};


//获取所有用例列表
var CaseListInit = function () {

    function getcaseslist(){
        // 调用用例列表接口
        $.get("/cases/caseslist/", {}, function (resp) {
            if(resp.success === "true"){
                let cases = resp.data.caseslist;
                let ul =document.getElementById("caseList");  

                for(let i=0;i<cases.length; i++){
                    let checkBox=document.createElement("input");  
                    checkBox.setAttribute("type","checkbox");  
                    checkBox.setAttribute("value",cases[i]['cid']); 
                    checkBox.setAttribute("name",'case_check');   
                      
                    let li=document.createElement("li");  
                    li.appendChild(checkBox);  
                    li.appendChild(document.createTextNode(cases[i]['c_name']));
                    ul.appendChild(li);
                }

            }else{
                window.alert(resp.message);
            }

        });
    }
    // 调用getcaseslist函数
    getcaseslist(); 

};
    