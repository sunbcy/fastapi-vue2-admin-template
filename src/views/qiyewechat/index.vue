<template>
  <div class="robot-debug">
    <el-row class="input-row" align="top">
      <el-col :span="24">
        <span>1、秘钥配置：</span>
      </el-col>
      <el-col :span="20">
        <el-input
          v-model="secretKey"
          type="password"
          placeholder="请输入秘钥"
          show-password
        />
      </el-col>
    </el-row>

    <el-row class="input-row" align="top">
      <el-col :span="24">
        <span>2、文字消息：</span>
      </el-col>
      <el-col :span="20">
        <el-input
          v-model="textMessage"
          placeholder="请输入文字消息"
          clearable
          @keyup.enter.native="sendMessage"
        />
      </el-col>
      <el-col :span="4">
        <el-button type="primary" @click="sendMessage">发送消息</el-button>
      </el-col>
    </el-row>
  </div>
</template>

<script>
import { sendText } from '@/api/qiyewechat'

export default {
  data() {
    return {
      secretKey: '',
      textMessage: '你好，Vue-WebToOls测试！--fastapi'
    }
  },
  methods: {
    sendMessage() {
      // 在这里实现你的发送消息的逻辑
      const s_data = {
        'text': this.textMessage
      }
      console.log(s_data)
      sendText(s_data) // encodeURIComponent .then(response => {}).catch(error => { this.$message.error('服务端异常, 搜索失败.'); })
        .then(res => {
          this.sendResults = res.sendResults // -->
          console.log(this.sendResults)
          this.$message.success('消息发送成功!')
          // console.log(res.code.list);
          // setTimeout(() => {
          //   this.sendResults = res.sendResults
          // }, 500)
        })
        .catch(err => {
          console.log(err)
          this.$message.error('服务端异常, 发送失败.')
        })
    }
  }
}
</script>

  <style scoped>
  .robot-debug .input-row {
    margin-bottom: 20px; /* 设置行的底部外边距 */
  }
  .robot-debug .el-input,
  .robot-debug .el-button {
    width: 100%; /* 使输入框和按钮宽度100%，以填满其容器的宽度 */
  }
  </style>
