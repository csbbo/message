<template>
  <div class="commentconp">
    <RichEditor @richText="richEditorChange" ref="editor" />
    <button @click="addComment" class="submit">提交</button>
  </div>
</template>

<script>
import RichEditor from '@/components/RichEditor'
import { AddComment } from "@/common/api"
export default {
  name: 'Comment',
  components: {
    RichEditor
  },
  data() {
    return {
      form: {
        content: '',
      },
    }
  },
  props: ['mid'],
  methods: {
    addComment() {
        AddComment({mid: this.mid, content: this.form.content}).then(resp => {
          if (resp.err === null) {
            this.clearForm()
          } else {
              alert(resp.msg)
          }
        })
    },
    richEditorChange(content) {
        this.form.content = content
    },
    clearForm() {
        this.form.content = ''
        this.$refs.editor.clearEditor()
    }
  }
}
</script>

<style lang="scss" scoped>
.commentconp {
    width: 100%;
    .submit {
        border: none;
        padding: 3px 12px;
        background-color: #e0e0e0;
        margin-top: 10px;
        border-radius: 2px;
        float: right;
        color: #616161;
    }
}
</style>
