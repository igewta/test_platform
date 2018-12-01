var ProjectInit = function (_cmbProject, _cmbModule, defaultProject, defaultModule) {
    var cmbProject = document.getElementById(_cmbProject);
    var cmbModule = document.getElementById(_cmbModule);
    var dataList = [];

    //window.alert(defaultProject);
    //window.alert(defaultMudle);
    //设置默认选项
    function cmbSelect(cmb, id) {
        for(var i=0; i< cmb.options.length; i++){
            if(cmb.options[i].value == id){
                cmb.selectedIndex = i;
                return;
            }
        }
    }
    //创建下拉选项
    function cmbAddOption(cmb, id, name, obj) {
       //传入的是项目/模块的id 和名称
        var option = document.createElement("option");
        cmb.options.add(option);
        option.text = name;
        option.value = id;
        option.obj = obj;
    }
    
    //改变项目
    function changeProject() {
        cmbModule.options.length = 0;
        //cmbModule.onchange = null;
        if (cmbProject.selectedIndex == -1) {
            return;
        }
        var item = cmbProject.options[cmbProject.selectedIndex].obj;
        for (var i = 0; i < item.moduleList.length; i++) {
            cmbAddOption(cmbModule, item.moduleList[i].mid,item.moduleList[i].m_name, null);
        }

        cmbSelect(cmbModule, defaultModule);
    }

    function getProjectList(){
        // 调用项目服务列表接口
        $.get("/cases/get_project_list/", {}, function (resp) {
            console.log('调用后台接口');
            if(resp.success === "true"){
                dataList = resp.data;
                //遍历项目
                for (var i = 0; i < dataList.length; i++) {

                    cmbAddOption(cmbProject, dataList[i]['pid'],dataList[i]['p_name'], dataList[i]);
                   }

                cmbSelect(cmbProject, defaultProject);
                changeProject();
                cmbProject.onchange = changeProject;
            }

            cmbSelect(cmbProject, defaultProject);
            //$("#result").html(resp);
        });
    }
    // 调用getProjectList函数
    getProjectList(); 
    
};
