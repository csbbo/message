<template>
  <div class="conversation">
    <div id="message-box" class="message-box">
      <div class="messages" v-for="(comment, i) in comments" :key="i">
        <span class="message" v-html="comment.content"></span>
      </div>
    </div>
    <textarea class="send-box" v-model="form.content"></textarea>
    <button @click="addComment" class="send-btn">发送</button>
  </div>
</template>

<script>
import { AddComment, QueryComment } from "@/common/api"
import io from 'socket.io-client'
export default {
    name: 'Conversation',
    data() {
        return {
            form: {
              content: '',
            },
            comments: [],
            socket : io('localhost:7070')
        }
    },
    props: ['mid'],
    methods: {
        addComment() {
            AddComment({mid: this.mid, content: this.form.content}).then(resp => {
                if (resp.err === null) {
                    this.form.content = ''
                }
            })
        },
        getComments() {
            QueryComment({mid: this.mid}).then(resp => {
              if (resp.err === null) {
                this.comments = resp.data.comments
              }
            })
        },
        UPDATE (data) {
          console.log(data)
        }
    },
    created () {
        this.getComments()
        this.sockets.subscribe('conversation', (mid) => {
          if(mid === this.mid) {
            this.getComments()
          }
        })
    },
    beforeDestroy () {
        this.sockets.unsubscribe('conversation')
    }
}
</script>

<style lang="scss" scoped>
.conversation {
    .message-box {
        border: 1px solid #bdbdbd;
        height: 500px;
        padding: 5px 10px;
        overflow: scroll;
        .messages {
            margin-bottom: 5px;
            .message {
              border: 1px solid #bdbdbd;
              padding: 3px;
              border-radius: 5px;
            }
        }
    }
    .send-box {
        resize: none;
        width: 98%;
        outline: none;
        border: 1px solid #bdbdbd;
        height: 100px;
        margin-top: 20px;
        padding: 10px 1%;
    }
    .send-btn {
        border: none;
        padding: 3px 12px;
        background-color: #e0e0e0;
        margin-top: 5px;
        border-radius: 2px;
        float: right;
        color: #616161;
        outline: none;
    }
}
</style>
