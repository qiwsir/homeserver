
//搜索特定名字的style对象
function getstyle(sname) { 
    for (var i=0;i< document.styleSheets.length;i++) { 
        var rules; 
        if (document.styleSheets[i].cssRules) { 
            rules = document.styleSheets[i].cssRules; 
        } 
        else { 
            rules = document.styleSheets[i].rules; 
        } 
        for (var j=0;j< rules.length;j++) { 
            if (rules[j].selectorText == sname) { 
                return rules[j].style; 
            } 
        } 
    } 
}

//用户登录
//判断用户名和密码是否符合规则
//将用户名和密码发送到服务器
//接收服务器返回信息:0-用户名和密码错误;1-系统管理员;2-企业用户
//根据反馈信息，用户进入不同路径
function loginto(){
    var username=document.getElementById("username").value;
    var password=document.getElementById("password").value;

    var reg = /^(\w|[\u4E00-\u9FA5])*$/;    //只允许汉字、字母和数字

    check_username=username.match(reg);
    check_password=password.match(reg);
    if (check_username && check_password){
        alert(username+"."+password);
        //send to service
        //if true from service,then go into the web as the type of username
        //else return false from service,then write 'username and password is false'
    }
    else{
        getstyle(".error").display="inline";
        document.getElementById("error").innerHTML="用户名或密码错误。请确认后登录。" ; 
    }
    
}
