<template>
  <div class="authlogin">
    <form class="form">
      <span class="input-comment">用户名:</span><input class="input" type="text" v-model="form.username"> <br>
      <span @keyup.enter="submitForm" class="input-comment">密码:</span><input class="input" type="password" v-model="form.password"> <br>
      <button @click="submitForm" class="submit-btn" type="button">提交</button>
      <button class="reset-btn" type="reset">清空</button>
    </form>
  </div>
</template>

<script>
import { LoginAPI, GetUser } from "@/common/api"
export default {
  name: 'AuthLogin',
  data() {
    return {
      form: {
        username: '',
        password: '',
      },
    };
  },
  methods: {
    submitForm() {
      LoginAPI({username: this.form.username, password: this.form.password}).then(resp => {
        if (resp.err === null) {
          GetUser().then(res => {
            if(res.err === null) {
                this.$store.commit('SET_USERNAME', res.data)
                this.$router.push({path: '/'})
            }
          })
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
