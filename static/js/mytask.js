//显示用例信息
var TaskInit = function (taskId) {

   function gettaskinfo(){
        // 调用task_info接口
        
        $.get("/cases/task_info/", {'tid':taskId}, function (resp) {
            if(resp.success === "true"){
                result = resp.data;

                document.getElementById("task_name").value = result.name;
                document.getElementById("task_describe").value = result.describe;
                document.getElementById("task_status").value = result.status;
                let task_cases = result.cases.split(',')
                
        }
    });

        $.get("/cases/caseslist/", {}, function (resp) {
            console.log('222')
            if(resp.success === "true"){
                let cases = resp.data.caseslist;
                let ul =document.getElementById("caseList");  

                for(let i=0;i<cases.length; i++){
                    let checkBox=document.createElement("input");  
                    checkBox.setAttribute("type","checkbox");  
                    checkBox.setAttribute("value",cases[i]['cid']);
                    checkBox.setAttribute("class",'case_check'); 
                    checkBox.setAttribute("name",'case_check');   
                    if(cases[i]['cid'] in task_cases){
                        checkBox.setAttribute("checked",'true'); 
                    }
              
                    let li=document.createElement("li");  
                    li.appendChild(checkBox);  
                    li.appendChild(document.createTextNode(cases[i]['c_name']));
                    ul.appendChild(li);
            }

        }else{
            window.alert(resp.message);
            }
    });
    // 调用gettaskinfo函数
    gettaskinfo(); 
    console.log('执行了gettaskinfo')

};

