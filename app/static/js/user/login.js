/**
 * Created by luojie on 2018/8/14.
 */
;
var user_login_ops={
    init:function () {
      this.eventBind();
    },
    eventBind:function () {
      $(".login_wrap .do-login").click(function () {
          var login_name = $(".login_wrap input[name=login_name]").val();
          var login_pwd = $(".login_wrap input[name=login_pwd]").val();
          if(login_name==undefined||login_name.length<1){
              common_ops.alert("请输入正确的登陆用户名")
              return;
          }
          if(login_pwd==undefined||login_pwd.length<1){
              common_ops.alert("请输入正确的登陆用户名")
              return;
          }

          $.ajax({
              url:common_ops.buildUrl("/user/login"),
              type:"POST",
              data:{
                  'login_name':login_name,
                  'login_pwd':login_pwd
              },
              success:function (res) {

              }
          })
      })
    }
}
$(document).ready(function () {
   user_login_ops.init();
});