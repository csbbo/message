<template>
  <div class="authregister">
    <form class="form">
      <span class="input-comment">用户名:</span><input class="input" type="text" v-model="form.username"> <br>
      <span class="input-comment">密码:</span><input class="input" type="password" v-model="form.password"> <br>
      <span class="input-comment">确认密码:</span><input class="input" type="password" v-model="form.check_pass"> <br>
      <button @click="submitForm" class="submit-btn" type="button">提交</button>
      <button class="reset-btn" type="reset">清空</button>
    </form>
  </div>
</template>

<script>
import { RegisterAPI } from "@/common/api"
export default {
  name: 'AuthRegister',
  data() {
      return {
        form: {
          username: '',
          password: '',
          check_pass: '',
        },
      };
    },
    methods: {
      submitForm() {
        if (this.form.password !== this.form.check_pass) {
          alert('两次密码不同')
          return
        }
        RegisterAPI({'username': this.form.username, 'password': this.form.password}).then(resp => {
          if (resp.err != null) {
            alert(resp.msg);
            console.log(resp)
          } else {
            this.$router.push({path: '/login'})
          }
        })
      },
    }
}
</script>

<style scoped>
  .form {
    margin-top: 30px;
    margin-left: 30px;
  }
  .input-comment {
    width: 70px;
    text-align: right;
    margin-right: 10px;
  }
  .input {
    width: 200px;
    height: 20px;
    margin-top: 5px;
  }
  .submit-btn {
    padding: 1px 8px;
    margin-top: 10px;
    margin-left: 80px;
  }
  .reset-btn {
    padding: 1px 8px;
    margin-top: 10px;
    margin-left: 10px;
  }
</style>
