<template>
  <div class="recommend">
    <ul class="list-message">
      <router-link
        :to="{path: '/message/'+message.id}"
        tag="li"
        v-for="(message, i) in messages"
        :key="i"
        class="message">
        <div class="card">
            <div class="title">{{message.title}}</div>
        </div>
      </router-link>
    </ul>
  </div>
</template>

<script>
import { QueryMessage } from "@/common/api"
export default {
  name: 'Recommend',
  data() {
    return {
      messages: []
    };
  },
  created() {
    this.get_message()
  },
  methods: {
    get_message() {
      QueryMessage().then(resp => {
        if (resp.err === null) {
          console.log(resp)
          this.messages = resp.data.messages
        }
      })
    }
  }
}
</script>

<style lang="scss" scoped>
.list-message {
    margin: 10px;
    list-style: none;
    .message {
        color: #333333;
        text-decoration: none;
        border: 1px solid #e0e0e0;
        width: 30%;
        padding: 5px;
        margin-bottom: 4px;
        border-radius: 5px;
        .title {
            font-size: 17px;
        }
    }
}
</style>