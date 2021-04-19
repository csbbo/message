<template>
  <div class="profile">
    <div class="user-info">
      <div>{{user_info.username}}</div>
    </div>
    <div class="action">
      <router-link class="publish" to="/publish">发布</router-link>
    </div>
  </div>
</template>

<script>
import { GetUser } from "@/common/api"
export default {
  name: 'Profile',
  data() {
    return {
      user_info: []
    };
  },
  created() {
      this.getuser()
  },
  methods: {
    getuser() {
      GetUser().then(resp => {
        console.log(resp)
        this.user_info = resp.data
      })
    }
  }
}
</script>

<style lang="scss" scoped>
  .profile {
      margin: 10px 20px;
      .action {
          margin-top: 20px;
          .publish {
              text-decoration: none;
              border: 1px solid #bdbdbd;
              padding: 2px 5px;
              color: #212121;
              border-radius: 5px;
          }
      }
  }
</style>
