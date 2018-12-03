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
                //获取不到用例列表，长度为空。。。。。。。。。。   
                let cases_check = document.getElementsByClassName('case_check')

                console.log(cases_check.length)//为空值，下列for语句无法执行
                for (let i=0;i<cases_check.length;i++){s
                    console.log('cases_check:',cases_check)
                    if ($.inArray(cases_check[i].value, task_cases) >= 0 ){
                        console.log('li:',cases_check[i].value)
                        cases_check[i].checked = true;
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
    console.log('执行了gettaskinfo')

};

