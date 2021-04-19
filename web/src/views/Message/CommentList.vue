<template>
  <div class="commentlist">
    <div v-for="(comment, i) in comments" :key="i">
      <div class="content" v-html="comment.content"></div>
    </div>
  </div>
</template>

<script>
import { QueryComment } from "@/common/api"
export default {
  name: 'CommentList',
  data() {
    return {
      comments: [],
    }
  },
  props: ['mid'],
  created() {
    this.getComments()
  },
  methods: {
    getComments() {
        QueryComment({mid: this.mid}).then(resp => {
          if (resp.err === null) {
            this.comments = resp.data.comments
          }
        })
    }
  }
}
</script>

<style lang="scss" scoped>

</style>
