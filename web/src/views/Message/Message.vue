<template>
  <div class="message">
      <div class="content">
        <h2>{{message.title}}</h2>
        <hr class="content-hr"/>
        <div v-html="message.content"></div>
      </div>

      <div class="comment">
        <div class="option-bar">
            <a class="option-item" @click="switchShow('commentlist')">消息</a>
            <a class="option-item" @click="switchShow('comment')">评论</a>
            <a class="option-item" @click="switchShow('conversation')">对话</a>
        </div>
        <hr class="comment-hr"/>
        <CommentList :mid="this.$route.params.mid" v-if="showItem==='commentlist'" />
        <Comment :mid="this.$route.params.mid" v-if="showItem==='comment'" />
        <Conversation :mid="this.$route.params.mid" v-if="showItem==='conversation'" />
      </div>
  </div>
</template>

<script>
import CommentList from '@/views/Message/CommentList'
import Comment from '@/views/Message/Comment'
import Conversation from '@/views/Message/Conversation'
import { GetMessage, QueryComment, AddComment } from "@/common/api"
export default {
  name: 'Message',
  components: {
    CommentList,
    Comment,
    Conversation,
  },
  data() {
    return {
      showItem: 'commentlist',
      message: {},
      comments: [],
      form: {
          comment: '',
      }
    }
  },
  created() {
    this.get_message_commend()
  },
  methods: {
    get_message_commend() {
      const message_id = this.$route.params.mid
      GetMessage({id: message_id}).then(resp => {
        if (resp.err != null){
          alert(resp.msg)
        } else {
          console.log(resp.data)
          this.message = resp.data.message
          QueryComment({mid: message_id}).then(sub_resp => {
            if (sub_resp.err != null){
              alert(sub_resp.msg)
            } else {
              console.log(sub_resp.data)
              console.log('get message and commend success!')
              this.comments = sub_resp.data.comments
            }
          })
        }
      })
    },
    switchShow(name) {
      this.showItem = name
    },
    submitForm() {
      const message_id = this.$route.params.mid
      AddComment({mid: message_id, content: this.form.comment}).then(resp => {
        if (resp.err != null) {
          alert(resp.msg)
        } else {
          this.switch_show = 'list'
        }
      })
    },
  }
}
</script>

<style scoped>
  .message {
      display: flex;
      flex-direction: row;
      padding: 10px 20px;
  }
  .content-hr {
      margin-bottom: 10px;
  }
  .content {
      width: 30%;
  }
  .comment {
      width: 70%;
      padding-left: 100px;
  }
  .option-item {
      color: #333333;
      text-decoration: none;
      border: 1px solid #333333;
      border-radius: 5px;
      padding: 1px 2px;
      margin-right: 5px;
  }
  .comment-hr {
      margin-top: 8px;
      margin-bottom: 10px;
  }
  .comment-text {
    width: 90%;
    height: 400px;
  }
  .comment-btn {
    padding: 1px 8px;
    margin-top: 10px;
  }
</style>
