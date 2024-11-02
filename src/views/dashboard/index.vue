<template>
  <div class="dashboard-container">
    <span> {{ todayQuote }} </span>

<!--    <div class="button-container">-->
<!--      <el-button type="primary" @click="updateProject">项目更新</el-button>-->
<!--      <el-button type="primary" @click="compileProject">项目编译</el-button>-->
<!--      <el-button type="primary" @click="restartProject">项目重启</el-button>-->
<!--      <el-button type="danger" @click="oneClickRestart">一键重启</el-button>-->
<!--    </div>-->
<!--    <el-card>-->
<!--      <h3>System Information</h3>-->
<!--      <p><strong>Current Time:</strong> {{ currentTime }}</p>-->
<!--      <p><strong>System Type:</strong> {{ osType }}-{{ systemType }}</p>-->
<!--      <p><strong>User Agent:</strong> {{ userAgent }}</p>-->
<!--      <p><strong>CPU Info:</strong> {{ cpuInfo }}</p>-->
<!--      <p><strong>Disk Info:</strong>-->
<!--        <p v-html="formattedInfo"> {{ diskInfo }}</p>-->
<!--      </p>-->
<!--      <p><strong>Local IP:</strong> {{ localIP }}</p>-->
<!--      <p><strong>Wan IP:</strong> {{ wanIP }}</p>-->
<!--      <p><strong>Latitude, Longitude:</strong> [{{ Latitude }}, {{ Longitude }}]</p>-->
<!--      <p><strong>IpInfo:</strong> {{ IpInfo }}</p>-->
<!--      <p><strong>Location:</strong> {{ Location }}</p>-->
<!--    </el-card>-->

    <component :is="currentRole" />

  </div>
</template>

<script>
import adminDashboard from './admin'
// import {get_system_info} from "@/api/system_info";
// import {update_project} from "@/api/system_info";
// import {compile_project} from "@/api/system_info";
// import {restart_project} from "@/api/system_info";
import { getTodayQuote } from '@/api/azquotes'

export default {
  name: 'Dashboard',
  components: { adminDashboard },
  data() {
    return {
      todayQuote: '',
      currentTime: '',
      systemType: '',
      userAgent: '',
      cpuInfo: '',
      diskInfo: '',
      localIP: '',
      osType: null,
      wanIP: '',
      Latitude: '',
      Longitude: '',
      IpInfo: '',
      Location: '',
      currentRole: 'adminDashboard'
    }
  },
  mounted() {
    // this.updateTime()
    // this.getSystemInfo()
    this.getQuote()
  },
  methods: {
    // updateProject() {
    //   // 请求后端接口进行项目更新
    //   this.$message.success('开始执行 git pull');
    //   update_project().then(res => {
    //     console.log(res.searchResults);
    //     this.$message.success('更新项目✅');
    //   }).catch(err => {
    //     console.log(err)
    //     this.$message.error('服务端异常, 获取失败.');
    //   });
    // },
    // compileProject() {
    //   // 请求后端接口进行项目编译
    //   this.$message.success('开始执行 npm run build:prod');
    //   compile_project().then(res => {
    //     console.log(res.searchResults);
    //     this.$message.success('编译项目✅');
    //   }).catch(err => {
    //     console.log(err)
    //     this.$message.error('服务端异常, 获取失败.');
    //   });
    // },
    // restartProject() {
    //   // 请求后端接口进行项目重启
    //   this.$message.success('开始重启项目');
    //   restart_project().then(res => {
    //     console.log(res.searchResults);
    //
    //   }).catch(err => {
    //     console.log(err)
    //     this.$message.error('服务端异常, 获取失败.');
    //   });
    // },
    // oneClickRestart() {
    //   // 请求后端接口进行一键重启
    //
    // },
    updateTime() {
      this.currentTime = new Date().toLocaleString()
      setInterval(() => {
        this.currentTime = new Date().toLocaleString()
      }, 1000)
    },
    getSystemInfo() {
      // 使用Node.js环境中的 `os` 模块来获取系统信息
      const os = require('os')

      this.systemType = os.type()
      this.userAgent = navigator.userAgent
      // get_system_info()
      //   .then(res => {
      //     this.osType = res.searchResults.os_type
      //     this.cpuInfo = res.searchResults.cpu_info
      //     this.diskInfo = res.searchResults.disk_info
      //     this.localIP = res.searchResults.local_ip
      //     this.wanIP = res.searchResults.wan_ip
      //     this.Latitude = res.searchResults.latitude
      //     this.Longitude = res.searchResults.longitude
      //     this.IpInfo = res.searchResults.ip_info
      //     this.Location = res.searchResults.location
      //     // console.log(res.searchResults);  // debug
      //     if (this.wanIP === 'ip not found!') {
      //       this.$message.error('服务器可能处于离线模式！请检查网络。。。');
      //     }
      //
      //   })
      //   .catch(err => {
      //     console.log(err)
      //     this.$message.error('服务端异常, 获取失败.');
      //   });
    },
    async getQuote() {
      try {
        const res = await getTodayQuote()
        this.todayQuote = res.searchResults
        console.log(this.todayQuote)
      } catch (err) {
        console.log(err)
        this.$message.error('服务端异常, 获取失败.')
      }
      // getTodayQuote()
      //   .then(res => {
      //     this.todayQuote = res.searchResults.text
      //   })
      //   .catch(err => {
      //     console.log(err)
      //     this.$message.error('服务端异常, 获取失败.')
      //   })
    }

  },
  computed: {
    // formattedInfo() {
    //   return this.diskInfo.replace(/\n/g, '<br>')
    // }
  }
}
</script>

<style lang="scss" scoped>
.dashboard {
  &-container {
  }

  &-text {
    font-size: 30px;
    line-height: 46px;
  }
}

.button-container {
  display: flex;
  gap: 10px; /* 按钮之间的间距 */
}

.custom {
  &-input {
    width: 80%
  }
}

.search-results {
  display: flex;
  flex-direction: column; /*卡片竖向排列 */
  // align-items: center;
}

.card {
  width: 80%;
  padding: 20px;
  margin: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.card:hover {
  transform: translateY(-5px);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

h3 {
  margin: 0 0 10px;
}

p {
  margin: 0;
}
</style>
