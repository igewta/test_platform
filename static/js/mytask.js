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
                task_cases = result.cases.split(',')
                cases_check = document.getElementsByName('case_check')
               
                console.log(cases_check.length)
                for (let i=0;i<cases_check.length;i++){
                    console.log('cases_check:',cases_check)
                    console.log('88888888888')
                    if ($.inArray(cases_check[i].value, task_cases) >= 0 ){
                        console.log('li:',cases_li[i].value)
                        cases_li[i].checked = true;
                    }
                }                
            }else{
                window.alert(resp.message);
            };

        });
    }
    // 调用gettaskinfo函数
    CaseListInit();
    gettaskinfo(); 

};

