<template>
  <div class="main">
    <div class="nav-menu">
      <router-link class="nav-link" to="/">推荐</router-link>
      <span 
        @mouseover="hoverUser = true" 
        @mouseleave="hoverUser = false" 
        v-if="this.$store.state.user.username" 
        class="nav-link"
      >
          {{this.$store.state.user.username}}
          <ul v-if="hoverUser" class="user">
            <router-link tag="li" to="/profile">个人中心</router-link>
            <li @click="logout">注销</li>
          </ul>
      </span>
      <router-link v-if="!this.$store.state.user.username" class="nav-link" to="/login">登录</router-link>
      <router-link v-if="!this.$store.state.user.username" class="nav-link" to="/register">注册</router-link>
    </div>
    <router-view></router-view>
  </div>
</template>

<script>
import { LogoutAPI, GetUser } from "@/common/api"
export default {
  name: 'Main',
  data() {
    return {
      hoverUser: false
    };
  },
  created() {
    this.getUser()
  },
  methods: {
    getUser() {
        GetUser().then(resp => {
            if(resp.err === null) {
              this.$store.commit('SET_USERNAME', resp.data)
            }
        })
    },
    logout() {
      this.hoverUser = false
      LogoutAPI().then(resp => {
        if(resp.err === null) {
            this.$store.commit('SET_USERNAME', {})
            this.$router.push({path: '/login'})
        }
      })
    },
  }
}
</script>

<style lang="scss" scoped>
  .nav-menu {
    border: 1px solid black;
    padding: 10px;
    .nav-link {
      text-decoration: none;
      margin-right: 10px;
      color: #333333;
      .user {
        list-style: none;
        position: fixed;
        border: 1px solid #e0e0e0;
        background-color: #fafafa;
        padding: 1px 4px;
        width: 65px;
        text-align: left;
        border-radius: 5px;
        font-size: 14px;
      }
    }
  }
</style>
