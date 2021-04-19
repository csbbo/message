<template>
  <div class="publish">
    <div class="form">
      <input class="title" v-model="form.title" placeholder="请输入标题">
      <RichEditor @richText="richEditorChange" :content="form.content" ref="editor" />
    </div>
    <div class="menu-bar">
      <button @click="submitForm">提交</button>
      <button @click="clearForm">清空</button>
    </div>
  </div>
</template>

<script>
import RichEditor from '@/components/RichEditor'
import { AddMessage } from "@/common/api"
export default {
  name: 'Publish',
  components: {
    RichEditor
  },
  data() {
    return {
      form: {
        title: '',
        content: ''
      },
    };
  },
  created() {
  },
  methods: {
    submitForm() {
      AddMessage({title: this.form.title, content: this.form.content}).then(resp => {
        if (resp.err === null) {
          this.clearForm()
          alert('发布成功!')
        }
      })
    },
    richEditorChange(content) {
      this.form.content = content
    },
    clearForm() {
        this.form.title = ''
        this.form.content = ''
        this.$refs.editor.clearEditor()
    }
  },
  beforeDestroy() {
    this.editor.destroy()
  },
}
</script>

<style lang="scss" scoped>
.publish {
    display: flex;
    width: 1000px;
    margin: auto;
    margin-top: 10px;
    .form {
        width: 900px;
        .title {
            width: 890px;
            display: block;
            margin: auto;
            outline: none;
            border: none;
            height: 40px;
            margin-bottom: 10px;
            font-size: 25px;
            padding: 5px;
        }
    }
    .menu-bar {
        width: 100px;
        button {
            display: block;
            margin: auto;
            width: 70px;
            font-size: 14px;
            margin-bottom: 10px;
            border: none;
            padding: 3px;
            background-color: #e0e0e0;
            color: #212121;
        }
    }
}
</style>