<template>
  <div class="home">
    <div id="demo1"></div>
  </div>
</template>

<script>

import wangEditor from 'wangeditor'
export default {
  data() {
    return {
      editor: null,
      editorData: ''
    }
  },
  props: ['content'],
  mounted() {
    this.createEditor()
  },
  methods: {
    createEditor() {
        const editor = new wangEditor(`#demo1`)

        // 配置 onchange 回调函数，将数据同步到 vue 中
        editor.config.onchange = (newHtml) => {
        this.editorData = newHtml
        }

        // 创建编辑器
        editor.create()

        this.editor = editor
        this.editor.txt.html(this.content)
    },
    getEditorData() {
      // 通过代码获取编辑器内容
      let data = this.editor.txt.html()
      alert(data)
    },
    clearEditor() {
        this.editor.destroy()
        this.editor = null
        this.createEditor()
    }
  },
  beforeDestroy() {
    // 调用销毁 API 对当前编辑器实例进行销毁
    this.editor.destroy()
    this.editor = null
  },
}
</script>

<style lang="scss">
  .home {
    width: 1200px;
    margin: auto;
    position: relative;
    .btn {
      position: absolute;
      right: 0;
      top: 0;
      padding: 5px 10px;
      cursor: pointer;
    }
    h3 {
      margin: 30px 0 15px;
    }
  }
</style>
